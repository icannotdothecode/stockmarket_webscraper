# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 17:49:23 2020

@author: javax
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/javax/Documents/Python Scripts/Basic python projects/webscraper_lucky/drivers/chromedriver.exe')
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Edge()

def isTitle(self, givenTitle):
    if self.givenTitle == driver.title:
        print("\ngiven title does not equal true title")
        print("\ntrue title = ", driver.title)
    main()

def returnSearch(self, search):
    pass

def returnSite(self, site):
    pass

def returnTitle():
    print(driver.title)
    main()
    
def end():
    driver.quit()
    
def randSearch():
    pass

def exampleCode():
    driver.find_element_by_name("q").send_keys("asdf")
    time.sleep(2)
    driver.find_element_by_name("btnK").click()
    print(driver.title)
    time.sleep(2)
    driver.find_link_by_tag_name("a").click()
    time.sleep(10000)
    main()
    #not functional atm
    #idea is that first result is clicked
    
def main():
    driver.set_page_load_timeout(10)
    driver.get("https://google.com")
    
    action = input("\nenter action, isTitle, returnSearch, returnSite, exampleCode, or End")
    if action == "isTitle":
        title = input("\ngive title:")
        isTitle(title)
    elif action == "returnSearch":
        pass
    elif action == "returnSite":
        pass
    elif action == "returnTitle":
        returnTitle()
    elif action == "End":
        end()
    elif action == "exampleCode":
        exampleCode()
    
    else:
        print("error reading input, re-enter")
        main()

main()

time.sleep(5)
driver.quit()