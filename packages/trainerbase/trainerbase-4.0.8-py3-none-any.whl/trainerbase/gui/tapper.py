from typing import override
from uuid import uuid4

from dearpygui import dearpygui as dpg

from trainerbase.common.keyboard import ReleaseHotkeySwitch
from trainerbase.common.tapper import Tapper
from trainerbase.gui.helpers import add_components
from trainerbase.gui.misc import HotkeyHandlerUI, TextUI
from trainerbase.gui.types import AbstractUIComponent


class TapperUI(AbstractUIComponent):
    DPG_TAG_TAPPER_DELAY_INPUT_PREFIX = "tag_tapper_delay_input"
    DPG_TAG_TAPPER_PRESET_INPUT_PREFIX = "tag_tapper_preset_input"

    PRESETS: tuple[float, ...] = (0.05, 0.15, 0.25, 0.3, 0.5, 0.7, 1, 2, 5, 10)

    def __init__(
        self,
        tapper: Tapper | None = None,
        key: str = "PageUp",
        default_delay: float = 0.15,
    ):
        if tapper is None:
            self.tapper = Tapper(default_delay)
            self.default_delay = default_delay
        else:
            self.tapper = tapper
            self.default_delay = tapper.delay

        self.key = key
        self.dpg_tag_tapper_delay_input = f"{self.DPG_TAG_TAPPER_DELAY_INPUT_PREFIX}_{uuid4()}"
        self.dpg_tag_tapper_preset_input = f"{self.DPG_TAG_TAPPER_PRESET_INPUT_PREFIX}_{uuid4()}"

    @override
    def add_to_ui(self) -> None:
        add_components(
            TextUI(f"Tapper for {self.tapper.device} {self.tapper.button}"),
            HotkeyHandlerUI(ReleaseHotkeySwitch(self.tapper, self.key), "Tapper"),
        )

        dpg.add_input_double(
            tag=self.dpg_tag_tapper_delay_input,
            label="Tapper Delay",
            min_value=0.0,
            max_value=60.0,
            default_value=self.default_delay,
            min_clamped=True,
            max_clamped=True,
            callback=self.on_delay_change,
        )

        dpg.add_slider_int(
            tag=self.dpg_tag_tapper_preset_input,
            label="Preset",
            min_value=0,
            max_value=len(self.PRESETS) - 1,
            clamped=True,
            default_value=self.get_closest_preset_index(self.default_delay),
            callback=self.on_preset_change,
        )

    def on_preset_change(self):
        new_delay = self.PRESETS[dpg.get_value(self.dpg_tag_tapper_preset_input)]
        self.tapper.delay = new_delay
        dpg.set_value(self.dpg_tag_tapper_delay_input, new_delay)

    def on_delay_change(self):
        new_delay = dpg.get_value(self.dpg_tag_tapper_delay_input)
        closest_preset_index = self.get_closest_preset_index(new_delay)
        self.tapper.delay = new_delay
        dpg.set_value(self.dpg_tag_tapper_preset_input, closest_preset_index)

    def get_closest_preset_index(self, delay: float) -> int:
        closest_preset = min(self.PRESETS, key=lambda preset: abs(preset - delay))
        return self.PRESETS.index(closest_preset)
