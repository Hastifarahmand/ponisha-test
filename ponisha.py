from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
driver.get("https://ponisha.ir")
dvs=driver.find_elements(By.CLASS_NAME,"MuiIconButton-sizeMedium")

time.sleep(10)
dv=dvs[1].click()
time.sleep(5)
di=driver.find_elements(By.ID,"input-username")[0].send_keys("your phone")


time.sleep(10)
klik=driver.find_elements(By.CLASS_NAME,"MuiButton-root")[0].click()
time.sleep(5)
ns=input()
print(ns)
ramz=driver.find_elements(By.CLASS_NAME,"vi")[0].send_keys(ns)
time.sleep(5)
driver.get("https://ponisha.ir/search/projects?filterSkillsByUserId=3290553")
time.sleep(5)
jostojo=driver.find_elements(By.ID ,"input-query")[0].send_keys("پایتون")
time.sleep(5)
# file=driver.find_elements(By.CLASS_NAME ,"MuiButtonBase-root")
# print(len(file))
# file=driver.find_elements(By.CLASS_NAME ,"breakpoint no-ssr")
# print(len(file))

