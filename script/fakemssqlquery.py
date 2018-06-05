import re
import random
import time
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pymssql
import pymysql
import names

class sqldbfakequery:

    def __init__(self, mode, hostip, usrname, pwd, dbname):
        self.mode = mode
        self.hostip = hostip
        self.usrname = usrname
        self.pwd = pwd
        self.dbname = dbname
        if self.mode == "mssql":
            self.conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        elif self.mode == "mysql":
            self.conn = pymysql.connect(host=self.hostip, user=self.usrname, password=self.pwd, db=self.dbname)
    
    def fakesql(self, tablename, colnames, cutopt):
        selcol = ", ".join(set([colnames[random.randint(0, len(colnames)-1)] for i in range(3)]))
        if cutopt:
            cutstr = " where " + cutopt[random.randint(0, len(cutopt)-1)]
        else:
            cutstr = ""
        sqlstr = "select " + selcol + " from " + tablename + cutstr
        print(sqlstr)
        return sqlstr
 
    def parsesqlquery(self, sqlquery):
        #Aim, first, the column on where condition, second, get value in that where condition.
        #If none, return empty list
        if "where" not in sqlquery:
            return [],[]
        else:
            col_pattern_list = [
                "(?<=where )(.*?)(?=\>|\<|\=|between|like|in|is)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
                #"(?<=and )(.*?)(?=\>|\<|\=|between|like|in|is)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
                #"(?<=or )(.*?)(?=\>|\<|\=|between|like|in|is)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
            ]
            colnames = []
            for pattern in col_pattern_list:
                thiscolnames = [x.split(',') for x in re.findall(pattern, sqlquery)]
                for x in thiscolnames:
                    colnames += x
            colnames = [x.strip() for x in colnames if x]

            #FIXME, do we have a better way to write this?
            val_pattern_list = [
                "(?<=\>)(.*?)($)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
                "(?<=\<)(.*?)($)",
                "(?<=\=)(.*?)($)",
                #"(?<=and )(.*?)(?=\>|\<|\=|between|like|in|is)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
                #"(?<=or )(.*?)(?=\>|\<|\=|between|like|in|is)", # case 2, where a > a0 and/or b > b0, https://www.w3schools.com/sql/sql_where.asp
            ]
            values = []
            for pattern in val_pattern_list:
                thisvalue = [list(x) for x in re.findall(pattern, sqlquery)]
                for x in thisvalue:
                    values += x
            values = [x.strip().strip("'") for x in values if x]

        return colnames, values

    def fakequerypii(self, cnt):
        if self.mode == "mssql":
            conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        elif self.mode == "mysql":
            conn = pymysql.connect(host=self.hostip, user=self.usrname, password=self.pwd, db=self.dbname)

        c = conn.cursor()
        tabnames = ["pii_2nd", "pii_3rd", "pii_4th"]
        sqlparas = {"pii_2nd": (["firstname", "lastname", "gender", "tab2col1", "tab2col2"], ["gender = 'male'", "gender = 'female'"]), "pii_3rd": (["phonenumber", "email", "tab3col1", "tab3col2"], []), "pii_4th": (["country", "city", "stateprovince", "tab4col1", "tab4col2"], ["country = 'CHN'", "country = 'USA'"])}
        for i in range(cnt):
            thistabstr = tabnames[random.randint(0, len(tabnames)-1)]
            thissqlquery = self.fakesql(thistabstr, sqlparas[thistabstr][0], sqlparas[thistabstr][1])
            #print(self.parsesqlquery(thissqlquery))
            c.execute(thissqlquery)
            time.sleep(abs(random.gauss(1, 0.3)))
        conn.close()
        return
    
if __name__ == "__main__":
    mysqldbfakequery = sqldbfakequery("mssql", "192.168.7.155", "SA", "Helios123", "huaPIITest")
    #mysqldbfakequery = sqldbfakequery("mysql", "192.168.7.21", "root", "Helios123", "huaPIITest")
    while 1:
        mysqldbfakequery.fakequerypii(random.randint(1, 10))
        time.sleep(abs(random.gauss(10, 3.0)))
        #time.sleep(abs(random.gauss(1, 0.3)))
