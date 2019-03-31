from time import sleep

from appium import webdriver
from behave import *
#from appium.saucetestcase import SAUCE_USERNAME, SAUCE_ACCESS_KEY

class Calculation_Steps:
    driver=None 
    #sauce_username='Arch2019'
    #sauce_id='56b055dc-5081-4163-a14c-0fd3e921950f'
    
    @given(u'App is launched')
    def app_is_launched(self):
        desired_caps={
          "deviceName": "device",
          "platformName": "Android",
          "appPackage": "com.android.calculator2",
          "appActivity": "com.android.calculator2.Calculator"
        }
        #self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
         
        self.driver = webdriver.Remote('http://'+'Arch2019'+':'+'56b055dc-5081-4163-a14c-0fd3e921950f'+'@ondemand.saucelabs.com:80/wd/hub', desired_caps)
        sleep(3)
    
    @when('user adds number')
    def user_adds_number(self):
        self.driver.find_element_by_id("com.android.calculator2:id/digit_2").click()    
        self.driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
        sleep(3)
        self.driver.find_element_by_id("com.android.calculator2:id/op_add").click()
        sleep(3)
        self.driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
        sleep(3)
           
    @then('output should be displayed')
    def output_should_be_displayed(self):
        self.driver.find_element_by_id("com.android.calculator2:id/eq").click()
        sleep(3)
            
    
    @then(u'close app')
    def step_impl(self):
        self.driver.close_app()