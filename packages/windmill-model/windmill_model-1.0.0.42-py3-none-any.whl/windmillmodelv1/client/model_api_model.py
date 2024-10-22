#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/29
# @Author  : yanxiaodong
# @File    : model_api_model.py
"""
import re
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Dict

from pygraphv1.client.graph_api_graph import GraphContent

model_name_regex = re.compile(
    "^workspaces/(?P<workspace_id>.+?)/modelstores/(?P<model_store_name>.+?)/models/(?P<local_name>.+?)$"
)


class Category(Enum):
    """
    Model Category
    """
    CategoryImageOCR = "Image/OCR"
    CategoryImageClassificationMultiClass = "Image/ImageClassification/MultiClass"
    CategoryImageClassificationMultiTask = "Image/ImageClassification/MultiTask"
    CategoryImageObjectDetection = "Image/ObjectDetection"
    CategoryImageSemanticSegmentation = "Image/SemanticSegmentation"
    CategoryImageInstanceSegmentation = "Image/InstanceSegmentation"
    CategoryImageKeypointDetection = "Image/KeypointDetection"
    CategoryImageChangeDetectionInstanceSegmentation = "Image/ChangeDetection/InstanceSegmentation"
    CategoryImageChangeDetectionObjectDetection = "Image/ChangeDetection/ObjectDetection"
    CategoryImageChangeDetectionSemanticSegmentation = "Image/ChangeDetection/SemanticSegmentation"
    CategoryImageAnomalyDetection = "Image/AnomalyDetection"
    CategoryImageObjectTracking = "Image/ObjectTracking"

    CategoryImageEnsemble = "Image/Ensemble"
    CategoryImagePreprocess = "Image/Preprocess"
    CategoryImagePostprocess = "Image/Postprocess"

    CategoryMultimodal = "Multimodal"
    CategoryNLPTextGeneration = "NLP/TextGeneration"
    CategoryNLPQuestionAnswering = "NLP/QuestionAnswering"


class ModelName(BaseModel):
    """
    The name of model.
    """

    workspace_id: str
    model_store_name: str
    local_name: str

    class Config:
        """
        命名空间配置
        : 避免命名空间冲突
        """
        protected_namespaces = []

    def get_name(self):
        """
        get name
        :return:
        """
        return f"workspaces/{self.workspace_id}/modelstores/{self.model_store_name}/models/{self.local_name}"


class Label(BaseModel):
    """
    The label of model.
    """

    id: Optional[int] = None
    name: Optional[str] = None
    displayName: Optional[str] = None
    parentID: Optional[int] = None


class InputSize(BaseModel):
    """
    The size of input.
    """

    width: Optional[int] = None
    height: Optional[int] = None


class ModelMetadata(BaseModel):
    """
    The metadata of model.
    """

    experimentName: Optional[str] = None
    experimentRunID: Optional[str] = None
    jobName: Optional[str] = None
    jobDisplayName: Optional[str] = None
    labels: Optional[List[Label]] = None
    algorithmParameters: Optional[Dict[str, str]] = None
    maxBoxNum: Optional[int] = None
    inputSize: Optional[InputSize] = None
    subModels: Optional[Dict[str, str]] = None
    extraModels: Optional[Dict[str, str]] = None
    graphContent: Optional[GraphContent] = None


def parse_model_name(name: str) -> Optional[ModelName]:
    """
    Get ModelName。
    """
    m = model_name_regex.match(name)
    if m is None:
        return None
    return ModelName(
        workspace_id=m.group("workspace_id"),
        model_store_name=m.group("model_store_name"),
        local_name=m.group("local_name"),
    )