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


def crap():
    USEREMAIL = 'yuxian12070908@gmail.com'
    PASSWORD = 'Andy551209'
    LOGIN_URL = "https://www.bitopro.com/"

    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath('//input[@name="authenticity_token"]/@value')))[0]

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '249',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.2.2079334811.1526893889; _gid=GA1.2.1931645170.1527002809; lang=0; s9ecf44a227006834=bcfc042a2e057f282073f72e2e553af6bcabc37fb9e7382a2f82191b8b04db7d; session=6a918c1740814ff5dced4d3c8e506b20',
        'origin': 'https://www.bitopro.com',
        'referer': 'https://www.bitopro.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'x-csrf-token': authenticity_token,
        'x-requested-with': 'XMLHttpRequest',
    }

    payload = {
        'email': USEREMAIL,
        'password': PASSWORD,
        'csrfmiddlewaretoken': authenticity_token
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = headers)

    print(result)


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
    