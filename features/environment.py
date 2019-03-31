import subprocess
from time import sleep

from appium import webdriver
import ipdb
  
    

def before_feature(context,feature):
    subprocess.Popen('appium ', shell=True)
    sleep(10)
    """desired_caps={
      "deviceName": "device",
      "platformName": "Android",
      "appPackage": "com.android.calculator2",
      "appActivity": "com.android.calculator2.Calculator"
    }
    driver=webdriver.Remote("http://127.0.0.1:5555/wd/hub", desired_caps)
    sleep(3)"""
    
def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
   print "This is after scenario"
   data = None
   data = str(context.scenario)
   print data
   data = data.split('">')
   print data
   data = data[0].split('_')
   print data
   data.reverse()
   print data

def after_feature(context, feature):
  pass

def after_all(context):
  pass