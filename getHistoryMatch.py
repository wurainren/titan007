# # selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("D:\\Tools\\WebDriver\\bin\\chromedriver.exe")
service.start()


driver = webdriver.Remote(service.service_url)

driver.get('http://bf.titan007.com/football/Over_20230512.htm')
# elements = driver.find_elements(By.TAG_NAME, 'table')
# for e in elements:
#     print(e.id)

