import pytest
from selene.support.shared import browser, config
from selene import be, have

@pytest.fixture(scope='session')
def open_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1500
    browser.open('https://google.com')
    pass

def test_nothing_found(open_browser):
    browser.element('[name="q"]').should(be.blank).type('qwertyuiopasdfgghhjklzxc').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    return "Ничего не нашлось"

