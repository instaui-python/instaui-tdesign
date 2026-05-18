from __future__ import annotations

import typing

from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class BackTop(BaseElement):
    def __init__(
        self,
        content: typing.Optional[str] = None,
        **kwargs: Unpack[TBackTopProps],
    ):
        super().__init__("t-back-top")
        self.props({"content": content})
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_click(self, handler: EventMixin):
        self.on("click", handler)
        return self


class TBackTopProps(TypedDict, total=False):
    container: str
    duration: float
    offset: list
    shape: typing.Literal["circle", "square"]
    size: typing.Literal["medium", "small"]
    target: str
    theme: typing.Literal["light", "primary", "dark"]
    visible_height: typing.Union[float, str]
    on_click: EventMixin
