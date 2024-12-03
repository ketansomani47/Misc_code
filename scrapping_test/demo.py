import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url = "https://www.softwareadvice.com/crm/dealertrack-dms-profile/reviews/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get(url)
time.sleep(5)
data_list = []
count = 0
while True:
    flag = False
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    div_review_list = soup.find("div", attrs={"id": "reviews-list"})
    div_review_component = div_review_list.find_all("div", attrs={"data-testid": "ReviewsListComponent"})
    for component in div_review_component:
        data_dict = {}
        pros_comp = component.find("p", attrs={"data-testid": "review-pros-content"})
        if pros_comp:
            data_dict["description"] = pros_comp.text
            data_dict["sentiments"] = 1
            data_list.append(data_dict)
        data_dict = {}
        cons_comp = component.find("p", attrs={"data-testid": "review-cons-content"})
        if cons_comp:
            data_dict["description"] = cons_comp.text
            data_dict["sentiments"] = -1
            data_list.append(data_dict)
        data_dict = {}
        title_comp = component.find("h4", attrs={"data-testid": "review-title"})
        if title_comp:
            data_dict["description"] = title_comp.text
            data_dict["sentiments"] = 0
            data_list.append(data_dict)
    button_tags = driver.find_elements(By.CLASS_NAME, 'primary-button')
    for button_tag in button_tags:
        button_text = button_tag.text
        if button_text == "Next":
            button_tag.click()
            time.sleep(10)
            flag = True
    if flag is False:
        break

df = pd.DataFrame(data_list)
print(df)
df = df.dropna(axis=1, how="all")
df.to_csv('test_with_title.csv', index=False)