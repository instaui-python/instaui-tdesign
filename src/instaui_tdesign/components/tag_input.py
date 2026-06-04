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


class TagInput(BaseElement):
    def __init__(
        self,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TTagInputProps],
    ):
        super().__init__("t-tag-input")

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

    def on_drag_sort(self, handler: ui.TEvent):
        self.on("drag-sort", handler)
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

    def on_remove(self, handler: ui.TEvent):
        self.on("remove", handler)
        return self


class TTagInputProps(TypedDict, total=False):
    auto_width: bool
    borderless: bool
    clearable: bool
    collapsed_items: str
    disabled: bool
    drag_sort: bool
    excess_tags_display_type: typing.Literal["scroll", "break-line"]
    input_props: dict
    input_value: typing.Union[float, str]
    default_input_value: typing.Union[float, str]
    label: str
    max: float
    min_collapsed_num: float
    placeholder: str
    readonly: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tag: str
    tag_props: dict
    tips: str
    default_value: list[str]
    value_display: str
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_click: ui.TEvent
    on_drag_sort: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_input_change: ui.TEvent
    on_mouseenter: ui.TEvent
    on_mouseleave: ui.TEvent
    on_paste: ui.TEvent
    on_remove: ui.TEvent
