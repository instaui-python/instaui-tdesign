from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import make_icon_for_bool_or_str

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props


class Tree(BaseElement):
    def __init__(
        self,
        data: list,
        *,
        activable: typing.Optional[bool] = None,
        hover: typing.Optional[bool] = None,
        transition: typing.Optional[bool] = None,
        icon: typing.Union[str, bool, None] = None,
        **kwargs: Unpack[TTreeProps],
    ):
        super().__init__("t-tree")
        self.props(
            {
                "data": data,
                "activable": activable,
                "hover": hover,
                "transition": transition,
            }
        )
        make_icon_for_bool_or_str(self, "icon", icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_active(self, handler: ui.TEvent):
        self.on("active", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self

    def on_drag_end(self, handler: ui.TEvent):
        self.on("drag-end", handler)
        return self

    def on_drag_leave(self, handler: ui.TEvent):
        self.on("drag-leave", handler)
        return self

    def on_drag_over(self, handler: ui.TEvent):
        self.on("drag-over", handler)
        return self

    def on_drag_start(self, handler: ui.TEvent):
        self.on("drag-start", handler)
        return self

    def on_drop(self, handler: ui.TEvent):
        self.on("drop", handler)
        return self

    def on_expand(self, handler: ui.TEvent):
        self.on("expand", handler)
        return self

    def on_load(self, handler: ui.TEvent):
        self.on("load", handler)
        return self

    def on_scroll(self, handler: ui.TEvent):
        self.on("scroll", handler)
        return self


class TTreeProps(TypedDict, total=False):
    active_multiple: bool
    actived: list
    allow_drop: str
    allow_fold_node_on_filter: bool
    check_props: dict
    check_strictly: bool
    checkable: bool
    disable_check: bool | str
    disabled: bool
    draggable: bool
    empty: str
    expand_all: bool
    expand_level: float
    expand_mutex: bool
    expand_on_click_node: bool
    expand_parent: bool
    expanded: list
    filter: str
    height: typing.Union[float, str]
    keys: dict
    label: typing.Literal["boolean"]
    lazy: bool
    line: typing.Union[bool, str]
    load: str
    max_height: typing.Union[float, str]
    operations: str
    scroll: dict
    value: list
    default_value: list
    value_mode: typing.Literal["onlyLeaf", "parentFirst", "all"]
    on_active: ui.TEvent
    on_change: ui.TEvent
    on_click: ui.TEvent
    on_drag_end: ui.TEvent
    on_drag_leave: ui.TEvent
    on_drag_over: ui.TEvent
    on_drag_start: ui.TEvent
    on_drop: ui.TEvent
    on_expand: ui.TEvent
    on_load: ui.TEvent
    on_scroll: ui.TEvent
