import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import csv

with open('straipsniu_nuorodos.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

array = []

PATH = r"C:\Users\Pc\PycharmProjects\scraping\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.15min.lt/tema/svietimas')

time.sleep(5)

for k in range(1000):

    time.sleep(5)

    try:

        elem = driver.find_element_by_tag_name("body")
        no_of_pagedowns = 15

        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            no_of_pagedowns-=1

        time.sleep(3)

        post_elems = driver.find_elements_by_tag_name("h3")

        for post in post_elems:
            links = driver.find_element_by_link_text(post.text)
            array.append(links.get_attribute('href'))

    except:
        pass

    time.sleep(3)

    show_more_button = driver.find_element_by_link_text("Rodyti senesnius straipsnius")
    show_more_button.click()

df = pd.DataFrame(array)
df.to_csv('straipsniu_nuorodos.csv')
