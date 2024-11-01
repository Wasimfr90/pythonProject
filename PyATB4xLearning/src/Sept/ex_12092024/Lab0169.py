from BrowserPackage.OpenBrowser import start_browser
from BrowserPackage.CloseBrowser import close_browser

def test_case():
    start_browser()
    print("I am executing a code TC1")
    close_browser()

test_case()