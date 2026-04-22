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

    def on_drag_sort(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drag-sort",
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

    def on_paste(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "paste",
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
    on_blur: EventMixin
    on_change: EventMixin
    on_clear: EventMixin
    on_click: EventMixin
    on_drag_sort: EventMixin
    on_enter: EventMixin
    on_focus: EventMixin
    on_input_change: EventMixin
    on_mouseenter: EventMixin
    on_mouseleave: EventMixin
    on_paste: EventMixin
    on_remove: EventMixin
