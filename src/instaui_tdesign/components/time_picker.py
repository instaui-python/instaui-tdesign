from __future__ import annotations

import typing

from instaui.internal.ui.event import EventMixin
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

    def on_blur(self, handler: EventMixin):
        self.on("blur", handler)
        return self

    def on_change(self, handler: EventMixin):
        self.on("change", handler)
        return self

    def on_clear(self, handler: EventMixin):
        self.on("clear", handler)
        return self

    def on_close(self, handler: EventMixin):
        self.on("close", handler)
        return self

    def on_confirm(self, handler: EventMixin):
        self.on("confirm", handler)
        return self

    def on_focus(self, handler: EventMixin):
        self.on("focus", handler)
        return self

    def on_input(self, handler: EventMixin):
        self.on("input", handler)
        return self

    def on_open(self, handler: EventMixin):
        self.on("open", handler)
        return self

    def on_pick(self, handler: EventMixin):
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

    def on_blur(self, handler: EventMixin):
        self.on("blur", handler)
        return self

    def on_change(self, handler: EventMixin):
        self.on("change", handler)
        return self

    def on_focus(self, handler: EventMixin):
        self.on("focus", handler)
        return self

    def on_input(self, handler: EventMixin):
        self.on("input", handler)
        return self

    def on_pick(self, handler: EventMixin):
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
    on_blur: EventMixin
    on_change: EventMixin
    on_clear: EventMixin
    on_close: EventMixin
    on_confirm: EventMixin
    on_focus: EventMixin
    on_input: EventMixin
    on_open: EventMixin
    on_pick: EventMixin


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
    on_blur: EventMixin
    on_change: EventMixin
    on_focus: EventMixin
    on_input: EventMixin
    on_pick: EventMixin
