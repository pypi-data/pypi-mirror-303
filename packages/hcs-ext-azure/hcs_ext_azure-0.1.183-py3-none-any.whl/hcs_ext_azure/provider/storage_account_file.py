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

from hcs_core.plan import actions, PluginException
from hcs_ext_daas.av_helper import fs_copy, fs_delete, fs_refresh

import logging

log = logging.getLogger(__name__)


def deploy(data: dict, state: dict, save_state) -> dict:
    try:
        deployment = fs_copy(data, state)
    except Exception as e:
        raise PluginException("Exception while copying AV files to storage account.") from e
    return deployment


def refresh(data: dict, state: dict) -> dict:
    return fs_refresh(data, state)


def decide(data: dict, state: dict):
    _is_skip = True
    if state:
        for _rec in state:
            if _rec.get("status") and _rec.get("status") != "success":
                _is_skip = False
                break
    if _is_skip:
        return actions.skip


def destroy(data: dict, state: dict, force: bool) -> dict:
    return fs_delete(data)
    # TODO: Implement wait


def eta(action: str, data: dict, state: dict):
    return "3m"
