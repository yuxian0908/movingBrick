import time
import pyotp
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

import pytesseract
from PIL import Image

class bitoproHelper:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Chrome()
        self.browser = browser
        return

    def totp(self):
        totp = pyotp.TOTP("SMWULMNPRNJOQEWW") 
        print(totp.now())
        return totp.now()

    def login(self):
        LOGIN_URL = "https://www.bitopro.com/"
        USEREMAIL = 'yuxian12070908@gmail.com'
        PASSWORD = 'Andy551209'

        
        browser = self.browser

        # enter loginin div
        browser.get(LOGIN_URL)
        browser.find_element_by_xpath(".//*[@id='navbar']/ul/*[3]/a").click()

        # find verify code img url and open it in another browser
        time.sleep(1)  
        imgURL = browser.find_element_by_xpath(".//*[@id='captcha_key']/../*[1]").get_attribute("src")
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        browser2 = webdriver.Chrome(chrome_options=option)
        # browser2 = webdriver.Chrome()    
        browser2.get(imgURL)
        browser2.save_screenshot('vericode.jpg')
        time.sleep(1) 
        img = Image.open('vericode.jpg')
        img.show()
        
        # type in the code
        print('type in the code you see')
        vericode = input("code:")
        browser2.close()

        # auto enter input
        browser.find_element_by_xpath(".//*[@id='loginForm']/div/input[@name='email']").send_keys(USEREMAIL)
        browser.find_element_by_xpath(".//*[@id='loginForm']/div/input[@name='password']").send_keys(PASSWORD)
        browser.find_element_by_xpath(".//*[@id='captcha']").send_keys(vericode)

        # submit form
        try:
            browser.find_element_by_xpath(".//*[@id='login-btn']").click()
        except:
            print('you need to rerun again')
            return

        # get opt
        time.sleep(1)  
        try:
            browser.find_element_by_xpath(".//*[@id='otp']").send_keys(self.totp())
        except:
            print('you need to rerun again')
            return
        time.sleep(1)  
        
        

    def getTick(self,lookingCoinType):
        if lookingCoinType=="btc":
            browser = self.browser
            test = browser.find_element_by_xpath(".//*[@id='quote']").get_attribute("class")
            print(test)
            return "aaa"