from driverfile import *
import time
import pandas as pd

dataframe = pd.DataFrame(columns=["Product Name", "Price", "Product Link"])


def wait(t):
    time.sleep(t)


def amazon():
    global dataframe
    driver.get('https://amazon.in')
    driver.maximize_window()
    wait(5)
    search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
    search.send_keys('Cashew')
    wait(2)
    driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
    wait(10)
    i = 1
    while i < 8:
        product_name_list = []
        for item in driver.find_elements_by_css_selector('span.a-size-base-plus.a-color-base.a-text-normal'):
            product_name_list.append(item.text)

        price_list = []
        for item in driver.find_elements_by_css_selector('a.a-size-base.a-link-normal.s-no-hover.a-text-normal'):
            price_list.append(item.text)

        link_list = []
        for item in driver.find_elements_by_css_selector('a.a-link-normal.a-text-normal'):
            link_list.append(item.get_attribute("href"))
        mylist = zip(product_name_list, price_list, link_list)
        for product, price, link in mylist:
            dataframe = dataframe.append({
                'Product Name': product,
                'Price': price,
                'Product Link': link,
            }, ignore_index=True)

        driver.find_element_by_css_selector('li.a-last').click()
        i += 1
        wait(10)

    dataframe.to_csv("Cashew_Products_Prices_Of_Amazon.csv", index=False)
