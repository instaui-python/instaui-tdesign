from __tests.testing_web.context import Context
from instaui_tdesign import td
from instaui import ui


def test_options(context: Context):
    @context.register_page
    def index():
        selected = ui.state("")
        options = [
            {"content": "foo", "value": 1},
            {"content": "bar", "value": 2},
        ]

        @ui.event(inputs=[ui.event_context.e()], outputs=[selected])
        def on_click(e):
            return e["content"]

        with td.dropdown(options, on_click=on_click):
            ui.text("Dropdown")

        ui.text("selected:" + selected, as_="p")

    context.open()
    context.find_by_text("Dropdown").hover()
    context.find_by_text("foo").click()
    context.should_see("selected:foo")


def test_dropdown_menu(context: Context):
    @context.register_page
    def index():
        selected = ui.state("")

        @ui.event(inputs=[ui.event_context.e()], outputs=[selected])
        def on_click(e):
            return e["content"]

        with td.dropdown(on_click=on_click):
            ui.text("Dropdown")

            with td.dropdown_menu():
                td.dropdown_item("foo", value=1)
                td.dropdown_item("bar", value=2)

        ui.text("selected:" + selected, as_="p")

    context.open()
    context.find_by_text("Dropdown").hover()
    context.find_by_text("foo").click()
    context.should_see("selected:foo")
