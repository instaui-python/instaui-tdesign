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


class Cascader(BaseElement):
    def __init__(
        self,
        options: list[dict],
        *,
        value: typing.Optional[typing.Union[int, str]] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TCascaderProps],
    ):
        super().__init__("t-cascader")
        self.props({"options": options})
        try_setup_vmodel(self, value)

        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)

        self.props(handle_props(kwargs))  # type: ignore
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

    def on_popup_visible_change(self, handler: ui.TEvent):
        self.on("popup-visible-change", handler)
        return self

    def on_remove(self, handler: ui.TEvent):
        self.on("remove", handler)
        return self


class TCascaderProps(TypedDict, total=False):
    autofocus: bool
    borderless: bool
    check_props: dict
    check_strictly: bool
    clearable: bool
    collapsed_items: str
    disabled: bool
    empty: str
    filter: str
    filterable: bool
    input_props: dict
    keys: dict
    label: str
    lazy: bool
    load: str
    loading: bool
    loading_text: str
    max: float
    min_collapsed_num: float
    multiple: bool
    option: str
    panel_bottom_content: str
    panel_top_content: str
    placeholder: str
    popup_props: dict
    popup_visible: bool
    default_popup_visible: bool
    readonly: bool
    reserve_keyword: bool
    select_input_props: dict
    show_all_levels: bool
    size: typing.Literal["large", "medium", "small"]
    status: typing.Literal["default", "success", "warning", "error"]
    suffix: str
    tag_input_props: dict
    tag_props: dict
    tips: str
    trigger: typing.Literal["click", "hover"]
    default_value: typing.Union[int, str]
    value_display: str
    value_mode: typing.Literal["onlyLeaf", "parentFirst", "all"]
    value_type: typing.Literal["single", "full"]
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_focus: ui.TEvent
    on_popup_visible_change: ui.TEvent
    on_remove: ui.TEvent
