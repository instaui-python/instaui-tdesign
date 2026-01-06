from __tests.testing_web.context import Context
from instaui_tdesign import td
from instaui import ui


def test_base(context: Context):
    @context.register_page
    def index():
        with td.breadcrumb():
            td.breadcrumb_item("foo")
            td.breadcrumb_item("bar")

    context.open()
    context.should_see("foo")


def test_item_vfor(context: Context):
    @context.register_page
    def index():
        items = ["foo", "bar"]

        with td.breadcrumb():
            with ui.vfor(items) as item:
                td.breadcrumb_item(item)

    context.open()
    context.should_see("foo")
