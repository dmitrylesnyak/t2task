from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")

element = driver.find_element_by_class_name("specially-for-floctory")
time.sleep(3)
element.click()
iframe=driver.find_element_by_id("fl-153069")
driver.switch_to.frame(iframe)
f1=driver.find_element(By.ID, "tel")
f1.send_keys("8999")
f2=driver.find_element(By.ID, "name")
f2.send_keys("abcd")
time.sleep(3)
f3=driver.find_element_by_tag_name("a")
f3.click()

#Иногда форма "нашли предложение лучше?" не прокливается и выпадает ошибка "element not interactable"


