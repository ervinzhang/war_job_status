# -*- coding:UTF-8 -*- 

from selenium import webdriver
from __builtin__ import classmethod
import unittest
import os,time,sys,datetime
from war_redmine_login import AllLogin

#if your sys default encoding is not utf8 ,you need the 2 lines below
#reload(sys)  
#sys.setdefaultencoding('utf8') 
class GetDeveloperData():
    @classmethod   
    def setUp(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        AllLogin.setUp(driver)

        #deal with status,in this part,choose the status not equal to has solved
        try:
            driver.find_element_by_css_selector("#tr_status_id > td.field > label")
            a = True
        except:
            a = False
        if a == True:
            try:
                driver.find_element_by_css_selector("#operators_status_id")
                b = True
            except:
                b = False
            if b == True:
                driver.find_element_by_css_selector("#operators_status_id > option:nth-child(3)").click()
                driver.find_element_by_css_selector("#values_status_id_1 > option:nth-child(4)").click()
            elif b == False:
                driver.find_element_by_css_selector("#cb_status_id").click()
                driver.find_element_by_css_selector("#operators_status_id > option:nth-child(3)").click()
                driver.find_element_by_css_selector("#values_status_id_1 > option:nth-child(4)").click()
        elif a == False:
            driver.find_element_by_css_selector("#add_filter_select > option:nth-child(2)").click()
            driver.find_element_by_css_selector("#operators_status_id > option:nth-child(3)").click()
            driver.find_element_by_css_selector("#values_status_id_1 > option:nth-child(4)").click()


        #add assgin to
        driver.find_element_by_css_selector("#add_filter_select > option:nth-child(6)").click()
        driver.find_element_by_css_selector("#operators_assigned_to_id > option:nth-child(1)").click()


        element_huachangmiao = "#values_assigned_to_id_1 > option:nth-child(8)"
        element_liushuai     = "#values_assigned_to_id_1 > option:nth-child(4)"
        element_weiwei       = "#values_assigned_to_id_1 > option:nth-child(48)"
        element_qiaohuan     = "#values_assigned_to_id_1 > option:nth-child(2)"
        element_wangguojun   = "#values_assigned_to_id_1 > option:nth-child(26)"
        element_huangguofang = "#values_assigned_to_id_1 > option:nth-child(51)"
        element_wangyan      = "#values_assigned_to_id_1 > option:nth-child(29)"
        element_zhaoyang     = "#values_assigned_to_id_1 > option:nth-child(44)"


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
                bug_num_developer = driver.find_element_by_css_selector("#content > span > span > span").text
                total_num_developer = bug_num_developer.split('/')[1].split(')')[0]
            elif a==False:
                total_num_developer = 0

            return total_num_developer


        #huachangmiao
        total_num_HCM = getTextData(element_huachangmiao)

        #liushuai
        total_num_LS = getTextData(element_liushuai)

        #WEIWEI
        total_num_WW = getTextData(element_weiwei)

        #QIAOHUAN
        total_num_QH = getTextData(element_qiaohuan)

        #WANGGUOJUN
        total_num_WGJ = getTextData(element_wangguojun)

        #HUANGGUOFANG
        total_num_HGF = getTextData(element_huangguofang)

        #wangyan
        total_num_WY = getTextData(element_wangyan)

        #zhaoyang
        total_num_ZY = getTextData(element_zhaoyang)
        
        driver.quit()

        return  total_num_HCM,total_num_LS,total_num_WW,total_num_QH,total_num_WGJ,total_num_HGF,total_num_WY,total_num_ZY
  
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
