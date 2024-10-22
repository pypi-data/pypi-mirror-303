#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/8/2
# @Author  : yanxiaodong
# @File    : model_metadata_update.py
"""
import os
from typing import Dict, List
import yaml

import bcelogger
from pygraphv1.client.graph_api_graph import GraphContent
from windmillmodelv1.client.model_api_model import Category, Label


def update_metadata(graph: GraphContent, model_metadata: Dict, input_uri: str = "/home/windmill/tmp/model"):
    """
    Update the model metadata.
    """
    # 1. 获取后处理节点
    model_name = None
    category = None
    for node in graph.nodes:
        for property_ in node.properties:
            if property_.name == "localName":
                model_name = property_.value
            if property_.name == "category" and property_.value == Category.CategoryImagePostprocess.value:
                category = property_.value
        if model_name is not None and category is not None:
            break
    assert category is not None, "No postprocess model found"
    bcelogger.info(f"Postprocess model name: {model_name}, category: {category}")

    # 2. 解析后处理节点
    labels = []
    label_set = set()
    filepath = os.path.join(input_uri, model_name, "parse.yaml")
    data = yaml.load(open(filepath, "r"), Loader=yaml.FullLoader)
    assert len(data["outputs"]) > 0, f"No output found in {data}"
    assert "fields_map" in data["outputs"][0], f'Field fields_map not in {data["outputs"][0]}'

    for item in data["outputs"][0]["fields_map"]:
        if len(item["categories"]) == 0:
            continue
        elif isinstance(item["categories"][0], list):
            for sub_item in item["categories"]:
                parse_labels(sub_item, label_set, item["model_name"], labels)
        elif isinstance(item["categories"][0], dict):
            parse_labels(item["categories"], label_set, item["model_name"], labels)
        else:
            bcelogger.error(f'Model name {item["model_name"]} laebls {item["categories"]} is invalid')

    model_metadata["labels"] = labels
    model_metadata["graphContent"] = graph.dict(by_alias=True, exclude_none=True)


def parse_labels(model_labels: List[Dict], label_set: set, model_name: str, labels: List[Dict]):
    """
    Parse the labels.
    """
    for label in model_labels:
        if label["id"] in label_set:
            continue
        bcelogger.info(f'Model {model_name} label: {label}')
        if "display_name" in label:
            idx = label["id"]
            name = label["name"]
            display_name = label["display_name"]
            label_set.add(label["name"])
        else:
            idx = len(labels)
            name = label["id"]
            display_name = label["name"]
            label_set.add(label["id"])
        labels.append(Label(id=idx, name=name, displayName=display_name).dict())