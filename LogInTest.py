import time
import unittest
from globalData import driver
from logInPage import logInPg
from HudlHompage import HudlHomePg


class logInTest(unittest.TestCase):

    def TestHome(self):
        home = HudlHomePg()
        self.assertTrue(home.is_title_matches())
        home.clickLogin()
        time.sleep(15)
        driver.close()


    def TestLogin(self):
        Login = logInPg()

        Login.testRemeberMe()
        time.sleep(15)
        driver.close()

        Login.testHelp()
        time.sleep(15)
        driver.close()

        Login.testLogIn()
        time.sleep(15)
        driver.close()





