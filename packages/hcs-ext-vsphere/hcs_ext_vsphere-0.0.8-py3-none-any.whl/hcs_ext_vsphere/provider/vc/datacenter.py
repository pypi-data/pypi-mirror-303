from . import govc


def get(name: str) -> dict:
    ret = govc.get(f"datacenter.info -json {name}", raise_on_failure=True)
    if ret:
        dc = ret["datacenters"][0]
        dc["mor"] = dc["self"]["value"]
        return dc
