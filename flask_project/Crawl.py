from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

templist=[]# 검색 HREF
templist2=[]

 # 선택 자손번호 위에서 부터 1
#최초1회만 실행##################
driv=webdriver.Chrome(executable_path='chromedriver.exe')
type(driv)

#요청시 여기서 부터 반복#
def naverMovie(movieName):
    lst = []
    url="https://movie.naver.com/"
    driv.get(url)
    elem = driv.find_element_by_id("ipt_tx_srch")
    #영화이름 입력 받기 or db 가져오기#####
    elem.send_keys(movieName) #영화 이름 타이핑
    elem.send_keys(Keys.RETURN)  #엔터입력
    html2=driv.page_source #이동한 페이지 소스받아오기
    soup2 = BeautifulSoup(html2,"html.parser") #soup2에 저장
    # search1=soup2.select('#old_content > ul.search_list_1> li > dl > dt > a')
    search1=soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a, ul:nth-child(4) dd.etc')# 검색 리스트 불러오기
    type(search1)
    for i in search1:
        lst.append(i.getText())

    return lst

        # print(i.getText())
        #위에서부터 1 ,2 ,3
        #검색에서 리스트 뿌려주기


##### 2번쨰
def searchC(choice):
    html2=driv.page_source
    soup2 = BeautifulSoup(html2,"html.parser")
    search2=soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a')
    driv.find_element_by_css_selector("#old_content > ul.search_list_1 > li:nth-child("+str(choice)+") > dl > dt > a").click()
    #셀레니움 끝
    html=driv.page_source
    soup = BeautifulSoup(html, 'html.parser')
    mname= soup.select("#content > div.article > div.mv_info_area >div.mv_info > h3 > a:nth-child(1)")
    mstar= soup.select("div.mv_info > div.main_score > div.score.score_left > div.star_score")
    userexp=soup.select("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_result > ul > li > div.score_reple > p")
    story= soup.select("p.con_tx")
    movie_Name=mname[0].getText()
    userStar="네티즌 별점 :"+mstar[0].getText().strip()
    stroy1=story[0].getText()
    uxlist2=[]
    for i in userexp:
        uxlist2.append(i.getText().strip()+"\n")
    hreflist=[]
    for i in search2:
        hreflist.append("https://movie.naver.com"+i.attrs['href'])
    herflist=hreflist[choice-1]
    return movie_Name, userStar, stroy1, uxlist2, herflist #영화 이름, 유저평점, 줄거리, 유저리뷰, 페이지링크

naverMovie("아이언맨")
searchC(4)
