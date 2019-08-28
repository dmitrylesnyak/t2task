from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")

element = driver.find_element_by_class_name("specially-for-floctory")
driver.implicitly_wait(3)
element.click()
driver.implicitly_wait(3)
#form = element.find_element_by_class_name("flocktory-widget")

#Чуть не уничтожил компьютер на этом таске
#Я не могу подобрать подходящий селектор к этому input
#Ни By.ID, ни class_name, даже xpath не помогает и я не могу понять почему, особенно в случае с ID


#f1=driver.find_element(By.ID, "tel")
#f1 = driver.find_element_by_id("tel")
#f1= driver.find_element_by_xpath("//*[@id='tel']")
#f1 = driver.find_element_by_css_selector("input[id='tel']")
#f1 = driver.find_element_by_css_selector("#tel")
f1.send_keys("8999")



