from __future__ import annotations

import typing

from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Transfer(BaseElement):
    def __init__(
        self,
        value: typing.Optional[list] = None,
        *,
        model_value: typing.Optional[list] = None,
        **kwargs: Unpack[TTransferProps],
    ):
        super().__init__("t-transfer")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: EventMixin):
        self.on("change", handler)
        return self

    def on_checked_change(self, handler: EventMixin):
        self.on("checked-change", handler)
        return self

    def on_page_change(self, handler: EventMixin):
        self.on("page-change", handler)
        return self

    def on_scroll(self, handler: EventMixin):
        self.on("scroll", handler)
        return self

    def on_search(self, handler: EventMixin):
        self.on("search", handler)
        return self


class TTransferProps(TypedDict, total=False):
    checkbox_props: dict
    checked: list
    data: list
    direction: typing.Literal["left", "right", "both"]
    disabled: typing.Union[bool, list]
    empty: str
    footer: typing.Union[bool, list]
    keys: dict
    operation: typing.Union[bool, list]
    pagination: dict | list
    search: dict | list | bool
    show_check_all: list | bool
    target_draggable: bool
    target_sort: typing.Literal["original", "push", "unshift"]
    title: typing.Union[bool, list]
    transfer_item: str
    tree: str
    default_value: list
    on_change: EventMixin
    on_checked_change: EventMixin
    on_page_change: EventMixin
    on_scroll: EventMixin
    on_search: EventMixin
