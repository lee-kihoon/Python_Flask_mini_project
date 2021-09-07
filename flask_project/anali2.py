import cx_Oracle
import matplotlib.pyplot as plt

def fig():
    con = cx_Oracle.connect(
    user="rlgns", password='dksehdxizhdiRl1', dsn='edudb_high')
    cur = con.cursor()

    try:
        sql = """
        select* from
        (select count(MNAME) as NM, DIR, avg(USTAR)
        from NMV
        WHERE DIR IS NOT NULL
        group by DIR
        ORDER BY NM DESC)
        where ROWNUM<=10
        """
#
        list_d = []  # 갯수
        list_c = []  # 감독
        list_a = []
        cur.execute(sql)
        for i in cur.fetchall():
            list_d.append(i[0])  # 영화갯수
            cur.execute(sql)


        for i in cur.fetchall():
            list_c.append(i[1])  # 감독
            cur.execute(sql)
        for i in cur.fetchall():
            list_a.append(i[2])

        plt.rcParams["figure.figsize"] = (14, 5)

        plt.bar(list_c, [3.6414285714285715,
                         3.1633333333333336,
                         0,
                         4.8203157894736846,
                         7.864761904761905,
                         8.24,
                         3.507283950617284,
                         3.8375675675675676,
                         6.026769230769231,
                         0])


        plt.savefig('static/assets/img/analy1.png')
    except Exception as e:
        print("no")

    finally:
    # resources closing
        plt.close('all')
        cur.close()
        con.close()
