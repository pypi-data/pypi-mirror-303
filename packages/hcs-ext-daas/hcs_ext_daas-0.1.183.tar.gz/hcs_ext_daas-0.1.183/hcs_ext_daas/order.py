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

from hcs_core.ctxp import context
from datetime import datetime, timezone

_config_name = "daas-order"


def get():
    return _get_config()


def add(data: dict):
    current_orders = _get_config()
    current_orders.update(data)
    return context.set(_config_name, current_orders)


def remove(order_type: str):
    current_orders = _get_config()

    if not order_type in current_orders.keys():
        return

    removed_order = current_orders.pop(order_type)
    removed_order["deleted_at"] = str(datetime.now(timezone.utc))
    current_orders["deleted"].append({order_type: removed_order})
    return context.set(_config_name, current_orders)


def file():
    data = _get_config()
    context.set(_config_name, data)
    return context.file(_config_name)


def _get_config():
    return context.get(_config_name, default={"deleted": []})
