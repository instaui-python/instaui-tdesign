from __future__ import annotations

import typing

from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import (
    make_prefix_icon,
    make_suffix_icon,
)

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Link(BaseElement):
    def __init__(
        self,
        href: typing.Optional[str] = None,
        *,
        content: typing.Optional[str] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TLinkProps],
    ):
        super().__init__("t-link")
        self.props({"content": content, "href": href})
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_click(self, handler: EventMixin):
        self.on("click", handler)
        return self


class TLinkProps(TypedDict, total=False):
    disabled: bool
    download: typing.Union[bool, str]
    hover: typing.Literal["color", "underline"]
    size: typing.Literal["small", "medium", "large"]
    target: str
    theme: typing.Literal["default", "primary", "danger", "warning", "success"]
    underline: bool
    on_click: EventMixin
