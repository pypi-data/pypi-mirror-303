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

import json
import logging
from .. import vc
from hcs_core.ctxp import CtxpException

log = logging.getLogger(__name__)


def _managed_obj_summary(obj):
    return {
        "type": obj["self"]["type"],
        "mor": obj["self"]["value"],
        "name": obj["name"],
    }


def _find_snapshot(input: dict):
    datacenter = input.get("datacenter")
    folder_path = input.get("folder_path")
    vm_name = input.get("vm_name")
    snapshot_name = input.get("snapshot_name")

    tree = vc.vm.get_snapshot_tree(datacenter_name=datacenter, folder_path=folder_path, vm_name=vm_name)

    def _is_target_node(n):
        if snapshot_name:
            return n.get("name") == snapshot_name
        else:
            return n.get("current")

    def _dfs(n):
        # print(n)
        if not n:
            return
        if _is_target_node(n):
            return n
        children = n.get("childSnapshotList")
        if not children:
            return
        for c in children:
            t = _dfs(c)
            if t:
                return t

    return _dfs({"childSnapshotList": tree})


def _find_snapshot2(input: dict):
    datacenter = input.get("datacenter")
    folder_path = input.get("folder_path")
    vm_name = input.get("vm_name")
    snapshot_name = input.get("snapshot_name")

    vm_info = vc.vm.info(datacenter_name=datacenter, folder_path=folder_path, vm_name=vm_name)

    def _is_target_node(n):
        if snapshot_name:
            return n.get("name") == snapshot_name
        else:
            return n["snapshot"]["value"] == vm_info["snapshot"]["currentSnapshot"]["value"]

    def _dfs(n):
        # print(n)
        if not n:
            return
        if _is_target_node(n):
            return n
        children = n.get("childSnapshotList")
        if not children:
            return
        for c in children:
            t = _dfs(c)
            if t:
                return t

    tree = {"snapshot": {"value": None}, "name": None, "childSnapshotList": vm_info["snapshot"]["rootSnapshotList"]}
    ret = _dfs(tree)

    if ret:
        ret["vmInstanceUuid"] = vm_info["config"]["instanceUuid"]
    return ret


def _find_datacenter(input: dict):
    name = input["name"]
    r = vc.datacenter.get(name)
    if not r:
        raise Exception("Datacenter not found: " + name)
    return _managed_obj_summary(r)


def _find_datastore(input: dict):
    name = input["name"]
    dc_name = input["datacenter"]
    r = vc.datastore.get(name, datacenter_name=dc_name)
    if not r:
        raise Exception("Datastore not found: " + name)
    ret = _managed_obj_summary(r)
    ret["datastoreType"] = "VSAN"  # TODO
    return ret


def _find_network(input: dict):
    name = input["name"]
    datacenter_name = input["datacenter"]
    r = vc.network.get(name, datacenter_name)
    if not r:
        raise Exception("Network not found: " + name)
    return _managed_obj_summary(r)


_fn_map = {
    "snapshot": _find_snapshot2,
    "datacenter": _find_datacenter,
    "datastore": _find_datastore,
    "network": _find_network,
}


def process(data: dict, state: dict) -> dict:
    ret = {}
    for k in data:
        type = data[k]["type"]
        input = data[k]["data"]
        fn = _fn_map.get(type)
        if not fn:
            raise Exception(f"Unknown type: {type}")
        ret[k] = fn(input)
    return ret


def destroy(data: dict, state: dict, force: bool):
    return


def eta(action: str, data: dict, state: dict):
    return "1m"
