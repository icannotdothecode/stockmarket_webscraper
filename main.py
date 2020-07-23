# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:49:23 2020

@author: javax
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/javax/Documents/Python Scripts/Basic python projects/webscraper_lucky/drivers/chromedriver.exe')

def main():
    driver.set_page_load_timeout(10)
    driver.get("https://google.com")
    



main()

time.sleep(5)
driver.quit()