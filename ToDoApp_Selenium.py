# Prerequisites:
# 1. Selenium WebDriver (Chrome) is installed
# 2. Google Chrome is installed
# 3. Modify the <Username> & <Password> fields to the desired input
# 4. Modify the time.sleep(*) value as desired. A longer value will result in a longer waiting time

from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import string

print('Simulation Start')

# Open Google Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()

# Input Login Details here
def login():
    # Click on Github button
    driver.find_element(By.XPATH, "//a[@class='btn btn-social btn-github']").click()
    time.sleep(5)

    # Change Selenium to point to Login Prompt
    winhan1 = driver.window_handles[1]
    driver.switch_to.window(winhan1)
    time.sleep(1)

    # Input Login Details
    driver.find_element(By.XPATH, "//input[@id='login_field']").send_keys("<INPUT USERNAME>")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("<INPUT PASSWORD")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='commit']").click()

    # Change Selenium to point back to Main Page
    winhan0 = driver.window_handles[0]
    driver.switch_to.window(winhan0)
    time.sleep(1)

def logout():
    driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

def createstr():
    s_length = 20
    s = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    return s

def main():

    repeat = 0
    # Navigate to Test Link
    driver.get("https://todo-list-login.firebaseapp.com/#!/")
    time.sleep(5)
    login()
    time.sleep(5)

    # Create 10 to do lists with random string
    while repeat != 10:
        driver.find_element(By.XPATH, "//input[@ng-model='home.list']").send_keys(str(createstr()))
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='btn btn-success btn-block glyphicon glyphicon-plus task-btn']").click()
        time.sleep(1)
        repeat += 1

    time.sleep(2)
    logout()
    time.sleep(5)

    # Click on Github button
    driver.find_element(By.XPATH, "//a[@class='btn btn-social btn-github']").click()
    time.sleep(5)

    # Delete the 10th entry
    if repeat == 10:
        driver.find_element(By.XPATH, "//li[10]//div[1]//div[2]//button[1]").click()
        repeat -= 1
        time.sleep(2)

    # Delete subsequent 5-9 entries
    while repeat > 4:
        driver.find_element(By.XPATH, f"/html[1]/body[1]/ng-view[1]/div[1]/div[3]/div[1]/ul[1]/li[{str(repeat)}]/div[1]/div[2]/button[1]").click()
        repeat -=1
        time.sleep(2)

    logout()
    time.sleep(5)
    driver.close()
    print('Simulation ended')

main()