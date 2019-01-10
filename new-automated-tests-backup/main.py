import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from selenium import webdriver
from splinter import Browser

# FMC Automation Global Variables

# browser variables
CHROME = 'chrome'
FIREFOX = 'firefox'

# FMC server variables
MANUAL_PATH = '/manual-set-locale'
AU_PATH = '/au/'
US_PATH = '/us/'

STOREFRONT_URL_STAGE = 'https://stage.fitmycar.com'
STOREFRONT_URL_PRODTEST = 'https://prodtest.fitmycar.com'
STOREFRONT_URL_PRODUCTION = 'https://www.fitmycar.com'

# FMC locale variables
AUSTRALIA = 'Australia'
USA = 'U.S.A'

# test status variables
TEST_FAILED = 'FAILED'
TEST_PASSED = 'PASSED'
TEST_PENDING = 'PENDING'

def main():
	iphoneSix = { "deviceName" : "iPhone 6" }
	chromeOptions = webdriver.ChromeOptions()
	chromeOptions.add_experimental_option("mobileEmulation", iphoneSix)
	chromeBrowser = Browser(CHROME, options=chromeOptions)
	
	chromeBrowser.visit(STOREFRONT_URL_PRODUCTION + AU_PATH)
	chromeBrowser.find_by_css('li[class=ht-search-li').click()
	for key in chromeBrowser.type('query', 'car mats' + Keys.ENTER, slowly=True):
		pass
	# scroll down then scroll up OPEN
	assert chromeBrowser.find_by_id('productSelect')
	chromeBrowser.find_by_id('ht-sbc-tab2').click()
	for key in chromeBrowser.type('make-input', 'mazda', slowly=True):
		pass
	chromeBrowser.find_by_css('li[rel="34"').click()
	for key in chromeBrowser.type('model-input', 'mazda 6', slowly=True):
		pass
	chromeBrowser.find_by_css('li[rel="243"').click()
	chromeBrowser.find_by_css('li[rel="2"').click() #Wagon
	chromeBrowser.find_by_css('li[rel="129"').click() #2012-Current
	chromeBrowser.find_by_id('vehicleSearchCategoryButton').click()

	time.sleep(5)
	chromeBrowser.quit()

if __name__ == "__main__":
	main()