# -*- coding:UTF-8 -*- 

from selenium import webdriver
from __builtin__ import classmethod
import unittest
import os,time,sys,datetime

#if your sys default encoding is not utf8 ,you need the 2 lines below
#reload(sys)  
#sys.setdefaultencoding('utf8') 
class AllLogin():
    @classmethod  

    def setUp(self,driver):

        # navigate to the application main page
        driver.get("http://120.26.4.254/")
        time.sleep(1)

        driver.find_element_by_css_selector("#account > ul > li:nth-child(1) > a").click()
        time.sleep(1)

        name = driver.find_element_by_name("username")
        name.clear()
        name.send_keys("zhangjingfeng")
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("314159zjf")

        driver.find_element_by_xpath("//*[@id=\"login-form\"]/form/table/tbody/tr[4]/td[2]/input").click()
        time.sleep(1)

        driver.find_element_by_css_selector("#top-menu > ul > li:nth-child(3) > a").click()
        time.sleep(1)

        driver.find_element_by_css_selector("#projects-index > ul > li > div > a").click()
        time.sleep(1)

        driver.find_element_by_css_selector("#main-menu > ul > li:nth-child(4) > a").click()
        time.sleep(1)

        #driver.find_element_by_css_selector("#add_filter_select").click()
        driver.find_element_by_css_selector("#add_filter_select > optgroup:nth-child(17) > option:nth-child(1)").click()

        date_text = driver.find_element_by_css_selector("#values_created_on_1")
        
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        #yesterday = today
        #systime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
        date_text.clear()
        date_text.send_keys(yesterday)
    
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
