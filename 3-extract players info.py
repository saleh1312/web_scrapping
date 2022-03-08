from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('headless')


driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")
driver.get("https://www.theguardian.com/football/datablog/2012/dec/24/world-best-footballers-top-100-list")
saved=r"C:\Users\mohamed\Desktop\scrap\scrapped_data"


rows=driver.find_elements_by_xpath("//table[@class='in-article sortable']/tbody/tr")



names=[]
poss=[]
clubs=[]
natios=[]
for row in rows:
    name=row.find_element_by_xpath("./td[2]").text
    pos=row.find_element_by_xpath("./td[3]").text
    club=row.find_element_by_xpath("./td[4]").text
    natio=row.find_element_by_xpath("./td[5]").text
    
    names.append(name)
    poss.append(pos)
    clubs.append(club)
    natios.append(natio)

driver.quit()
    
    
data = {"name":names,"position":poss,"club":clubs,"nationality":natios}
dataframe=pd.DataFrame(data)  
dataframe.to_csv(r'..\scrapped_data\players_info.csv', index=False)
    
    

