import pytest
from selenium import webdriver

browsers = {
                'firefox': webdriver.Firefox(),
                'chrome': webdriver.Chrome('/Users/unagaswamy/Downloads/chromedriver'),
          }

@pytest.fixture(scope='session', params=browsers.keys())
def driver(request):
    browser = browsers[request.param]
    request.addfinalizer(lambda *args: browser.quit())
    return browser

@pytest.mark.parametrize("site, expected_title",
                [
                    ("https://nixos.org/nix", "Nix"),
                    ("https://pytest.org/latest", "pytest")
                ]
          )
def test_site_in_website_title(site, expected_title, driver):
    driver.get(site)
    assert expected_title in driver.title
