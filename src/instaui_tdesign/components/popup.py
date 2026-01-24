from __future__ import annotations
import typing
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props


class Popup(BaseElement):
    def __init__(
        self,
        content: str,
        **kwargs: Unpack[TPopupProps],
    ):
        super().__init__("t-popup")
        self.props({"content": content})
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_overlay_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "overlay-click",
            handler,
            params=params,
        )
        return self

    def on_scroll(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "scroll",
            handler,
            params=params,
        )
        return self

    def on_scroll_to_bottom(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "scroll-to-bottom",
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


class TPopupProps(TypedDict, total=False):
    attach: str
    delay: typing.Union[float, list]
    destroy_on_close: bool
    disabled: bool
    hide_empty_popup: bool
    overlay_class_name: typing.Union[str, dict, list]
    overlay_inner_class_name: typing.Union[str, dict, list]
    overlay_inner_style: typing.Union[str, dict, list]
    overlay_style: typing.Union[str, dict, list]
    placement: str
    popper_options: dict
    show_arrow: bool
    trigger: typing.Literal["hover", "click", "focus", "mousedown", "context-menu"]
    trigger_element: str
    visible: bool
    z_index: float
    on_overlay_click: EventMixin
    on_scroll: EventMixin
    on_scroll_to_bottom: EventMixin
    on_visible_change: EventMixin


TPopupPlacementValue = typing.Literal[
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
