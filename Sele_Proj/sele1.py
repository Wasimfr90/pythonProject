"""
TEST CASE:
---------
1) Open Web browser(chrome/edge/firefox)
2) Open URL https://admin-demo.nopcommerce.com/login or https://opensource-demo.orangehrmlive.com/
3) Provide email (admin@yourstore.com) (Admin)
4) Provide pawd (admin) (admin123)
5) Click on login
6) Capture the title on the dashboard page.
7) Verify the titlte of the dashboard page.
8) Close the browser.
"""

"""
#SELENIUM 3
from selenium import webdriver

#driver = webdriver.Chrome("C:\Driver\chromedriver-win64\chromedriver.exe")


cService = webdriver.ChromeService(executable_path="D:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = cService)

driver.get("https://opensource-demo.orangehrmlive.com/")

while(True):
    continue
    #pass
driver.find_element("username").send_keys("Admin")
driver.find_element("password").send_keys("admin123")
driver.find_element("submit").click()

act_title = driver.title
exp_title = "orangeHRM"

if act_title == exp_title :
    print("Login test passed!!!")
else:
    print("Login test failed!!!")

driver.close()

"""
"""
while(True):
    pass

"""


#SELENIUM 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

serv_obj = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")

#driver = webdriver.Chrome("C:\Driver\chromedriver-win64\chromedriver.exe")


#cService = webdriver.ChromeService(executable_path="D:\Drivers\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=serv_obj)
dri_op = Options()
dri_op.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=serv_obj,options=dri_op)
driver.get("https://opensource-demo.orangehrmlive.com/")

#while(True):
    #continue
    #pass

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("admin")
#driver.find_element(By.ID,"password").send_keys("admin123")
#driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
#driver.find_element("username").send_keys("Admin")
#driver.find_element("password").send_keys("admin123")
#driver.find_element("submit").click()

act_title = driver.title
exp_title = "orangeHRM"

if act_title == exp_title:
    print("Login test passed!!!")
else:
    print("Login test failed!!!")

driver.close()

