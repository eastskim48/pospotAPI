from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from crawling.models import Taglist

def get_tag_nums(tag):
    options=Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
    driver.set_page_load_timeout(30)
    driver.get('https://www.instagram.com/tags/'+tag)
    time.sleep(1) #안전성을 위해서 넣어야됨
    tag_count = driver.find_elements_by_class_name('g47SY')[0].text.replace(',', '')
    imgs = driver.find_elements_by_tag_name('img')
    if Taglist.objects.filter(tag_name=tag).count()==0:
        t=Taglist()
        t.tag_name=tag
    else:
        t=Taglist.objects.get(tag_name=tag)
    t.num_tag=tag_count
    imglist="["
    for img in imgs:
        imglist+='"'+img.get_attribute("src")+'",'
    imglist=imglist[:-1]
    imglist+="]"
    t.imgurls=imglist
    t.save()
    driver.quit()
    return
