from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class InputNumber(BaseElement):
    def __init__(
        self,
        value: typing.Optional[typing.Union[str, int, float]] = None,
        *,
        model_value: typing.Optional[typing.Union[str, int, float]] = None,
        **kwargs: Unpack[TInputNumberProps],
    ):
        super().__init__("t-input-number")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_enter(self, handler: ui.TEvent):
        self.on("enter", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_keydown(self, handler: ui.TEvent):
        self.on("keydown", handler)
        return self

    def on_keypress(self, handler: ui.TEvent):
        self.on("keypress", handler)
        return self

    def on_keyup(self, handler: ui.TEvent):
        self.on("keyup", handler)
        return self

    def on_validate(self, handler: ui.TEvent):
        self.on("validate", handler)
        return self


class TInputNumberProps(TypedDict, total=False):
    align: typing.Literal["left", "center", "right"]
    allow_input_over_limit: bool
    auto_width: bool
    decimal_places: typing.Union[float, dict]
    disabled: bool
    format: str
    input_props: dict
    label: str
    large_number: bool
    max: typing.Union[float, str]
    min: typing.Union[float, str]
    placeholder: str
    readonly: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    step: typing.Union[float, str]
    suffix: str
    theme: typing.Literal["column", "row", "normal"]
    tips: str
    default_value: typing.Union[str, int, float]
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_keydown: ui.TEvent
    on_keypress: ui.TEvent
    on_keyup: ui.TEvent
    on_validate: ui.TEvent
