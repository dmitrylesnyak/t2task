from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")

element = driver.find_element_by_class_name("actions-container")
elem=element.find_element_by_tag_name("a")
elem.click()
iframe=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
#el=driver.find_element_by_id("loginDialog")
#if1=element.find_element_by_tag_name("iframe")
#driver.switch_to.frame(if1)

#elem1 = driver.find_element_by_id("card-auth")
#elem1.send_keys("8999")


#Чтобы зайти в ЛК необходимо быть абонентом Tele2
#Поэтому я не могу выполнить вторую часть задания

