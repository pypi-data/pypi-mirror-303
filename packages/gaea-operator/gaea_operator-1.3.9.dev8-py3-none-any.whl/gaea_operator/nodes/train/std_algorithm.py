#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : train_component.py
"""
import os
import json
import yaml
from argparse import ArgumentParser
import shutil
from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillmodelv1.client.model_api_model import ModelName
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmillmodelv1.client.model_api_model import ModelMetadata
from windmillclient.client.windmill_client import WindmillClient
import bcelogger
from gaea_operator.utils import find_upper_level_folder

from gaea_operator.metric.types.metric import LOSS_METRIC_NAME, \
    MAP_METRIC_NAME, \
    AP50_METRIC_NAME, \
    AR_METRIC_NAME, \
    BOUNDING_BOX_MEAN_AVERAGE_PRECISION_METRIC_NAME, \
    ACCURACY_METRIC_NAME, \
    CLASSIFICATION_ACCURACY_METRIC_NAME, \
    SEG_MAP_METRIC_NAME, \
    SEG_AP50_METRIC_NAME, \
    SEG_AR_METRIC_NAME
from gaea_operator.trainer import Trainer
from gaea_operator.model import Model
from gaea_operator.metric import get_score_from_file, update_metric_file_with_dataset
from gaea_operator.utils import write_file
from gaea_operator.utils import NX_METRIC_MAP, NX_CATEGORY_MAP, _retrive_path, _copy_annotation_file_2_backup_path, \
    get_annotation_type, _modify_annotation, pre_listdir_folders

def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--org-id", type=str, default=os.environ.get("ORG_ID"))
    parser.add_argument("--user-id", type=str, default=os.environ.get("USER_ID"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--scene", type=str, default=os.environ.get("SCENE"))
    parser.add_argument("--public-model-store",
                        type=str,
                        default=os.environ.get("PUBLIC_MODEL_STORE", "workspaces/public/modelstores/public"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--train-dataset-name",
                        type=str,
                        default=os.environ.get("TRAIN_DATASET_NAME"))
    parser.add_argument("--val-dataset-name", type=str, default=os.environ.get("VAL_DATASET_NAME"))
    parser.add_argument("--base-train-dataset-name",
                        type=str,
                        default=os.environ.get("BASE_TRAIN_DATASET_NAME"))
    parser.add_argument("--base-val-dataset-name", type=str, default=os.environ.get("BASE_VAL_DATASET_NAME"))
    parser.add_argument("--model-name", type=str, default=os.environ.get("MODEL_NAME"))
    parser.add_argument("--model-display-name",
                        type=str,
                        default=os.environ.get("MODEL_DISPLAY_NAME"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))
    parser.add_argument("--train_config_params_uri", type=str, default=os.environ.get("TRAIN_CONFIG_PARAMS_URI"))

    args, _ = parser.parse_known_args()

    return args

def std_algorithm_train(args):
    """
    Train component for ppyoloe_plus model.
    """
    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint,
                                     context={"OrgID": args.org_id, "UserID": args.user_id})
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.tracking_uri,
                                       experiment_name=args.experiment_name,
                                       experiment_kind=args.experiment_kind,
                                       project_name=args.project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))
    
    response = windmill_client.get_artifact(name=args.train_dataset_name)
    filesystem = windmill_client.suggest_first_filesystem(workspace_id=response.workspaceID,
                                                                       guest_name=response.parentName)
    bcelogger.info(f"------filesystem------ : {filesystem}")
    
    train_val_annotation_files = {}
    local_dst_path = '/root/annotations'
    if not os.path.exists(local_dst_path):
        os.makedirs(local_dst_path)
    
    # 获取目前全部参与训练图片所在文件夹的路径
    label_description_path = ''
    all_image_folders = set()
    for _path in response.metadata["paths"]:
        relative_path = windmill_client.get_path(filesystem, _path)
        local_dataset_path = os.path.join(tracker_client.work_dir, relative_path)
        bcelogger.info(f"-----local_dataset_path----- : {local_dataset_path}")

        # 获取 label_description_path
        if os.path.exists(os.path.join(local_dataset_path, 'label_description.yaml')):
            label_description_path = os.path.join(local_dataset_path, 'label_description.yaml')
            os.system(f'cp {label_description_path} /root/annotations/')

        prefix = ['train', 'val']
        for p in prefix:
            src_names = []
            if not os.path.isfile(local_dataset_path):
                src_names = _retrive_path(local_dataset_path, ['json', 'txt'], p)
            else:
                src_names.append(local_dataset_path)
            if len(src_names) <= 0:
                continue
            abs_work_path = find_upper_level_folder(src_names[0], 2) # according to document MUST have annotation-folder
            for src_name in src_names:
                dst_name = _modify_annotation(src_name, local_dst_path, abs_work_path, all_image_folders)
                if p in train_val_annotation_files:
                    train_val_annotation_files[p].append(dst_name)
                else:
                    train_val_annotation_files[p] = [dst_name]

    # 通过 os.listdir() 预先缓存所有文件夹，避免后续的 os.listdir() 耗时
    pre_listdir_folders(all_image_folders)

    # 获取标签类型
    annotation_type = get_annotation_type(label_description_path)

    # 读取 v2x config YAML 文件
    input_config_file = "/root/train_code/v2x_model_standardization/configs/input_config.yaml"
    bcelogger.info(f"------input_config_file------: {input_config_file}")

    with open(input_config_file, 'r') as f:
        config = yaml.safe_load(f)

    # 将 dataset 配置清空，读取实际的 dataset 配置，并填充
    if 'data_load' in config and isinstance(config['data_load'], dict):
        config['data_load']['train'] = {}
        config['data_load']['eval'] = {}
        config['data_load']['infer'] = {}

    task_name = config['task_name']
    bcelogger.info(f"------task_name is------: {task_name}")

    image_dir_name = "image_dir"
    data_dir_name = "dataset_dir"
    anno_dir_name = "anno_path"
    key_sample_prob = 'sample_prob'

    config['data_load']['label_description'] = '/root/annotations/label_description.yaml'
    config['data_load']['train'][image_dir_name] = "./"
    config['data_load']['train'][data_dir_name] = '/'
    config['data_load']['train'][anno_dir_name] = train_val_annotation_files['train']
    config['data_load']['train'][key_sample_prob] = 1

    config['data_load']['eval'][image_dir_name] = "./"
    config['data_load']['eval'][data_dir_name] = '/'
    config['data_load']['eval'][anno_dir_name] = train_val_annotation_files['val']

    config['data_load']['infer'][image_dir_name] = "none"
    config['data_load']['infer'][data_dir_name] = "none"
    config['data_load']['infer'][anno_dir_name] = "none"

    if not os.path.exists(args.output_model_uri):
        os.makedirs(args.output_model_uri, exist_ok=True)

    config['output_root_dir'] = args.output_model_uri
    with open(input_config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    # 同时将 input_config_file 写入到 output_model_uri，用于后面模型评测
    input_config_path2 = os.path.join(args.output_model_uri, 'input_config.yaml')
    os.system(f'cp {input_config_file} {input_config_path2}')
    bcelogger.info(f'cp {input_config_file} {input_config_path2}')

    bcelogger.info(f"-----input_config_file------:{config}")

    for k, v in train_val_annotation_files.items():
        for name in v:
            _copy_annotation_file_2_backup_path(name, args.output_uri)

    trainer = Trainer(framework="PaddlePaddle", tracker_client=tracker_client)
    metric_names = NX_METRIC_MAP['metric_names'].get(annotation_type, [])
    trainer.track_model_score(metric_names=metric_names)
    std_alg_log_name = os.path.join(args.output_uri, 'std-algorithm-train.log') 

    model_name = config.get('model_name', 'StandardizeModel2')
    train_command = (
            f'cd /root/train_code/ && '
            f'python -m v2x_model_standardization --model_name {model_name} --step train ; '
            f'python -m v2x_model_standardization --model_name {model_name} --step generate_encapsulation_config ; '
            f'python -m v2x_model_standardization --model_name {model_name} --step export ')
    result = os.system(train_command)
    bcelogger.info(f"train result: {result}")
    trainer.training_exit_flag = True

    bcelogger.info('standardization-algorithm-train-log file: {}'.format(std_alg_log_name))

    # 5. 更新指标文件
    update_metric_file_with_dataset(dataset_name=args.train_dataset_name,
                                    input_dir=args.output_model_uri,
                                    file_name="metric.json")
    
    # 6. 创建模型
    bcelogger.info(f"------begin to create model------")
    metric_name = NX_METRIC_MAP['metric_name'].get(annotation_type, BOUNDING_BOX_MEAN_AVERAGE_PRECISION_METRIC_NAME)
    if os.path.exists(os.path.join(args.output_model_uri, "metric.json")):
        current_score = get_score_from_file(filepath=os.path.join(args.output_model_uri, "metric.json"),
                                        metric_name=metric_name)
    else:
        current_score = 1.0

    best_score, version = Model(windmill_client=windmill_client). \
        get_best_model_score(model_name=args.model_name, metric_name=metric_name)
    tags = {metric_name: str(current_score)}
    alias = None
    if current_score >= best_score and version is not None:
        alias = ["best"]
        bcelogger.info(
            f"{metric_name.capitalize()} current score {current_score} >= {best_score}, update [best]")
        tags.update(
            {"bestReason": f"current.score({current_score}) greater than {version}.score({best_score})"})
    if version is None:
        alias = ["best"]
        bcelogger.info(f"First alias [best] score: {current_score}")
        tags.update({"bestReason": f"current.score({current_score})"})

    ## 构造 artifact_metadata
    meta_data = ModelMetadata(
            experimentName=tracker_client.experiment_name,
            jobName=tracker_client.job_name,
            jobDisplayName=tracker_client.job_display_name,
            algorithmParameters=None,
            experimentRunID=tracker_client.run_id)

    model_name = parse_model_name(args.model_name)
    workspace_id = model_name.workspace_id
    model_store_name = model_name.model_store_name
    local_name = model_name.local_name
    response = windmill_client.create_model(workspace_id=workspace_id,
                                            model_store_name=model_store_name,
                                            local_name=local_name,
                                            display_name=args.model_display_name,
                                            category=NX_CATEGORY_MAP[annotation_type],
                                            model_formats=["PaddlePaddle"],
                                            artifact_alias=alias,
                                            artifact_tags=tags,
                                            artifact_metadata=meta_data.dict(),
                                            artifact_uri=args.output_model_uri)
    bcelogger.info(f"Model {args.model_name} created response: {response}")

    # 7. 输出文件
    write_file(obj=json.loads(response.raw_data)["artifact"], output_dir=args.output_model_uri)


if __name__ == "__main__":
    args = parse_args()
    std_algorithm_train(args=args)
