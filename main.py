# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:49:23 2020

@author: javax
"""

import time
from selenium import webdriver

driver = webdriver.Chrome(
    'C:/Users/javax/Documents/Python Scripts/Basic python projects/webscraper_lucky/drivers/chromedriver.exe')


# returns today's increase/decrease in market value as well as current value

class ReturnSP:
    def return_sp_current(self):
        element = driver.find_element_by_class_name("wsod_last")
        return element.text

    def return_sp_change(self):
        element = driver.find_element_by_class_name("wsod_change")
        return element.text


class ReturnNas:
    def return_nas_current(self):
        element = driver.find_element_by_class_name("wsod_last")
        return element.text

    def return_nas_change(self):
        element = driver.find_element_by_class_name("wsod_change")
        return element.text


class ReturnDow:
    def return_dow_current(self):
        element = driver.find_element_by_class_name("wsod_last")
        return element.text

    def return_dow_change(self):
        element = driver.find_element_by_class_name("wsod_change")
        return element.text


def return_all():
    # dow
    print("-------------------------------------------------------------------------")

    driver.get("https://money.cnn.com/data/markets/dow")
    print("\nDow Jones current value:\n", ReturnDow().return_dow_current())
    print("\nDow Jones change:\n", ReturnDow().return_dow_change(), "\n")
    print("-------------------------------------------------------------------------")

    # nasdaq
    driver.get("https://money.cnn.com/data/markets/nasdaq/")
    print("\nNASDAQ current value:\n", ReturnNas().return_nas_current())
    print("\nNASDAQ change:\n", ReturnNas().return_nas_change(), "\n")
    print("-------------------------------------------------------------------------")

    # s&p
    driver.get("https://money.cnn.com/data/markets/sandp/")
    print("\nS&P current value:\n", ReturnSP().return_sp_current())
    print("\nS&P change:\n", ReturnSP().return_sp_change(), "\n")
    print("-------------------------------------------------------------------------")


def main():
    global mainURL, searchBar

    mainURL = "https://money.cnn.com/data/markets/"

    # sets a 10-second timeout for the page
    driver.set_page_load_timeout(10)
    driver.get("https://google.com")
    # goes to the given site (in this case i chose the stock market)
    searchBar = driver.find_element_by_name("q")
    driver.get(mainURL)
    # prints all results
    return_all()


main()
time.sleep(5)
driver.quit()
