from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path="C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://msk.tele2.ru/")
element = driver.find_element_by_class_name("price")
TarifPrice=element.text
element.click()
element = driver.find_element_by_class_name("price")
Tarif2Price=element.text
if TarifPrice == Tarif2Price:
    print("sovpadaet")
else:
    print("ne sovpadaet")

#Нерабочая версия скрипта для сравнения всех тарифов - не выходит сравнить цену тарифа с его ценой на странице в цикле

#element = driver.find_element_by_class_name("swiper-wrapper")
#all_children_by_css = element.find_elements_by_class_name("ssc-tariff-box")
#n=0
#element=all_children_by_css
#print ("len(all_children_by_css): " + str(len(all_children_by_css)))
#while n<(len(all_children_by_css)):
 #   title=all_children_by_css[n].find_element_by_class_name("tariff-title")
 #   element = all_children_by_css[n].find_element_by_class_name("price")
 #   TarifPrice=element.text
 #   element = driver.find_element_by_class_name("price")
 #   Tarif2Price=element.text
 #   print(title.text)
 #   driver.execute_script("window.open('element.click()')")
    #if TarifPrice == Tarif2Price:
    #    print("sovpadaet")
    #else:
    #    print("ne sovpadaet")
    #driver.close
    #driver.get("https://msk.tele2.ru/")
 #   n=n+1

#driver.execute_script("window.open('https://www.yahoo.com')")
#WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
#windows_after = driver.window_handles
#new_window = [x for x in windows_after if x != windows_before][0]
#driver.switch_to_window(new_window)

