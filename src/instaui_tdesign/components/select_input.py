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


class SelectInput(BaseElement):
    def __init__(
        self,
        value: typing.Optional[typing.Union[str, int, float, bool]] = None,
        *,
        model_value: typing.Optional[typing.Union[str, int, float, bool]] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TSelectInputProps],
    ):
        super().__init__("t-select-input")

        try_setup_vmodel(self, value)
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)
        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_clear(self, handler: ui.TEvent):
        self.on("clear", handler)
        return self

    def on_enter(self, handler: ui.TEvent):
        self.on("enter", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_input_change(self, handler: ui.TEvent):
        self.on("input-change", handler)
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

    def on_popup_visible_change(self, handler: ui.TEvent):
        self.on("popup-visible-change", handler)
        return self

    def on_tag_change(self, handler: ui.TEvent):
        self.on("tag-change", handler)
        return self


class TSelectInputProps(TypedDict, total=False):
    allow_input: bool
    auto_width: bool
    autofocus: bool
    borderless: bool
    clearable: bool
    collapsed_items: str
    disabled: bool
    input_props: dict
    input_value: typing.Union[float, str]
    default_input_value: typing.Union[float, str]
    keys: dict
    label: str
    loading: bool
    min_collapsed_num: float
    multiple: bool
    panel: str
    placeholder: str
    popup_props: dict
    popup_visible: bool
    default_popup_visible: bool
    readonly: bool
    reserve_keyword: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tag: str
    tag_input_props: dict
    tag_props: dict
    tips: str
    value_display: str
    on_blur: ui.TEvent
    on_clear: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_input_change: ui.TEvent
    on_mouseenter: ui.TEvent
    on_mouseleave: ui.TEvent
    on_paste: ui.TEvent
    on_popup_visible_change: ui.TEvent
    on_tag_change: ui.TEvent
