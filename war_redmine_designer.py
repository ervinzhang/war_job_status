# -*- coding:UTF-8 -*- 

from selenium import webdriver
from __builtin__ import classmethod
import unittest
import os,time,sys,datetime
from war_redmine_login import AllLogin

#if your sys default encoding is not utf8 ,you need the 2 lines below
#reload(sys)  
#sys.setdefaultencoding('utf8') 
class GetDesignerData():
    @classmethod   
    def setUp(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        AllLogin.setUp(driver)

        #close the status 
        try:
            driver.find_element_by_css_selector("#operators_status_id")
            a=True
        except:
            a=False
        if a==True:
            driver.find_element_by_css_selector("#cb_status_id").click()

        driver.find_element_by_css_selector("#add_filter_select > option:nth-child(5)").click()
        time.sleep(1)


        element_xuezhisheng = "#values_author_id_1 > option:nth-child(39)"
        element_yangming    = "#values_author_id_1 > option:nth-child(23)"
        element_niexinyu    = "#values_author_id_1 > option:nth-child(34)"
        element_yinxu       = "#values_author_id_1 > option:nth-child(11)"
        element_xuebowei    = "#values_author_id_1 > option:nth-child(38)"
        element_lizhiyuan   = "#values_author_id_1 > option:nth-child(19)"
        element_yuchenghui  = "#values_author_id_1 > option:nth-child(3)"
        element_liuhongrui  = "#values_author_id_1 > option:nth-child(5)"
        element_qiuhan      = "#values_author_id_1 > option:nth-child(45)"
        element_dihaoran    = "#values_author_id_1 > option:nth-child(25)"
        element_duyuye      = "#values_author_id_1 > option:nth-child(22)"


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
                bug_or_tested_num_designer = driver.find_element_by_css_selector("#content > span > span > span").text
                total_or_tested_num_designer = bug_or_tested_num_designer.split('/')[1].split(')')[0]
            elif a==False:
                total_or_tested_num_designer = 0

            return total_or_tested_num_designer


        #Xuezhisheng
        total_num_XZSH = getTextData(element_xuezhisheng)

        #yangming
        total_num_YM = getTextData(element_yangming)

        #niexinyu
        total_num_NXY = getTextData(element_niexinyu)

        #yinxu
        total_num_YX = getTextData(element_yinxu)

        #xuebowei
        total_num_XBW = getTextData(element_xuebowei)

        #lizhiyuan
        total_num_LZY = getTextData(element_lizhiyuan)

        #yuchenghui
        total_num_YCH = getTextData(element_yuchenghui)

        #liuhongrui
        total_num_LHR = getTextData(element_liuhongrui)

        #qiuhan
        total_num_QiuH = getTextData(element_qiuhan)

        #dihaoran
        total_num_DHR = getTextData(element_dihaoran)

        #dUYUYE
        total_num_DYY = getTextData(element_duyuye)


        #add status,make sure open
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

        #xuezhisheng
        total_tested_num_XZSH = getTextData(element_xuezhisheng)
    
        #yangming
        total_tested_num_YM = getTextData(element_yangming)

        #niexinyu
        total_tested_num_NXY = getTextData(element_niexinyu)
        
        #yinxu
        total_tested_num_YX = getTextData(element_yinxu)

        #xuebowei
        total_tested_num_XBW = getTextData(element_xuebowei)

        #lizhiyuan
        total_tested_num_LZY = getTextData(element_lizhiyuan)

        #yuchenghui
        total_tested_num_YCH = getTextData(element_yuchenghui)

        #LIUHONGRUI
        total_tested_num_LHR = getTextData(element_liuhongrui)

        #QIUHAN
        total_tested_num_QiuH = getTextData(element_qiuhan)

        #DIHAORAN
        total_tested_num_DHR = getTextData(element_dihaoran)

        #DIYUYE
        total_tested_num_DYY = getTextData(element_duyuye)


        driver.quit()
        return  yesterday,total_num_XZSH,total_num_YM,total_num_NXY,total_num_YX,total_num_XBW,total_num_LZY,total_num_YCH,total_num_LHR,total_num_QiuH,\
        total_tested_num_XZSH,total_tested_num_YM,total_tested_num_NXY,total_tested_num_YX,total_tested_num_XBW,total_tested_num_LZY,\
        total_tested_num_YCH,total_tested_num_LHR,total_tested_num_QiuH,total_num_DHR,total_tested_num_DHR,total_num_DYY,total_tested_num_DYY
  
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
