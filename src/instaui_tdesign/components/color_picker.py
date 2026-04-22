from __future__ import annotations
import typing
from ._base_element import BaseElement
from instaui.internal.ui.event import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props, try_setup_vmodel


class ColorPicker(BaseElement):
    def __init__(
        self,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        recent_colors: typing.Optional[typing.Union[list[str, bool]]] = None,
        **kwargs: Unpack[TColorPickerProps],
    ):
        super().__init__("t-color-picker")

        self.props({"recent-colors": recent_colors})
        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

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

    def on_palette_bar_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "palette-bar-change",
            handler,
            params=params,
        )
        return self

    def on_recent_colors_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "recent-colors-change",
            handler,
            params=params,
        )
        return self


class ColorPickerPanel(BaseElement):
    def __init__(
        self,
        value: typing.Optional[str] = None,
        *,
        model_value: typing.Optional[str] = None,
        recent_colors: typing.Optional[typing.Union[list[str], bool]] = None,
        **kwargs: Unpack[TColorPickerPanelProps],
    ):
        super().__init__("t-color-picker-panel")

        self.props({"recent-colors": recent_colors})
        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

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

    def on_palette_bar_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "palette-bar-change",
            handler,
            params=params,
        )
        return self

    def on_recent_colors_change(
        self,
        handler: EventMixin,
        *,
        params: typing.Optional[list] = None,
    ):
        self.on(
            "recent-colors-change",
            handler,
            params=params,
        )
        return self


class TColorPickerProps(TypedDict, total=False):
    borderless: bool
    clearable: bool
    color_modes: list
    disabled: bool
    enable_alpha: bool
    enable_multiple_gradient: bool
    format: typing.Literal[
        "HEX", "HEX8", "RGB", "RGBA", "HSL", "HSLA", "HSV", "HSVA", "CMYK", "CSS"
    ]
    input_props: dict
    popup_props: dict
    default_recent_colors: list
    select_input_props: dict
    show_primary_color_preview: bool
    size: typing.Literal["small", "medium", "large"]
    swatch_colors: list
    default_value: str
    on_change: EventMixin
    on_clear: EventMixin
    on_palette_bar_change: EventMixin
    on_recent_colors_change: EventMixin


class TColorPickerPanelProps(TypedDict, total=False):
    color_modes: list
    disabled: bool
    enable_alpha: bool
    enable_multiple_gradient: bool
    format: typing.Literal[
        "HEX", "HEX8", "RGB", "RGBA", "HSL", "HSLA", "HSV", "HSVA", "CMYK", "CSS"
    ]
    default_recent_colors: list
    show_primary_color_preview: bool
    swatch_colors: list
    default_value: str
    on_change: EventMixin
    on_palette_bar_change: EventMixin
    on_recent_colors_change: EventMixin
