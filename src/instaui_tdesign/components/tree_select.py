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


class TreeSelect(BaseElement):
    def __init__(
        self,
        value: typing.Optional[typing.Union[str, int, list]] = None,
        *,
        model_value: typing.Optional[typing.Union[str, int, list]] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TTreeSelectProps],
    ):
        super().__init__("t-tree-select ")

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

    def on_enter(self, handler: ui.TEvent):
        self.on("enter", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_input_change(self, handler: ui.TEvent):
        self.on("input-change", handler)
        return self

    def on_popup_visible_change(self, handler: ui.TEvent):
        self.on("popup-visible-change", handler)
        return self

    def on_remove(self, handler: ui.TEvent):
        self.on("remove", handler)
        return self

    def on_search(self, handler: ui.TEvent):
        self.on("search", handler)
        return self


class TTreeSelectProps(TypedDict, total=False):
    auto_width: bool
    autofocus: bool
    borderless: bool
    clearable: bool
    collapsed_items: str
    data: list
    disabled: bool
    empty: str
    filter: str
    filterable: bool
    input_props: dict
    input_value: float | str
    default_input_value: float | str
    keys: dict
    label: str
    loading: bool
    loading_text: str
    max: float
    min_collapsed_num: float
    multiple: bool
    panel_bottom_content: str
    panel_top_content: str
    placeholder: str
    popup_props: dict
    popup_visible: bool
    default_popup_visible: bool
    readonly: bool
    reserve_keyword: bool
    select_input_props: dict
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tag_props: dict
    tips: str
    tree_props: dict
    default_value: typing.Union[str, int, list]
    value_display: str
    value_type: typing.Literal["value", "object"]
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_input_change: ui.TEvent
    on_popup_visible_change: ui.TEvent
    on_remove: ui.TEvent
    on_search: ui.TEvent
