import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

url = "https://www.getapp.com/industries-software/a/dealer-management-solutions/reviews/"
page = 1
# url = "https://www.getapp.com/industries-software/a/dealer-management-solutions/reviews/page-{page}".format(page=page)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get(url)
time.sleep(30)

soup = BeautifulSoup(driver.page_source, features="html.parser")
# print(soup)
div_review_res = soup.find("div", attrs={"id": "reviewResults"})

if div_review_res:
    h2_tag = div_review_res.find("h2", attrs={"class": "Typography"})
    print(h2_tag.text)
    # total_review = h2_tag.text.split(" ")[0]
    # total_review = int(total_review)
    # per_page = 25
    # page = total_review // per_page
    # count = 1
    # while count <= page:
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 10):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    div_review_res = soup.find("div", attrs={"id": "reviewResults"})
    div_review_card_list = div_review_res.find_all("div", attrs={"data-testid": "lazy-review-card"})
    list_data = []
    if div_review_card_list:
        for review_card in div_review_card_list:
            div_grid_tag = review_card.find("div", attrs={"class": "Grid"})
            if div_grid_tag:
                div_review_details_list = div_grid_tag.find_all("div", attrs={"class": "ReviewContent_row__xhAtE"})
                if div_review_details_list:
                    dict_data = {}
                    # for div_review_details in div_review_details_list:
                    p_tag = div_review_details_list[0].find("p")
                    if p_tag:
                        dict_data["description"] = p_tag.text.replace('>', '').replace('’', "'")
                        dict_data["sentiments"] = 1
                        list_data.append(dict_data)
                    dict_data = {}
                    p_tag = div_review_details_list[1].find("p")
                    if p_tag:
                        dict_data["description"] = p_tag.text.replace('>', '').replace('’', "'")
                        dict_data["sentiments"] = 0
                        list_data.append(dict_data)
    df = pd.DataFrame(list_data)
    print(df)
    # df = df.dropna(axis=1, how="any")
    # df['description'] = df['description'].dropna()
    # df = df[df['description'].notna()]
    df = df.replace({'description': {'None': np.nan, 'none': np.nan, 'na': np.nan, 'n.a.': np.nan}})
    print(df)
    # df = df.dropna(axis=1, how="any")
    df = df[df['description'].notna()]
    df.to_csv('get_app_{page}.csv'.format(page=page), index=False)
driver.close()

# if div_review_res:
#     h2_tag = div_review_res.find("h2", attrs={"class": "Typography"})
#     print(h2_tag.text)
#     total_review = h2_tag.text.split(" ")[0]
#     total_review = int(total_review)
#     per_page = 25
#     page = total_review // per_page
#     count = 1
#     while count <= page:
#         total_height = int(driver.execute_script("return document.body.scrollHeight"))
#
#         for i in range(1, total_height, 10):
#             driver.execute_script("window.scrollTo(0, {});".format(i))
#
#         div_review_res = soup.find("div", attrs={"id": "reviewResults"})
#         div_review_card_list = div_review_res.find_all("div", attrs={"data-testid": "lazy-review-card"})
#         if div_review_card_list:
#             print(len(div_review_card_list))
#             import pdb; pdb.set_trace()
#             for review_card in div_review_card_list:
#                 div_review_details = review_card.find("div", attrs={"class": "Details"})
#                 print(div_review_details)
#                 break
#         count += 1
#         url = "https://www.getapp.com/industries-software/a/dealer-management-solutions/reviews/page-{number}".format(
#             number=count)
#         time.sleep(10)
#         driver.get(url)
#         time.sleep(10)
#         soup = BeautifulSoup(driver.page_source, features="html.parser")
#
# driver.close()
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
