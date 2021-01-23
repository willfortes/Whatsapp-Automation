from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyqrcode
import png
import os

class autoWhats:

    #Initialize path variables
    dir_path = os.getcwd()
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    profile = os.path.join(dir_path, "profile", "wpp")

    #Contructor add arguments and initialize Chromedriver
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir={}".format(self.profile))
        self.options.add_argument('--no-sandbox')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--disable-setuid-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(self.chromedriver, options=self.options)
        self.driver.get("https://web.whatsapp.com/")
        print("Inicializando Automação de whatsapp...")
        self.driver.implicitly_wait(15)

    #Open new chat 
    def newChat(self, contact):
        try:
            self.box_msg = self.driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")
            self.box_msg.send_keys(contact, Keys.ENTER)
        except Exception as e:
            raise e
    
    #send message in open chat
    def sendMessage(self, msg):
        try:
            time.sleep(2)
            self.box_msg = self.driver.find_elements_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")[1]
            self.box_msg.send_keys(msg)
            time.sleep(1)
            self.button_send = self.driver.find_element_by_xpath("//button[@class='_2Ujuu']")
            self.button_send.click()
            sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

#Start Whatsapp Bot
if __name__ == '__main__':
    names = ["<Number>", "<Name>"]
    count = 0

    bot = autoWhats() 

    while True:
        bot.newChat(names[count])
        bot.sendMessage(f'Ola {names[count]}')
        count = count + 1