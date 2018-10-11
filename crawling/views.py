from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
import time
# Create your views here.

def tagnum(request,pk):
    driver = webdriver.Chrome(os.getcwd())
    driver.get('https://www.instagram.com/tags/'+pk)
    time.sleep(1) #안전성을 위해서 넣어야됨
    rst = driver.find_elements_by_class_name('g47SY')[0]
    driver.quit()
    return HttpResponse(rst.text)

def pictures(requests):
    return HttpResponse("준비중입니다")
