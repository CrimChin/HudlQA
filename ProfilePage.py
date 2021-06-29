import globalData
from globalData import wait,driver, UserNameCss
from selenium.webdriver.support import expected_conditions as conditions


class ProfilePg(object):

    def is_logged_in(self):
        """Verifies if the user is logged in"""
        element = wait.until(
            conditions.visibility_of_element_located(globalData.UserNameCss),
            "The element didn't exist after 15 seconds.")
        return element.is_displayed()

    def is_title_matches(self):
        """Verifies if the title of the main page is the expected"""
        return wait.until(
            lambda x: (UserNameCss in driver.title))
