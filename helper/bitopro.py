import time
import pyotp
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

import pytesseract
from PIL import Image


def totp():
    totp = pyotp.TOTP("SMWULMNPRNJOQEWW") 
    print(totp.now())
    return totp.now()

    # im = Image.open('test.jpg').convert('RGBA')
    # im.show()

def login():

    LOGIN_URL = "https://www.bitopro.com/"
    USEREMAIL = 'yuxian12070908@gmail.com'
    PASSWORD = 'Andy551209'
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    # browser = webdriver.Chrome(chrome_options=option)

    browser = webdriver.Chrome()

    # enter loginin div
    browser.get(LOGIN_URL)
    browser.find_element_by_xpath(".//*[@id='navbar']/ul/*[3]/a").click()

    # find verify code img url and open it in another browser
    time.sleep(0.1)  
    imgURL = browser.find_element_by_xpath(".//*[@id='captcha_key']/../*[1]").get_attribute("src")
    browser2 = webdriver.Chrome()    
    browser2.get(imgURL)
    browser2.save_screenshot('vericode.jpg')
    
    # type in the code
    print('type in the code you see')
    vericode = input("code:")
    browser2.close()

    # auto enter input
    browser.find_element_by_xpath(".//*[@id='loginForm']/div/input[@name='email']").send_keys(USEREMAIL)
    browser.find_element_by_xpath(".//*[@id='loginForm']/div/input[@name='password']").send_keys(PASSWORD)
    browser.find_element_by_xpath(".//*[@id='captcha']").send_keys(vericode)

    # submit form
    browser.find_element_by_xpath(".//*[@id='login-btn']").click()

    # get opt
    time.sleep(1)  
    browser.find_element_by_xpath(".//*[@id='otp']").send_keys(totp())
    