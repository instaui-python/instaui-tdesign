from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Radio(BaseElement):
    def __init__(
        self,
        checked: typing.Optional[bool] = None,
        **kwargs: Unpack[TRadioProps],
    ):
        super().__init__("t-radio")
        allow_uncheck = kwargs.pop("allow_uncheck", None)
        checked_value = kwargs.pop("checked_value", None)

        self.props({"allow-uncheck": allow_uncheck})
        try_setup_vmodel(self, checked)

        self.props(handle_props(kwargs, model_value=checked_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_click(self, handler: ui.TEvent):
        self.on("click", handler)
        return self


class RadioGroup(BaseElement):
    def __init__(
        self,
        options: typing.Optional[
            typing.Sequence[typing.Union[str, int, bool, dict]]
        ] = None,
        value: typing.Optional[typing.Union[bool, int, str]] = None,
        **kwargs: Unpack[TRadioGroupProps],
    ):
        super().__init__("t-radio-group")
        model_value = kwargs.pop("model_value", None)
        self.props({"options": options})
        try_setup_vmodel(self, value)
        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self


class TRadioProps(TypedDict, total=False):
    checked_value: bool
    allow_uncheck: bool
    default_checked: bool
    disabled: bool
    label: str
    name: str
    readonly: bool
    value: typing.Union[bool, float, str]
    on_change: ui.TEvent
    on_click: ui.TEvent


class TRadioGroupProps(TypedDict, total=False):
    model_value: typing.Union[bool, int, str]
    allow_uncheck: bool
    disabled: bool
    name: str
    readonly: bool
    size: typing.Literal["small", "medium", "large"]
    theme: typing.Literal["radio", "button"]
    default_value: typing.Union[bool, int, str]
    variant: typing.Literal["outline", "primary-filled", "default-filled"]
    on_change: ui.TEvent
