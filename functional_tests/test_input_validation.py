from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from .base import FunctionalTest
import sys

def InputValidationUser(FunctionalTest):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url


    def setUp(self):
        self.browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
            firefox_path='D:\\PyCharm_Project\\Mozilla_ESR\\firefox.exe'
        ))
        #Wait for the web to load, total waiting time is 3 second
        self.browser.implicitly_wait(6)

    def tearDown(self):
        self.browser.quit()

    
