from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import csv
import urllib.request
from bs4 import BeautifulSoup
import numpy as np

with open('straipsniu_nuorodos.csv', newline='') as csvfile:
    data1 = list(csv.reader(csvfile))

data = [''.join(ele) for ele in data1]
i = 1
test = data[:1000]

array = []

for element in test:

    array.append(i)

    html = urllib.request.urlopen(element)
    htmlParse = BeautifulSoup(html, 'html.parser')
    for paragraph in htmlParse.find_all("p"):
        array.append(paragraph.get_text())

    i=i+1

df = pd.DataFrame(array)
df.to_csv('data10.csv', encoding='utf_8_sig')
