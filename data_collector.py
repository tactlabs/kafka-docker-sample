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

PATH = "/Users/suresh/tact/libs/chromedriver"
driver = webdriver.Chrome(PATH)

# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# chrome_driver_binary = PATH
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

def startpy():

    # driver.get("https://spaceishare.com/Listings")
    # element = driver.find_elements_by_class_name("search-box-bg")
    # for ele in element:
    #     link = ele.get_attribute('style')
    #     print(link)


    driver.get("https://en.wikipedia.org/wiki/Canadian_Tire")

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

                info_dict[_th.text] = _td.text

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

    print(info_dict)
        
if __name__ == '__main__':
    startpy()