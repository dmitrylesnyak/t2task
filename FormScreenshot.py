from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")

element = driver.find_element_by_class_name("tizer-home-block")
#element = driver.find_element_by_class_name("specially-for-floctory")
driver.implicitly_wait(3)
window_before = driver.window_handles[0]

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .key_down(Keys.ENTER) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .key_up(Keys.ENTER) \
    .perform() \

window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.save_screenshot('screen.png')
#element=driver.find_element_by_link_text("https://tele2.ru/api/media/content?contentId=m2180056")

#Да, мне все еще не удалось подобрать правильный локатор для работы
#С содержимым той формы. Сделал таск хоть как-то
