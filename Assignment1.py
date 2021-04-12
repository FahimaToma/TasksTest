from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time
from random import choice


driver = webdriver.Chrome\
    (r"D:\Study\python Softwares\pythonPractise\seleniumBasics\chromedriver.exe")


class Box():
    def test(self):
        url = "https://www.paysera.lt/v2/en-LT/fees/currency-conversion-calculator#/"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(50)

        SCROLL_PAUSE_TIME = 0.5
        time.sleep(SCROLL_PAUSE_TIME)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sell = driver.find_element_by_xpath \
            ('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[1]/input')

        buy = driver.find_element_by_xpath \
            ('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[3]/input')

        filter = driver.find_element_by_xpath\
            ('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[4]/button')

        #Taking Alpha numeric value, numeric value as random input
        randomValue = ['100', '200', '300', '400', '500', '600', '700',
                       '800', '900', '1000', 'EUR', 'USD', '@Ran']
        key = choice(randomValue)

        #Assignment 1- Test Case 1: Put Value in Buy Field check Sell field Value

        try:
            filter.click()
            time.sleep(2)
            b= buy.send_keys(key)
            s = buy.send_keys()
            time.sleep(2)

            if buy is not None and s is None:
                    print("Expected Result is matched with Actual result: Sell field is empty because Buy field has value.")

            else:
                print("Test Case 1: Actual Result does not match with Expected Result")


        except:
            print("Field not found")

        time.sleep(5)
       # Assignment 1- Test Case 2: Put Value in Sell Field check Buy field value
        try:
            s = sell.send_keys(key)
            b = buy.send_keys()
            time.sleep(2)

            if sell is not None and b is None:
                    print("Expected Result is matched with Actual result: Buy field is empty because Sell field has value.")

            else:
                print("Test Case 2: Actual Result does not match with Expected Result")


        except:
            print("Field not found")

        # Assignment 1- Test Case 3: Keep both field empty

        try:
            time.sleep(5)
            s = sell.clear()
            b = buy.clear()
            time.sleep(2)

            if sell is not None and buy is not None:
                    print("Expected Result is matched with Actual result: Both fields are empty.")

            else:
                print("Test Case 3: Actual Result does not match with Expected Result")


        except:
            print("Field not found")

        # Assignment 1- Test Case 4: Try to put value in both field at the same time

        try:
            time.sleep(5)
            s = sell.send_keys(key)
            time.sleep(1)
            b = buy.send_keys(key)
            time.sleep(1)

            if s is None or b is None:
                    print("Expected Result is matched with Actual result: Both fields can't have value at the same time")

            else:
                    print("Test Case 4: Actual Result does not match with Expected Result")


        except:
                print("Field not found")

        time.sleep(5)
        driver.quit()

b= Box()
b.test()
