from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Textarea(BaseElement):
    def __init__(
        self,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        **kwargs: Unpack[TTextareaProps],
    ):
        super().__init__("t-textarea")

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


class TTextareaProps(TypedDict, total=False):
    allow_input_over_max: bool
    autofocus: bool
    autosize: typing.Union[bool, dict]
    disabled: bool
    maxcharacter: float
    maxlength: int
    name: str
    placeholder: str
    readonly: bool
    status: typing.Literal["default", "success", "warning", "error"]
    tips: str
    default_value: str
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_focus: ui.TEvent
    on_keydown: ui.TEvent
    on_keypress: ui.TEvent
    on_keyup: ui.TEvent
    on_validate: ui.TEvent
