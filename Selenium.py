# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:58:37 2020

@author: abisht
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
 

USERNAME=""
PASS=""


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
driver=webdriver.Chrome(executable_path=r"C:\Users\abisht\Documents\Deloitte Docs\SOFTWARES INSTALLED\python libraries\selenium\chromedriver.exe",options=chrome_options) #Path to Chrome Driver

#login
driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(USERNAME)

driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(60)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(PASS)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)
driver.get('https://analytics.google.com/analytics/web/')
sleep(40)
driver.find_element_by_xpath('//*[@id="suite-top-nav"]/suite-header/div/md-toolbar/div/suite-universal-picker/button').click()
sleep(5)
driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/suite-entity-panel/div/md-content[3]/suite-entity-list/md-virtual-repeat-container/div/div[2]/li[1]/a/suite-entity-item').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div/a/div').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[4]/div/a/div').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[3]/div[2]/div/div/ga-nav-link[4]/div[2]/div/div/ga-nav-link[4]/div/report-link/a/div').click()


sleep(120)


iframe = driver.find_element_by_id("galaxyIframe")    
driver.switch_to.frame(iframe)
driver.find_element_by_xpath('//*[@id="ID-explorer-table-tableControl"]/div/div[1]/ul/li[3]/div').click()
driver.find_element_by_xpath('//*[@id="ID-explorer-table-tableControl"]/div/div[4]/div/div[1]/div[5]/div[1]').click()
driver.find_element_by_xpath('//*[@id="ID-explorer-table-tableControl"]/div/div[4]/div/div[1]/div[5]/div[2]/div[1]/div[1]').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="ID-reportHeader-reportToolbar"]/div[1]/div[2]/span[2]').click()
sleep(5)
driver.find_element_by_xpath('//*[@id="ID-reportHeader-reportToolbar-exportControl"]/div/ul/li[5]/span[2]').click()

sleep(30)
#driver.switch_to.default_content()
#driver.find_element_by_xpath("/html/body/div[97]/div[2]/div/form/div[3]/input").click()
driver.find_element_by_xpath('//*[text()="Request Unsampled"]').click()


print('passed')
#//*[@id="ID-reportHeader-reportToolbar"]/div[1]/div[2]/span[2]/span
sleep(5)



time.sleep(5) # Wait for 5 seconds, so that you can see something.
#driver.quit()





