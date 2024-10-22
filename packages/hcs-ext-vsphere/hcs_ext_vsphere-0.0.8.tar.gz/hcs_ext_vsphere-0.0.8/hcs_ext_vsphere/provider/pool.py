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

from hcs_core.plan import actions
from . import vc


def deploy(data: dict, state: dict) -> dict:
    ipath = data["ipath"]
    pool = vc.pool.get(ipath)
    if not pool:
        pool = vc.pool.create(ipath)
    return pool


def refresh(data: dict, state: dict) -> dict:
    ipath = data["ipath"]
    return vc.pool.get(ipath)


def decide(data: dict, state: dict):
    return actions.skip


def destroy(data: dict, state: dict, force: bool) -> dict:
    ipath = data["ipath"]
    return vc.pool.destroy(ipath)


def eta(action: str, data: dict, state: dict):
    if action == actions.create:
        return "10s"
    if action == actions.delete:
        return "10s"


def text(state: dict) -> str:
    name = state.get("name")
    mor = state.get("self", {}).get("value")
    return f"{name} ({mor})"
