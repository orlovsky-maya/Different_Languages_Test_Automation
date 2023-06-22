import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language, example: fr, ru or es")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_data_dir', action='store', default=None,
                     help="Enter user directory for browser")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
        chrome_options.add_argument("--remote-debugging-port=9515")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.close()
