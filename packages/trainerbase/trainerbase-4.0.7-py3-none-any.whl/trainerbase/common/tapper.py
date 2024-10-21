from collections.abc import Callable
from enum import StrEnum, auto
from functools import partial
from typing import assert_never, override

from keyboard import send
from mouse import click

from trainerbase.abc import Switchable
from trainerbase.scriptengine import ScriptEngine


class TappingDevice(StrEnum):
    MOUSE = auto()
    KEYBOARD = auto()

    @property
    def function(self) -> Callable[[str], None]:
        match self:
            case self.MOUSE:
                return click
            case self.KEYBOARD:
                return send
            case _:
                assert_never(self)


class Tapper(Switchable):
    def __init__(self, default_delay: float, tap_button: str = "left", device: TappingDevice = TappingDevice.MOUSE):
        self._delay = default_delay
        self.button = tap_button
        self.device = device
        self.tapper_script_engine: ScriptEngine | None = None
        self.tapper_function = partial(device.function, tap_button)

    @override
    def enable(self):
        self.disable()

        self.tapper_script_engine = ScriptEngine(self._delay)
        self.tapper_script_engine.simple_script(self.tapper_function, enabled=True)
        self.tapper_script_engine.start()

    @override
    def disable(self):
        if self.tapper_script_engine is not None:
            self.tapper_script_engine.stop()

    @property
    def delay(self):
        return self._delay

    @delay.setter
    def delay(self, new_delay: float):
        if self.tapper_script_engine is not None:
            self.tapper_script_engine.delay = new_delay

        self._delay = new_delay
