# import time
# import pandas as pd
# import numpy as np
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from bs4 import BeautifulSoup
#
# url = "https://www.featuredcustomers.com/vendor/dealertrack/testimonials"
#
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options)
#
# driver.get(url)
# time.sleep(10)
# soup = BeautifulSoup(driver.page_source, features="html.parser")
# print(soup)

import requests
import json
import pandas as pd

url = "https://www.featuredcustomers.com/api/v1/vendor/dealertrack/testimonials?ind=&p=1&size=&sort=&view=100"

payload = {}
headers = {
  'Cookie': 'csrftoken=EVihpoFAQe7zsZ0280Wqze44DmDHspGU3OmsuPiRbJNElfiyh1o09GimtO2BjuoS'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)["reviews"]
list_data = []
print(len(data))
for review in data:
    dict_data = {}
    dict_data["description"] = review["body"].replace('“', '').replace('"', '').replace('’', "'").replace('”', '').replace('—', '-')
    dict_data["sentiments"] = None
    list_data.append(dict_data)

df = pd.DataFrame(list_data)
print(df)
# df = df.dropna(axis=1, how="all")
df.to_csv('featured_data.csv', index=False)


