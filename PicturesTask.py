from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://more.tele2.ru/")
#element = driver.find_elements_by_css_selector("picture")
#print(element.text)
all_children_by_css = driver.find_elements_by_css_selector("picture")
n=0
print ("len(all_children_by_css): " + str(len(all_children_by_css)))
while n<(len(all_children_by_css)):
    title=all_children_by_css[n].find_element_by_css_selector("img")
    #settings=all_children_by_css[n].find_elements_by_class_name("hit-image")
    print(title.get_attribute("src"))  
    n=n+1
