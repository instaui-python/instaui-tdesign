from __tests.testing_web.context import Context
from instaui import ui
import instaui_tdesign as td


def test_table(context: Context):
    @context.register_page
    def index():
        cols = [
            {"colKey": "value", "title": "name"},
        ]
        data = ui.state(
            [
                {"value": "foo"},
                {"value": "bar"},
            ]
        )

        td.table(data, columns=cols)

    context.open()
    context.should_see("name")
    context.should_see("foo")


def test_cell_slot(context: Context):
    @context.register_page
    def index():
        cols = [
            {"colKey": "name", "title": "name", "cell": "c_name"},
        ]
        data = ui.state(
            [
                {"name": "foo"},
                {"name": "bar"},
            ]
        )

        with td.table(data, columns=cols).add_cell_slot("c_name") as slot:
            td.button(slot.param("row")["name"])

    context.open()
    context.expect(context.find("button", name="foo")).to_be_visible()


def test_update_data_with_cell_slot(context: Context):
    @context.register_page
    def index():
        cols = [
            {"colKey": "name", "title": "name", "cell": "c_name"},
            {"colKey": "mid", "title": "mid", "cell": "c_mid"},
            {"colKey": "new_value", "title": "new value", "cell": "c_new_value"},
        ]
        data = ui.state(
            [
                {"name": "value", "pre": "x", "mid": "foo"},
            ]
        )

        table = td.table(data, columns=cols)

        with table.add_cell_slot("c_new_value") as slot:
            ui.text(
                ui.str_format(
                    "{pre}-{mid}-{value}",
                    pre=slot.param("row")["pre"],
                    mid=slot.param("row")["mid"],
                    value=slot.param("row")["name"],
                )
            )

        with table.add_cell_slot("c_mid") as slot:
            td.input(slot.param("row")["mid"])

    context.open()
    context.should_see("x-foo-value")
    context.find("input").fill("bar")
    context.should_see("x-bar-value")
