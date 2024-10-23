import json
import pathlib
import tarfile
from os import environ
from pathlib import Path
from shutil import which

from moku.exceptions import (IncompatibleMokuException,
                             IncompatiblePackageException, MokuException,
                             NoInstrumentBitstream)
from moku.session import RequestSession
from moku.version import MIN_COMPAT_FW, SUPPORTED_PROXY_VERSION

_data_path = environ.get("MOKU_DATA_PATH", str(Path(__file__).parent.joinpath("data")))
MOKU_DATA_PATH = Path(_data_path).expanduser()

MOKU_CLI_PATH = environ.get("MOKU_CLI_PATH", which("mokucli"))
if MOKU_CLI_PATH:
    MOKU_CLI_PATH = str(Path(MOKU_CLI_PATH).expanduser())


class Moku:
    """
    Moku base class. This class does all the heavy lifting required to
    deploy and control instruments.
    """

    def __init__(
        self,
        ip,
        force_connect,
        ignore_busy,
        persist_state,
        connect_timeout,
        read_timeout,
        **kwargs,
    ):
        self.session = RequestSession(ip, connect_timeout, read_timeout, **kwargs)
        self.claim_ownership(force_connect, ignore_busy, persist_state)

        props = self.describe()

        if "proxy_version" not in props:
            raise IncompatibleMokuException(
                f"Incompatible Moku firmware, this version of "
                f"package supports firmware version"
                f"{MIN_COMPAT_FW} or above."
            )

        if int(props["proxy_version"]) < SUPPORTED_PROXY_VERSION:
            raise IncompatiblePackageException(
                f"Incompatible Moku package, please update the package using pip"
            )
        elif int(props["proxy_version"]) > SUPPORTED_PROXY_VERSION:
            raise IncompatibleMokuException(
                "You are using an old version of Moku firmware. "
                "Please update your firmware to the latest version using the Moku Desktop app."
            )

        self.firmware_version = props["firmware"]
        self.hardware = props["hardware"].replace(":", "").lower()
        self.bitstreams = props["bitstreams"]
        self.manage_bitstreams = kwargs.get("manage_bitstreams", True)
        self.claim_ownership(force_connect, ignore_busy, persist_state)

    def _upload_bitstream_if_required(self, bs_name, rmt_chksum, bs_path=None):
        if bs_path:
            bs_path = pathlib.Path(bs_path)
            if not bs_path.exists():
                raise MokuException(f"Cannot find {bs_path}")
            bs_file_name = bs_name
        else:
            fw_ver_base = self.firmware_version.split(".")[0]
            bs_path = self._get_data_file(fw_ver_base)
            hw_dir = {"mokupro": "mokupro", "mokugo": "mokugo", "mokulab": "moku20"}
            bs_file_name = f"{hw_dir[self.hardware]}/{bs_name}"

        with tarfile.open(bs_path) as _ts:
            bar_data = _ts.extractfile(bs_file_name)
            with tarfile.open(fileobj=bar_data, mode="r") as _bar:
                bs_man_file = _bar.extractfile("MANIFEST")
                bs_manifest = json.loads(bs_man_file.read())
                local_chksum = bs_manifest["items"][0]["sha256"]
                if not (rmt_chksum and local_chksum == rmt_chksum):
                    bar_data.seek(0)
                    self.upload("bitstreams", bs_name, bar_data.read())

    def upload_bitstream(self, name, bs_path=None):
        if self.manage_bitstreams:
            name = f"{name}.bar"
            exists = [b[1] for b in self.bitstreams.items() if b[0] == name]
            rmt_chksum = exists[0] if exists else None
            self._upload_bitstream_if_required(name, rmt_chksum, bs_path)

    def set_connect_timeout(self, value):
        "Sets requests session connect timeout"
        if not isinstance(value, tuple([int, float])):
            raise ValueError(
                "set_connect_timeout value should be " "either integer or float"
            )
        self.session.connect_timeout = value

    def set_read_timeout(self, value):
        "Sets requests session read timeout"
        if not isinstance(value, tuple([int, float])):
            raise ValueError("read_timeout value should be either " "integer or float")
        self.session.read_timeout = value

    def platform(self, platform_id):
        "Configures platform for the given ID"
        platform_map = {"mokupro": [1, 4], "mokugo": [1, 2], "mokulab": [1, 2]}
        if platform_id not in platform_map[self.hardware]:
            raise MokuException(
                f"The platform_id {platform_id} is invalid. For '{self.hardware}' available options are {platform_map[self.hardware]}"
            )  # noqa

        operation = f"platform/{platform_id}"
        self.upload_bitstream(f"{platform_id:02}-000")
        for i in range(0, platform_id):
            self.upload_bitstream(f"{platform_id:02}-000-{i:02}")
        return self.session.get("moku", operation)

    @staticmethod
    def _get_data_file(firmware_version):
        file_name = f"mokudata-{firmware_version}.tar"
        path = MOKU_DATA_PATH.joinpath(file_name)
        if not path.exists():
            raise NoInstrumentBitstream(
                f"Instrument files not available, please run `moku download --fw_ver={firmware_version}` to download latest instrument data"
            )  # noqa
        return path

    def claim_ownership(
        self, force_connect=True, ignore_busy=False, persist_state=False
    ):
        """
        Claim the ownership of Moku.

        :type force_connect: `boolean`
        :param force_connect: Force connection to Moku disregarding any existing connections

        :type ignore_busy: `boolean`
        :param ignore_busy: Ignore the state of instrument including any in progress data logging sessions and proceed with the deployment # noqa

        :type persist_state: `boolean`
        :param persist_state: When true, tries to retain the previous state of the instrument(if available) # noqa

        """
        operation = "claim_ownership"
        params = dict(
            force_connect=force_connect,
            ignore_busy=ignore_busy,
            persist_state=persist_state,
        )
        return self.session.post("moku", operation, params)

    def relinquish_ownership(self):
        """
        Relinquish the ownership of Moku.
        """
        operation = "relinquish_ownership"
        return self.session.post("moku", operation)

    def name(self):
        """
        name.
        """
        operation = "name"
        return self.session.get("moku", operation)

    def serial_number(self):
        """
        serial_number.
        """
        operation = "serial_number"
        return self.session.get("moku", operation)

    def summary(self):
        """
        summary.
        """
        operation = "summary"
        return self.session.get("moku", operation)

    def describe(self):
        """
        describe.
        """
        operation = "describe"
        return self.session.get("moku", operation)

    def calibration_date(self):
        """
        calibration_date.
        """
        operation = "calibration_date"
        return self.session.get("moku", operation)

    def firmware_version(self):
        """
        firmware_version.
        """
        operation = "firmware_version"
        return self.session.get("moku", operation)

    def get_power_supplies(self):
        """
        get_power_supplies.
        """
        operation = "get_power_supplies"
        return self.session.get("moku", operation)

    def get_power_supply(self, id):
        """
        get_power_supply.

        :type id: `integer`
        :param id: ID of the power supply

        """
        operation = "get_power_supply"
        params = dict(
            id=id,
        )
        return self.session.post("moku", operation, params)

    def set_power_supply(self, id, enable=True, voltage=3, current=0.1):
        """
        set_power_supply.

        :type id: `integer`
        :param id: ID of the power supply to configure

        :type enable: `boolean`
        :param enable: Enable/Disable power supply

        :type voltage: `number`
        :param voltage: Voltage set point

        :type current: `number`
        :param current: Current set point

        """
        operation = "set_power_supply"
        params = dict(
            id=id,
            enable=enable,
            voltage=voltage,
            current=current,
        )
        return self.session.post("moku", operation, params)

    def get_external_clock(self):
        """
        get_external_clock.
        """
        operation = "get_external_clock"
        return self.session.get("moku", operation)

    def set_external_clock(self, enable=True):
        """
        set_external_clock.

        :type enable: `boolean`
        :param enable: Switch between external and internal reference clocks

        """
        operation = "set_external_clock"
        params = dict(
            enable=enable,
        )
        return self.session.post("moku", operation, params)

    def upload(self, target, file_name, data):
        """
        Upload files to bitstreams, ssd, logs, persist.

        :type target: `string`, (bitstreams, ssd, logs, persist, media)
        :param target: Destination where the file should be uploaded to.

        :type file_name: `string`
        :param file_name: Name of the file to be uploaded

        :type data: `bytes`
        :param data: File content

        """
        operation = f"upload/{file_name}"
        return self.session.post_file(target, operation, data)

    def delete(self, target, file_name):
        """
        Delete files from bitstreams, ssd, logs, persist.

        :type target: `string`, (bitstreams, ssd, logs, persist, media)
        :param target: Destination where the file should be uploaded to.

        :type file_name: `string`
        :param file_name: Name of the file to be deleted

        """
        operation = f"delete/{file_name}"
        return self.session.delete_file(target, operation)

    def list(self, target):
        """
        List files at bitstreams, ssd, logs, persist.

        :type target: `string`, (bitstreams, ssd, logs, persist, media)
        :param target: Target directory to list files for

        """
        operation = "list"
        return self.session.get(target, operation)

    def download(self, target, file_name, local_path):
        """
        Download files from bitstreams, ssd, logs, persist.

        :type target: `string`, (bitstreams, ssd, logs, persist, media)
        :param target: Destination where the file should be downloaded from.

        :type file_name: `string`
        :param file_name: Name of the file to be downloaded

        :type local_path: `string`
        :param local_path: Local path to download the file

        """
        operation = f"download/{file_name}"
        return self.session.get_file(target, operation, local_path)

    def modify_hardware(self, data=None):
        """
        CAUTION: Never use to update the state of the Moku
        Raw access to Moku hardware state
        """
        if data is None:
            data = {}
        return self.session.post("moku", "modify_hardware", data)

    def modify_calibration(self, data=None):
        """
        Query or update the calibration coefficients
        """
        if data is None:
            data = {}
        return self.session.post("moku", "modify_calibration", data)

    def set_configuration(self, data=None):
        """
        Update the Moku device/network configuration.
        """
        if data is None:
            data = {}
        return self.session.post("moku", "modify_calibration", data)

    def get_configuration(self):
        """
        Retreive the Moku device/network configuration.
        """
        return self.session.get("moku", "get_configuration")
