import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url = "https://www.getapp.com/industries-software/a/dealer-management-solutions/reviews/page-2"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get(url)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)
soup = BeautifulSoup(driver.page_source, features="html.parser")
print(soup)
# div_review_res = soup.find("div", attrs={"id": "reviewResults"})
# if div_review_res:
#     h2_tag = div_review_res.find("h2", attrs={"class": "Typography"})
#     print(h2_tag.text)
#     total_review = h2_tag.text.split(" ")[0]
#     # div_review_card_list = div_review_res.find_all("div", attrs={"data-testid": "lazy-review-card"})
#     # if div_review_card_list:
#     #     print(len(div_review_card_list))
#     #     for review_card in div_review_card_list:
#     #         print(review_card)
# # driver.close()
# per_page = 25
# total_review = int(total_review)
# page = 1
# total_page = total_review // per_page
# while page <= total_page+1:
#     page += 1
#     url = "https://www.getapp.com/industries-software/a/dealer-management-solutions/reviews/page-{number}".format(number=page)
#     print(url)
#     driver.get(url)
#     time.sleep(10)
#     soup = BeautifulSoup(driver.page_source, features="html.parser")
#     # print(soup)
#     div_review_res = soup.find("div", attrs={"id": "reviewResults"})
#     if div_review_res:
#         div_review_card_list = div_review_res.find_all("div", attrs={"data-testid": "lazy-review-card"})
#         if div_review_card_list:
#             print(len(div_review_card_list))
#             # for review_card in div_review_card_list:
#             #     print(review_card)
