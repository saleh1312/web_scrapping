from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")


driver.get("https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85_%D8%AD%D8%B3%D8%A8_%D8%A7%D9%84%D8%A8%D9%84%D8%AF")

table=driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter']//tr")

for row in table:
    try:
        
        region=row.find_element_by_xpath("./td[1]/a").text
        count=row.find_element_by_xpath("./td[2]").text
        per_region_population=row.find_element_by_xpath("./td[3]").text
        per_muslims_world=row.find_element_by_xpath("./td[4]").text
        print(region+"  "+count+"  "+per_region_population+"  "+per_muslims_world)
    except:
        continue

driver.quit()