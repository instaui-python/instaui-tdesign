from __future__ import annotations

import typing

from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Divider(BaseElement):
    def __init__(
        self,
        *,
        content: typing.Optional[str] = None,
        **kwargs: Unpack[TDividerProps],
    ):
        super().__init__("t-divider")
        self.props({"content": content})

        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore


class TDividerProps(TypedDict, total=False):
    align: typing.Literal["left", "right", "center"]
    dashed: bool
    layout: typing.Literal["horizontal", "vertical"]
    theme: typing.Literal["horizontal", "vertical"]
