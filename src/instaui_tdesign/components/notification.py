from __future__ import annotations
import typing
from typing_extensions import TypedDict, Unpack
import copy
from instaui import ui
from instaui_tdesign.components._icon_param_utils import make_icon_for_bool_or_str
from ._base_element import BaseElement
from instaui.event.event_mixin import EventMixin
from ._utils import handle_props, handle_event_from_props

if typing.TYPE_CHECKING:
    from instaui.vars.types import TMaybeRef


class Notification(BaseElement):
    def __init__(
        self,
        content: typing.Optional[str] = None,
        *,
        title: typing.Optional[str] = None,
        icon: typing.Union[str, bool, None] = None,
        **kwargs: Unpack[TNotificationProps],
    ):
        super().__init__("t-notification")
        self.props({"content": content, "title": title})
        make_icon_for_bool_or_str(self, "icon", icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_close_btn_click(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "close-btn-click",
            handler,
            extends=extends,
        )
        return self

    def on_duration_end(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "duration-end",
            handler,
            extends=extends,
        )
        return self


class NotifyPlugin:
    @staticmethod
    def info(**options: Unpack[TNotificationOptions]):
        return ui.js_event(
            inputs=[_handle_notification_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.NotifyPlugin.info(options)",
        )


class TNotificationProps(TypedDict, total=False):
    close_btn: typing.Union[str, bool]
    duration: float
    footer: TMaybeRef[str]
    theme: TMaybeRef[typing.Literal["info", "success", "warning", "error"]]
    on_close_btn_click: EventMixin
    on_duration_end: EventMixin


class TNotificationOptions(TypedDict, total=False):
    content: str
    title: str
    attach: str
    offset: tuple[typing.Union[str, int], typing.Union[str, int]]
    placement: typing.Literal["top-right", "top-left", "bottom-right", "bottom-left"]
    zIndex: int

    close_btn: typing.Union[str, bool]
    duration: float
    footer: TMaybeRef[str]


def _handle_notification_options(options: dict):
    options = copy.deepcopy(options)
    if "close_btn" in options:
        options["closeBtn"] = options.pop("close_btn")

    return options
