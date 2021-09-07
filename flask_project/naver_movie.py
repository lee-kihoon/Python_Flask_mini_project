from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def naverMovie(movieName):
    driv = webdriver.Chrome(executable_path='chromedriver.exe')
    templist2 = []
    url = "https://movie.naver.com/"
    driv.get(url)
    elem = driv.find_element_by_id("ipt_tx_srch")
    #영화이름 입력 받기 or db 가져오기#####
    elem.send_keys(movieName)  # 영화 이름 타이핑
    elem.send_keys(Keys.RETURN)  # 엔터입력
    html2 = driv.page_source  # 이동한 페이지 소스받아오기
    soup2 = BeautifulSoup(html2, "html.parser")  # soup2에 저장
    # search1=soup2.select('#old_content > ul.search_list_1> li > dl > dt > a')
    search1=soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a, ul:nth-child(4) dd.etc')
    search2=soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a')
    search2
    # 검색 리스트 불러오기
    hreflist=[]
    for i in search2:
        i.attrs['href']
        hreflist.append("https://movie.naver.com"+i.attrs['href'])
    tempstr3=movieName
    #
    len1=int(len(search1)/3)
    templist2=[]
    cnt=0
    cntin=0
    for i in search1:
        cnt+=1
        if cnt%3==1:
            cntin+=1
            templist2.append(str(cntin)+"번 : "+i.getText())
        else:templist2.append(i.getText())
    a=[]
    cnt=1
    for j in range(0,len(templist2),3):
        a.append(templist2[j:j+3])
        cnt+=1
    return a, tempstr3


def searchC(choice, dv):
    hreflist = []
    uxlist2=[]

    url="https://movie.naver.com/movie/search/result.nhn?query="+dv
    driv = webdriver.Chrome(executable_path='chromedriver.exe')
    html2 = driv.get(url)
    html2 = driv.page_source
    soup2 = BeautifulSoup(html2, "html.parser")
    search2 = soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a')
    driv.find_element_by_css_selector(
        "ul.search_list_1 > li:nth-child(" + choice + ") > dl > dt > a").click()
    # 셀레니움 끝

    html = driv.page_source
    soup = BeautifulSoup(html, 'html.parser')
    mname = soup.select(
        "#content > div.article > div.mv_info_area >div.mv_info > h3 > a:nth-child(1)")
    mstar = soup.select(
        "div.mv_info > div.main_score > div.score.score_left > div.star_score")
    userexp = soup.select(
        "#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_result > ul > li > div.score_reple > p")
    story = soup.select("p.con_tx")
    movie_Name = mname[0].getText()

    try:
        userStar="네티즌 별점 :"+mstar[0].getText().strip()
    except:
        userStar="네티즌 별점이 없습니다."
    try:
        stroy1=story[0].getText()
    except:
        stroy1="줄거리가 없습니다."
    try:
        for i in userexp:
            uxlist2.append(i.getText().strip())
    except:
        uxlist2="유저 리뷰글이 없습니다."
    # 영화 이름, 유저평점, 줄거리, 유저리뷰, 페이지링크

    soup = BeautifulSoup(html, 'html.parser')
    mname= soup.select("#content > div.article > div.mv_info_area >div.mv_info > h3 > a:nth-child(1)")
    mstar= soup.select("div.mv_info > div.main_score > div.score.score_left > div.star_score")
    userexp=soup.select("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_result > ul > li > div.score_reple > p")
    story= soup.select("p.con_tx")
    #새로 추가된부분
    dircter=soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dt.step2+ dd a")
    year_info=soup.select("strong.h_movie2")
    grade= soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dt.step4 + dd a")
    #감독
    try:
        dircter=dircter[0].getText().strip()
    except:
        dircter="NULL"
    #연도
    try:
        year_info=int(year_info[0].getText().strip()[-4:])
    except:
        year_info=1000
    #등급
    try:
        grade=grade[0].getText().strip()
    except:
        grade="NULL"
    try:
        movie_Name=mname[0].getText().replace("'","")
    except:
        movie_Name="NULL"
        #별점
    try:
        userStar=float(mstar[0].getText().strip())
    except:
        userStar=1000
        #줄거리
    try:
        stroy1=story[0].getText()
        stroy1=stroy1.replace("'","")
    except:
        stroy1="NULL"
        #유저리뷰

    #제목,별점,줄거리,감독,연도,등급
    try:
        import cx_Oracle
        con = cx_Oracle.connect(user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()
        sql=f"insert into NMV VALUES('{movie_Name}','{userStar}','{stroy1}','{dircter}','{year_info}','{grade}')"
        cur.execute(sql)
        cur.execute("update NMV set year = null where year = 1000")
        cur.execute("update NMV set USTAR = null where ustar = 1000")
        cur.execute("commit")
    except:
        pass
    finally:
        print('hi')
    return movie_Name, userStar, stroy1, uxlist2


# def naverMovie(movieName, drv):
#     lst = []
#     driv = drv
#     url="https://movie.naver.com/"
#     driv.get(url)
#     elem = driv.find_element_by_id("ipt_tx_srch")
#     #영화이름 입력 받기 or db 가져오기#####
#     elem.send_keys(movieName) #영화 이름 타이핑
#     elem.send_keys(Keys.RETURN)  #엔터입력
#     html2=driv.page_source #이동한 페이지 소스받아오기
#     soup2 = BeautifulSoup(html2,"html.parser") #soup2에 저장
#     # search1=soup2.select('#old_content > ul.search_list_1> li > dl > dt > a')
#     search1=soup2.select('#old_content > ul:nth-child(4) > li > dl > dt > a, ul:nth-child(4) dd.etc')# 검색 리스트 불러오기
#     type(search1)
#     for i in search1:
#         lst.append(i.getText())
#
#     return lst
