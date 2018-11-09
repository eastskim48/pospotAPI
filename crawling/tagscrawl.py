#-*-coding: utf-8
import requests
import json
from crawling.models import Taglist
titles=[]
URL = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=tIdYKCsxdgAhM0wG9UJDpooJzQOCYOUkR0AhRKPuF7wxYLmQ82Rf7C7oDm3PreMahRMtJURA5JHX5XB8SqFTRQ%3D%3D&numOfRows=10000&contentTypeId=12&arrange=A&MobileOS=ETC&MobileApp=AppTest&_type=json&areaCode="

for c in range(1,9):
    res = requests.get(URL+str(c))
    data = json.loads(res.text)
    items=data['response']['body']['items']['item']
    for i in items:
        if '(' in i['title']:
            titles.append(i['title'].split('(')[0])
        else:
            titles.append(i['title'])

#print(len(titles))
for t in titles:
    if Taglist.objects.filter(tag_name=tag).count()==0:
        tag=Taglist()
        tag.tag_name=t
        tag.save()




