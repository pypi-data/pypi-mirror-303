import json
from pathlib import Path

from moku import Moku
from moku.exceptions import InvalidParameterException, MokuException


class NeuralNetwork(Moku):
    """Neural Network instrument object.

    The Neural Network instrument allows running feed forward, multi-layer
    neural networks on serial and parallel input signals.

    """

    def __init__(self, multi_instrument, slot=None, **kwargs):
        self.id = 128
        self.operation_group = "neuralnetwork"

        if multi_instrument is None:
            raise MokuException(
                "Neural Network instrument can only be run in multi-instrument mode"
            )

        self.platform_id = multi_instrument.platform_id
        self.slot = slot
        self.session = multi_instrument.session
        self.firmware_version = multi_instrument.firmware_version
        self.hardware = multi_instrument.hardware
        self.bitstreams = multi_instrument.bitstreams
        self.manage_bitstreams = multi_instrument.manage_bitstreams
        self.upload_bitstream(f"{self.platform_id:02}-{self.id:03}-{self.slot - 1:02}")
        self.session.get(f"slot{self.slot}", self.operation_group)

    @classmethod
    def for_slot(cls, slot, multi_instrument):
        """
        Configures instrument at given slot in multi instrument mode.
        """
        return cls(slot=slot, multi_instrument=multi_instrument)

    def summary(self):
        """
        summary.
        """
        operation = "summary"
        return self.session.get(f"slot{self.slot}/{self.operation_group}", operation)

    def set_defaults(self):
        """Set the Neural Network to sane defaults"""
        operation = "set_defaults"
        return self.session.post(
            f"slot{self.slot}/{self.operation_group}",
            operation,
        )

    def set_input_sample_rate(self, sample_rate, strict=True):
        """
        Set the input samplerate

        type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        type sample_rate: `number`
        :param sample_rate: Input sample rate

        """
        operation = "set_input_sample_rate"
        params = dict(sample_rate=sample_rate, strict=strict)
        return self.session.post(
            f"slot{self.slot}/{self.operation_group}", operation, params
        )

    def set_input(self, channel, low_level, high_level, strict=True):
        """
        Set the voltage range for a a given input

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type channel: `integer`
        :param channel: Target channel

        :type low_level: `number`
        :param low_level: Low level

        :type high_level: `number`
        :param high_level: High level

        """
        operation = "set_input"
        params = dict(
            channel=channel, low_level=low_level, high_level=high_level, strict=strict
        )
        return self.session.post(
            f"slot{self.slot}/{self.operation_group}", operation, params
        )

    def set_output(
        self, channel, enabled, low_level=None, high_level=None, strict=True
    ):
        """
        Set the output range for a given output

        :type strict: `boolean`
        :param strict: Disable all implicit conversions and coercions.

        :type channel: `integer`
        :param channel: Target channel

        :type enabled: `boolean`
        :param enabled: Enable or disable the output channel

        :type low_level: `number`
        :param low_level: Low level

        :type high_level: `number`
        :param high_level: High level

        """
        operation = "set_output"
        params = dict(
            channel=channel,
            enabled=enabled,
            low_level=low_level,
            high_level=high_level,
            strict=strict,
        )
        return self.session.post(
            f"slot{self.slot}/{self.operation_group}", operation, params
        )

    def upload_network(self, linn):
        """
        Upload a neural network in .linn JSON format.

        :type linn: `dict` or `path`
        :param linn: A dict like linn data or absolute path to linn file
        """
        network = None
        if isinstance(linn, dict):
            network = linn
        else:
            p = Path(linn)
            if not all([p.exists(), p.is_file()]):
                raise InvalidParameterException(
                    f"Cannot find {linn}, make sure the file exists"
                )
            network = json.loads(p.read_text())

        operation = "upload_network"
        return self.session.post_raw_json(
            f"slot{self.slot}/{self.operation_group}", operation, network
        )

    def describe_network(self):
        """
        Provide a description of the currently loaded network
        """
        operation = "describe_network"
        return self.session.get(f"slot{self.slot}/{self.operation_group}", operation)
