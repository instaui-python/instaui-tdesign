from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class AutoComplete(BaseElement):
    def __init__(
        self,
        options: typing.Optional[list] = None,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        **kwargs: Unpack[TAutoCompleteProps],
    ):
        super().__init__("t-auto-complete")

        self.props({"options": options})
        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_clear(self, handler: ui.TEvent):
        self.on("clear", handler)
        return self

    def on_compositionend(self, handler: ui.TEvent):
        self.on("compositionend", handler)
        return self

    def on_compositionstart(self, handler: ui.TEvent):
        self.on("compositionstart", handler)
        return self

    def on_enter(self, handler: ui.TEvent):
        self.on("enter", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_select(self, handler: ui.TEvent):
        self.on("select", handler)
        return self


class TAutoCompleteProps(TypedDict, total=False):
    autofocus: bool
    borderless: bool
    clearable: bool
    disabled: bool
    empty: str
    filter: str
    filterable: bool
    highlight_keyword: bool
    input_props: dict
    panel_bottom_content: str
    panel_top_content: str
    placeholder: str
    popup_props: dict
    readonly: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    textarea_props: dict
    tips: str
    trigger_element: str
    default_value: str
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_clear: ui.TEvent
    on_compositionend: ui.TEvent
    on_compositionstart: ui.TEvent
    on_enter: ui.TEvent
    on_focus: ui.TEvent
    on_select: ui.TEvent
