import requests
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver = "C:\\Users\\ketansomani\\Downloads\\chromedriver_win32\\chromedriver"

url = "https://www.softwareadvice.com/crm/dealertrack-dms-profile/reviews/"

driver = webdriver.Chrome(chrome_driver)
driver.get(url)
# soup = BeautifulSoup(driver.page_source, features="html.parser")
# print(soup)
driver.close()
