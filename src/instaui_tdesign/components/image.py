from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Image(BaseElement):
    def __init__(
        self,
        src: str,
        **kwargs: Unpack[TImageProps],
    ):
        super().__init__("t-image")
        self.props({"src": src})
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_error(self, handler: ui.TEvent):
        self.on("error", handler)
        return self

    def on_load(self, handler: ui.TEvent):
        self.on("load", handler)
        return self


class TImageProps(TypedDict, total=False):
    alt: str
    error: str
    fallback: str
    fit: typing.Literal["contain", "cover", "fill", "none", "scale-down"]
    gallery: bool
    lazy: bool
    loading: str
    overlay_content: str
    overlay_trigger: typing.Literal["always", "hover"]
    placeholder: str
    position: str
    referrerpolicy: typing.Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    shape: typing.Literal["circle", "round", "square"]
    srcset: dict
    on_error: ui.TEvent
    on_load: ui.TEvent
