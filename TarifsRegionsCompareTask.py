from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")
element = driver.find_element_by_class_name("price")
TarifPrice=element.text
driver.get("https://rostov.tele2.ru/")
element = driver.find_element_by_class_name("price")
Tarif2Price=element.text
if TarifPrice == Tarif2Price:
    print("sovpadaet")
else:
    print("ne sovpadaet")



