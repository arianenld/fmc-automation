import requests

from fmcGlobals import *
from splinter import Browser

class BrowserTester:

	def __init__(self, browser, url):
		self.browser = Browser(browser)
		self.browser.visit(url)
		self.baseUrl = url
		self.expectedUrl = ""
		self.status = TEST_PENDING
		print (NORMAL_WHITE_FONT)
				
	def loadPage(self, selectedButton):
		selectedButton.click()
		try:
			assert self.isCorrectPageSuccessfullyLoaded()
			self.status = TEST_PASSED
		except Exception as err:
			print (FAILED + "[ERROR] Page is not successfully loaded.")
			self.status = TEST_FAILED
			self.quit()

	def isCorrectPageSuccessfullyLoaded(self):
		return self.isUrlCorrect() and self.isHttpStatusSuccess()

	def isUrlCorrect(self):
		return self.expectedUrl == self.browser.url

	def isHttpStatusSuccess(self):
		httpRequest = requests.get(self.browser.url)
		return httpRequest.status_code == requests.codes.ok

	def back(self):
		self.browser.back()

	def forward(self):
		self.browser.forward()

	def quit(self):
		self.browser.quit()

	def result(self, testName):
		if(self.status == TEST_PASSED):
			resultDisplay = PASSED

		elif(self.status == TEST_PENDING):
			resultDisplay = PENDING

		# TEST_FAILED is handled in exception
		print (resultDisplay + testName)


class ManualLocalePageVerifier(BrowserTester):

	def testLocale(self, selectedLocale):
		try:
			assert self.browser.url == self.baseUrl + MANUAL_SET_LOCALE

			if(AUSTRALIA == selectedLocale):
				self.expectedUrl = self.baseUrl + AU_PATH
				localeButton = self.browser.find_by_tag('h4')[0]
			elif(USA == selectedLocale):
				self.expectedUrl = self.baseUrl + US_PATH
				localeButton = self.browser.find_by_tag('h4')[1]
			
			self.checkElements()
			self.loadPage(localeButton)

		except Exception as err:
			print (FAILED + "[ERROR] Incorrect URL provided as parameter.")
			self.quit()

	def checkElements(self):
		try:
			# add id to fitmycar logo on manual_set_locale, then assert this element
			# add id to "Choose a Country", then assert this element
			assert self.browser.find_by_text(AUSTRALIA)
			assert self.browser.find_by_text(USA)
		except Exception as err:
			print (FAILED + "[ERROR] Expected element/s not displaying on website.")
			self.quit()			

# test functions
def manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional():
	chromeTester = ManualLocalePageVerifier(CHROME_BROWSER, PROD_URL_FMC_STOREFRONT)
	chromeTester.testLocale(AUSTRALIA)
	chromeTester.back()
	chromeTester.testLocale(USA)
	chromeTester.result(manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional.__name__)
	chromeTester.quit()

# test execution
def main():
	manualSetLocalePageLoadShouldBeSuccessfulAndFullyFunctional()

main()