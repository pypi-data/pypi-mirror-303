from . import govc
import json
import tempfile
import os


def create_from_lib(
    lib_template_path: str,
    datacenter_name: str,
    host: str,
    folder_path: str,
    datastore_name: str,
    pool_path: str,
    ovf_spec: dict,
):
    # govc library.deploy -options edge-ovf-spec-nanw.json -dc=WDC-4 -folder=/WDC-4/vm/EdgeVMs -ds=/WDC-4/datastore/vsanDatastore -pool=/WDC-4/host/POD30/Resources/EdgeVMs /edgecontentlib/edge-gw-2.3.2.0-21738834_OVF10 Nanw-edge
    folder = f"/{datacenter_name}/vm/{folder_path}"
    ds = f"/{datacenter_name}/datastore/{datastore_name}"
    pool = f"/{datacenter_name}/host/{host}/Resources/{pool_path}"
    name = ovf_spec["Name"]

    temp_fd, temp_file_name = tempfile.mkstemp()
    try:
        os.write(temp_fd, str.encode(json.dumps(ovf_spec, indent=4)))
    finally:
        os.close(temp_fd)

    try:
        cmd = f"library.deploy -options {temp_file_name} -dc={datacenter_name} -folder={folder} -ds={ds} -pool={pool} {lib_template_path} {name}"
        govc.run(cmd, raise_on_failure=True)
        return get(datacenter_name, folder_path, name)
    finally:
        os.remove(temp_file_name)


def destroy(datacenter_name: str, folder_path: str, vm_name: str):
    return govc.get(f"vm.destroy -json -vm.ipath=/{datacenter_name}/vm/{folder_path}/{vm_name}")


def get(datacenter_name: str, folder_path: str, vm_name: str):
    if datacenter_name:
        cmd = f"vm.info -json -vm.ipath=/{datacenter_name}/vm/{folder_path}/{vm_name}"
        ret = govc.get(cmd, as_json=True)
    else:
        cmd = f"vm.info -json {vm_name}"
        ret = govc.get(cmd, as_json=True)

    if ret:
        ret = ret.get("virtualMachines")
        if ret:
            vm = ret[0]
            vm["mor"] = vm["self"]["value"]
            return vm


def get_snapshot_tree(datacenter_name: str, folder_path: str, vm_name: str) -> dict:
    if datacenter_name:
        cmd = f"snapshot.tree -i -json -vm.ipath=/{datacenter_name}/vm/{folder_path}/{vm_name}"
    else:
        cmd = f"snapshot.tree -i -json -vm {vm_name}"
    return govc.get(cmd, as_json=True, raise_on_failure=True)


def info(datacenter_name: str, folder_path: str, vm_name: str) -> dict:
    if datacenter_name:
        cmd = f"vm.info -json -vm.ipath=/{datacenter_name}/vm/{folder_path}/{vm_name}"
    else:
        cmd = f"vm.info -json -vm {vm_name}"
    ret = govc.get(cmd, as_json=True, raise_on_failure=True)
    if ret:
        ret = ret.get("virtualMachines")
        if ret:
            return ret[0]
