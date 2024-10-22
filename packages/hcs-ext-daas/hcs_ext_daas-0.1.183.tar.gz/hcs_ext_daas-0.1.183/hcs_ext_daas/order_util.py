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
from hcs_core.ctxp import choose
from hcs_cli.service import ims, av

log = logging.getLogger(__file__)


def configure_desktops(var: dict):
    org_id = var["orgId"]

    def _select_desktop_type():
        types = ["FLOATING", "DEDICATED", "MULTI_SESSION"]
        template_type = choose("Desktop type:", types)
        var["template"]["type"] = template_type
        return template_type

    def _select_image_and_vm_sku():
        multi_session = False
        if var["template"]["type"] == "MULTI_SESSION":
            multi_session = True

        images = ims.helper.get_images_by_provider_instance_with_asset_details(var["providerInstanceId"], org_id)
        images = [i for i in images if i["multiSession"] == multi_session]
        fn_get_text = lambda d: f"{d['name']}: {d['os']}"
        prev_selected_image = None
        if var["image"]["streamId"]:
            for i in images:
                if i["id"] == var["desktop"]["streamId"]:
                    prev_selected_image = i
                    break
        selected_image = choose("Select image:", images, fn_get_text, selected=prev_selected_image)
        var["image"]["streamId"] = selected_image["id"]
        var["image"]["name"] = selected_image["name"]
        var["image"]["os"] = selected_image["os"]

        fn_get_text = lambda m: f"{m['name']}"
        selected_marker = choose("Select marker:", selected_image["markers"], fn_get_text)
        var["image"]["markerId"] = selected_marker["id"]
        var["image"]["markerName"] = selected_marker["name"]

        image_asset_details = selected_image["_assetDetails"]["data"]
        var["image"]["sku"] = image_asset_details["vmSize"]
        var["image"]["gen"] = "Gen2" if image_asset_details["generationType"] == "V2" else "Gen1"

    _select_desktop_type()
    _select_image_and_vm_sku()


def configure_apps(var: dict):
    org_id = var["orgId"]

    def _select_applications():
        app_info_list = []
        av_list = {}
        fn_get_text = lambda d: f"{d['name']}: {d['description']}"
        while _add_application() == "1":
            av_list = av.app.list_apps(org_id) if not av_list and not app_info_list else av_list
            if not av_list:
                log.info("No applications found. Skipping app configurations")

            _app_info = {}
            _selected_app = choose("Select application:", av_list, fn_get_text, selected=None, select_by_default=False)
            _app_info["applicationId"] = _selected_app["id"]
            _app_info["name"] = _selected_app["name"]

            _app_versions = _selected_app.get("appVersions")
            if not _app_versions:
                log.info(
                    "No versions found for application '%s'. Skipping further configuration for this application",
                    _selected_app["name"],
                )
                av_list = [app for app in av_list if app.get("id", "") != _app_info.get("applicationId")]
            else:
                latest_app_version = max(_app_versions, key=lambda k: k["updatedAt"])
                _selected_version = choose(
                    "Select application version:",
                    _app_versions,
                    fn_get_text,
                    selected=latest_app_version,
                    select_by_default=True,
                )
                _app_info["appVersionId"] = _selected_version["id"]
                _app_info["version"] = _selected_version["version"]

            if "appVersionId" in _app_info and "applicationId" in _app_info and _app_info not in app_info_list:
                app_info_list.append(_app_info)
                av_list = [app for app in av_list if app.get("id", "") != _app_info.get("applicationId")]

            if not av_list:
                log.info("All existing applications configured successfully")
                break

        var["application"]["info"] = app_info_list

    def _add_application():
        options = ["Yes", "No"]
        input_option = choose("Do you want to add applications to order:", options)
        if input_option == "No":
            return "0"
        return "1"

    _select_applications()
