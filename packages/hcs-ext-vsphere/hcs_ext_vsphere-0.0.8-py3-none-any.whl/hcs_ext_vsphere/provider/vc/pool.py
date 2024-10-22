from . import govc


def create(ipath: str):
    govc.run(f"pool.create -json {ipath}", raise_on_failure=True)
    return get(ipath)


def destroy(ipath: str):
    govc.run(f"pool.destroy -json {ipath}", raise_on_failure=True)


def get(ipath: str):
    ret = govc.get(f"pool.info -json {ipath}", raise_on_failure=False)
    if not ret:
        return
    items = ret.get("resourcePools")
    if not items:
        return
    ret = items[0]
    ret["mor"] = ret["self"]["value"]
    return ret
