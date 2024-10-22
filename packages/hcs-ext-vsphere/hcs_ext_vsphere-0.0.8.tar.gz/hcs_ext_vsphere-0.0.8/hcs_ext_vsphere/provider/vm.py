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
    container = data["container"]
    dc = container["datacenter"]
    folder = container["folder"]
    ds = container["datastore"]
    host = container["host"]
    pool = container["pool"]
    template = data["template"]
    ovf_spec = data["ovfSpec"]
    name = ovf_spec["Name"]
    vm = vc.vm.get(dc, folder, name)
    if not vm:
        vm = vc.vm.create_from_lib(template, dc, host, folder, ds, pool, ovf_spec)
    return vm


def refresh(data: dict, state: dict) -> dict:
    container = data["container"]
    dc = container["datacenter"]
    folder = container["folder"]
    ovf_spec = data["ovfSpec"]
    name = ovf_spec["Name"]
    return vc.vm.get(dc, folder, name)


def decide(data: dict, state: dict):
    return actions.skip


def destroy(data: dict, state: dict, force: bool) -> dict:
    container = data["container"]
    dc = container["datacenter"]
    folder = container["folder"]
    ovf_spec = data["ovfSpec"]
    name = ovf_spec["Name"]
    return vc.vm.destroy(dc, folder, name)


def eta(action: str, data: dict, state: dict):
    if action == actions.create:
        return "3m"
    if action == actions.delete:
        return "1m"


def text(vm: dict):
    return f'{vm["name"]} ({vm["self"]["value"]})'
