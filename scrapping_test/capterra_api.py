# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
#
# url = "https://www.capterra.com/p/100994/Dealertrack-DMS/reviews/"
#
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options)
#
# driver.get(url)
# time.sleep(60)
# soup = BeautifulSoup(driver.page_source, features="html.parser")
# count = 1
#
# h2_tag = soup.find("h2")
# h2_tag_text_list = h2_tag.text.split(" ")
#
# # /html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[26]/div/div/button
# # /html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[51]/div/div/button
# per_page = h2_tag_text_list[1]
# total_review = h2_tag_text_list[3]
# per_page = int(per_page)
# total_review = int(total_review)
# page = total_review // per_page
# print(page)
# while count <= page+1:
#     x_path = "/html/body/div[1]/div/div[2]/div/div[4]/div/div[3]/div[{value}]/div/div/button".format(
#         value=(per_page*count)+1)
#     button_tag = driver.find_element(By.XPATH, x_path)
#     print(button_tag)
#     if button_tag:
#         count += 1
#         button_tag.click()
#         time.sleep(60)
#
# soup = BeautifulSoup(driver.page_source, features="html.parser")
# div_pros_sec = soup.find("div", attrs={"data-testid": "pros-section"})
# div_pros_component = div_pros_sec.find_all("div", attrs={"class": "nb-italic"})
# list_data = []
# for pros in div_pros_component:
#     dict_data = {}
#     dict_data["description"] = pros.text
#     dict_data["sentiments"] = 1
#     list_data.append(dict_data)
#
# div_cons_sec = soup.find("div", attrs={"data-testid": "cons-section"})
# div_cons_component = div_cons_sec.find_all("div", attrs={"class": "nb-italic"})
# for cons in div_cons_component:
#     dict_data = {}
#     dict_data["description"] = cons.text
#     dict_data["sentiments"] = 0
#     list_data.append(dict_data)
#
# div_review = soup.find("div", attrs={"class": "gtm-review-section"})
# review_card_list = div_review.find_all("div", attrs={"data-test-id": "review-card"})
# for review_card in review_card_list:
#     review_content_div = review_card.find("div", attrs={"data-test-id": "review-content"})
#     text_div_list = review_content_div.find_all("div", attrs={"class": "nb-text-md"})
#     for text_div in text_div_list:
#         dict_data = {}
#         strong_tag = text_div.find("strong")
#         if strong_tag.text.startswith("Pros"):
#             dict_data["description"] = text_div.text
#             dict_data["sentiments"] = 1
#             list_data.append(dict_data)
#         elif strong_tag.text.startswith("Cons"):
#             dict_data["description"] = text_div.text
#             dict_data["sentiments"] = 0
#             list_data.append(dict_data)
#         else:
#             dict_data["description"] = text_div.text
#             dict_data["sentiments"] = 2
#             list_data.append(dict_data)
#
# df = pd.DataFrame(list_data)
# print(df)
# df = df.dropna(axis=1, how="all")
# df.to_csv('capterra_data.csv', index=False)
#
#     # from selenium.webdriver.support.ui import WebDriverWait
#     # from selenium.webdriver.support import expected_conditions as EC
#     #
#     # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
#     #         By.CLASS_NAME, 'nb-button')))
#     # if button:
#     #     count += 1
#     #     button.click()
#
#         # driver.implicitly_wait(10)
#         # ActionChains(driver).move_to_element(button_tag).click(button_tag).perform()
#
#
# # while True:
# #     flag = False
# #     div_review_list = soup.find("div", attrs={"id": "reviews-list"})
# #     div_review_component = div_review_list.find_all("div", attrs={"data-testid": "ReviewsListComponent"})
# #     for component in div_review_component:
# #         data_dict = {}
# #         pros_comp = component.find("p", attrs={"data-testid": "review-pros-content"})
# #         if pros_comp:
# #             data_dict["description"] = pros_comp.text
# #             data_dict["sentiments"] = 1
# #             data_list.append(data_dict)
# #         data_dict = {}
# #         cons_comp = component.find("p", attrs={"data-testid": "review-cons-content"})
# #         if cons_comp:
# #             data_dict["description"] = cons_comp.text
# #             data_dict["sentiments"] = -1
# #             data_list.append(data_dict)
# #         data_dict = {}
# #         title_comp = component.find("h4", attrs={"data-testid": "review-title"})
# #         if title_comp:
# #             data_dict["description"] = title_comp.text
# #             data_dict["sentiments"] = 0
# #             data_list.append(data_dict)
# #     button_tags = driver.find_elements(By.CLASS_NAME, 'primary-button')
# #     for button_tag in button_tags:
# #         button_text = button_tag.text
# #         if button_text == "Next":
# #             button_tag.click()
# #             time.sleep(10)
# #             flag = True
# #     if flag is False:
# #         break

# import requests
#
# cookie_value = "experimentSessionId=bd34e91c-7c26-41ff-8fb7-f151b8b0c4ac; rt_var=prd; device=Desktop; country_code=IN; _capterra2_session=e626f9ee13bd0a70075cbb62f59ae341; _gid=GA1.2.674267823.1686812485; pxcts=7acbf2e5-0b4a-11ee-b56e-4b527a476551; _pxvid=7acbdfa0-0b4a-11ee-b56e-34ae3b2d35ab; _gcl_au=1.1.2091382668.1686812506; _fbp=fb.1.1686812512975.925856971; ln_or=eyIyNjk3MCI6ImQifQ%3D%3D; _rdt_uuid=1686812521673.b21b205f-29f6-4f82-8d76-d265dc406ee1; seerid=3f0d2882-4fdc-415d-a0a6-3af3d53effe8; fs_uid=#18VAT4#6298800674582528:4637894051901440:::#/1718348525; AMCVS_04D07E1C5E4DDABB0A495ED1%40AdobeOrg=1; AMCV_04D07E1C5E4DDABB0A495ED1%40AdobeOrg=-637568504%7CMCIDTS%7C19524%7CMCMID%7C23998873922199624730155550107014306164%7CMCAAMLH-1687417337%7C12%7CMCAAMB-1687417337%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1686819737s%7CNONE%7CvVersion%7C5.1.1; SignUpShowingProductToSaveExperiment=9275c060-0b4a-11ee-b427-b7dc13966e0a; seerses=e; _ga=GA1.2.1988310727.1686812485; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+15+2023+15%3A33%3A35+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.capterra.com%2Fp%2F100994%2FDealertrack-DMS%2Freviews%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _uetsid=d0a4ced00b6211ee91d29560d0aac77e; _uetvid=d0a55b100b6211ee80825fc5c91ec8ea; _px3=d43022b32f7382d230f531dcb8bde53a46ee3df540254c5900aacecdbda231f3:8t/b3du7gXnwABrn2QTzb3hvInN00eQaJqqnq9w9iJvEe9WNFGX2xNvwh/VqLiVZdVdm+8BJQ9dMVcSjEntMLw==:1000:HPiLRaVGqmrIGWuH5k8kvyxLoLIueFtEWNyoyglOX8aLlPZJfTbjX7mXZNHImhRbyvC6xGzo7kw2TnjB7uGR3HY66oL+7X54hEIFLkKghIOVuUgMgV7lbM5TfUJ9hMu+DcXwT/g1u2UrRP6766HwOiXESg2s+AQmTehivS1WY7BjoZsoQu/3J2jM3P+4AIeWxSnwcoRW0dvWPasDme473A==; _pxde=851af3ea88ee2f0da2b6d5949319676b87b8b7fe48397d35dc05bdf5047a0874:eyJ0aW1lc3RhbXAiOjE2ODY4MjM0OTUxOTUsImZfa2IiOjAsImlwY19pZCI6W119; _gat_UA-126190-1=1; _ga_T9V61700R6=GS1.1.1686822949.3.1.1686823516.60.0.0; _ga_M5DGBDHG2R=GS1.1.1686822949.3.1.1686823516.56.0.0"
#
# header = {'Cookie': cookie_value}
# response = requests.get("https://www.capterra.com/spotlight/rest/reviews?apiVersion=2&productId=100994&from=0&size=1000", headers=header)
# print(response)
# print(len(response))

import requests

url = "https://www.capterra.com/spotlight/rest/reviews?apiVersion=2&productId=100994&from=0&size=1000"

payload = {}
headers = {
  'Cookie': 'experimentSessionId=bd34e91c-7c26-41ff-8fb7-f151b8b0c4ac; rt_var=prd; device=Desktop; country_code=IN; _capterra2_session=e626f9ee13bd0a70075cbb62f59ae341; _gid=GA1.2.674267823.1686812485; pxcts=7acbf2e5-0b4a-11ee-b56e-4b527a476551; _pxvid=7acbdfa0-0b4a-11ee-b56e-34ae3b2d35ab; _gcl_au=1.1.2091382668.1686812506; _fbp=fb.1.1686812512975.925856971; ln_or=eyIyNjk3MCI6ImQifQ%3D%3D; _rdt_uuid=1686812521673.b21b205f-29f6-4f82-8d76-d265dc406ee1; seerid=3f0d2882-4fdc-415d-a0a6-3af3d53effe8; fs_uid=#18VAT4#6298800674582528:4637894051901440:::#/1718348525; AMCVS_04D07E1C5E4DDABB0A495ED1%40AdobeOrg=1; AMCV_04D07E1C5E4DDABB0A495ED1%40AdobeOrg=-637568504%7CMCIDTS%7C19524%7CMCMID%7C23998873922199624730155550107014306164%7CMCAAMLH-1687417337%7C12%7CMCAAMB-1687417337%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1686819737s%7CNONE%7CvVersion%7C5.1.1; SignUpShowingProductToSaveExperiment=9275c060-0b4a-11ee-b427-b7dc13966e0a; seerses=e; _ga=GA1.2.1988310727.1686812485; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+15+2023+15%3A33%3A35+GMT%2B0530+(India+Standard+Time)&version=202301.2.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.capterra.com%2Fp%2F100994%2FDealertrack-DMS%2Freviews%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _uetsid=d0a4ced00b6211ee91d29560d0aac77e; _uetvid=d0a55b100b6211ee80825fc5c91ec8ea; _px3=d43022b32f7382d230f531dcb8bde53a46ee3df540254c5900aacecdbda231f3:8t/b3du7gXnwABrn2QTzb3hvInN00eQaJqqnq9w9iJvEe9WNFGX2xNvwh/VqLiVZdVdm+8BJQ9dMVcSjEntMLw==:1000:HPiLRaVGqmrIGWuH5k8kvyxLoLIueFtEWNyoyglOX8aLlPZJfTbjX7mXZNHImhRbyvC6xGzo7kw2TnjB7uGR3HY66oL+7X54hEIFLkKghIOVuUgMgV7lbM5TfUJ9hMu+DcXwT/g1u2UrRP6766HwOiXESg2s+AQmTehivS1WY7BjoZsoQu/3J2jM3P+4AIeWxSnwcoRW0dvWPasDme473A==; _pxde=851af3ea88ee2f0da2b6d5949319676b87b8b7fe48397d35dc05bdf5047a0874:eyJ0aW1lc3RhbXAiOjE2ODY4MjM0OTUxOTUsImZfa2IiOjAsImlwY19pZCI6W119; _gat_UA-126190-1=1; _ga_T9V61700R6=GS1.1.1686822949.3.1.1686823516.60.0.0; _ga_M5DGBDHG2R=GS1.1.1686822949.3.1.1686823516.56.0.0; _pxhd=sWFsePEo/JN/OXMZOl2drS2vpGczXI6bqT9awgi49Z68dNeYDTTnRXDE188nTrRPBHlPQ8bYa1Vnna3dxedHKg==:RWXd7V0BJmG7z7MZ5ts4KA/ubiBME9ZdAYjVxk27TNsm8sUOPMF/CaJg9p8ksPp/jaqsmWccJh-Q2J9luVDP5Dg70KNoaMRPx/i0/Ei6IGs='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
