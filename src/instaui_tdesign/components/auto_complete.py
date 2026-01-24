from __future__ import annotations
import typing
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props, try_setup_vmodel


class AutoComplete(BaseElement):
    def __init__(
        self,
        options: typing.Optional[list] = None,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        **kwargs: Unpack[TAutoCompleteProps],
    ):
        super().__init__("t-auto-complete")

        self.props({"options": options})
        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "blur",
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

    def on_clear(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "clear",
            handler,
            params=params,
        )
        return self

    def on_compositionend(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "compositionend",
            handler,
            params=params,
        )
        return self

    def on_compositionstart(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "compositionstart",
            handler,
            params=params,
        )
        return self

    def on_enter(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "enter",
            handler,
            params=params,
        )
        return self

    def on_focus(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "focus",
            handler,
            params=params,
        )
        return self

    def on_select(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "select",
            handler,
            params=params,
        )
        return self


class TAutoCompleteProps(TypedDict, total=False):
    autofocus: bool
    borderless: bool
    clearable: bool
    disabled: bool
    empty: str
    filter: str
    filterable: bool
    highlight_keyword: bool
    input_props: dict
    panel_bottom_content: str
    panel_top_content: str
    placeholder: str
    popup_props: dict
    readonly: bool
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    textarea_props: dict
    tips: str
    trigger_element: str
    default_value: str
    on_blur: EventMixin
    on_change: EventMixin
    on_clear: EventMixin
    on_compositionend: EventMixin
    on_compositionstart: EventMixin
    on_enter: EventMixin
    on_focus: EventMixin
    on_select: EventMixin
