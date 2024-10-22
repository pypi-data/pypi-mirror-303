#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/9/10
# @Author  : zhangzhijun
# @File    : dump_model.py
"""
import os
from argparse import ArgumentParser

import bcelogger
from windmillclient.client.windmill_client import WindmillClient


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--model_name", required=False, type=str, default="")
    parser.add_argument("--output_uri", required=False, type=str, default="/data/model")

    args, _ = parser.parse_known_args()

    return args


def run():
    """
    dump model.
    """
    args = parse_args()
    org_id = os.getenv("ORG_ID", "")
    user_id = os.getenv("USER_ID", "")
    windmill_endpoint = os.getenv("WINDMILL_ENDPOINT", "")
    windmill_client = WindmillClient(endpoint=windmill_endpoint,
                                     context={"OrgID": org_id, "UserID": user_id})

    output_uri = os.path.join(args.output_uri, args.model_name)
    if not os.path.exists(output_uri):
        os.makedirs(output_uri)

    if len(os.listdir(output_uri)) > 0:
        bcelogger.warning(f"Output directory {output_uri} already exists and is not empty.")
        return

    windmill_client.dump_models(artifact_name=args.model_name, rename="ensemble", output_uri=output_uri)
    bcelogger.info(f"Model {args.model_name} dumped successfully")


if __name__ == "__main__":
    run()
