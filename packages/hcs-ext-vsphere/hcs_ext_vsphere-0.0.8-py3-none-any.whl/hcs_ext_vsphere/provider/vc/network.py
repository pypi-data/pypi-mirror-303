from . import govc


def get(name: str, datacenter_name: str) -> dict:
    ret = govc.get(f"ls -json /{datacenter_name}/network/{name}", raise_on_failure=True)
    if ret:
        r = ret["elements"][0]["Object"]
        r["mor"] = r["self"]["value"]
        return r
