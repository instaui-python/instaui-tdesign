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


class RangeInput(BaseElement):
    def __init__(
        self,
        value: typing.Optional[list] = None,
        *,
        model_value: typing.Optional[list] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TRangeInputProps],
    ):
        super().__init__("t-range-input")

        try_setup_vmodel(self, value)
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)
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

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self

    def on_enter(self, handler: ui.TEvent):
        self.on("enter", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_mouseenter(self, handler: ui.TEvent):
        self.on("mouseenter", handler)
        return self

    def on_mouseleave(self, handler: ui.TEvent):
        self.on("mouseleave", handler)
        return self


class TRangeInputProps(TypedDict, total=False):
    active_index: float
    borderless: bool
    clearable: bool
    disabled: bool
    format: typing.Union[str, list]
    input_props: typing.Union[dict, list]
    label: str
    placeholder: typing.Literal["Array"]
    readonly: bool
    separator: str
    show_clear_icon_on_empty: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tips: str
    default_value: list
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_click: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_mouseenter: ui.TEvent
    on_mouseleave: ui.TEvent


class TRangeInputPopupProps(TypedDict, total=False):
    auto_width: bool
    disabled: bool
    input_value: list
    default_input_value: list
    label: str
    panel: str
    popup_props: dict
    popup_visible: bool
    default_popup_visible: bool
    range_input_props: dict
    readonly: bool
    status: typing.Literal["default", "success", "warning", "error"]
    tips: str
    on_input_change: ui.TEvent
    on_popup_visible_change: ui.TEvent
