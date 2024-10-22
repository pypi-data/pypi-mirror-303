from . import govc


def create(ipath: str):
    govc.run(f"folder.create -json {ipath}", raise_on_failure=True)
    return get(ipath)


def destroy(ipath: str):
    govc.run(f"object.destroy -json {ipath}", raise_on_failure=False)


def get(ipath: str):
    ret = govc.get(f"folder.info -json {ipath}", raise_on_failure=False)
    if not ret:
        return
    items = ret.get("folders")
    if not items:
        return
    ret = items[0]
    ret["mor"] = ret["self"]["value"]
    return ret
