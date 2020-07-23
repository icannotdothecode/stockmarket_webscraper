# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:49:23 2020

@author: javax
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/javax/Documents/Python Scripts/Basic python projects/webscraper_lucky/drivers/chromedriver.exe')





def main():
    global searchURL, searchBar

    searchURL = "https://money.cnn.com/data/markets/"

    # sets a 10-second timeout for the page
    driver.set_page_load_timeout(10)
    driver.get("https://google.com")

    # goes to the given site (in this case i chose the stock market)
    searchBar = driver.find_element_by_name("q")
    searchBar.send_keys("https://money.cnn.com/data/markets/")
    
    driver.find_element_by_name("btnK").click()

main()

time.sleep(5)
driver.quit()