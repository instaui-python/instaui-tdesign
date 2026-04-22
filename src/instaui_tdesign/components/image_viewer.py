from __future__ import annotations
import typing
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props


class ImageViewer(BaseElement):
    def __init__(
        self,
        images: typing.Optional[list[str]] = None,
        **kwargs: Unpack[TImageViewerProps],
    ):
        super().__init__("t-image-viewer")
        self.props({"images": images})
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

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

    def on_download(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "download",
            handler,
            params=params,
        )
        return self

    def on_index_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "index-change",
            handler,
            params=params,
        )
        return self


class TImageViewerProps(TypedDict, total=False):
    attach: str
    close_btn: typing.Union[bool, str]
    close_on_esc_keydown: bool
    close_on_overlay: bool
    draggable: bool
    image_referrerpolicy: typing.Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    image_scale: dict
    index: float
    default_index: float
    mode: typing.Literal["modal", "modeless"]
    navigation_arrow: typing.Union[bool, str]
    show_overlay: bool
    title: str
    trigger: str
    viewer_scale: dict
    visible: bool
    default_visible: bool
    z_index: float
    on_close: EventMixin
    on_download: EventMixin
    on_index_change: EventMixin
