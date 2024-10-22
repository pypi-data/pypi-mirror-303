import logging
from . import govc
from hcs_core.util import ssl_util

log = logging.getLogger(__name__)

info = {}


def init(config: dict, test_health: bool = True):
    global info
    if not info:
        govc.init(config)
        thumbprint = ssl_util.get_cert_thumbprints(config["url"])
        if test_health:
            about = govc.get("about -json", as_json=True, raise_on_failure=True)
            if about:
                about = about.get("about")
        info |= {"config": config, "about": about, "thumbprint": thumbprint}
    return info
