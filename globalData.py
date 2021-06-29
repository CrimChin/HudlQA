from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
wait = WebDriverWait(driver, 15)

validEmail = "tonyewue@students.kennesaw.edu"
invalidEmail = "chinyony@gmail.com"
validPassword = "testPass123"
invalidPassword = "gibberish2123"

EmailId = (By.ID, "email")
EmailCss = (By.CSS_SELECTOR, "input#email")
PassId = (By.ID, "password")
PassCss = (By.CSS_SELECTOR, "input#password")
LoginBttnID = (By.ID, "logIn")
LoginBttnCss = (By.CSS_SELECTOR, "button#logIn")
errorTextCss = (By.CSS_SELECTOR, "div.login-error-container > p")
HomeLogInXpath = (By.XPATH, "//a[@href='/login']")

UserNameCss = (By.CSS_SELECTOR, "div.hui-globalusermenu")
DisplayNameCss = (By.CSS_SELECTOR, "div.hui-globaluseritem__display-name > span")


