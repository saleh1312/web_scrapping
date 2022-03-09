from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import sys




def ww(driver,xpath,exite=True,coll=False):
    try:
        if coll ==True:
            
            element = WebDriverWait(driver,20).until(
             EC.presence_of_all_elements_located((By.XPATH, xpath)))
        else:
            element = WebDriverWait(driver,20).until(
             EC.presence_of_element_located((By.XPATH, xpath)))
            
        
        return element
        
    except:
        if exite==True:
            print("not found")
            sys.exit()
        else:
            return None




driver = webdriver.Chrome("C:\\Users\\mohamed\\Desktop\\scrap\driver\\chromedriver.exe")
driver.get("https://twitter.com/")


button=ww(driver,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
button.click()



text_box=ww(driver,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
text_box.send_keys("profsoft1312@gmail.com")
ele="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]"
login_button=driver.find_element_by_xpath(ele)
login_button.click()




text_box=ww(driver,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input",False)
if text_box != None:
    text_box.send_keys("ProfSoft6")
    ele="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div"
    login_button=driver.find_element_by_xpath(ele)
    login_button.click()


text_box=ww(driver,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
text_box.send_keys("mohamed13122001")
ele="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]"
login_button=driver.find_element_by_xpath(ele)
login_button.click()





num_of_tweetes=len(ww(driver,"//div/div[@class='css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']",True,True))
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while num_of_tweetes <100:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    num_of_tweetes=len(ww(driver,"//div/div[@class='css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']",True,True))
    
    
    
    
    
    
tweets=ww(driver,"//div/div[@class='css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']",True,True)
for tweet in tweets:
    print(tweet.text)
    


time.sleep(60)

driver.quit()