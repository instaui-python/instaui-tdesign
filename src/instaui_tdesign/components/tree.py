from __future__ import annotations
import typing

from instaui_tdesign.components._icon_param_utils import make_icon_for_bool_or_str
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props


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

    def on_active(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "active",
            handler,
            params=params,
        )
        return self

    def on_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "change",
            handler,
            params=params,
        )
        return self

    def on_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "click",
            handler,
            params=params,
        )
        return self

    def on_drag_end(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drag-end",
            handler,
            params=params,
        )
        return self

    def on_drag_leave(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drag-leave",
            handler,
            params=params,
        )
        return self

    def on_drag_over(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drag-over",
            handler,
            params=params,
        )
        return self

    def on_drag_start(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drag-start",
            handler,
            params=params,
        )
        return self

    def on_drop(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "drop",
            handler,
            params=params,
        )
        return self

    def on_expand(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "expand",
            handler,
            params=params,
        )
        return self

    def on_load(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "load",
            handler,
            params=params,
        )
        return self

    def on_scroll(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "scroll",
            handler,
            params=params,
        )
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
    on_active: EventMixin
    on_change: EventMixin
    on_click: EventMixin
    on_drag_end: EventMixin
    on_drag_leave: EventMixin
    on_drag_over: EventMixin
    on_drag_start: EventMixin
    on_drop: EventMixin
    on_expand: EventMixin
    on_load: EventMixin
    on_scroll: EventMixin
