from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

alist=[]
list_c 
for i in list_c:
    driv.get("https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=3&ie=utf8&query="+i+" 감독")
    html=driv.page_source
    soup=BeautifulSoup(html,"html.parser")
    award=soup.select("#people_info_z > div > div.api_cs_wrap > div.cont_noline > div > dl > dt:contains('수상')+ dd")
    for j in award:
        alist.append([i+"감독 : "+j.getText()])
alist
