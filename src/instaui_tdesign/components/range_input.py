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

    def on_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "click",
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

    def on_mouseenter(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "mouseenter",
            handler,
            params=params,
        )
        return self

    def on_mouseleave(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "mouseleave",
            handler,
            params=params,
        )
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
    on_blur: EventMixin
    on_change: EventMixin
    on_clear: EventMixin
    on_click: EventMixin
    on_enter: EventMixin
    on_focus: EventMixin
    on_mouseenter: EventMixin
    on_mouseleave: EventMixin


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
    on_input_change: EventMixin
    on_popup_visible_change: EventMixin
