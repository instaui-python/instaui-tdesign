from instaui import ui
import instaui_tdesign as td
from __tests.testing_web.context import Context
from __tests.testing_web.style_testing_utils import update_style, use_computed_style

td.use()


def test_base(context: Context):
    @context.register_page
    def index():
        info = use_computed_style("background-color", target_selector=".target")
        info.create_button()

        with ui.theme(accent_color="blue"):
            ui.text(info.value)
            td.button("test").classes("target")

    context.open()
    update_style(context)
    context.should_see("rgb(0, 144, 255)")


def test_dark(context: Context):
    @context.register_page
    def index():
        info = use_computed_style("background-color", target_selector=".target")
        info.create_button()
        dark = ui.use_dark()

        with ui.theme(accent_color="blue"):
            td.checkbox(dark)
            ui.text(info.value)
            td.button("test").classes("target")

    context.open()
    checkbox = context.find("checkbox")
    checkbox.set_checked(True, force=True)

    update_style(context)
    context.should_see("rgb(59, 158, 255)")

    checkbox.set_checked(False, force=True)

    update_style(context)
    context.should_see("rgb(0, 144, 255)")
