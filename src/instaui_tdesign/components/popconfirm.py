from __future__ import annotations
import typing

from instaui_tdesign.components._icon_param_utils import make_icon_for_str
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props


class Popconfirm(BaseElement):
    def __init__(
        self,
        content: typing.Optional[str] = None,
        *,
        theme: typing.Optional[typing.Literal["default", "warning", "danger"]] = None,
        icon: typing.Union[str, None] = None,
        **kwargs: Unpack[TPopconfirmProps],
    ):
        super().__init__("t-popconfirm")
        self.props({"content": content})
        make_icon_for_str(self, icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_cancel(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "cancel",
            handler,
            params=params,
        )
        return self

    def on_confirm(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "confirm",
            handler,
            params=params,
        )
        return self

    def on_visible_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "visible-change",
            handler,
            params=params,
        )
        return self


class TPopconfirmProps(TypedDict, total=False):
    cancel_btn: typing.Union[str, dict]
    confirm_btn: typing.Union[str, dict]
    destroy_on_close: bool
    placement: typing.Literal[
        "top",
        "left",
        "right",
        "bottom",
        "top-left",
        "top-right",
        "bottom-left",
        "bottom-right",
        "left-top",
        "left-bottom",
        "right-top",
        "right-bottom",
    ]
    popup_props: dict
    show_arrow: bool
    trigger_element: str
    visible: bool
    default_visible: bool
    on_cancel: EventMixin
    on_confirm: EventMixin
    on_visible_change: EventMixin
