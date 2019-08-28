from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")
element = driver.find_element_by_class_name("swiper-wrapper")
all_children_by_css = element.find_elements_by_class_name("ssc-tariff-box")
n=0
print ("len(all_children_by_css): " + str(len(all_children_by_css)))
while n<(len(all_children_by_css)):
    title=all_children_by_css[n].find_element_by_class_name("tariff-title")
    settings=all_children_by_css[n].find_elements_by_class_name("hit-image")
    if settings != []:
        print(title.text)
        print("Hit")
    n=n+1
    
