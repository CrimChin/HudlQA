from globalData import wait, driver
from selenium.webdriver.common.by import By


class HudlHomePg:
    homePageTitle = "Performance analysis tools for sports teams and athletes at every level."

    def clickLogin(self):
        """Click the Login button from the homepage"""
        driver.get("http://www.hudl.com")
        wait()
        HomeLogInXpath = (By.XPATH, "//a[@href='/login']")
        LoginPage = driver.find_element(HomeLogInXpath).click()
        return LoginPage

    def is_title_matches(self):
        """Verifies if the title of the homepage is the expected"""
        return wait.until(
            lambda x: (self.homePageTitle in driver.title))
