from __future__ import annotations

import typing

from instaui import ui
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import make_icon_for_bool_or_str

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Steps(BaseElement):
    def __init__(
        self,
        current: typing.Optional[typing.Union[int, str]] = None,
        *,
        current_value: typing.Optional[bool] = None,
        **kwargs: Unpack[TStepsProps],
    ):
        super().__init__("t-steps")

        try_setup_vmodel(self, current)

        self.props(handle_props(kwargs, model_value=current_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self


class StepItem(BaseElement):
    def __init__(
        self,
        *,
        icon: typing.Union[bool, str, None] = None,
        **kwargs: Unpack[TStepItemProps],
    ):
        super().__init__("t-step-item")
        make_icon_for_bool_or_str(self, "icon", icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore


class TStepsProps(TypedDict, total=False):
    default_current: typing.Union[float, str]
    layout: typing.Literal["horizontal", "vertical"]
    options: list[TStepItemProps]
    readonly: bool
    separator: typing.Literal["line", "dashed", "arrow"]
    sequence: typing.Literal["positive", "reverse"]
    theme: typing.Literal["default", "dot"]
    on_change: ui.TEvent


class TStepItemProps(TypedDict, total=False):
    content: str
    extra: str
    status: typing.Literal["default", "process", "finish", "error"]
    title: str
    value: typing.Union[int, str]
