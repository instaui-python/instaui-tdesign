from __future__ import annotations

import typing

from instaui import ui
from instaui.internal.ui.components.content import Content
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import make_icon_for_str

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Button(BaseElement):
    def __init__(
        self,
        content: typing.Optional[str] = None,
        **kwargs: Unpack[TButtonProps],
    ):
        """Create a button element.

        Args:
            content (Optional[str], optional): _description_. Defaults to None.
        """

        super().__init__("t-button")
        icon = kwargs.pop("icon", None)

        if content is not None:
            with self:
                Content(content)

        make_icon_for_str(self, icon)

        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self


class TButtonProps(TypedDict, total=False):
    icon: str
    block: bool
    disabled: bool
    form: str
    ghost: bool
    href: str
    loading: bool
    shape: typing.Literal["rectangle", "square", "round", "circle"]
    loading_props: dict
    size: typing.Literal["small", "medium", "large"]
    suffix: str
    tag: typing.Literal["button", "a", "div"]
    theme: typing.Literal["default", "primary", "danger", "warning", "success"]
    type: typing.Literal["submit", "reset", "button"]
    variant: typing.Literal["base", "outline", "dashed", "text"]
    on_click: ui.TEvent
