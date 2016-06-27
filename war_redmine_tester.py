# -*- coding:UTF-8 -*- 

from selenium import webdriver
from __builtin__ import classmethod
import unittest
import os,time,sys,datetime
from war_redmine_login import AllLogin


#if your sys default encoding is not utf8 ,you need the 2 lines below
#reload(sys)  
#sys.setdefaultencoding('utf8') 
class GetData():
    @classmethod  
    def setUp(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        AllLogin.setUp(driver)

        #status,make sure it closed
        try:
            driver.find_element_by_css_selector("#operators_status_id")
            a=True
        except:
            a=False
        if a==True:
            driver.find_element_by_css_selector("#cb_status_id").click()

        driver.find_element_by_css_selector("#add_filter_select > option:nth-child(5)").click()
        time.sleep(1)


        element_liuxuefeng  = "#values_author_id_1 > option:nth-child(7)"
        element_yuantianshi = "#values_author_id_1 > option:nth-child(40)"
        element_songliyuan  = "#values_author_id_1 > option:nth-child(10)"
        element_wangyang    = "#values_author_id_1 > option:nth-child(28)"
        element_wangyanrong = "#values_author_id_1 > option:nth-child(30)"


        def getTextData(element_person):
            driver.find_element_by_css_selector(element_person).click()
            #click use button
            driver.find_element_by_css_selector("#query_form_with_buttons > p > a.icon.icon-checked").click()
            try:
                driver.find_element_by_css_selector("#content > span > span > span")
                a=True
            except:
                a=False


            if a==True:
                bug_or_tested_num_person = driver.find_element_by_css_selector("#content > span > span > span").text
                total_or_tested_num_person = bug_or_tested_num_person.split('/')[1].split(')')[0]
            elif a==False:
                total_or_tested_num_person = 0

            return total_or_tested_num_person

        #liuxuefeng
        total_num_LXF = getTextData(element_liuxuefeng)

        #yuantianshi
        total_num_YTS = getTextData(element_yuantianshi)

        #songliyuan
        total_num_SLY = getTextData(element_songliyuan)

        #wangyang
        total_num_wangyang = getTextData(element_wangyang)

        #wangyanrong
        total_num_wangyanrong = getTextData(element_wangyanrong)


        #deal with status,make sure it open
        try:
            driver.find_element_by_css_selector("#operators_status_id")
            b=True
        except:
            b=False

        if b==True:
            driver.find_element_by_css_selector("#operators_status_id > option:nth-child(2)").click()
            driver.find_element_by_css_selector("#values_status_id_1 > option:nth-child(6)").click()
        else:
            driver.find_element_by_css_selector("#add_filter_select > option:nth-child(2)").click()
            driver.find_element_by_css_selector("#operators_status_id > option:nth-child(2)").click()
            driver.find_element_by_css_selector("#values_status_id_1 > option:nth-child(6)").click()
        
        #liuxuefeng
        total_tested_num_LXF = getTextData(element_liuxuefeng)
        
        #yuantianshi
        total_tested_num_YTS = getTextData(element_yuantianshi)

        #songliyuan          
        total_tested_num_SLY = getTextData(element_songliyuan)

        #wangyang          
        total_tested_num_wangyang = getTextData(element_wangyang)

        #wangyanrong          
        total_tested_num_wangyanrong = getTextData(element_wangyanrong)
  
        driver.quit()
        return  yesterday,total_num_LXF,total_num_YTS,total_num_SLY,total_num_wangyang,total_tested_num_LXF,total_tested_num_YTS,\
                total_tested_num_SLY,total_tested_num_wangyang,total_num_wangyanrong,total_tested_num_wangyanrong

    
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
