from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class TimePicker(BaseElement):
    def __init__(
        self,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        **kwargs: Unpack[TTimePickerProps],
    ):
        super().__init__("t-time-picker")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_clear(self, handler: ui.TEvent):
        self.on("clear", handler)
        return self

    def on_close(self, handler: ui.TEvent):
        self.on("close", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_input(self, handler: ui.TEvent):
        self.on("input", handler)
        return self

    def on_open(self, handler: ui.TEvent):
        self.on("open", handler)
        return self

    def on_pick(self, handler: ui.TEvent):
        self.on("pick", handler)
        return self


class TimeRangePicker(BaseElement):
    def __init__(
        self,
        value: typing.Optional[list] = None,
        *,
        model_value: typing.Optional[list] = None,
        **kwargs: Unpack[TTimeRangePickerProps],
    ):
        super().__init__("t-time-range-picker")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_input(self, handler: ui.TEvent):
        self.on("input", handler)
        return self

    def on_pick(self, handler: ui.TEvent):
        self.on("pick", handler)
        return self


class TTimePickerProps(TypedDict, total=False):
    allow_input: bool
    borderless: bool
    clearable: bool
    disable_time: str
    disabled: bool
    format: str
    hide_disabled_time: bool
    input_props: dict
    label: str
    placeholder: str
    popup_props: dict
    presets: dict
    readonly: bool
    select_input_props: dict
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    steps: list
    tips: str
    default_value: str
    value_display: str
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_close: ui.TEvent
    on_confirm: ui.TEvent
    on_focus: ui.TEvent
    on_input: ui.TEvent
    on_open: ui.TEvent
    on_pick: ui.TEvent


class TTimeRangePickerProps(TypedDict, total=False):
    allow_input: bool
    auto_swap: bool
    borderless: bool
    clearable: bool
    disable_time: str
    disabled: bool | list
    format: str
    hide_disabled_time: bool
    label: typing.Literal["TNode"]
    placeholder: typing.Literal["Array"]
    popup_props: dict
    presets: dict
    range_input_props: dict
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    steps: list
    tips: typing.Literal["TNode"]
    default_value: list
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_focus: ui.TEvent
    on_input: ui.TEvent
    on_pick: ui.TEvent
