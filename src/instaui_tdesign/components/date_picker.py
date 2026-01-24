from __future__ import annotations
from datetime import date
import typing

from instaui_tdesign.components._icon_param_utils import (
    make_prefix_icon,
    make_suffix_icon,
)
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack

from ._utils import handle_props, handle_event_from_props, try_setup_vmodel


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

    def on_confirm(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "confirm",
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

    def on_pick(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "pick",
            handler,
            params=params,
        )
        return self

    def on_preset_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "preset-click",
            handler,
            params=params,
        )
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

    def on_confirm(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "confirm",
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

    def on_input(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "input",
            handler,
            params=params,
        )
        return self

    def on_pick(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "pick",
            handler,
            params=params,
        )
        return self

    def on_preset_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "preset-click",
            handler,
            params=params,
        )
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

    def on_cell_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "cell-click",
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

    def on_confirm(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "confirm",
            handler,
            params=params,
        )
        return self

    def on_month_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "month-change",
            handler,
            params=params,
        )
        return self

    def on_panel_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "panel-click",
            handler,
            params=params,
        )
        return self

    def on_preset_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "preset-click",
            handler,
            params=params,
        )
        return self

    def on_time_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "time-change",
            handler,
            params=params,
        )
        return self

    def on_year_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "year-change",
            handler,
            params=params,
        )
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

    def on_cell_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "cell-click",
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

    def on_confirm(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "confirm",
            handler,
            params=params,
        )
        return self

    def on_month_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "month-change",
            handler,
            params=params,
        )
        return self

    def on_panel_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "panel-click",
            handler,
            params=params,
        )
        return self

    def on_preset_click(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "preset-click",
            handler,
            params=params,
        )
        return self

    def on_time_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "time-change",
            handler,
            params=params,
        )
        return self

    def on_year_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "year-change",
            handler,
            params=params,
        )
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
    on_blur: EventMixin
    on_change: EventMixin
    on_confirm: EventMixin
    on_focus: EventMixin
    on_pick: EventMixin
    on_preset_click: EventMixin


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
    on_blur: EventMixin
    on_change: EventMixin
    on_confirm: EventMixin
    on_focus: EventMixin
    on_input: EventMixin
    on_pick: EventMixin
    on_preset_click: EventMixin


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
    on_cell_click: EventMixin
    on_change: EventMixin
    on_confirm: EventMixin
    on_month_change: EventMixin
    on_panel_click: EventMixin
    on_preset_click: EventMixin
    on_time_change: EventMixin
    on_year_change: EventMixin


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
    on_cell_click: EventMixin
    on_change: EventMixin
    on_confirm: EventMixin
    on_month_change: EventMixin
    on_panel_click: EventMixin
    on_preset_click: EventMixin
    on_time_change: EventMixin
    on_year_change: EventMixin
