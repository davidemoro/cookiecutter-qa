

def test_basic(browser, base_url):
    browser.visit(base_url)
    assert '{{cookiecutter.base_url}}' in browser.url
