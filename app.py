from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyqrcode
import png
import os
import PySimpleGUI as sg

class autoWhats:
    #Initialize path variables
    dir_path = os.getcwd()
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    profile = os.path.join(dir_path, "profile", "wpp")

    #Contructor add arguments and initialize Chromedriver
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument(r"user-data-dir={}".format(self.profile))
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--headless')
        self.options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument('--disable-setuid-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(self.chromedriver, options=self.options)
        self.driver.get("https://web.whatsapp.com/")
        print("Inicializando Automação de whatsapp...")
        self.driver.implicitly_wait(15)

    def getQrCode(self):
        try:
            print("Getting QRCODE...")
            time.sleep(2)
            qrcode = self.driver.find_element_by_xpath("//div[@class='_1yHR2']").get_attribute("data-ref")
            qrcodeRender = pyqrcode.create(qrcode)
            qrcodeRender.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
            time.sleep(1)
            sg.Window('Whatsapp QRCODE').Layout([[ sg.Image('code.png') ]]).Read()
        except Exception as e:
            raise e

    #Open new chat 
    def newChat(self, contact):
        try:
            print("Open new chat...")
            self.box_msg = self.driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")
            self.box_msg.send_keys(contact, Keys.ENTER)
        except Exception as e:
            raise e
    
    #send message in open chat
    def sendMessage(self, msg):
        try:
            print("Sending message...")
            time.sleep(2)
            self.box_msg = self.driver.find_elements_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")[1]
            self.box_msg.send_keys(msg)
            time.sleep(1)
            self.button_send = self.driver.find_element_by_xpath("//button[@class='_2Ujuu']")
            self.button_send.click()
            time.sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

#Start Whatsapp Bot
if __name__ == '__main__':
    names = ["Willian", "Volltech"]

    bot = autoWhats() 
    bot.getQrCode()

    time.sleep(10)

    for name in names:
        bot.newChat(name)
        bot.sendMessage(f'Ola {name}')

        