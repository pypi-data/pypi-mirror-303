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

from azure.core.exceptions import ResourceNotFoundError

from hcs_core.sglib.client_util import wait_for_res_status
from hcs_ext_azure.provider._az_facade import resource_management_client as client
from hcs_ext_azure.provider._az_facade import storage_management_client as sclient
from azure.storage.fileshare import ShareClient, ShareFileClient
from hcs_core.util import hcs_constants

log = logging.getLogger(__file__)


def fs_copy(data: dict, state: dict):
    _copy_metadata = []
    _source_files = data["sourceFiles"]
    _file_path = data["filePath"]
    _dest_client = _get_des_client(data["resGroup"], data["destinationShareName"], data["storageAccountName"])
    for _blob in _source_files:
        res = check_copy_done(state, _blob)
        _f_name = _blob.split(hcs_constants.FORWARD_SLASH)[-1]
        _dest_file = _dest_client.get_file_client(_file_path + _f_name)
        if not res:
            _dest_file.start_copy_from_url(_blob)
            _result = _wait_for_fs_copy_completion(data["resGroup"], _blob, _dest_file)
        _copy_metadata.append(_file_properties_to_dict(_dest_file.get_file_properties()))
    return _copy_metadata


def check_copy_done(state: dict, _blob):
    result = False
    if state:
        for _rec in state:
            if _rec.get("fsource") and _rec.get("fsource") == _blob and _rec.get("status") == "success":
                result = True
                break
            else:
                result = False
    return result


def _get_sa_info(res_grp_name: str, acc_name: str):
    ret_val = dict()
    for i in client().resources.list_by_resource_group(res_grp_name):
        if i.type == hcs_constants.MS_STORAGE_ACCOUNTS:
            storage_keys = sclient().storage_accounts.list_keys(res_grp_name, acc_name)
            storage_keys = {v.key_name: v.value for v in storage_keys.keys}
            ret_val["storage_key"] = storage_keys["key1"]
    return ret_val


def _get_des_client(res_grp: str, des_share_name: str, storage_acc_name: str):
    _dest_client = None
    try:
        ret_val = _get_sa_info(res_grp, storage_acc_name)
        if ret_val:
            acc_key = ret_val.get("storage_key")
            des_con_str = (
                hcs_constants.CONN_STR_1
                + storage_acc_name
                + hcs_constants.CONN_STR_2
                + acc_key
                + hcs_constants.CONN_STR_3
            )
            _dest_client = ShareClient.from_connection_string(des_con_str, des_share_name)
        else:
            raise Exception("Unknown error occurred while copying source files to storage account")
    except ResourceNotFoundError as e:
        pass
    except Exception as e:
        raise Exception("Exception while creating destination client.") from e
    return _dest_client


def _file_properties_to_dict(_file_properties):
    return {
        "name": _file_properties.name,
        "path": _file_properties.path,
        "share": _file_properties.share,
        "size": _file_properties.size,
        "status": _file_properties.copy.status,
        "fsource": _file_properties.copy.source,
    }


def _wait_for_fs_copy_completion(res_group: str, _blob: str, _dest_file: ShareFileClient, timeout: str = "10m"):
    name = "fs-copy-completion-/" + res_group

    def fn_get():
        return _check_fs_copy_done(_blob, _dest_file)

    status_map = {
        "ready": hcs_constants.COMPLETE,
        "error": hcs_constants.ERROR,
        "transition": hcs_constants.FS_COPY_TRANSITION_STATUS,
    }
    return wait_for_res_status(
        resource_name=name, fn_get=fn_get, get_status=hcs_constants.STATUS, status_map=status_map, timeout=timeout
    )


def _check_fs_copy_done(_blob: str, _dest_file: ShareFileClient):
    _result = dict()
    _result["status"] = hcs_constants.START
    try:
        _f_prop = _dest_file.get_file_properties()
        _f_copy_status = _f_prop["copy"]["status"]
        if _f_prop and _f_copy_status == hcs_constants.SUCCESS:
            _result["status"] = hcs_constants.COMPLETE
        else:
            _result["status"] = hcs_constants.INCOMPLETE
    except Exception as e:
        _result["status"] = hcs_constants.ERROR
        raise
    return _result


def fs_refresh(data: dict, state: dict):
    if _is_fs_res_grp_exists(data["resGroup"]):
        _file_list = _get_sa_fs(data)
        if state:
            for _rec in state:
                if _rec.get("name") and _rec.get("name") not in _file_list:
                    _rec["status"] = hcs_constants.START
    return state


def _get_sa_fs(data: dict):
    _file_list = []
    try:
        _full_file_path = data["destinationShareName"] + hcs_constants.FORWARD_SLASH + data["filePath"]
        _dest_client = _get_des_client(data["resGroup"], _full_file_path, data["storageAccountName"])
        if _dest_client:
            _file_list = [file["name"] for file in list(_dest_client.list_directories_and_files())]
    except ResourceNotFoundError as e:
        pass
    return _file_list


def fs_delete(data: dict):
    if _is_fs_res_grp_exists(data["resGroup"]):
        _file_list = _get_sa_fs(data)
        _source_files = data["sourceFiles"]
        _file_path = data["filePath"]
        _dest_client = _get_des_client(data["resGroup"], data["destinationShareName"], data["storageAccountName"])
        for _blob in _source_files:
            _f_name = _blob.split(hcs_constants.FORWARD_SLASH)[-1]
            if _file_list and _f_name in _file_list:
                _dest_file = _dest_client.get_file_client(_file_path + _f_name)
                _dest_file.delete_file()
    return


def _is_fs_res_grp_exists(res_grp_name: str):
    ret_val = False
    try:
        for _i in client().resources.list_by_resource_group(res_grp_name):
            if _i and _i.id and res_grp_name in _i.id:
                ret_val = True
                break
            else:
                ret_val = False
    except ResourceNotFoundError as e:
        ret_val = False
    return ret_val
