from instaui import html, ui

from __tests.testing_web.context import Context
from __tests.utils.anchor_utils import click_anchor_item, should_anchor_item_active
from instaui_tdesign import td


def test_base(context: Context):
    @context.register_page
    def index():
        with td.card().style("position: fixed;  right: 2rem;"), td.anchor():
            td.anchor_item(href="#page1", title="Page 1")
            td.anchor_item(href="#page2", title="Page 2")
            td.anchor_item(href="#page3", title="Page 3")

        with td.card().style("height: 100vh"):
            html.h1("Page1").props({"id": "page1"})
            ui.text("Content1")

        with ui.column().style("height: 100vh"):
            html.h1("Page2").props({"id": "page2"})
            ui.text("Content2")

        with ui.column().style("height: 100vh"):
            html.h1("Page3").props({"id": "page3"})
            ui.text("Content3")

    context.open()
    context.find_by_text("Content3").scroll_into_view_if_needed()

    should_anchor_item_active(context, "Page 2")
    click_anchor_item(context, "Page 1")

    context.should_see("Content1")
