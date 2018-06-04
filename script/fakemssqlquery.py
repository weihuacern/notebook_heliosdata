from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pymssql
import pymysql
import names
import random
import time

class sqldbfakequery:

    def __init__(self, mode, hostip, usrname, pwd, dbname):
        self.mode = mode
        if self.mode == "mssql":
            self.conn = pymssql.connect(hostip, usrname, pwd, dbname)
        elif self.mode == "mysql":
            self.conn = pymysql.connect(host=hostip, user=usrname, password=pwd, db=dbname)
    
    def fakesql(self, tablename):
        if self.mode == "mssql":
            colnames = ["firstname", "lastname", "birthdate", "gender", "country", "street", "city", "stateprovince", "latitude", "rd1", "rd2", "rd3"]
            cutopt = ["gender = 'male'", "gender = 'female'", "stateprovince = 'USA'", "gender = 'PA'"]
        elif self.mode == "mssql":
            colnames = ["firstname", "lastname", "birthdate", "gender", "country", "street", "city", "stateprovince", "latitude", "rd1", "rd2", "rd3"]
            cutopt = ["gender = 'male'", "gender = 'female'", "stateprovince = 'USA'", "gender = 'PA'"]

        selcol = ", ".join(set([colnames[random.randint(0,len(colnames)-1)] for i in range(10)]))
        cutstr = " where " + cutopt[random.randint(0,len(cutopt)-1)]
        sqlstr = "select " + selcol + " from " + tablename + cutstr
        print(sqlstr)
        return sqlstr
    
    def fakequerypii(self, cnt):
        c = self.conn.cursor()
        entries = []
        for i in range(cnt):
            c.execute(self.fakesql("TBL_1"))
        return
    
if __name__ == "__main__":
    mysqldbfakequery = sqldbfakequery("mssql", "192.168.7.155", "SA", "Helios123", "WILFRED")
    #mysqldbfakequery = sqldbfakequery("mysql", "192.168.7.21", "root", "Helios123", "WILFRED")
    while 1:
        mysqldbfakequery.fakequerypii(1)
        time.sleep(abs(random.gauss(10, 3.0)))
        #time.sleep(random.gauss(2, 1.0))
