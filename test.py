from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture(scope="sessions", autouse=True)
def window_size():
    browser.config.window_height = 500
    browser.config.window_width = 1000