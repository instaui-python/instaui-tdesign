from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import (
    make_prefix_icon,
    make_suffix_icon,
)

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Input(BaseElement):
    def __init__(
        self,
        value: typing.Optional[typing.Union[str, int, float]] = None,
        **kwargs: Unpack[TInputProps],
    ):
        super().__init__("t-input")
        model_value = kwargs.pop("model_value", None)
        prefix_icon = kwargs.pop("prefix_icon", None)
        suffix_icon = kwargs.pop("suffix_icon", None)

        try_setup_vmodel(self, value)
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def prefix_slot(self):
        return self.add_slot("prefix")

    def suffix_slot(self):
        return self.add_slot("suffix")

    def prefix_icon_slot(self):
        return self.add_slot("prefixIcon")

    def suffix_icon_slot(self):
        return self.add_slot("suffixIcon")

    def label_slot(self):
        return self.add_slot("label")

    def tips_slot(self):
        return self.add_slot("tips")

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_clear(self, handler: ui.TEvent):
        self.on("clear", handler)
        return self

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self

    def on_compositionend(self, handler: ui.TEvent):
        self.on("compositionend", handler)
        return self

    def on_compositionstart(self, handler: ui.TEvent):
        self.on("compositionstart", handler)
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

    def on_mouseenter(self, handler: ui.TEvent):
        self.on("mouseenter", handler)
        return self

    def on_mouseleave(self, handler: ui.TEvent):
        self.on("mouseleave", handler)
        return self

    def on_paste(self, handler: ui.TEvent):
        self.on("paste", handler)
        return self

    def on_validate(self, handler: ui.TEvent):
        self.on("validate", handler)
        return self

    def on_wheel(self, handler: ui.TEvent):
        self.on("wheel", handler)
        return self


class InputGroup(BaseElement):
    def __init__(
        self,
        *,
        separate: typing.Optional[bool] = None,
    ):
        super().__init__("t-input-group")

        self.props({"separate": separate})


class TInputProps(TypedDict, total=False):
    model_value: typing.Union[str, int, float]
    prefix_icon: str
    suffix_icon: str
    align: typing.Literal["left", "center", "right"]
    allow_input_over_max: bool
    auto_width: bool
    autocomplete: str
    autofocus: bool
    borderless: bool
    clearable: bool
    disabled: bool
    format: str
    input_class: typing.Union[str, dict, list]
    label: str
    maxcharacter: float
    maxlength: typing.Union[float, str]
    name: str
    placeholder: str
    readonly: bool
    show_clear_icon_on_empty: bool
    show_limit_number: bool
    size: typing.Literal["small", "medium", "large"]
    spell_check: bool
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tips: str
    type: typing.Literal[
        "text", "number", "url", "tel", "password", "search", "submit", "hidden"
    ]
    default_value: typing.Union[str, int, float]
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_click: ui.TEvent
    on_compositionend: ui.TEvent
    on_compositionstart: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_keydown: ui.TEvent
    on_keypress: ui.TEvent
    on_keyup: ui.TEvent
    on_mouseenter: ui.TEvent
    on_mouseleave: ui.TEvent
    on_paste: ui.TEvent
    on_validate: ui.TEvent
    on_wheel: ui.TEvent
