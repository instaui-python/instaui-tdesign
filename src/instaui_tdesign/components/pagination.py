from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Pagination(BaseElement):
    def __init__(
        self,
        current: typing.Optional[int] = None,
        *,
        current_value: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        page_size_value: typing.Optional[int] = None,
        **kwargs: Unpack[TPaginationProps],
    ):
        super().__init__("t-pagination")

        try_setup_vmodel(self, current, prop_name="current")
        try_setup_vmodel(self, page_size, prop_name="page-size")

        if page_size_value is not None:
            self.props({"page-size": page_size_value})

        if current_value is not None:
            self.props({"current": current_value})

        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_current_change(self, handler: ui.TEvent):
        self.on("current-change", handler)
        return self

    def on_page_size_change(self, handler: ui.TEvent):
        self.on("page-size-change", handler)
        return self


class PaginationMini(BaseElement):
    def __init__(
        self,
        current: typing.Optional[int] = None,
        *,
        current_value: typing.Optional[bool] = None,
        **kwargs: Unpack[TPaginationMiniProps],
    ):
        super().__init__("t-pagination-mini")

        try_setup_vmodel(self, current)

        self.props(handle_props(kwargs, model_value=current_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self


class TPaginationProps(TypedDict, total=False):
    default_current: int
    disabled: bool
    folded_max_page_btn: int
    max_page_btn: int
    page_ellipsis_mode: typing.Literal["mid", "both-ends"]
    default_page_size: int
    page_size_options: list
    select_props: dict
    show_first_and_last_page_btn: bool
    show_jumper: bool
    show_page_number: bool
    show_page_size: bool
    show_previous_and_next_btn: bool
    size: typing.Literal["small", "medium"]
    theme: typing.Literal["default", "simple"]
    total: int
    total_content: typing.Union[bool, str]
    on_change: ui.TEvent
    on_current_change: ui.TEvent
    on_page_size_change: ui.TEvent


class TPaginationMiniProps(TypedDict, total=False):
    disabled: typing.Union[bool, dict]
    layout: typing.Literal["horizontal", "vertical"]
    show_current: bool
    size: typing.Literal["small", "medium", "large"]
    tips: dict
    variant: typing.Literal["text", "outline"]
    on_change: ui.TEvent
