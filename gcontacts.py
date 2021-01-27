from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

class googleContacts:
    #User Variables
    email = "<Your mail>"
    password = "<Your password>"

    #Initialize path variables
    dir_path = os.getcwd()
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    profile = os.path.join(dir_path, "profile", "gcontacts")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument(r"user-data-dir={}".format(self.profile))
        self.options.add_argument('--no-sandbox')
        #self.options.add_argument('--headless')
        self.options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--disable-setuid-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=self.options)
        self.driver.get("https://contacts.google.com/")

    def login(self):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@type='email']").send_keys(self.email, Keys.ENTER)
            time.sleep(2)
            self.driver.find_element_by_xpath("//input[@type='password']").send_keys(self.password, Keys.ENTER)
        except Exception as e:
            raise e

    def exportContacts(self):
        try:
            time.sleep(4)
            self.driver.find_element_by_link_text("Exportar").click()
            time.sleep(2)
            actions = ActionChains(self.driver) 
            actions.send_keys(Keys.TAB * 2)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        except Exception as e:
            raise e


if __name__ == '__main__':
    gContacts = googleContacts()
    gContacts.login()
    gContacts.exportContacts()