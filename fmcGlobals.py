# FMC Automation Global Variables

# browser variables
CHROME_BROWSER = 'chrome'
FIREFOX_BROWSER = 'firefox'

# FMC server variables
MANUAL_SET_LOCALE = '/manual-set-locale'
AU_PATH = '/au/'
US_PATH = '/us/'

STAGE_URL_FMC_STOREFRONT = 'https://stage.fitmycar.com'
PRODTEST_URL_FMC_STOREFRONT = 'https://prodtest.fitmycar.com'
PROD_URL_FMC_STOREFRONT = 'https://www.fitmycar.com'

# FMC locale variables
AUSTRALIA = 'Australia'
USA = 'U.S.A'

# test status variables
TEST_FAILED = 'FAILED'
TEST_PASSED = 'PASSED'
TEST_PENDING = 'PENDING'

# font modifiers
""" Change terminal background and font color:
#http://ozzmaker.com/add-colour-to-text-in-python/
	\033[	Escape code
	0		Text Style, no effect
	1		Text Style, bold
	31		Text color, red
	32		Text color, green
	37		Text color, white 
	40m		Background color, black
"""
BOLD_GREEN_FONT = '\033[1;32;40m'
BOLD_RED_FONT = '\033[1;31;40m'
BOLD_WHITE_FONT = '\033[1;37;40m'
NORMAL_WHITE_FONT = '\033[0;37;40m'

# test result variables
STYLED_PASSED = BOLD_GREEN_FONT + 'PASSED' + NORMAL_WHITE_FONT + ' - '
STYLED_FAILED = BOLD_RED_FONT + 'FAILED' + NORMAL_WHITE_FONT + ' - '
STYLED_PENDING = BOLD_WHITE_FONT + 'PENDING' + NORMAL_WHITE_FONT + ' - '