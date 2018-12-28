from TestHelpers import BrowserTester
from fmcGlobals import *
#from selenium import webdriver

# test also on Safari
def canSuccessfullyPurchaseItemsOnAuSiteViaChromeOnIphone():
	"""
	targetMobile = {"device" : "Google Nexus 5"}
	chromeOptions = webdriver.chromeOptions()
	chromeOptions.add_experimental_option('mobileEmulation', targetMobile)
	chromeTester = BrowserTester('chrome', options=chromeOptions)
	"""

	chromeTester = BrowserTester(CHROME_BROWSER)
	chromeTester.visitUrl(PROD_URL_FMC_STOREFRONT + AU_PATH)
	# check if elements are present
	chromeTester.browser.find_by_css('li[class=ht-search-li').click()
	for key in chromeTester.browser.type('query', 'car mats', slowly=True):
		pass
	# press enter key
	# chromeTester.quit()

# test execution
def main():
	canSuccessfullyPurchaseItemsOnAuSiteViaChromeOnIphone()
	# https://stackoverflow.com/questions/45645838/python-having-errors-with-selenium-webdriver?rq=1

if __name__ == "__main__":
	main()