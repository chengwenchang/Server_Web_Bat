# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions
import unittest, time, re,os,sys
import string

class Web_test(unittest.TestCase):
    
    @classmethod
    def setting(cls,IP):
        cls.IP = IP

    @classmethod
    def setUpClass(cls):
        #cwd = os.getcwd() + "/"
        #cls.driver = webdriver.Chrome(cwd + "chromedriver.exe")
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.base_url = cls.IP
        cls.verificationErrors = []
        cls.accept_next_alert = True
       
        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()   
    
      
    def test_Login_Page(self):
        #Login_Page
        
        driver = self.driver 
        base_url = "http://" +self.base_url +  "/"
        driver.get(base_url + "/")
        driver.find_element_by_name("login_btn").click()
        self.assertEqual("Please type the username.", self.close_alert_and_get_its_text())
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("login_btn").click()
        self.assertEqual("Please type the password.", self.close_alert_and_get_its_text())
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("123")
        driver.find_element_by_name("login_btn").click()
        self.assertEqual("Login failed.Please check the username and password.", self.close_alert_and_get_its_text())
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("admin")
        driver.find_element_by_name("login_btn").click()
        #self.assertEqual("Firmware Version: 3.0.0",str(driver.find_element_by_id("official_fw_ver").text).strip())

    def test_File_System(self):
        #Raid Status
        driver = self.driver     
        driver.find_element_by_xpath("//div[@id='masterdiv']/div").click()
        driver.find_element_by_xpath("//span[@id='sub3']/div").click()
        driver.switch_to_frame("mainContent")
        self.is_element_to_be_clickable_by_id(self.driver,"ygtvlabelel1")
        driver.find_element_by_id("ygtvlabelel1").click()
        driver.find_element_by_id("ygtvlabelel1").click()
        driver.find_element_by_xpath("//a[@id='ygtvlabelel2']/span").click()
        driver.find_element_by_xpath("//a[@id='ygtvlabelel3']/span").click()
        
        ##Create Raid
        #driver.find_element_by_xpath("//span[@id='tab_create_span']").click()
        #self.is_element_to_be_clickable_by_id(self.driver,"moveToRight")         
        #driver.find_element_by_id("Disk 1").click()
        #driver.find_element_by_id("moveToRight").click()
        #driver.find_element_by_id("Disk 1").click()
        #driver.find_element_by_id("moveToLeft").click()
        #driver.find_element_by_xpath("//div[@id='resetBTN']").click()
        #driver.find_element_by_id("Disk 1").click()
        #driver.find_element_by_id("Disk 2").click()
        #driver.find_element_by_id("moveToRight").click()
        #driver.find_element_by_xpath("//div[@id='createBTN']").click()
        #driver.find_element_by_xpath("//span[2]/span/button").click()     
        #self.is_element_to_be_clickable_by_id(self.driver,"moveToRight") 
        #driver.find_element_by_xpath("//div[@id='createBTN']").click()
        #driver.find_element_by_xpath("//div[@id='confirmCreateDlg']/div[2]/input").click()
        #driver.find_element_by_xpath("//span[1]/span/button").click()
        #self.is_alert_to_be_switch(self.driver)
        #self.assertEqual("Create volume OK.", self.close_alert_and_get_its_text())
        #self.is_element_to_be_clickable_by_id(self.driver,"ygtvlabelel1")

        ##Formate Volume
        #driver.find_element_by_xpath("//span[@id='tab_format_span']").click()
        #self.is_element_to_be_clickable_by_id(self.driver,"resetBTN")
        #driver.find_element_by_xpath("//td[@id='yui-dt0-bdrow0-cell0']/input").click()
        #driver.find_element_by_xpath("//div[@id='resetBTN']").click()
        #self.is_element_to_be_clickable_by_id(self.driver,"resetBTN")
        #driver.find_element_by_xpath("//td[@id='yui-dt0-bdrow0-cell0']/input").click()
        #driver.find_element_by_xpath("//div[@id='formatBTN']/span").click()
        #driver.find_element_by_id("confirm_chk").click()
        #driver.find_element_by_xpath("//span[2]/span/button").click()
        #driver.find_element_by_xpath("//div[@id='formatBTN']/span").click()
        #driver.find_element_by_id("confirm_chk").click()
        #driver.find_element_by_xpath("//span[1]/span/button").click()
        #self.is_alert_to_be_switch(self.driver)
        #self.assertEqual("The volume has been formatted.", self.close_alert_and_get_its_text())
        #self.is_element_to_be_clickable_by_id(self.driver,"ygtvlabelel1")

        ##Modify Volume
        #driver.find_element_by_xpath("//span[@id='tab_modify_span']").click()
        #self.is_element_to_be_clickable_by_id(self.driver,"resetBTN")
        #driver.find_element_by_xpath("//div[@id='resetBTN']").click()
        #time.sleep(5)       

        ##Delete Volume
        #self.is_element_to_be_clickable_by_xpath(self.driver,"//span[@id='tab_delete_span']")
        #driver.find_element_by_xpath("//span[@id='tab_delete_span']").click()
        #self.is_element_to_be_clickable_by_xpath(self.driver,"//td[@id='yui-dt0-bdrow0-cell0']/input")
        #driver.find_element_by_xpath("//td[@id='yui-dt0-bdrow0-cell0']/input").click()
        #driver.find_element_by_id("deleteBTN").click()
        #driver.find_element_by_id("confirm_chk").click()
        #driver.find_element_by_xpath("//span[2]/span/button").click()
        #driver.find_element_by_id("deleteBTN").click()
        #driver.find_element_by_id("confirm_chk").click()
        #driver.find_element_by_xpath("//span[1]/span/button").click()
        #self.is_alert_to_be_switch(self.driver)
        #self.assertEqual("The volume has been deleted.", self.close_alert_and_get_its_text())
        #self.is_element_to_be_clickable_by_id(self.driver,"ygtvlabelel1")

        #ISCSI Initiator
        driver._switch_to.default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div").click()
        driver.find_element_by_xpath("//span[@id='sub3']/div[2]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("dis_address").clear()
        driver.find_element_by_id("dis_address").send_keys("10.0.129.214")        
        driver.find_element_by_xpath("//div[@id='addContactorBTN']/span").click()
        driver.find_element_by_xpath("//a[contains(text(),'Log On')]").click()
        driver.find_element_by_xpath("//span[2]/span/button").click()
        driver.find_element_by_xpath("//a[contains(text(),'Log On')]").click()
        driver.find_element_by_xpath("//button").click()
        self.assertEqual("Log on successfully.", self.close_alert_and_get_its_text())
        self.is_element_to_be_clickable_by_xpath(driver,"//a[contains(text(),'Log Off')]")
        driver.find_element_by_xpath("//a[contains(text(),'Log Off')]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^If this target has been created as a RAID volume, logging it off may destroy the current recording files\. Do you want to continue[\s\S]$")
        self.assertEqual("Log off successfully.", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//a[contains(text(),'Log On')]").click()
        driver.find_element_by_xpath("//input[@id='authen_chap']").click()
        driver.find_element_by_xpath("//button").click()
        self.assertEqual("Log on successfully.", self.close_alert_and_get_its_text())
        self.is_element_to_be_clickable_by_xpath(driver,"//a[contains(text(),'Log Off')]")
        driver.find_element_by_xpath("//a[contains(text(),'Log Off')]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^If this target has been created as a RAID volume, logging it off may destroy the current recording files\. Do you want to continue[\s\S]$")
        self.assertEqual("Log off successfully.", self.close_alert_and_get_its_text())  
        delete_target =driver.find_element_by_xpath("//div[@id='target_list']")
        delete_target.find_elements_by_class_name("DeleteDevice")[0].click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to delete this target[\s\S]$")
        driver.find_element_by_xpath("//td[@class='yui-dt-col-Delete yui-dt-last']/div/div[@class='DeleteDevice']").click() 
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to delete this target portal[\s\S]$")

       
        #Network Storage
        driver._switch_to.default_content() 
        driver.find_element_by_xpath("//div[@id='masterdiv']/div").click()
        driver.find_element_by_xpath("//span[@id='sub3']/div[3]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_xpath("//input[@id='dis_address']").clear()
        #driver.find_element_by_xpath("//input[@id='dis_address']").send_keys("10.0.129.165:/nfs/V_bc0a11ff0b6d64aff2299e8d53873095")
        driver.find_element_by_xpath("//input[@id='dis_address']").send_keys("123")
        driver.find_element_by_xpath("//div[@id='addContactorBTN']").click()
        self.assertEqual("Invalid format for export path", self.close_alert_and_get_its_text())
        #driver.find_element_by_xpath("//td[@class='yui-dt-col-Delete yui-dt-last']/div/div[@class='DeleteDevice']").click()
        #self.assertEqual("This NFS Volume will be unmounted", self.close_alert_and_get_its_text())
        self.is_element_to_be_clickable_by_xpath(driver,"//div[@id='addContactorBTN']")
        driver.find_element_by_xpath("//input[@id='dis_address']").clear()
        driver.find_element_by_id("addContactorBTN").click()
        self.assertEqual("ExportPath cannot be blank.", self.close_alert_and_get_its_text())

    def test_Network_Setup(self):
        driver = self.driver 
        
        #Network Setup
        driver._switch_to.default_content() 
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[2]").click()
        driver.find_element_by_xpath("//span[@id='sub4']/div").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_xpath("//td[3]/div/span").click()
        driver.find_element_by_id("form_ComName").clear()
        driver.find_element_by_id("form_ComName").send_keys("Tim")
        Select(driver.find_element_by_id("form_WanInf")).select_by_visible_text("LAN 2")
        driver.find_element_by_xpath("//input[@id='ProtocolAuto1']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolManual1']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolAuto0']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolManual0']").click()
        driver.find_element_by_xpath("//div[@id='cancelBTN']").click()

        #DDNS Setup
        driver.find_element_by_xpath("//td[5]/div/span").click()
        time.sleep(2)
        self.is_element_to_be_clickable_by_xpath(driver,"//input[@id='enable_update_ddns']")
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        Select(driver.find_element_by_id("ddns_interface")).select_by_index(1)
        Select(driver.find_element_by_id("ddns_interface")).select_by_index(0)
        Select(driver.find_element_by_id("ddns_provider_selector")).select_by_index(1)
        Select(driver.find_element_by_id("ddns_provider_selector")).select_by_index(0)
        driver.find_element_by_id("ddns_username").send_keys("123")
        driver.find_element_by_id("ddns_password").send_keys("1234")
        driver.find_element_by_id("ddns_hostname").send_keys("1234")
        Select(driver.find_element_by_id("ddns_update_period")).select_by_visible_text("2")
        driver.find_element_by_id("modifyBTN").click()
        self.assertEqual("DDNS settings have been updated.", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_id("resetBTN").click()
        driver.find_element_by_id("ddns_username").clear()
        driver.find_element_by_id("ddns_password").clear()
        driver.find_element_by_id("ddns_hostname").clear()
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_id("modifyBTN").click()
        self.assertEqual("DDNS settings have been updated.", self.close_alert_and_get_its_text())
        
        #Network Service
        #MGS
        driver._switch_to.default_content() 
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[2]").click()
        driver.find_element_by_xpath("//span[@id='sub4']/div[2]").click()
        time.sleep(2)
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("5255")
        driver.find_element_by_id("cancelBTN").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
        

        #RS
        driver.find_element_by_xpath("//td[3]/div/span").click()
        time.sleep(2)
        driver.find_element_by_id("MS_IP").clear()
        driver.find_element_by_id("MS_IP").send_keys("192.168.0.1")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("124")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("lanport1").clear()
        driver.find_element_by_id("lanport1").send_keys("125")
        driver.find_element_by_id("wanip").clear()
        driver.find_element_by_id("wanip").send_keys("192.168.0.100")
        driver.find_element_by_id("wanport").clear()
        driver.find_element_by_id("wanport").send_keys("126")
        driver.find_element_by_xpath("//div[@id='cancelBTN']/span").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
      


        #MDS
        driver.find_element_by_xpath("//td[5]/div/span").click()
        time.sleep(2)
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("MS_IP").clear()
        driver.find_element_by_id("MS_IP").send_keys("192.168.0.10")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("lanport1").clear()
        driver.find_element_by_id("lanport1").send_keys("236")
        driver.find_element_by_id("wanip").clear()
        driver.find_element_by_id("wanip").send_keys("192.168.0.11")
        driver.find_element_by_id("wanport").clear()
        driver.find_element_by_id("wanport").send_keys("237")
        driver.find_element_by_xpath("//div[@id='cancelBTN']/span").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
        

        #web
        driver.find_element_by_xpath("//td[7]/div/span").click()
        time.sleep(1)
        driver.find_element_by_id("form_WebPort").clear()
        driver.find_element_by_id("form_WebPort").send_keys("1024")
        driver.find_element_by_xpath("//div[@id='resetBTN']/span").click()
        time.sleep(2)        
        driver.find_element_by_xpath("//div[@id='saveBTN']/span").click()
        self.assertEqual("The new port is the same as the old port", self.close_alert_and_get_its_text())
    
    def test_Management(self):  
        driver = self.driver 
        
        #Change_Password_Page
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div/div[3]").click()
        driver.find_element_by_xpath("//span[@id='sub5']/div").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("new_passwd").clear()
        driver.find_element_by_id("new_passwd").send_keys("admin")
        driver.find_element_by_id("retype_passwd").clear()
        driver.find_element_by_id("retype_passwd").send_keys("admin")
        driver.find_element_by_xpath("//div[@id='modifyBTN']/span").click()
        self.assertEqual("Success to change hardware password.", self.close_alert_and_get_its_text())
        driver.find_element_by_id("new_passwd").clear()
        driver.find_element_by_id("new_passwd").send_keys("admin")
        driver.find_element_by_id("retype_passwd").clear()
        driver.find_element_by_id("retype_passwd").send_keys("a")
        driver.find_element_by_css_selector("#modifyBTN > span.trans").click()
        self.assertEqual("The passwords do not match.", self.close_alert_and_get_its_text())
        driver.find_element_by_id("new_passwd").clear()
        driver.find_element_by_id("new_passwd").send_keys("")
        driver.find_element_by_id("retype_passwd").clear()
        driver.find_element_by_id("retype_passwd").send_keys("")
        driver.find_element_by_id("modifyBTN").click()
        self.assertEqual("Please type the password.", self.close_alert_and_get_its_text())
        driver.find_element_by_id("new_passwd").clear()
        driver.find_element_by_id("new_passwd").send_keys("admin")
        driver.find_element_by_id("retype_passwd").clear()
        driver.find_element_by_id("retype_passwd").send_keys("admin")
        driver.find_element_by_css_selector("#resetBTN > span.trans").click()

        #Log_System
        driver.switch_to_default_content()                 
        driver.find_element_by_xpath("//span[@id='sub5']/div[2]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("last100").click()
        driver.find_element_by_id("last500").click()
        driver.find_element_by_id("last1000").click()
        driver.find_element_by_id("lastall").click()
        

        #Load_Configuration
        driver.switch_to_default_content() 
        driver.find_element_by_xpath("//span[@id='sub5']/div[3]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("form_Network").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("//div[@id='loadDefBTN']/span").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to reset all configurations to factory default and restart the system[\s\S] The password will be reset to the default value:admin$")

    def test_System(self):  
        driver = self.driver 

        #System_Information
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div").click()

        #System_Setting
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[2]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("HANperiod").clear()
        driver.find_element_by_id("HANperiod").send_keys("1000")
        driver.find_element_by_id("cancelBTN").click()
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())

        #Upgrade
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[3]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_xpath("//div[@id='CancelBTN']/span").click()
        driver.find_element_by_xpath("//div[@id='OKBTN']/span").click()
        self.assertEqual("Select a file first.", self.close_alert_and_get_its_text())

        #Date_time
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[4]").click()
        driver.switch_to_frame("mainContent")
        Select(driver.find_element_by_id("form_TimeZone")).select_by_visible_text("(GMT+08:00) Beijing, Hong Kong, Kuala Lumpur, Perth, Singapore, Taipei, Urumqi")
        driver.find_element_by_name("ntp_sync_mode").click()
        Select(driver.find_element_by_id("form_Year")).select_by_visible_text("2006")
        Select(driver.find_element_by_id("form_Month")).select_by_visible_text("January")
        Select(driver.find_element_by_id("form_Day")).select_by_visible_text("8")
        Select(driver.find_element_by_id("form_Hour")).select_by_visible_text("0")
        Select(driver.find_element_by_id("form_Minute")).select_by_visible_text("23")
        Select(driver.find_element_by_id("form_Second")).select_by_visible_text("3")
        driver.find_element_by_xpath("(//input[@name='ntp_sync_mode'])[2]").click()
        Select(driver.find_element_by_id("form_NTP_Interval_Type")).select_by_visible_text("Every month")
        Select(driver.find_element_by_id("form_NTP_Interval_Day")).select_by_visible_text("2")
        Select(driver.find_element_by_id("form_NTP_Interval_Hour")).select_by_visible_text("3:00")
        driver.find_element_by_id("form_NTP_Server").clear()
        driver.find_element_by_id("form_NTP_Server").send_keys("123")
        driver.find_element_by_id("ntpBTN").click()
        self.assertEqual("Invalid IP Address.", self.close_alert_and_get_its_text())
        driver.find_element_by_id("form_DayLightSaving_check").click()
        Select(driver.find_element_by_id("form_DLSHour")).select_by_visible_text("+2")
        Select(driver.find_element_by_id("start_Month")).select_by_visible_text("February")
        Select(driver.find_element_by_id("start_Day")).select_by_visible_text("19")
        Select(driver.find_element_by_id("start_Hour_type1")).select_by_visible_text("18:00")
        driver.find_element_by_xpath("(//input[@name='ntp_sync_mode'])[2]").click()
        Select(driver.find_element_by_id("startmonth1")).select_by_visible_text("February")
        Select(driver.find_element_by_id("startweekolder")).select_by_visible_text("Second")
        Select(driver.find_element_by_id("start_Hour_type2")).select_by_visible_text("18:00")
        driver.find_element_by_name("enddatetype").click()
        Select(driver.find_element_by_id("end_Month")).select_by_visible_text("February")
        Select(driver.find_element_by_id("end_Day")).select_by_visible_text("20")
        Select(driver.find_element_by_id("end_Hour_type1")).select_by_visible_text("21:00")
        driver.find_element_by_xpath("(//input[@name='enddatetype'])[2]").click()
        Select(driver.find_element_by_id("endmonth1")).select_by_visible_text("March")
        Select(driver.find_element_by_id("endweekolder")).select_by_visible_text("Third")
        Select(driver.find_element_by_id("endday1")).select_by_visible_text("Wednesday")
        Select(driver.find_element_by_id("end_Hour_type2")).select_by_visible_text("20:00")
        driver.find_element_by_id("cancelBTN").click()
        time.sleep(2)
        driver.find_element_by_id("okBTN").click()
        self.is_alert_to_be_switch(driver)
        self.assertEqual("Time has been adjusted.", self.close_alert_and_get_its_text())
        
        


        #Reboot / Shutdown
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[5]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("radioShutdown").click()
        driver.find_element_by_id("radioReboot").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^This action stops all services, shuts down and restarts the server\. Are you sure[\s\S]$")
        driver.find_element_by_id("radioShutdown").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^This action stops all services and shuts down the server so that it can be safely turned off\. Are you sure[\s\S]$")

    def test_R1_R2_System(self):  
        driver = self.driver 

        #System_Information
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div").click()

        #System_Setting
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[2]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("radioDisable").click()
        driver.find_element_by_id("cancelBTN").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Service has started.", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//td[3]/div/span").click()


        #Upgrade
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[3]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_xpath("//div[@id='CancelBTN']/span").click()
        driver.find_element_by_xpath("//div[@id='OKBTN']/span").click()
        self.assertEqual("Select a file first.", self.close_alert_and_get_its_text())

        #Date_time
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[4]").click()
        driver.switch_to_frame("mainContent")
        Select(driver.find_element_by_id("form_TimeZone")).select_by_visible_text("(GMT+08:00) Beijing, Hong Kong, Kuala Lumpur, Perth, Singapore, Taipei, Urumqi")
        driver.find_element_by_name("ntp_sync_mode").click()
        Select(driver.find_element_by_id("form_Year")).select_by_visible_text("2006")
        Select(driver.find_element_by_id("form_Month")).select_by_visible_text("January")
        Select(driver.find_element_by_id("form_Day")).select_by_visible_text("8")
        Select(driver.find_element_by_id("form_Hour")).select_by_visible_text("0")
        Select(driver.find_element_by_id("form_Minute")).select_by_visible_text("23")
        Select(driver.find_element_by_id("form_Second")).select_by_visible_text("3")
        driver.find_element_by_xpath("(//input[@name='ntp_sync_mode'])[2]").click()
        Select(driver.find_element_by_id("form_NTP_Interval_Type")).select_by_visible_text("Every month")
        Select(driver.find_element_by_id("form_NTP_Interval_Day")).select_by_visible_text("2")
        Select(driver.find_element_by_id("form_NTP_Interval_Hour")).select_by_visible_text("3:00")
        driver.find_element_by_id("form_NTP_Server").clear()
        driver.find_element_by_id("form_NTP_Server").send_keys("123")
        driver.find_element_by_id("ntpBTN").click()
        self.assertEqual("Invalid IP Address.", self.close_alert_and_get_its_text())
        driver.find_element_by_id("form_DayLightSaving_check").click()
        Select(driver.find_element_by_id("form_DLSHour")).select_by_visible_text("+2")
        Select(driver.find_element_by_id("start_Month")).select_by_visible_text("February")
        Select(driver.find_element_by_id("start_Day")).select_by_visible_text("19")
        Select(driver.find_element_by_id("start_Hour_type1")).select_by_visible_text("18:00")
        driver.find_element_by_xpath("(//input[@name='ntp_sync_mode'])[2]").click()
        Select(driver.find_element_by_id("startmonth1")).select_by_visible_text("February")
        Select(driver.find_element_by_id("startweekolder")).select_by_visible_text("Second")
        Select(driver.find_element_by_id("start_Hour_type2")).select_by_visible_text("18:00")
        driver.find_element_by_name("enddatetype").click()
        Select(driver.find_element_by_id("end_Month")).select_by_visible_text("February")
        Select(driver.find_element_by_id("end_Day")).select_by_visible_text("20")
        Select(driver.find_element_by_id("end_Hour_type1")).select_by_visible_text("21:00")
        driver.find_element_by_xpath("(//input[@name='enddatetype'])[2]").click()
        Select(driver.find_element_by_id("endmonth1")).select_by_visible_text("March")
        Select(driver.find_element_by_id("endweekolder")).select_by_visible_text("Third")
        Select(driver.find_element_by_id("endday1")).select_by_visible_text("Wednesday")
        Select(driver.find_element_by_id("end_Hour_type2")).select_by_visible_text("20:00")
        driver.find_element_by_id("cancelBTN").click()
        time.sleep(2)
        driver.find_element_by_id("okBTN").click()
        self.is_alert_to_be_switch(driver)
        self.assertEqual("Time has been adjusted.", self.close_alert_and_get_its_text())
        
        


        #Reboot / Shutdown
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[4]").click()
        driver.find_element_by_xpath("//span[@id='sub6']/div[5]").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("radioShutdown").click()
        driver.find_element_by_id("radioReboot").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^This action stops all services, shuts down and restarts the server\. Are you sure[\s\S]$")
        driver.find_element_by_id("radioShutdown").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^This action stops all services and shuts down the server so that it can be safely turned off\. Are you sure[\s\S]$")

    def test_R2_Network_Setup(self):
        driver = self.driver 
        
        #Network Setup
        driver._switch_to.default_content() 
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[2]").click()
        driver.find_element_by_xpath("//span[@id='sub4']/div").click()
        driver.switch_to_frame("mainContent")
        driver.find_element_by_xpath("//td[3]/div/span").click()
        driver.find_element_by_id("form_ComName").clear()
        driver.find_element_by_id("form_ComName").send_keys("Tim")
        Select(driver.find_element_by_id("form_WanInf")).select_by_visible_text("LAN 2")
        driver.find_element_by_xpath("//input[@id='ProtocolAuto1']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolManual1']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolAuto0']").click()
        driver.find_element_by_xpath("//input[@id='ProtocolManual0']").click()
        driver.find_element_by_xpath("//div[@id='cancelBTN']").click()

        #DDNS Setup
        driver.find_element_by_xpath("//td[5]/div/span").click()
        time.sleep(2)
        self.is_element_to_be_clickable_by_xpath(driver,"//input[@id='enable_update_ddns']")
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        Select(driver.find_element_by_id("ddns_interface")).select_by_index(1)
        Select(driver.find_element_by_id("ddns_interface")).select_by_index(0)
        Select(driver.find_element_by_id("ddns_provider_selector")).select_by_index(1)
        Select(driver.find_element_by_id("ddns_provider_selector")).select_by_index(0)
        driver.find_element_by_id("ddns_username").send_keys("123")
        driver.find_element_by_id("ddns_password").send_keys("1234")
        driver.find_element_by_id("ddns_hostname").send_keys("1234")
        Select(driver.find_element_by_id("ddns_update_period")).select_by_visible_text("2")
        driver.find_element_by_id("modifyBTN").click()
        self.assertEqual("DDNS settings have been updated.", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_id("resetBTN").click()
        driver.find_element_by_id("ddns_username").clear()
        driver.find_element_by_id("ddns_password").clear()
        driver.find_element_by_id("ddns_hostname").clear()
        driver.find_element_by_xpath("//input[@id='enable_update_ddns']").click()
        driver.find_element_by_id("modifyBTN").click()
        self.assertEqual("DDNS settings have been updated.", self.close_alert_and_get_its_text())
        
        #Network Service
        #MGS
        driver._switch_to.default_content() 
        driver.find_element_by_xpath("//div[@id='masterdiv']/div[2]").click()
        driver.find_element_by_xpath("//span[@id='sub4']/div[2]").click()
        time.sleep(2)
        driver.switch_to_frame("mainContent")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("5255")
        driver.find_element_by_id("cancelBTN").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
        

        #RS
        driver.find_element_by_xpath("//td[3]/div/span").click()
        time.sleep(2)
        driver.find_element_by_id("MS_IP").clear()
        driver.find_element_by_id("MS_IP").send_keys("192.168.0.1")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("124")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("lanport1").clear()
        driver.find_element_by_id("lanport1").send_keys("125")
        driver.find_element_by_id("wanip").clear()
        driver.find_element_by_id("wanip").send_keys("192.168.0.100")
        driver.find_element_by_id("wanport").clear()
        driver.find_element_by_id("wanport").send_keys("126")
        driver.find_element_by_xpath("//div[@id='cancelBTN']/span").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
      


        #MDS
        driver.find_element_by_xpath("//td[5]/div/span").click()
        time.sleep(2)
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("MS_IP").clear()
        driver.find_element_by_id("MS_IP").send_keys("192.168.0.10")
        driver.find_element_by_id("commandPort").clear()
        driver.find_element_by_id("commandPort").send_keys("234")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("lanport1").clear()
        driver.find_element_by_id("lanport1").send_keys("236")
        driver.find_element_by_id("wanip").clear()
        driver.find_element_by_id("wanip").send_keys("192.168.0.11")
        driver.find_element_by_id("wanport").clear()
        driver.find_element_by_id("wanport").send_keys("237")
        driver.find_element_by_xpath("//div[@id='cancelBTN']/span").click()
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_xpath("//div[@id='okBTN']/span").click()
        self.assertEqual("Update server successfully.", self.close_alert_and_get_its_text())
        
        #Storage Service
        driver.find_element_by_xpath("//td[7]/div/span").click()
        time.sleep(3)
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("cancelBTN").click()
        time.sleep(3)
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("By enabling storage service, all other services like management services will stop automatically.", self.close_alert_and_get_its_text())
        self.is_alert_to_be_switch(driver)
        self.assertEqual("Update server successfully", self.close_alert_and_get_its_text())
        self.is_element_to_be_clickable_by_xpath(driver,"//tbody[2]/tr/td[2]")
        driver.find_element_by_xpath("//tbody[2]/tr/td[2]").click()
        driver.find_element_by_id("modifyBTN").click()
        time.sleep(5)
        driver.find_element_by_xpath("//tbody[2]/tr/td[2]").click()
        driver.find_element_by_id("resetBTN").click()
        self.assertEqual("This Volume will not be available for the client user anymore.", self.close_alert_and_get_its_text())
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='restartBTN']/span").click()
        self.assertEqual("Restart storage server successfully", self.close_alert_and_get_its_text())
        time.sleep(5)
        driver.find_element_by_id("enableServer").click()
        driver.find_element_by_id("okBTN").click()
        self.assertEqual("Update server successfully", self.close_alert_and_get_its_text())
        time.sleep(3)

        #web
        driver.find_element_by_xpath("//td[9]/div/span").click()
        time.sleep(1)
        driver.find_element_by_id("form_WebPort").clear()
        driver.find_element_by_id("form_WebPort").send_keys("1024")
        driver.find_element_by_xpath("//div[@id='resetBTN']/span").click()
        time.sleep(2)        
        driver.find_element_by_xpath("//div[@id='saveBTN']/span").click()
        self.assertEqual("The new port is the same as the old port", self.close_alert_and_get_its_text())
                                                                                    


#---------------------------------------------------------------------------
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
  
    def is_element_to_be_clickable_by_id(self,driver,ID):
        try: 
            wait = WebDriverWait(driver,90)
            wait.until(expected_conditions.element_to_be_clickable((By.ID,ID)))          
        except NoSuchElementException, e: return False
        return True

    def is_element_to_be_clickable_by_xpath(self,driver,xpath):
        try: 
            wait = WebDriverWait(driver,90)
            wait.until(expected_conditions.element_to_be_clickable((By.XPATH,xpath)))          
        except NoSuchElementException, e: return False
        return True

    def is_element_to_be_clickable_by_Link_Text(self,driver,text):
        try: 
            wait = WebDriverWait(driver,90)
            wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,text)))          
        except NoSuchElementException, e: return False
        return True

    def is_frame_to_be_switch(self,driver,FrameName):
        try: 
            wait = WebDriverWait(driver,90)
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(FrameName))
        except NoSuchFrameException, e: return False
        return True
      
    def is_alert_to_be_switch(self,driver):
        try:
            wait = WebDriverWait(driver,90)
            wait.until(expected_conditions.alert_is_present())
        except NoAlertPresentException, e: return False
        return True  

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = str(alert.text).strip()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def assertEqual(self, first, second, msg = None):
        try:super(Web_test, self).assertEqual(first, second, msg)
        except AssertionError as e: print(str(e))
    
    def assertRegexpMatches(self, text, expected_regexp, msg = None):
        try: super(Web_test, self).assertRegexpMatches(text, expected_regexp, msg)
        except AssertionError as e: print(str(e))




if __name__ == "__main__":
     
    def suite_VM():
        suite = unittest.TestSuite()
        suite.addTest(Web_test("test_Login_Page"))
        suite.addTest(Web_test("test_File_System"))
        suite.addTest(Web_test("test_Network_Setup"))
        suite.addTest(Web_test("test_Management"))
        suite.addTest(Web_test("test_System"))
        return suite  
      
    def suite_R1():
        suite = unittest.TestSuite()
        suite.addTest(Web_test("test_Login_Page"))
        suite.addTest(Web_test("test_File_System"))
        suite.addTest(Web_test("test_Network_Setup"))
        suite.addTest(Web_test("test_Management"))
        suite.addTest(Web_test("test_R1_R2_System"))
        return suite   
     
    def suite_R2():
        suite = unittest.TestSuite()
        suite.addTest(Web_test("test_Login_Page"))
        suite.addTest(Web_test("test_File_System"))
        suite.addTest(Web_test("test_R2_Network_Setup"))
        suite.addTest(Web_test("test_Management"))
        suite.addTest(Web_test("test_R1_R2_System"))
        return suite    


    runner = unittest.TextTestRunner(verbosity=2)
   
    try:
        IP = sys.argv[1]
        Product = sys.argv[2] 
        Web_test.setting(IP)

        if Product == "VM" : runner.run(suite_VM())
        elif Product == "R2" : runner.run(suite_R2())
        elif Product == "R1" : runner.run(suite_R1())

    except Exception as err:
        print(err)

    
