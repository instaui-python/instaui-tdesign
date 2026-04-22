from __future__ import annotations
import typing

from instaui_tdesign.components._icon_param_utils import (
    make_prefix_icon,
    make_suffix_icon,
)
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props, try_setup_vmodel


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

    def on_blur(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "blur",
            handler,
            params=params,
        )
        return self

    def on_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "change",
            handler,
            params=params,
        )
        return self

    def on_clear(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "clear",
            handler,
            params=params,
        )
        return self

    def on_enter(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "enter",
            handler,
            params=params,
        )
        return self

    def on_focus(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "focus",
            handler,
            params=params,
        )
        return self

    def on_input_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "input-change",
            handler,
            params=params,
        )
        return self

    def on_popup_visible_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "popup-visible-change",
            handler,
            params=params,
        )
        return self

    def on_remove(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "remove",
            handler,
            params=params,
        )
        return self

    def on_search(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "search",
            handler,
            params=params,
        )
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
    on_blur: EventMixin
    on_change: EventMixin
    on_clear: EventMixin
    on_enter: EventMixin
    on_focus: EventMixin
    on_input_change: EventMixin
    on_popup_visible_change: EventMixin
    on_remove: EventMixin
    on_search: EventMixin
