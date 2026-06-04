from __future__ import annotations

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Affix(BaseElement):
    def __init__(
        self,
        **kwargs: Unpack[TAffixProps],
    ):
        super().__init__("t-affix")

        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_fixed_change(self, handler: ui.TEvent):
        self.on("fixed-change", handler)
        return self


class TAffixProps(TypedDict, total=False):
    container: str
    offset_bottom: float
    offset_top: float
    z_index: int
    on_fixed_change: ui.TEvent
