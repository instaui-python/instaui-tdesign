import pytest
from __tests.testing_zero.context import ZeroContext as Context
from instaui import zero
from instaui.internal.ui.layout import clear_layout
from instaui_tdesign import td


@pytest.fixture(scope="function", autouse=True)
def page_init_lifespan_setup():
    clear_layout()
    yield


def test_default_locale(context: Context):
    def index():
        td.pagination(total=6)

    context.open(zero().to_html_str(index))
    context.should_see("共 6 条数据")


def test_us_locale(context: Context):
    td.use(locale="en_US")

    def index():
        td.pagination(total=6)

    context.open(zero().to_html_str(index))
    context.should_see("6 items")
