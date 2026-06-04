from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Drawer(BaseElement):
    def __init__(
        self,
        visible: bool,
        *,
        header: typing.Optional[str] = None,
        body: typing.Optional[str] = None,
        **kwargs: Unpack[TDrawerProps],
    ):
        super().__init__("t-drawer")
        self.props({"header": header, "body": body})
        try_setup_vmodel(self, visible, prop_name="visible")
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_before_close(self, handler: ui.TEvent):
        self.on("before-close", handler)
        return self

    def on_before_open(self, handler: ui.TEvent):
        self.on("before-open", handler)
        return self

    def on_cancel(self, handler: ui.TEvent):
        self.on("cancel", handler)
        return self

    def on_close(self, handler: ui.TEvent):
        self.on("close", handler)
        return self

    def on_close_btn_click(self, handler: ui.TEvent):
        self.on("close-btn-click", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_esc_keydown(self, handler: ui.TEvent):
        self.on("esc-keydown", handler)
        return self

    def on_overlay_click(self, handler: ui.TEvent):
        self.on("overlay-click", handler)
        return self

    def on_size_drag_end(self, handler: ui.TEvent):
        self.on("size-drag-end", handler)
        return self


class TDrawerProps(TypedDict, total=False):
    attach: str
    cancel_btn: typing.Union[str, dict]
    close_btn: typing.Literal["boolean"]
    close_on_esc_keydown: bool
    close_on_overlay_click: bool
    confirm_btn: dict
    destroy_on_close: bool
    drawer_class_name: str
    footer: typing.Union[bool, str]
    lazy: bool
    mode: typing.Literal["overlay", "push"]
    placement: typing.Literal["left", "right", "top", "bottom"]
    prevent_scroll_through: bool
    show_in_attached_element: bool
    show_overlay: bool
    size: str
    size_draggable: typing.Union[bool, dict]
    z_index: float
    on_before_close: ui.TEvent
    on_before_open: ui.TEvent
    on_cancel: ui.TEvent
    on_close: ui.TEvent
    on_close_btn_click: ui.TEvent
    on_confirm: ui.TEvent
    on_esc_keydown: ui.TEvent
    on_overlay_click: ui.TEvent
    on_size_drag_end: ui.TEvent
