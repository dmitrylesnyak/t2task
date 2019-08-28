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

driver.implicitly_wait(3)
window_before = driver.window_handles[0]

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .click(elem) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.ENTER) \
    .perform() \

#elem1 = driver.find_element_by_css_selector("#phone-ussd")
#elem1.send_keys("8999")
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)

#Два нюанса в этом таске:
#Чтобы зайти в ЛК необходимо быть абонентом Tele2, насколько я понял
#Я просто не могу выполнить оставшуюся часть этого таска
#И да, я опять не могу найти правильный селектор
