from TestHelpers import BrowserTester
from fmcGlobals import *

class ManualLocalePageVerifier(BrowserTester):

	def testLocale(self, selectedLocale):
		try:
			assert self.browser.url == self.baseUrl + MANUAL_SET_LOCALE
			self.checkElements()
			self.findLocaleButton(selectedLocale).click()
			self.verifySuccessfulPageLoad()

		except Exception as err:
			self.printErrorMessage ("[ERROR] Incorrect URL provided as parameter.")
			self.quit()

	def findLocaleButton(self, locale):
		localeButton = None

		if(AUSTRALIA == locale):
			self.expectedUrl = self.baseUrl + AU_PATH
			localeButton = self.browser.find_by_tag('h4')[0]
		elif(USA == locale):
			self.expectedUrl = self.baseUrl + US_PATH
			localeButton = self.browser.find_by_tag('h4')[1]

		return localeButton

	def checkElements(self):
		try:
			# add id to fitmycar logo on manual_set_locale, then assert this element
			# add id to "Choose a Country", then assert this element
			assert self.browser.find_by_text(AUSTRALIA)
			assert self.browser.find_by_text(USA)

		except Exception as err: # err variable not used
			self.printErrorMessage ("[ERROR] Expected element/s not displaying on website.")
			self.quit()			

class HomePageVerifier(BrowserTester):
	def testHomePage(self, homePageUrl):
		try:
			self.visitUrl(homePageUrl)
			assert self.browser.url == homePageUrl
			self.checkElements()
			# self.findLocaleButton(selectedLocale).click()
			# self.verifySuccessfulPageLoad()

		except Exception as err:
			self.printErrorMessage ("[ERROR] Incorrect URL provided as parameter.")
			self.quit()

	def checkElements(self):
		try:
			# add specific message for assertion
			# catch exact error
			assert self.browser.find_by_css('div[class="ht-carousel-container pos-fl w-100"') # USP
			assert self.browser.find_by_css('a[class="header-logo header-logo-image init"') # FMC Logo
			assert self.browser.find_by_id('ht-products-tab')
			assert self.browser.find_by_id('ht-sbc-tab')
			assert self.browser.find_by_id('ht-community-tab')
			assert self.browser.find_by_id('ht-help-tab')
			assert self.browser.find_by_css('li[class=ht-search-li')
			assert self.browser.find_by_css('li[class="hidden-xs hidden-sm ht-account-li"')
			assert self.browser.find_by_css('li[class=ht-cart-li')
			

			assert self.browser.find_by_css('div[class=homepage-banner-container')
			# assert image src = https://d3v52uw9mwsoe.cloudfront.net/fitmycar/static-assets/images/banner-homepage.jpg
			assert self.browser.find_by_css('div[class=homepage-banner-header')
			# assert header content "The gear your car needs to look its best"
			assert self.browser.find_by_css('button[class=sbc-body-button')
			# assert button text = "Shop by car"

			# Product Category Carousel 
			productCategoryCarousel = self.browser.find_by_css('div[class=carousel-image-container')
			# assert productCategoryCarousel

			# print failing element
			# assert self.browser.find_by_css('div[class="header-logo header-logo-image init"') #should fail assertion

		except Exception as err: # err variable not used
			self.printErrorMessage ("[ERROR] Expected element/s not displaying on website.")
			self.quit()

# test functions
def manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional():
	chromeTester = ManualLocalePageVerifier(CHROME_BROWSER)
	chromeTester.visitUrl(STAGE_URL_FMC_STOREFRONT)

	chromeTester.testLocale(AUSTRALIA)
	chromeTester.back()
	chromeTester.testLocale(USA)
	chromeTester.result(manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional.__name__)
	chromeTester.quit()

def homePageElementsShouldBeDisplayedAndFullyFunctional():
	firefoxTester = HomePageVerifier(FIREFOX_BROWSER)
	firefoxTester.testHomePage(STAGE_URL_FMC_STOREFRONT + AU_PATH)
	firefoxTester.quit()

# test execution
def main():
	manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional()
	# homePageElementsShouldBeDisplayedAndFullyFunctional()

if __name__ == "__main__":
	main()