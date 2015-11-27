import pytest
from selenium.webdriver import Firefox, Chrome

@pytest.fixture(scope='session')
def webdriver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_nix_in_website_title(webdriver):
    webdriver.get('https://nixos.org/nix')
    assert 'Nix' in webdriver.title

def test_pytest_in_website_title(webdriver):
    webdriver.get('https://pytest.org/latest')
    assert 'pytest' in webdriver.title
