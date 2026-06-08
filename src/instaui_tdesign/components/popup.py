from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


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

    def on_overlay_click(self, handler: ui.TEvent):
        self.on("overlay-click", handler)
        return self

    def on_scroll(self, handler: ui.TEvent):
        self.on("scroll", handler)
        return self

    def on_scroll_to_bottom(self, handler: ui.TEvent):
        self.on("scroll-to-bottom", handler)
        return self

    def on_visible_change(self, handler: ui.TEvent):
        self.on("visible-change", handler)
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
    on_overlay_click: ui.TEvent
    on_scroll: ui.TEvent
    on_scroll_to_bottom: ui.TEvent
    on_visible_change: ui.TEvent


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
