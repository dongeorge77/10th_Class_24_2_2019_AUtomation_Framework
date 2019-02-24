import time

from selenium import webdriver
import os

def test_setup():
    global driver
    driver_path=(os.getcwd().replace("Tests","").replace("\\","/")+"Drivers"+"/chromedriver.exe")
    driver=webdriver.Chrome(executable_path=driver_path)
    print(driver_path)
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)

def test_login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Login ']").click()

def test_logout():
    time.sleep(5)
    #driver.find_element_by_xpath("//a[@id='logoutLink']")
    #driver.find_element_by_class_name("logout").click()
    driver.find_element_by_id("logoutLink").click()
    time.sleep(3)
    driver.quit()

#test_setup()
#test_login()
#test_logout()

#insatall pytest from project interpretor and run command "python -m pytest"

#To get the html report: Install 'pytest-html' from project interpretor
#open in terminal an run command: 'python -m pytest --html=report1.html'