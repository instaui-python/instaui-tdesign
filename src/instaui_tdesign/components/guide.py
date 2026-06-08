from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Guide(BaseElement):
    def __init__(
        self,
        *,
        current: int,
        steps: list[TGuideStepValue],
        **kwargs: Unpack[TGuideProps],
    ):
        super().__init__("t-guide")
        self.props({"steps": steps})
        try_setup_vmodel(self, current, prop_name="current")
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_finish(self, handler: ui.TEvent):
        self.on("finish", handler)
        return self

    def on_next_step_click(self, handler: ui.TEvent):
        self.on("next-step-click", handler)
        return self

    def on_prev_step_click(self, handler: ui.TEvent):
        self.on("prev-step-click", handler)
        return self

    def on_skip(self, handler: ui.TEvent):
        self.on("skip", handler)
        return self


class TGuideProps(TypedDict, total=False):
    counter: str
    default_current: int
    finish_button_props: dict
    hide_counter: bool
    hide_prev: bool
    hide_skip: bool
    highlight_padding: float
    mode: typing.Literal["popup", "dialog"]
    next_button_props: dict
    prev_button_props: dict
    show_overlay: bool
    skip_button_props: dict
    z_index: float
    on_change: ui.TEvent
    on_finish: ui.TEvent
    on_next_step_click: ui.TEvent
    on_prev_step_click: ui.TEvent
    on_skip: ui.TEvent


class TGuideStepValue(TypedDict, total=False):
    body: str
    content: str
    element: str
    highlight_content: str
    highlight_padding: float
    mode: typing.Literal["popup", "dialog"]
    next_button_props: dict
    offset: list
    placement: typing.Union[TStepPopupPlacement, TStepDialogPlacement]
    popup_props: dict
    prev_button_props: dict
    show_overlay: bool
    skip_button_props: dict
    step_overlay_class: str
    title: str


TStepPopupPlacement = typing.Literal[
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
TStepDialogPlacement = typing.Literal["top", "center"]
