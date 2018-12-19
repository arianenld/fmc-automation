import requests

from fmcGlobals import *
from splinter import Browser

class BrowserTester:

	def __init__(self, browser):
		self.browser = Browser(browser)
		self.baseUrl = ''
		self.expectedUrl = ''
		self.status = TEST_PENDING

	def visitUrl(self, url):
		self.browser.visit(url)
		self.baseUrl = url
		self.setTerminalColors(NORMAL_WHITE_FONT)

	def setTerminalColors(self, style):
		print (style, end = '')

	def verifySuccessfulPageLoad(self):
		try:
			assert self.isCorrectPageSuccessfullyLoaded()
			self.status = TEST_PASSED
		except Exception:
			printErrorMessage ("[ERROR] Page is not successfully loaded.")
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
			self.setTerminalColors(STYLED_PASSED)

		elif(self.status == TEST_PENDING):
			self.setTerminalColors(STYLED_PENDING)

		# TEST_FAILED is handled in exception
		print (testName)

	def printErrorMessage(self, message):
		self.setTerminalColors(STYLED_FAILED)
		print (message)