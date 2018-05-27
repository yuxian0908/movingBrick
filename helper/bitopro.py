import time
import pyotp
import requests
import urllib
import json
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

class bitoproHelper:
    def __init__(self):
        return

    def totp(self):
        totp = pyotp.TOTP("SMWULMNPRNJOQEWW") 
        print(totp.now())
        return totp.now()

    def login(self):
        LOGIN_URL = "https://www.bitopro.com/"
        USEREMAIL = 'yuxian12070908@gmail.com'
        PASSWORD = 'Andy551209'

        open('helper/bitoproCookies.txt', 'w').close()

        indexes = ["1","2","3"]
        count = 0
        
        while count<len(indexes):
            try:
                index = indexes[count]
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                browser = webdriver.Chrome(chrome_options=option)
                # browser = webdriver.Chrome()

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
                browser.find_element_by_xpath(".//*[@id='login-btn']").click()

                # get opt
                time.sleep(1)  
                browser.find_element_by_xpath(".//*[@id='otp']").send_keys(self.totp())
                time.sleep(1)  
                browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/a").click()
                time.sleep(0.5)
                browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/ul[contains(@role,'menu')]/*["+index+"]/a").click()
                time.sleep(1)

                # get browser cookie
                cookies_list = browser.get_cookies()
                cookies_dict = {}
                for cookie in cookies_list:
                    cookies_dict[cookie['name']] = cookie['value']

                print(cookies_dict)
                cookies_dict = json.dumps(cookies_dict)
                cookiefile = open('helper/bitoproCookies.txt', "a+")
                cookiefile.write('{"'+index+'":')
                cookiefile.writelines(cookies_dict)
                cookiefile.write('}')
                cookiefile.write("\n")
                cookiefile.close()
                browser.close()
            except:
                print("=================something wrong===================")
                count = count-1
                
            count = count+1
        

        
    def getTick(self,lookingCoinType):
        browser = self.browser
        index = ''
        if lookingCoinType=="btc":
            index = '2'
        elif lookingCoinType=="ltc":
            index = '3'
        elif lookingCoinType=="eth":
            index = '4'
        data = browser.find_element_by_xpath(".//*[@id='quote']/div[contains(@class, 'ibox-content')]/table/tbody/*["+index+"]/*[2]").text
        return data

    def getBid(self,lookingCoinType):
        browser = self.browser
        browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/a").click()
        time.sleep(0.5)
        index = ''
        if lookingCoinType=="btc":
            index = '1'
        elif lookingCoinType=="ltc":
            index = '2'
        elif lookingCoinType=="eth":
            index = '3'
        browser.find_element_by_xpath(".//*[@id='navbar']/ul/li[contains(@class, 'currency')]/ul[contains(@role,'menu')]/*["+index+"]/a").click()
        time.sleep(1)

        # get browser cookie
        cookies_list = browser.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']

        # use request to get data
        currentTime = int(time.time())
        beginTime = str(currentTime-48000)
        currentTime = str(currentTime)
        apiData = requests.get("https://www.bitopro.com/trading_datas/history?resolution=180&from="+beginTime+"&to="+currentTime, cookies=cookies_dict)
        apiData = json.loads(apiData.text)
        
        results = list()
        
        for data in apiData:
            result = {
                'bid': data[1],
                'ask': data[2],
                'deal': data[4],
                'volumns': data[5]
            }
            results.append(result)
        
        return results