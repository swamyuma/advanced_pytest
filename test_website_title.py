import pytest
from selenium.webdriver import Firefox, Chrome

@pytest.fixture(scope='session')
def webdriver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.parametrize("site, expected_title",
                [
                    ("https://nixos.org/nix", "Nix"),
                    ("https://pytest.org/latest", "pytest")
                ]
          )
def test_site_in_website_title(site, expected_title, webdriver):
    webdriver.get(site)
    assert expected_title in webdriver.title
#    assert 'pytest' in webdriver.title
