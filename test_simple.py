from selene.support.shared import browser
from selene import be, have
import pytest

browser.config.hold_browser_open = True

@pytest.fixture(scope="session", autouse=True)
def window_size():
    browser.config.window_height = 1000
    browser.config.window_width = 1000


def test_demoqa_window_size():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Sergey')
    browser.element('[id=lastName]').type('Sergey')
    browser.element('[id=userEmail]').type('cochise111@mail.ru')
    browser.element(' [for=gender-radio-1]').click()
    browser.element('[id=userNumber').type('917917')
    browser.element('[id=currentAddress]').type('Moscow')

def test_negative():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('1111122222555556676767wwregefvfe').press_enter()
    browser.element('[id="search"]').should(have.text('1111122222555556676767wwregefvfe'))