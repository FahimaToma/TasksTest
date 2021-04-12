from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from random import choice
from random import randint

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome\
    (r"D:\Study\python Softwares\pythonPractise\seleniumBasics\chromedriver.exe")

class Box():
    def test(self):
        url = "https://www.paysera.lt/v2/en-LT/fees/currency-conversion-calculator#/"
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(50)


        flag = driver.find_element_by_xpath\
            ('/html/body/footer/div[2]/div/div/div[2]/div/span/span[1]')
        time.sleep(2)
        SCROLL_PAUSE_TIME = 5
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        flag.click()

        country = driver.find_element_by_id('countries-dropdown')
        country.click()
        time.sleep(10)
        try:

            c = driver.find_elements_by_class_name('dropdown-menu')


          # l = c[randint(0, len(c) - 1)]  # looking for random elements.
            k = choice(c)
            time.sleep(2)
            print(k)
            print(k.get_attribute("href"))
            k.click()
            print("Clicked")
            t= k.text
            print(t)

            currency = driver.find_element_by_xpath\
                  ('//*[@id="currency-exchange-app"]/div/div/div[2]/div[1]/form/div[1]/div/div[1]/span/span[2]/span')
            cr = currency.text

            if (t == "Lithuana" and cr == "EUR"):
                print("Actual Result matches with expected Result")
            elif (t == "Latvia" and cr == "EUR"):
                print("Actual Result matches with expected Result")
            elif (t == "Estonia" and cr == "EUR"):
                print("Actual Result matches with expected Result")
            elif (t == "Bulgaria" and cr == "BGN"):
                print("Actual Result matches with expected Result")
            elif (t == "Romania" and cr == "RON"):
                print("Actual Result matches with expected Result")
            elif (t == "Poland" and cr == "PLN"):
                print("Actual Result matches with expected Result")
            elif (t == "United Kingdom" and cr == "GBP"):
                print("Actual Result matches with expected Result")
            elif (t == "Russia" and cr == "RUB"):
                print("Actual Result matches with expected Result")
            elif (t == "Algeria" and cr == "DZD"):
                print("Actual Result matches with expected Result")
            elif (t == "Albania" and cr == "ALL"):
                print("Actual Result matches with expected Result")
            elif (t == "Kosovo" and cr == "EUR"):
                print("Actual Result matches with expected Result")
            elif (t == "Ukraine" and cr == "UAH"):
                print("Actual Result matches with expected Result")
            elif (t == "Another Country" and cr == "UAH"):
                print("Actual Result matches with expected Result")
            else:
                print("Actual Result does not match with expected Result")

            time.sleep(5)
        except:
            print("Element is not clickable")

        time.sleep(5)
        driver.quit()
b = Box()
b.test()