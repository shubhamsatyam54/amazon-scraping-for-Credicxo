import json
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

final_data = {}
time_taken = []

df = pd.read_csv("F:\\internship\\Credicxo\\task\\amzaon_list.csv")
urllist = df[["Asin", "country"]].sort_values(by="country")
i, total_url = 0, len(urllist)
while True:
    tempurllist = urllist.iloc[i:i + 100]
    start = time.time()
    for row in range(len(tempurllist)):
        tempdata = {}
        url = "https://www.amazon.{country}/dp/{Asin}".format(**tempurllist.iloc[row])
        driver.get(url)
        try:

            title = driver.find_element_by_id('productTitle')
            tempdata["product_title"] = title.text

            img = driver.find_element_by_class_name("a-dynamic-image")
            tempdata["product_image"] = img.get_attribute("src")

            price_symbol = driver.find_elements_by_xpath('.//span[@class="a-price-symbol"]')
            whole_price = driver.find_elements_by_xpath('.//span[@class="a-price-whole"]')
            fraction_price = driver.find_elements_by_xpath('.//span[@class="a-price-fraction"]')
            full_price = driver.find_elements_by_xpath('//span[@class="a-size-base a-color-price a-color-price"]')
            if whole_price != [] and fraction_price != [] and price_symbol != []:
                if price_symbol[0].text != "":
                    price = price_symbol[0].text + '.'.join([whole_price[0].text, fraction_price[0].text])
                else:
                    price = full_price[0].text
            elif full_price != []:
                price = full_price[0].text
            else:
                price = driver.find_elements_by_xpath('//span[@class="a-color-base"]')[0].text
            tempdata["price"] = price

            desc = driver.find_elements_by_xpath('//*[@id="bookDescription_feature_div"]/div/div[1]/span')
            desc2 = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/ul/li/span')
            if desc != []:
                tempdata["desc"] = desc[0].text
            elif desc2 != []:
                tempdata["desc"] = desc2[0].text

            final_data[url] = tempdata

        except:
            print(url + " " + "not found")

    end = time.time()
    i += 100
    time_taken.append(end - start)
    if i > total_url:
        break

with open("output.json", "w") as output:
    json.dump(final_data, output)

with open("time.json", "w") as outtime:
    json.dump(time_taken, outtime)

print(time_taken)
