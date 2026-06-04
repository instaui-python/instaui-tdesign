from __future__ import annotations

import typing
from datetime import date

from instaui import ui
from typing_extensions import TypedDict, Unpack

from instaui_tdesign.components._icon_param_utils import (
    make_prefix_icon,
    make_suffix_icon,
)

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class DatePicker(BaseElement):
    def __init__(
        self,
        value: typing.Optional[TDateMultipleValue] = None,
        *,
        model_value: typing.Optional[TDateMultipleValue] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TDatePickerProps],
    ):
        super().__init__("t-date-picker")

        try_setup_vmodel(self, value)
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_pick(self, handler: ui.TEvent):
        self.on("pick", handler)
        return self

    def on_preset_click(self, handler: ui.TEvent):
        self.on("preset-click", handler)
        return self


class DateRangePicker(BaseElement):
    def __init__(
        self,
        value: typing.Optional[TDateRangeValue] = None,
        *,
        model_value: typing.Optional[TDateRangeValue] = None,
        prefix_icon: typing.Optional[str] = None,
        suffix_icon: typing.Optional[str] = None,
        **kwargs: Unpack[TDateRangePickerProps],
    ):
        super().__init__("t-date-range-picker")

        try_setup_vmodel(self, value)
        make_prefix_icon(self, prefix_icon)
        make_suffix_icon(self, suffix_icon)
        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_blur(self, handler: ui.TEvent):
        self.on("blur", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_focus(self, handler: ui.TEvent):
        self.on("focus", handler)
        return self

    def on_input(self, handler: ui.TEvent):
        self.on("input", handler)
        return self

    def on_pick(self, handler: ui.TEvent):
        self.on("pick", handler)
        return self

    def on_preset_click(self, handler: ui.TEvent):
        self.on("preset-click", handler)
        return self


class DatePickerPanel(BaseElement):
    def __init__(
        self,
        value: typing.Optional[TDateMultipleValue] = None,
        *,
        model_value: typing.Optional[TDateMultipleValue] = None,
        **kwargs: Unpack[TDatePickerPanelProps],
    ):
        super().__init__("t-date-picker-panel")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_cell_click(self, handler: ui.TEvent):
        self.on("cell-click", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_month_change(self, handler: ui.TEvent):
        self.on("month-change", handler)
        return self

    def on_panel_click(self, handler: ui.TEvent):
        self.on("panel-click", handler)
        return self

    def on_preset_click(self, handler: ui.TEvent):
        self.on("preset-click", handler)
        return self

    def on_time_change(self, handler: ui.TEvent):
        self.on("time-change", handler)
        return self

    def on_year_change(self, handler: ui.TEvent):
        self.on("year-change", handler)
        return self


class DateRangePickerPanel(BaseElement):
    def __init__(
        self,
        value: typing.Optional[TDateRangeValue] = None,
        *,
        model_value: typing.Optional[TDateRangeValue] = None,
        **kwargs: Unpack[TDateRangePickerPanelProps],
    ):
        super().__init__("t-date-range-picker-panel")

        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_cell_click(self, handler: ui.TEvent):
        self.on("cell-click", handler)
        return self

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self

    def on_confirm(self, handler: ui.TEvent):
        self.on("confirm", handler)
        return self

    def on_month_change(self, handler: ui.TEvent):
        self.on("month-change", handler)
        return self

    def on_panel_click(self, handler: ui.TEvent):
        self.on("panel-click", handler)
        return self

    def on_preset_click(self, handler: ui.TEvent):
        self.on("preset-click", handler)
        return self

    def on_time_change(self, handler: ui.TEvent):
        self.on("time-change", handler)
        return self

    def on_year_change(self, handler: ui.TEvent):
        self.on("year-change", handler)
        return self


TDateValue = typing.Union[str, date]
TDateMultipleValue = list[TDateValue]
TDateRangeValue = list[TDateValue]


class TDatePickerProps(TypedDict, total=False):
    allow_input: bool
    borderless: bool
    clearable: bool
    default_time: str
    disable_date: typing.Union[str, dict, list]
    disabled: bool
    enable_time_picker: bool
    first_day_of_week: float
    format: str
    input_props: dict
    label: str
    mode: typing.Literal["year", "quarter", "month", "week", "date"]
    multiple: bool
    need_confirm: bool
    placeholder: typing.Union[str, list]
    popup_props: dict
    presets: dict
    presets_placement: typing.Literal["left", "top", "right", "bottom"]
    readonly: bool
    select_input_props: dict
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    time_picker_props: dict
    tips: str
    default_value: TDateMultipleValue
    value_display: str
    value_type: str
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_confirm: ui.TEvent
    on_focus: ui.TEvent
    on_pick: ui.TEvent
    on_preset_click: ui.TEvent


class TDateRangePickerProps(TypedDict, total=False):
    allow_input: bool
    borderless: bool
    cancel_range_select_limit: bool
    clearable: bool
    default_time: list
    disable_date: typing.Union[str, dict, list]
    disable_time: str
    disabled: bool
    enable_time_picker: bool
    first_day_of_week: float
    format: str
    label: str
    mode: typing.Literal["year", "quarter", "month", "week", "date"]
    need_confirm: bool
    panel_preselection: bool
    placeholder: typing.Literal["Array"]
    popup_props: dict
    presets: dict
    presets_placement: typing.Literal["left", "top", "right", "bottom"]
    readonly: bool
    range_input_props: dict
    separator: str
    size: typing.Literal["small", "medium", "large"]
    status: typing.Literal["default", "success", "warning", "error"]
    time_picker_props: dict
    tips: str
    default_value: TDateRangeValue
    value_type: typing.Literal[
        "time-stamp",
        "Date",
        "YYYY",
        "YYYY-MM",
        "YYYY-MM-DD",
        "YYYY-MM-DD HH",
        "YYYY-MM-DD HH",
    ]
    on_blur: ui.TEvent
    on_change: ui.TEvent
    on_confirm: ui.TEvent
    on_focus: ui.TEvent
    on_input: ui.TEvent
    on_pick: ui.TEvent
    on_preset_click: ui.TEvent


class TDatePickerPanelProps(TypedDict, total=False):
    default_time: str
    default_value: TDateMultipleValue
    disable_date: typing.Union[str, dict, list]
    enable_time_picker: bool
    first_day_of_week: float
    format: str
    mode: typing.Literal["year", "quarter", "month", "week", "date"]
    presets: dict
    presets_placement: typing.Literal["left", "top", "right", "bottom"]
    time_picker_props: dict
    on_cell_click: ui.TEvent
    on_change: ui.TEvent
    on_confirm: ui.TEvent
    on_month_change: ui.TEvent
    on_panel_click: ui.TEvent
    on_preset_click: ui.TEvent
    on_time_change: ui.TEvent
    on_year_change: ui.TEvent


class TDateRangePickerPanelProps(TypedDict, total=False):
    default_time: list
    default_value: TDateRangeValue
    disable_date: typing.Union[str, dict, list]
    enable_time_picker: bool
    first_day_of_week: float
    format: str
    mode: typing.Literal["year", "quarter", "month", "week", "date"]
    panel_preselection: bool
    presets: dict
    presets_placement: typing.Literal["left", "top", "right", "bottom"]
    time_picker_props: dict
    on_cell_click: ui.TEvent
    on_change: ui.TEvent
    on_confirm: ui.TEvent
    on_month_change: ui.TEvent
    on_panel_click: ui.TEvent
    on_preset_click: ui.TEvent
    on_time_change: ui.TEvent
    on_year_change: ui.TEvent
