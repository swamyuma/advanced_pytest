import pytest
from selenium.webdriver import Firefox, Chrome

@pytest.fixture
def webdriver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_nix_in_website_title(webdriver):
    webdriver.get('https://nixos.org/nix')
    assert 'Nix' in webdriver.title
