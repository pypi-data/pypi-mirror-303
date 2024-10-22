import subprocess
import json
import os

_env = {
    "GOVC_URL": None,
    "GOVC_USERNAME": None,
    "GOVC_PASSWORD": None,
    "GOVC_TLS_CA_CERTS": None,
    "GOVC_TLS_KNOWN_HOSTS": None,
    "GOVC_TLS_HANDSHAKE_TIMEOUT": None,
    "GOVC_INSECURE": "1",
    "GOVC_DATACENTER": None,
    "GOVC_DATASTORE": None,
    "GOVC_NETWORK": None,
    "GOVC_RESOURCE_POOL": None,
    "GOVC_HOST": None,
    "GOVC_GUEST_LOGIN": None,
    "GOVC_VIM_NAMESPACE": None,
    "GOVC_VIM_VERSION": None,
    "GOVC_VI_JSON": None,
}
_effective_env = {}


def init(config: dict = None):
    ignored = ["THUMBPRINT"]

    effective_config = {}
    if config:
        for k in config:
            v = config[k]
            k = k.upper()
            if k in ignored:
                continue
            k2 = k if k.startswith("GOVC_") else "GOVC_" + k
            if k2 not in _env:
                raise Exception("Unknown config: " + k)
            effective_config[k2] = v

    effective_config = os.environ | effective_config

    global _effective_env
    _effective_env = _env | effective_config

    keys = list(_effective_env.keys())
    for k in keys:
        if _effective_env[k] is None:
            del _effective_env[k]

    required = ["GOVC_URL"]

    for k in required:
        if not _effective_env[k]:
            raise Exception("Missing required GOVC config: " + k)

    # print("ENV:", json.dumps(_effective_env, indent=4))


def run(cmd, raise_on_failure: bool = False) -> subprocess.CompletedProcess:
    if type(cmd) == str:
        cmd = "govc " + cmd
    elif isinstance(cmd, list):
        cmd.insert(0, "govc")
    else:
        raise Exception(f"Unknown cmd argument type: {type(cmd).__name__}")

    # print("CMD:", cmd)
    p = subprocess.run(
        cmd, capture_output=True, shell=True, cwd=None, timeout=None, check=False, text=True, env=_effective_env
    )

    if p.returncode and raise_on_failure:
        raise Exception(f"Fail running command: '{cmd}'. Return={p.returncode}, STDOUT={p.stdout}, STDERR={p.stderr}")
    return p


def get(cmd: str, as_json: bool = True, raise_on_failure: bool = False) -> dict:
    p = run(cmd, raise_on_failure)
    if p.returncode:
        if raise_on_failure:
            raise Exception(
                f"Fail running command: {p.args}. Return={p.returncode}, STDOUT={p.stdout}, STDERR={p.stderr}"
            )

    output = p.stdout
    # this looks like a govc inconsistency bug. E.g. govc snapshot.tree has output in stderr.
    if not output and p.returncode == 0 and p.stderr:
        output = p.stderr

    if output:
        if as_json:
            return json.loads(output)
        return p.stdout
