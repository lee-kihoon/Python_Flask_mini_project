# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import pandas as pd
# import time
# import cx_Oracle
# cx_Oracle.init_oracle_client(config_dir=r"C:\dev\OracleWallet\Wallet_edudb")

templist = []  # 검색 HREF
# conn=cx_Oracle.connect('system','oracle','localhost:1521',encoding='UTF-8',nencoding='UTF-8')
# cur = conn.cursor()
# sql=f"insert into BYCICLE VALUES({asdasdasdasdasd},2,3,4,5)"
# sql="select * from BYCICLE"
# cur.execute(sql)
# 선택 자손번호 위에서 부터 1
#최초1회만 실행##################
#cur.execute('commit')
driv = webdriver.Chrome(executable_path='chromedriver.exe')
# conn=cx_Oracle.connect('system','oracle','localhost:1521',encoding='UTF-8',nencoding='UTF-8')

con = cx_Oracle.connect(
    user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
cur = con.cursor()
cur.execute('commit')
# cur.close()
# con.close()
# ID1=1
# for i in range(14010,14012):
#     try:
#         url="https://movie.naver.com/movie/bi/mi/basic.nhn?code="+str(i)
#         driv.get(url)
#         time.sleep(1)
#         html = driv.page_source
#     except:
#         print("??????????????????")
#         i+=1
#         url="https://movie.naver.com/movie/bi/mi/basic.nhn?code="+str(i+1)
#         driv.get(url)
#     html = driv.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     mname= soup.select("#content > div.article > div.mv_info_area >div.mv_info > h3 > a:nth-child(1)")
#     mstar= soup.select("div.mv_info > div.main_score > div.score.score_left > div.star_score")
#     userexp=soup.select("#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_result > ul > li > div.score_reple > p")
#     story= soup.select("p.con_tx")
#     #새로 추가된부분
#     genre = soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl dd > p > span:nth-child(1)")
#     contry= soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl dd > p > span:nth-child(2)")
#     runing= soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl dd > p > span:nth-child(3)")
#     dircter=soup.select("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p")
#     #감독
#     try:
#         dircter=dircter[0].getText().strip()
#     except:
#         dircter="NULL"
#         #러닝타임
#     try:
#         runing=runing[0].getText().strip()[:-1]
#         #장르
#     try:
#         genre=genre[0].getText().strip()
#     except:
#         genre = "NULL"
#         #제작국가
#     try:
#         contry=contry[0].getText().strip()[0:2]
#     except:
#         contry="NULL"
#
#     try:
#         movie_Name=mname[0].getText()
#     except:
#         movie_Name="NULL"
#     try:
#         userStar=mstar[0].getText().strip()
#     except:
#         userStar="NULL"
#     try:
#         stroy1=story[0].getText()
#         stroy1=stroy1.replace("'","")
#     except:
#         stroy1="NULL"
#     try:
#         uxlist2=[]
#         for i in userexp:
#             uxlist2.append(i.getText().strip()+"<br>")
#     except:
#         uxlist2="NULL"
#     sql=f"insert into NMV VALUES('{movie_Name}','{userStar}','{stroy1}','{dircter}','{genre}','{runing}','{contry}')"
#     #제목,별점,줄거리,감독,장르,러닝타임,제작국가
#     cur.execute(sql)
##################
###테스트##########
##################
#55001 ~ 61001
for i in range(201750,210001): #10001~20001
    try:
        url="https://movie.naver.com/movie/bi/mi/basic.nhn?code="+str(i)
        driv.get(url)
        html = driv.page_source
    except:
        print("영화코드 에러")
        i+=1
        url="https://movie.naver.com/movie/bi/mi/basic.nhn?code="+str(i+1)
        driv.get(url)
    html = driv.page_source
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
    try:
        uxlist2=[]
        for i in userexp:
            uxlist2.append(i.getText().strip()+"<br>")
    except:
        uxlist2="NULL"

    #제목,별점,줄거리,감독,연도,등급
    try:
        sql=f"insert into NMV VALUES('{movie_Name}','{userStar}','{stroy1}','{dircter}','{year_info}','{grade}')"
        cur.execute(sql)
    except:
        i+=1
    cur.execute('commit') #다 하면 커밋, 중간에 멈춰도 커밋
