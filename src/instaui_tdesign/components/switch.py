from __future__ import annotations

import typing

from instaui import ui
from instaui.internal.ui.slot import Slot
from typing_extensions import TypedDict, Unpack

from ._base_element import BaseElement
from ._utils import handle_event_from_props, handle_props, try_setup_vmodel


class Switch(BaseElement):
    def __init__(
        self,
        value: typing.Optional[bool] = None,
        **kwargs: Unpack[TSwitchProps],
    ):
        super().__init__("t-switch")
        model_value = kwargs.pop("model_value", None)
        try_setup_vmodel(self, value)

        self.props(handle_props(kwargs, model_value=model_value))  # type: ignore
        handle_event_from_props(self, kwargs)  # type: ignore

    @property
    def label_slot(self):
        """label_slot prop for easier access to label slot in td.switch.

        Example:
        .. code-block:: python
            with td.switch(size="large").label_slot as p:
                color = ui.js_computed(inputs=[p.value], code='v=> v ? "white" : "black"')
                ui.text(ui.str_format(r"value: {}", p.value)).style({"color": color})
        """
        return _LabelSlot(self.add_slot("label"))

    def on_change(self, handler: ui.TEvent):
        self.on("change", handler)
        return self


class _LabelSlot:
    def __init__(self, slot: Slot):
        self.__slot = slot

    @property
    def value(self):
        return self.__slot.slot_props("value")

    def __enter__(self):
        self.__slot.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.__slot.__exit__(exc_type, exc_val, exc_tb)


class TSwitchProps(TypedDict, total=False):
    model_value: bool
    before_change: str
    custom_value: list
    disabled: bool
    label: typing.Union[str, list]
    loading: bool
    size: typing.Literal["small", "medium", "large"]
    default_value: typing.Literal["number"]
    on_change: ui.TEvent
