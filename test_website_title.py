import pytest
from selenium import webdriver

browsers = {
                'firefox': webdriver.Firefox(),
                'chrome': webdriver.Chrome('chromedriver 2'),
          }

# dependency consrtuction is moved out of test case 
# use scope=session to use the same instance of a browser to test both sites
# pytest will cache this fixture for the entire test session
# pass in params which contains the browser names and details
# use addfinalizer for a clean teardown after the tests are completed
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
