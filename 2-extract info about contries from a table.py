from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")


driver.get("https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A7%D9%84%D8%AF%D9%88%D9%84_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_%D8%AD%D8%B3%D8%A8_%D8%B9%D8%AF%D8%AF_%D8%A7%D9%84%D8%B3%D9%83%D8%A7%D9%86")

table_xpath="//table[@class='sortable wikitable jquery-tablesorter']"
# getting some information about the table like the size
table=driver.find_elements_by_xpath(f"{table_xpath}/tbody//tr")
rows=len(table)


for row in range(1,rows+1):
    try:
        xpath_ele=f"{table_xpath}/tbody//tr[ position()={row} ]/td[2]/a"
        ele=driver.find_element_by_xpath(xpath_ele)
        name=ele.text
        
        ele.click()
        
        #   implictly waiting
        #driver.implicitly_wait(10)
        
        #   external waiting
        try:
            element = WebDriverWait(driver,20).until(
             EC.presence_of_element_located((By.XPATH, "//*[ text()='أعلى قمة' ]/..")))
            
            a3la_no8ta=" : "+element.find_element_by_xpath("./td[position()=1]/a[position()=1]").text
        except:
            a3la_no8ta=" : لا يوجد بيانات"
            
        print(name+a3la_no8ta)
        driver.back()
        
    except Exception as e:

        continue

driver.quit()