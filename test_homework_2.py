import pytest
from selene.support.shared import browser, config
from selene import be, have

@pytest.fixture(scope='session')
def open_browser():
    browser.config.window_height = 1200
    browser.config.window_width = 1500
    browser.open('https://google.com')
    pass

def test_first_test(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    pass

def test_nothing_found():
    browser.element('[aria-label="Очистить"]').click()
    browser.element('[name="q"]').should(be.blank).type('qwertyuiopasdfgghhjklzxc').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    pass

