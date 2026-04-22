from __future__ import annotations
import typing

from instaui_tdesign.components._icon_param_utils import make_icon_for_str
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props


class Tag(BaseElement):
    def __init__(
        self,
        content: typing.Optional[str] = None,
        *,
        icon: typing.Optional[str] = None,
        **kwargs: Unpack[TTagProps],
    ):
        super().__init__("t-tag")
        self.props({"content": content})

        make_icon_for_str(self, icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

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

    def on_close(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "close",
            handler,
            params=params,
        )
        return self


class TTagProps(TypedDict, total=False):
    closable: bool
    color: str
    disabled: bool
    max_width: typing.Union[float, str]
    shape: typing.Literal["square", "round", "mark"]
    size: typing.Literal["small", "medium", "large"]
    theme: typing.Literal["default", "primary", "warning", "danger", "success"]
    title: str
    variant: typing.Literal["dark", "light", "outline", "light-outline"]
    on_click: EventMixin
    on_close: EventMixin


class TCheckTagProps(TypedDict, total=False):
    checked: bool
    default_checked: bool
    checked_props: dict
    content: typing.Literal["number"]
    default: typing.Literal["TNode"]
    disabled: bool
    size: typing.Literal["small", "medium", "large"]
    unchecked_props: dict
    value: float | str
    on_change: EventMixin
    on_click: EventMixin


class TCheckTagGroupProps(TypedDict, total=False):
    checked_props: dict
    multiple: bool
    options: list
    unchecked_props: dict
    value: list
    default_value: list
    on_change: EventMixin
