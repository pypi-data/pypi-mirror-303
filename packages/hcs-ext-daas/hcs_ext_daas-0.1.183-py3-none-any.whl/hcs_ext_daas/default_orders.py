"""
Copyright 2023-2023 VMware Inc.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging

from hcs_cli.service import ims, av
from . import template, order

log = logging.getLogger(__name__)


def process(data: dict, state: dict) -> dict:
    org_id = data["orgId"]
    provider_id = _get_provider_id(data, state)

    images = ims.helper.get_images_by_provider_instance_with_asset_details(provider_id, org_id)

    if not images:
        raise Exception(
            "Failed to create default orders with infra images for org " + org_id + " provider_id " + provider_id
        )

    default_orders = [
        _create_default_order(data, state, images, multi_session=True),
        _create_default_order(data, state, images, multi_session=False),
    ]
    return default_orders


def _create_default_order(data: dict, state: dict, images: dict, multi_session: str):
    template_type = "MULTI_SESSION" if multi_session else "FLOATING"
    selected_image = None
    for image in images:
        if image["multiSession"] == multi_session:
            selected_image = image
            break
    if not selected_image:
        raise Exception("Failed to create default order for template: " + template_type)

    order_data = template.get("v1/tenant-order.var.yml")["var"]
    order_data["orgId"] = data["orgId"]
    order_data["providerInstanceId"] = _get_provider_id(data, state)
    order_data["edgeDeploymentId"] = _get_edge_id(data, state)
    order_data["application"]["info"] = []
    order_data["template"]["type"] = template_type
    order_data["image"]["streamId"] = selected_image["id"]
    order_data["image"]["name"] = selected_image["name"]
    order_data["image"]["os"] = selected_image["os"]
    order_data["application"]["info"] = _get_app_info_list(data["orgId"])

    if selected_image["markers"]:
        order_data["image"]["markerId"] = selected_image["markers"][0]["id"]
        order_data["image"]["markerName"] = selected_image["markers"][0]["name"]

    if selected_image["_assetDetails"]:
        order_data["image"]["sku"] = selected_image["_assetDetails"]["data"]["vmSize"]
        order_data["image"]["gen"] = (
            "Gen2" if selected_image["_assetDetails"]["data"]["generationType"] == "V2" else "Gen1"
        )

    order_type = state["deploymentId"] + "-default-" + template_type
    order.add({order_type: order_data})
    return order_type


def _get_provider_id(data: dict, state: dict):
    if data["provider"] and "id" in data["provider"] and data["provider"]["id"]:
        return data["provider"]["id"]

    return state["output"]["myProvider"]["id"]


def _get_edge_id(data: dict, state: dict):
    if data["edge"] and "id" in data["edge"] and data["edge"]["id"]:
        return data["edge"]["id"]

    return state["output"]["myEdge"]["id"]


def _get_app_info_list(org_id: str):
    app_info_list = []
    av_list = av.app.list_apps(org_id)
    if not av_list:
        return app_info_list

    for app in av_list:
        _app_info = {"applicationId": app["id"], "name": app["name"]}

        _app_versions = app.get("appVersions")
        if not _app_versions:
            continue
        else:
            latest_app_version = max(_app_versions, key=lambda k: k["updatedAt"])
            if latest_app_version:
                _app_info["appVersionId"] = latest_app_version["id"]
                _app_info["version"] = latest_app_version["version"]

        if "appVersionId" in _app_info and "applicationId" in _app_info and _app_info not in app_info_list:
            app_info_list.append(_app_info)

    return app_info_list


def destroy(data: dict, state: dict, force: bool):
    if state:
        for order_type in state:
            order.remove(order_type)


def eta(action: str, data: dict, state: dict):
    return "1m"
