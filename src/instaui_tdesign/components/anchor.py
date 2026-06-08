from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Anchor(BaseElement):
    def __init__(
        self,
        *,
        affix_props: typing.Optional[dict] = None,
        **kwargs: Unpack[TAnchorProps],
    ):
        super().__init__("t-anchor")
        self.props(
            {
                "affixProps": affix_props,
            }
        )
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self


class AnchorItem(BaseElement):
    def __init__(
        self,
        href: str,
        **kwargs: Unpack[TAnchorItemProps],
    ):
        super().__init__("t-anchor-item")
        self.props({"href": href})
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore


class TAnchorProps(TypedDict, total=False):
    bounds: float
    container: str
    cursor: str
    size: typing.Literal["small", "medium", "large"]
    target_offset: float
    on_change: ui.TEvent
    on_click: ui.TEvent


class TAnchorItemProps(TypedDict, total=False):
    target: typing.Literal["_self", "_blank", "_parent", "_top"]
    title: str


class TAnchorTargetProps(TypedDict, total=False):
    id: str
    tag: str
