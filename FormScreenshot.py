from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
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
f1=driver.find_element_by_class_name("js-rules")
f2=driver.find_element_by_class_name("js-personal")
window_before = driver.window_handles[0]

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .click(f1) \
    .click(f2) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.ENTER) \
    .perform() \

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.save_screenshot('screen.png')
time.sleep(3)
window_after = driver.window_handles[2]
driver.switch_to_window(window_after)
driver.save_screenshot('screen2.png')

#Иногда форма "нашли предложение лучше?" не прокливается и выпадает ошибка "element not interactable"



