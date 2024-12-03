import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url = "https://www.capterra.com/p/100994/Dealertrack-DMS/reviews/"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get(url)
time.sleep(30)
soup = BeautifulSoup(driver.page_source, features="html.parser")
count = 1

h2_tag = soup.find("h2")
h2_tag_text_list = h2_tag.text.split(" ")

# /html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[26]/div/div/button
# /html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[51]/div/div/button
per_page = h2_tag_text_list[1]
total_review = h2_tag_text_list[3]
per_page = int(per_page)
total_review = int(total_review)
page = total_review // per_page
print(page)
while count <= page:
    x_path = "/html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[{value}]/div/div/button".format(
        value=(per_page*count)+1)
    button_tag = driver.find_element(By.XPATH, x_path)
    print(button_tag)
    if button_tag:
        count += 1
        button_tag.click()
        time.sleep(60)

list_data = []
soup = BeautifulSoup(driver.page_source, features="html.parser")
div_pros_sec = soup.find("div", attrs={"data-test-id": "pros-section"})
# import pdb; pdb.set_trace()
if div_pros_sec:
    div_pros_component = div_pros_sec.find_all("div", attrs={"class": "nb-italic"})
    for pros in div_pros_component:
        dict_data = {}
        dict_data["description"] = pros.text.replace('"', "")
        dict_data["sentiments"] = 1
        list_data.append(dict_data)

div_cons_sec = soup.find("div", attrs={"data-test-id": "cons-section"})
if div_cons_sec:
    div_cons_component = div_cons_sec.find_all("div", attrs={"class": "nb-italic"})
    for cons in div_cons_component:
        dict_data = {}
        dict_data["description"] = cons.text.replace('"', "")
        dict_data["sentiments"] = 0
        list_data.append(dict_data)

div_review = soup.find("div", attrs={"class": "gtm-review-section"})
if div_review:
    review_card_list = div_review.find_all("div", attrs={"data-test-id": "review-card"})
    for review_card in review_card_list:
        review_content_div = review_card.find("div", attrs={"data-test-id": "review-content"})
        text_div_list = review_content_div.find_all("div", attrs={"class": "nb-text-md"})
        for text_div in text_div_list:
            dict_data = {}
            strong_tag = text_div.find("strong")
            if strong_tag.text.startswith("Pros"):
                dict_data["description"] = text_div.text.split(":\xa0")[1].replace("-", "").replace("\n", "")
                dict_data["sentiments"] = 1
                list_data.append(dict_data)
            elif strong_tag.text.startswith("Cons"):
                dict_data["description"] = text_div.text.split(":\xa0")[1].replace("-", "").replace("\n", "")
                dict_data["sentiments"] = 0
                list_data.append(dict_data)
            else:
                dict_data["description"] = text_div.text.split(":\xa0")[1].replace("-", "").replace("\n", "")
                dict_data["sentiments"] = None
                list_data.append(dict_data)

df = pd.DataFrame(list_data)
# print(df)
# df = df["description"].replace("none", np.nan).replace("None", np.nan).replace("na", np.nan).replace("n.a.", np.nan)
# df.replace(
#     dict.fromkeys(['Beer', 'Alcohol', 'Beverage', 'Drink'], 'Drink'),
#     regex=True
# )
df = df.replace({'description': {'None': np.nan, 'none': np.nan, 'na': np.nan, 'n.a.': np.nan}})
df = df.dropna(axis=1, how="any")
# df = df.dropna(axis=1, how="all")
df.to_csv('capterra_data_2.csv', index=False)
