# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:49:23 2020

@author: javax
"""

import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Edge()

def isTitle(self, givenTitle):
    if self.givenTitle == driver.title:
        print("\ngiven title does not equal true title")
        print("\ntrue title = ", driver.title)

def returnSearch(self, search):
    pass

def returnSite(self, site):
    pass

def returnTitle(self):
    print(driver.title)

def main():
    # driver.set_page_load_timeout(10)
    # driver.get("https://google.com")
    # driver.find_element_by_name("q").send_keys("Automation Step by Step")
    # driver.find_element_by_name("btnI").click()
    
    action = input("\nenter action, isTitle, returnSearch, returnSite, or End")
    if action == "isTitle":
        title = input("\ngive title:")
        isTitle(title)
    if action == "returnSearch":
        pass
    if action == "returnSite":
        pass
    if action == "returnTitle":
        returnTitle()
    else:
        print("error reading input, re-enter")
        main()


time.sleep(5)
driver.quit()