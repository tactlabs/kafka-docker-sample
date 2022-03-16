#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author:

Source:
    https://stackoverflow.com/questions/28022764/python-and-how-to-get-text-from-selenium-element-webelement-object
'''

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import unicodedata

# Local import
from env_reader import *

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = PATH
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

def get_info(url):

    # driver.get("https://spaceishare.com/Listings")
    # element = driver.find_elements_by_class_name("search-box-bg")
    # for ele in element:
    #     link = ele.get_attribute('style')
    #     print(link)


    driver.get(url)

    info_dict =  {}

    try:

        tr_list = driver.find_elements(by=By.CSS_SELECTOR, value="table.infobox tr")

        # print(tr_list)

        for tr in tr_list:
            # print(tr)

            try:
                _th = tr.find_element(
                    by = By.CSS_SELECTOR, 
                    value = "th"
                )

                # print(_th)
                # element = _th

                # print(_th.text)

                _td = tr.find_element(
                    by = By.CSS_SELECTOR, 
                    value = "td"
                )

                # print(_th)
                # element = _td

                # print(_td.text)

                _key = _th.text
                _value = _td.text

                # _key = _key.encode('ascii', 'ignore')
                # _value = _value.encode('ascii', 'ignore')

                _key = unicodedata.normalize('NFKD', _key).encode('ascii', 'ignore')
                _value = unicodedata.normalize('NFKD', _value).encode('ascii', 'ignore')

                _key = _key.decode('utf-8')
                _value = _value.decode('utf-8')

                info_dict[_key] = _value

            except Exception as err:
                # print('Error : ')
                # print(err)
                continue

            # print('-' * 80)
    except Exception as err:
        print('Error : ')
        print(err)
    finally:
        driver.quit()

    # print(info_dict)

    return info_dict

def startpy():

    url = "https://wiki2.org/en/Canadian_Tire"
    content = get_info(url)

    print(content)
        
if __name__ == '__main__':
    startpy()