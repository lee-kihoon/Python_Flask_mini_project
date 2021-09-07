# import
from flask import Flask, render_template, request, redirect, url_for
import cx_Oracle
import time

import naver_movie
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import os
import datetime
import cx_Oracle
import anali1 as fig
import anali2 as fig2
##


# matplot 폰트 설정
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
#

##
cx_Oracle.init_oracle_client(config_dir=r"C:\dev\OracleWallet\Wallet_edudb")

app = Flask(__name__)


@app.route('/')
def home_to_index():
    return render_template("index.html")


@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/naver_movie_name/')
def naver_movie_name():
    return render_template("naver_movie_name.html")


@app.route('/naver_movie_star/')
def naver_movie_star():
    return render_template("naver_movie_star.html")


@app.route('/naver_movie_story/')
def naver_movie_story():
    return render_template("naver_movie_story.html")


@app.route('/naver_movie_dir/')
def naver_movie_dir():
    return render_template("naver_movie_dir.html")


@app.route('/naver_movie_year/')
def naver_movie_year():
    return render_template("naver_movie_year.html")


###
@app.route("/name/", methods=['POST', 'GET'])
# 네이버 크롤링 DB에서 영화 이름명으로 조회
def name():
    try:
        con = cx_Oracle.connect(
            user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()

        res = request.form["res"]

        sql_count = f"""
            select count(distinct MNAME)
            from NMV
            where mname like \'%{res}%\'
            """

        sql = f"""
            select distinct *
            from NMV
            where mname like \'%{res}%\'
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.execute(sql_count)
        count_rows = cur.fetchall()
    #
    except Exception as e:
        print("no")

    finally:
        # resources closing
        cur.close()
        con.close()

    return render_template("naver_movie_name_crawling.html", res=rows, count_rows=count_rows)


@app.route("/star/", methods=['POST', 'GET'])
# 네이버 크롤링 DB에서 별점으로 조회
def star():
    try:
        con = cx_Oracle.connect(
            user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()

        res = request.form["res"]

        sql = f"""
            select distinct *
            from NMV
            where USTAR >= {res}
            order by USTAR
            """

        sql_count = f"""
            select count(distinct MNAME)
            from NMV
            where USTAR >= {res}
            order by USTAR
            """

        cur.execute(sql)
        rows = cur.fetchall()

        cur.execute(sql_count)
        count_rows = cur.fetchall()
    #
    except Exception as e:
        print("no")

    finally:
        # resources closing
        cur.close()
        con.close()

    return render_template("naver_movie_star_crawling.html", res=rows, count_rows=count_rows)


@app.route("/story/", methods=['POST', 'GET'])
# 네이버 크롤링 DB에서 영화 줄거리 키워드로 조회
def story():
    try:
        con = cx_Oracle.connect(
            user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()

        res = request.form["res"]

        sql_count = f"""
            select count(distinct MNAME)
            from NMV
            where story like \'%{res}%\'
            """

        sql = f"""
            select distinct *
            from NMV
            where story like \'%{res}%\'
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.execute(sql_count)
        count_rows = cur.fetchall()
    #
    except Exception as e:
        print("no")

    finally:
        # resources closing
        cur.close()
        con.close()

    return render_template("naver_movie_story_crawling.html", res=rows, count_rows=count_rows)


@app.route("/dir/", methods=['POST', 'GET'])
# 네이버 크롤링 DB에서 영화 감독명으로 조회
def dir():
    try:
        con = cx_Oracle.connect(
            user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()

        res = request.form["res"]

        sql_count = f"""
            select count(distinct MNAME)
            from NMV
            where dir like \'%{res}%\'
            """

        sql = f"""
            select distinct *
            from NMV
            where dir like \'%{res}%\'
            """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.execute(sql_count)
        count_rows = cur.fetchall()
    #
    except Exception as e:
        print("no")

    finally:
        # resources closing
        cur.close()
        con.close()

    return render_template("naver_movie_dir_crawling.html", res=rows, count_rows=count_rows)


@app.route("/year/", methods=['POST', 'GET'])
# 네이버 크롤링 DB에서 연로 조회
def year():
    try:
        con = cx_Oracle.connect(
            user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()

        res = int(request.form["res"])

        sql = f"""
            select distinct *
            from NMV
            where year = {res}
            """

        sql_count = f"""
            select count(distinct MNAME)
            from NMV
            where year = {res}
            """

        cur.execute(sql)
        rows = cur.fetchall()

        cur.execute(sql_count)
        count_rows = cur.fetchall()
    #
    except Exception as e:
        print("no")

    finally:
        # resources closing
        cur.close()
        con.close()

    return render_template("naver_movie_year_crawling.html", res=rows, count_rows=count_rows)


@app.route("/movie_review/")
def movie_review():
    return render_template("movie_review.html")


@app.route("/mv_sel/", methods=['POST', 'GET'])
def mv_sel():
    res = request.form["mv_name"]
    ret, hr = naver_movie.naverMovie(res)
    hl = '<input type="hidden" name="hh" value="' + hr + '">'
    return render_template("movie_review_crawling.html",  ret=hl, ret2=ret)


@app.route("/mv_select/", methods=['POST', 'GET'])
def mv_select():
    res = request.form["mv_select"]
    ht = request.form["hh"]
    res = str(res)
    movie_Name, userStar, story, user_review = naver_movie.searchC(res, ht)
    return render_template("movie_review_crwaling2.html", movie_Name=movie_Name, userStar=userStar, story=story, user_review=user_review)


@app.route('/analysis_movie_data/')
def analysis_movie_data():
    return render_template("analysis_movie_data.html")

@app.route('/analysis1/')
def analysis1():
    con = cx_Oracle.connect(
    user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
    cur = con.cursor()

    fig.fig()
    fig2.fig()

    cur.close()
    con.close()

    return render_template("analysis1.html")


@app.route('/analysis2/')
def analysis2():
    try:
        con = cx_Oracle.connect(
        user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
        cur = con.cursor()


        #별점 그래프
        list_s=[]
        for i in range(0,10):
            sql=f"""
            select COUNT(distinct MNAME)
            from NMV
            WHERE USTAR>{i} and USTAR<={i+1}
            """
            cur.execute(sql)
            list_s.append(cur.fetchall()[0][0])

        plt.rcParams["figure.figsize"] = (9,5)
        plot1=plt.plot([1,2,3,4,5,6,7,8,9,10],list_s)
        plt.savefig('static/assets/img/analy2.png')
        plt.cla()
#

    except Exception as e:
        print("no")

    finally:
    # resources closing
        cur.close()
        con.close()
    return render_template("analysis2.html")

@app.route('/analysis3/')
def analysis3():
    return render_template("analysis3.html")


@app.route('/analysis4/')
def analysis4():
    return render_template("analysis4.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
