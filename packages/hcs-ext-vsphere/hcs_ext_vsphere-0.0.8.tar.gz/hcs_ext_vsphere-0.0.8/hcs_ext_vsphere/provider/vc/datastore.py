from . import govc


def get(name: str, datacenter_name: str) -> dict:
    ret = govc.get(f"datastore.info -json -dc={datacenter_name} {name}", raise_on_failure=True)
    if ret:
        dc = ret["datastores"][0]
        dc["mor"] = dc["self"]["value"]
        return dc
