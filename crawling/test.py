from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
import time
import os
# Create your views here.
driver = webdriver.Chrome(os.getcwd())
driver.set_page_load_timeout(my_timeout_secs)
driver.get('https://www.instagram.com/tags/paris')
time.sleep(1) #안전성을 위해서 넣어야됨
rst = driver.find_elements_by_class_name('g47SY')[0]
driver.quit()
