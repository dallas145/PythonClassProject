import requests
import math
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import tkinter as tk
#end import

def crawl(sv):#爬資料
    url = "https://www.cwb.gov.tw/V8/C/W/week.html"
    browser = webdriver.Chrome()#開啟瀏覽器
    browser.get(url)#到目標url
    selectCity = Select(browser.find_element("a","span"))
    selectCity.select_by_value("Taiwan")
    selectItem = Select(browser.find_element("id","Item"))
    selectItem.select_by_value(sv)
    #選擇需要選項
    time.sleep(0.5)
    #等待載入正確表單

    html_source = browser.page_source
    sp = BeautifulSoup(html_source,"lxml")

    #標題
    title = sp.find(id="SubTitle").text
    dtitle = sp.find(class_="notes").text#這是單位
    titlelen = title.index(dtitle)
    #print(title[0:titlelen])

    #觀測站名
    points=[]
    rows = sp.select("tbody tr")
    for row in rows:
        cols = row.find(scope="row").string
        points.append(cols)
    #for i in range(25):
    #    print(points[i])