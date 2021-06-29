import globalData
from globalData import wait,driver





class logInPg:
    def testLogIn(self):
        """Tests the Login functionality by putting in a username and password,
        then pressing the login button """
        driver.get("https://www.hudl.com/login")
        wait()
        driver.find_element_by_id("email").send_keys(globalData.validEmail)
        driver.find_element_by_id("password").send_keys(globalData.validPassword)
        LoginButton = driver.find_element_by_id("logIn").click()

    def testHelp(self):
        """Tests the functionality of the help button by pressing it"""
        driver.get("https://www.hudl.com/login")
        wait()
        return driver.find_element_by_id("forgot-password-link").click()

    def testRemeberMe(self):
        """Test the functionality of the Remember Button by pressing it"""
        driver.get("https://www.hudl.com/login")
        wait()
        return driver.find_element_by_id("remember-me").click()

    """In future Work I would add to the existing methods a verification step
    to ensure that the help button brought users to the right page, and that
    the remember me button saved the user and password"""
