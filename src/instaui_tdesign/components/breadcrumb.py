from __future__ import annotations

from typing import Literal, Optional

from instaui import ui
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import make_icon_for_str

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Breadcrumb(BaseElement):
    def __init__(
        self,
        **kwargs: Unpack[TBreadcrumbProps],
    ):
        super().__init__("t-breadcrumb")

        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore


class BreadcrumbItem(BaseElement):
    def __init__(
        self,
        content: Optional[str] = None,
        **kwargs: Unpack[TBreadcrumbItemProps],
    ):
        super().__init__("t-breadcrumb-item")
        icon = kwargs.pop("icon", None)
        self.props({"content": content})
        make_icon_for_str(self, icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self


class TBreadcrumbProps(TypedDict, total=False):
    ellipsis: str
    items_after_collapse: float
    items_before_collapse: float
    max_item_width: str
    max_items: float
    options: list
    separator: str
    theme: Literal["light"]


class TBreadcrumbItemProps(TypedDict, total=False):
    icon: str
    disabled: bool
    href: str
    max_width: str
    replace: bool
    router: dict
    target: Literal["_blank", "_self", "_parent", "_top"]
    to: Literal["Route"]
    on_click: ui.TEvent
