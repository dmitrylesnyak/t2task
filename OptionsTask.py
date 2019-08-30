from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")

element=driver.find_element_by_id("root")
elem=element.find_element_by_css_selector("#root > div > div:nth-child(2)")
elem2=elem.find_element_by_css_selector("#root > div > div:nth-child(2) > div")
#print(elem2)

#element=driver.find_element_by_css_selector("#modalMenu > div > div.main-mobile-menu.main-mobile-menu-subsection")
#all_children_by_css=element.find_elements_by_tag_name("ul")
#n=0
#element=all_children_by_css
#print ("len(all_children_by_css): " + str(len(all_children_by_css)))
#print(element1)
    
#print ("len(all_children_by_css): " + str(len(all_children_by_css)))
#<div class="settings-link">

#Возникла проблема с селектором, без этого я не могу построить цикл перебора options
# я не понимаю, почему из #root > div > div:nth-child(2) нельзя перейти к
# дочернему #root > div > div:nth-child(2) > div
# все элементы этого дочернего div'a недоступны
