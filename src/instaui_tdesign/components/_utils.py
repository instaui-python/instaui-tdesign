from instaui import ui
from instaui.internal.ui.element import Element


def handle_props(props: dict, *, model_value=None):
    props = {
        k.replace("_", "-"): v for k, v in props.items() if not isinstance(v, ui.TEvent)
    }
    if model_value is not None:
        props["modelValue"] = model_value
    return props


def handle_event_from_props(element: Element, props: dict):
    for k, v in props.items():
        if isinstance(v, ui.TEvent):
            # 'on_click' -> 'click'
            element.on(k.replace("on_", ""), v)


def try_setup_vmodel(
    element: Element,
    value,
    *,
    prop_name: str = "value",
):
    if value is None:
        return
    if ui.is_expression(value):
        element.vmodel(value, prop_name=prop_name)
        return

    element.props({prop_name: value})
