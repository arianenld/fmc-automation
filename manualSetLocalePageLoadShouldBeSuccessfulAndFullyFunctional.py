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
			self.setTerminalColors(STYLE_FAILED)
			print ("[ERROR] Incorrect URL provided as parameter.")
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
		except Exception as err:
			self.setTerminalColors(STYLE_FAILED)
			print ("[ERROR] Expected element/s not displaying on website.")
			self.quit()			

# test functions
def manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional():
	chromeTester = ManualLocalePageVerifier(CHROME_BROWSER, STAGE_URL_FMC_STOREFRONT)
	chromeTester.testLocale(AUSTRALIA)
	chromeTester.back()
	chromeTester.testLocale(USA)
	chromeTester.result(manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional.__name__)
	chromeTester.quit()

def homePageElementsShouldBeDisplayedAndFullyFunctional():
	chromeTester = BrowserTester(CHROME_BROWSER, STAGE_URL_FMC_STOREFRONT)

# test execution
def main():
	manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional()
	# homePageElementsShouldBeDisplayedAndFullyFunctional()
	
main()