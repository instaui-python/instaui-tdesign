from __future__ import annotations
import copy
import typing

from instaui import ui
from instaui_tdesign.components._icon_param_utils import make_icon_for_bool_or_str
from ._base_element import BaseElement
from instaui.event.event_mixin import EventMixin
from typing_extensions import TypedDict, Unpack
from ._utils import handle_props, handle_event_from_props

if typing.TYPE_CHECKING:
    from instaui.vars.types import TMaybeRef


class Message(BaseElement):
    def __init__(
        self,
        content: typing.Optional[TMaybeRef[str]] = None,
        *,
        icon: str | bool | None = None,
        **kwargs: Unpack[TMessageProps],
    ):
        super().__init__("t-message")
        self.props({"content": content})
        make_icon_for_bool_or_str(self, "icon", icon)
        self.props(handle_props(kwargs))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    def on_close(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "close",
            handler,
            extends=extends,
        )
        return self

    def on_close_btn_click(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "close-btn-click",
            handler,
            extends=extends,
        )
        return self

    def on_duration_end(
        self,
        handler: EventMixin,
        *,
        extends: typing.Optional[typing.List] = None,
    ):
        self.on(
            "duration-end",
            handler,
            extends=extends,
        )
        return self


class MessagePlugin:
    @staticmethod
    def info(**options: Unpack[TMessageOptions]):
        """
        Displays an informational message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Info").on_click(
                td.message_plugin.info(content="Operation completed", duration=3000)
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.info(options)",
        )

    @staticmethod
    def warning(**options: Unpack[TMessageOptions]):
        """
        Displays a warning message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Warning").on_click(
                td.message_plugin.warning(content="Please check your input")
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.warning(options)",
        )

    @staticmethod
    def error(**options: Unpack[TMessageOptions]):
        """
        Displays an error message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Error").on_click(
                td.message_plugin.error(content="Operation failed")
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.error(options)",
        )

    @staticmethod
    def success(**options: Unpack[TMessageOptions]):
        """
        Displays a success message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Success").on_click(
                td.message_plugin.success(content="Operation successful")
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.success(options)",
        )

    @staticmethod
    def loading(**options: Unpack[TMessageOptions]):
        """
        Displays a loading message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Loading").on_click(
                td.message_plugin.loading(content="Processing...")
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.loading (options)",
        )

    @staticmethod
    def question(**options: Unpack[TMessageOptions]):
        """
        Displays a question message using TDesign's MessagePlugin.

        Args:
            content (str): The text content to display in the message.
            attach (str): CSS selector for the element to attach the message to.
            duration (float): How long the message stays visible in milliseconds.
            close_btn (str | bool): Close button configuration. Can be boolean or custom HTML string.
            class_name (str): Additional CSS class name for custom styling.
            offset (tuple[str | int, str | int]): Offset values for message positioning.
            placement (Literal): Position where the message appears. Options include:
                "center", "top", "left", "right", "bottom",
                "top-left", "top-right", "bottom-left", "bottom-right".
            zIndex (int): Z-index for controlling stack order.
            style (str): Inline CSS styles for the message.

        Example:
        .. code-block:: python
            td.button("Show Question").on_click(
                td.message_plugin.question(content="Are you sure?")
            )
        """
        return ui.js_event(
            inputs=[_handle_message_options(typing.cast(dict, options))],
            code=r"(options)=> $tdesign.MessagePlugin.question(options)",
        )

    @staticmethod
    def close_all():
        """
        Closes all currently open message instances.

        Example:
        .. code-block:: python
            td.button("Close All").on_click(
                td.message_plugin.close_all()
            )
        """
        return ui.js_event(
            code=r"()=> $tdesign.MessagePlugin.closeAll()",
        )


class TMessageProps(TypedDict, total=False):
    close_btn: str | bool
    duration: float
    theme: TMaybeRef[
        typing.Literal["info", "success", "warning", "error", "question", "loading"]
    ]
    on_close: EventMixin
    on_close_btn_click: EventMixin
    on_duration_end: EventMixin


class TMessageOptions(TypedDict, total=False):
    content: str
    attach: str
    duration: float
    close_btn: str | bool
    class_name: str
    offset: tuple[str | int, str | int]
    placement: typing.Literal[
        "center",
        "top",
        "left",
        "right",
        "bottom",
        "top-left",
        "top-right",
        "bottom-left",
        "bottom-right",
    ]
    zIndex: int
    style: str


def _handle_message_options(options: dict):
    options = copy.deepcopy(options)
    if "close_btn" in options:
        options["closeBtn"] = options.pop("close_btn")

    return options
