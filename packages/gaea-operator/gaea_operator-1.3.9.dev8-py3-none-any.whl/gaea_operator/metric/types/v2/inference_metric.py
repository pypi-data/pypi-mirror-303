#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/8/21
# @Author  : yanxiaodong
# @File    : inference_metric.py
"""
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from enum import Enum

from windmillmodelv1.client.model_api_model import Label

from ..metric import BaseMetric


class MetricName(Enum):
    """
    Metric
    """
    accuracy = "accuracy"
    precision = "precision"
    recall = "recall"
    f1_score = "f1Score"
    false_positive = "falsePositive"
    false_negative = "falseNegative"
    true_positive_rate = "truePositiveRate"
    average_precision = "averagePrecision"
    average_recall = "averageRecall"

    image_label_metric = "labelMetric"
    image_confusion_matrix = "confusionMatrix"

    bounding_box_metric = "boundingBoxMetric"
    bounding_box_precision_recall_curve = "boundingBoxPrecisionRecallCurve"
    bounding_box_label_metric = "boundingBoxLabelMetric"
    bounding_box_confusion_matrix = "boundingBoxConfusionMatrix"


class MetricDisplayName(Enum):
    """
    Metric display name
    """
    accuracy = "Accuracy(准确率)"
    precision = "Precision(精确率)"
    recall = "Recall(召回率)"
    f1_score = "F1Score(调和平均数)"
    false_positive = "误报"
    false_negative = "漏报"
    true_positive_rate = "检出率"
    average_precision = "平均精确率"
    average_recall = "平均召回率"

    label_metric = "图像级别评估结果"
    confusion_matrix = "混淆矩阵"

    bounding_box_precision_recall_curve = "P-R曲线"
    bounding_box_label_metric = "框级别评估结果"


class MetricCategory(Enum):
    """
    Metric category
    """
    category_image = "Image/Image"
    category_bbox = "Image/BBox"


class MetricDisplayType(Enum):
    """
    Metric display type
    """
    table = "table"  # 表格展示
    chart = "chart"  # 曲线图展示
    card = "card"  # 卡片展示


class ConfusionMatrixRow(BaseModel):
    """
    Confusion Matrix Result
    """
    row: Optional[List[int]] = None


class ConfusionMatrixMetricResult(BaseModel):
    """
    Confusion Matrix Result
    """
    lower_bound: Optional[int] = Field(None, alias="lowerBound")
    upper_bound: Optional[int] = Field(None, alias="upperBound")
    rows: Optional[List[ConfusionMatrixRow]] = None


class AnnotationSpecs(BaseModel):
    """
    Annotation Specs
    """
    name: Optional[str] = None
    display_name: Optional[str] = Field(None, alias="displayName")


class ConfusionMatrixMetric(BaseModel):
    """
    Confusion Matrix
    """
    name: Optional[str] = MetricName.image_confusion_matrix.value
    display_name: Optional[str] = Field(MetricDisplayName.confusion_matrix.value, alias="displayName")
    column_annotation_specs: Optional[Union[List[List[AnnotationSpecs]], List[AnnotationSpecs]]] = \
        Field(None, alias="columnAnnotationSpecs")
    row_annotation_specs: Optional[Union[List[List[AnnotationSpecs]], List[AnnotationSpecs]]] = \
        Field(None, alias="rowAnnotationSpecs")
    label_names: Optional[List[str]] = Field(None, alias="labelNames")
    category: Optional[str] = None
    display_type: Optional[str] = Field(MetricDisplayType.table.value, alias="displayType")
    result: Optional[Union[List[ConfusionMatrixMetricResult], ConfusionMatrixMetricResult]] = None


class LabelResult(BaseModel):
    """
    Metric result
    """
    label_name: Optional[str] = Field(None, alias="labelName")
    result: Optional[float] = None


class LabelMetricResult(BaseModel):
    """
    Inference label metric result
    """
    label_name: Optional[str] = Field(None, alias="labelName")
    precision: Optional[Union[float, List[LabelResult]]] = None
    recall: Optional[Union[float, List[LabelResult]]] = None
    accuracy: Optional[Union[float, List[LabelResult]]] = None
    f1_score: Optional[Union[float, List[LabelResult]]] = Field(None, alias="f1Score")
    false_positive: Optional[Union[float, List[LabelResult]]] = Field(None, alias="falsePositive")
    false_negative: Optional[Union[float, List[LabelResult]]] = Field(None, alias="falseNegative")
    true_positive_rate: Optional[Union[float, List[LabelResult]]] = Field(None, alias="truePositiveRate")

    average_precision: Optional[Union[float, List[LabelResult]]] = Field(None, alias="averagePrecision")
    average_recall: Optional[Union[float, List[LabelResult]]] = Field(None, alias="averageRecall")


class InferenceLabelMetric(BaseModel):
    """
    Inference label metric
    """
    name: Optional[str] = MetricName.image_label_metric.value
    display_name: Optional[str] = Field(MetricDisplayName.label_metric.value, alias="displayName")
    column_annotation_specs: Optional[List[AnnotationSpecs]] = Field(None, alias="columnAnnotationSpecs")
    category: Optional[str] = None
    display_type: Optional[str] = Field(MetricDisplayType.table.value, alias="displayType")
    result: Optional[List[LabelMetricResult]] = None


class InferenceSingleMetric(BaseModel):
    """
    Inference image metric
    """
    name: Optional[str] = None
    display_name: Optional[str] = Field(None, alias="displayName")
    category: Optional[str] = None
    display_type: Optional[str] = Field(MetricDisplayType.card.value, alias="displayType")
    result: Optional[float] = None


class BoundingBoxLabelConfidenceMetric(BaseModel):
    """
    Bounding Box Label Metric
    """
    recall: Optional[float] = None
    precision: Optional[float] = None


class BoundingBoxPRCurveMetricResult(BaseModel):
    """
    Bounding Box Label Metric
    """
    iou_threshold: Optional[float] = Field(None, alias="iouThreshold")
    average_precision: Optional[float] = Field(None, alias="averagePrecision")
    label_name: Optional[str] = Field(None, alias="labelName")
    confidence_metrics: Optional[List[BoundingBoxLabelConfidenceMetric]] = Field(None, alias="confidenceMetrics")


class BoundingBoxPRCurveMetric(BaseModel):
    """
    Bounding Box Label Metric
    """
    name: Optional[str] = MetricName.bounding_box_precision_recall_curve.value
    displayName: Optional[str] = MetricDisplayName.bounding_box_precision_recall_curve.value
    horizontal_axis_annotation_specs: Optional[str] = Field(None, alias="horizontalAxisAnnotationSpecs")
    vertical_axis_annotation_specs: Optional[str] = Field(None, alias="verticalAxisAnnotationSpecs")
    category: Optional[str] = None
    display_type: Optional[str] = Field(MetricDisplayType.chart.value, alias="displayType")
    result: Optional[List[BoundingBoxPRCurveMetricResult]] = None


class InferenceMetric(BaseMetric):
    """
    Object Detection Metric
    """
    labels: Optional[List[Label]] = None
    metrics: Optional[List[Union[
        InferenceLabelMetric,
        InferenceSingleMetric,
        ConfusionMatrixMetric,
        BoundingBoxPRCurveMetric]]] = None
