from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
# Create your views here.
options=Options()
options.add_argument('--headless')
driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
driver.set_page_load_timeout(10)
driver.get('https://www.instagram.com/tags/paris')
time.sleep(1) #안전성을 위해서 넣어야됨
rst = driver.find_elements_by_class_name('g47SY')[0]
print(rst.text.replace(',', ''))
driver.quit()

