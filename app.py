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
        print("Headless whatsapp bot init...")
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
        self.driver.implicitly_wait(15)

    #Simulate typing human
    def typing(self, element, text):
        print("Typing...")
        textArray = list(text)

        for text in textArray:
            time.sleep(0.1)

            #by new line
            if text == "¨":
               element.send_keys(Keys.SHIFT+Keys.ENTER)
               continue

            element.send_keys(text)

    #get and generate qrcode
    def get_qr_code(self):
        try:
            print("Getting qrcode...")
            time.sleep(2)
            qrcode = self.driver.find_element_by_xpath("//div[@class='_1yHR2']").get_attribute("data-ref")
            qrcodeRender = pyqrcode.create(qrcode)
            qrcodeRender.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
            time.sleep(1)
            window = sg.Window('Whatsapp QRCODE').Layout([[ sg.Image('code.png') ]]).Read()
            time.sleep(10)
        except Exception as e:
            raise e

    #Open New Chat without being on the schedule
    def new_chat_without(self, phonenumber):
        try:
            print("Open new chat without...")
            time.sleep(15)
            self.driver.get(f'https://api.whatsapp.com/send?phone={phonenumber}')
            time.sleep(2)
            self.driver.find_element_by_id("action-button").click()
            self.driver.find_element_by_partial_link_text("use o WhatsApp Web").click()
            time.sleep(6)
        except Exception as e:
            raise e

    #Open new chat 
    def new_chat(self, contact):
        try:
            print("Open new chat...")
            self.box_msg = self.driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")
            self.box_msg.send_keys(contact, Keys.ENTER)
        except Exception as e:
            raise e
    
    #send message in open chat
    def send_message(self, msg):
        try:
            print("Sending message...")
            time.sleep(2)
            self.box_msg = self.driver.find_elements_by_xpath("//div[@class='_1awRl copyable-text selectable-text']")[1]   
            self.typing(self.box_msg, msg)
            time.sleep(1)
            self.button_send = self.driver.find_element_by_xpath("//button[@class='_2Ujuu']")
            self.button_send.click()
            time.sleep(2)
        except Exception as e:
            print("Erro send message", e)

    #Filter and send media files
    def send_media(self, path, text=""):
        try
            pass
        except Exception as e:
            raise e

    #By send videos with and without text
    def send_video(self, path, text):
        try
            pass
        except Exception as e:
            raise e

    #By send images with and without text
    def send_image(self, path, text):
        try
            pass
        except Exception as e:
            raise e

    #By send files ex: PDF and etc..
    def send_file(self, path):
        try
            pass
        except Exception as e:
            raise e

#Start Whatsapp Bot
if __name__ == '__main__':
    names = ["<Contact Name>"]

    bot = autoWhats() 
    bot.get_qr_code()
    bot.new_chat_without('<Number new contact>')
    bot.send_message("<Text>")

    for name in names:
        bot.new_chat(name)
        bot.send_message(f'Hello *{name}*,¨<Text>')

        