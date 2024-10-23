from subprocess import PIPE, Popen
from .exceptions import MokuException


def check_mokucli_version(cli_path, req_ver=None):
    if cli_path:
        out, _ = Popen([cli_path, "--version"], stdout=PIPE, stderr=PIPE).communicate()
        if out:
            ver_str = out.decode("utf8").rstrip()
            if not req_ver:
                return
            result = ver_str.split("mokucli")[1].strip().split(".")
            _ma, _mi, _pa = map(int, result)
            if all([_ma >= req_ver[0], _mi >= req_ver[1], _pa >= req_ver[2]]):
                return
    req_ver_str = f"{req_ver[0]}.{req_ver[1]}.{req_ver[2]}" if req_ver else ""
    raise MokuException(
        f"Cannot find mokucli {req_ver_str}. \n"
        "Please download latest version of the CLI from https://www.liquidinstruments.com/software/utilities/. \n"  # noqa
        "If you have already installed, please set the MOKU_CLI_PATH environment variable to absolute path of mokucli."
    )  # noqa
