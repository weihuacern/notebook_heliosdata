from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pymssql
import names
import random
import time

class mssqldbfakequery:

    def __init__(self, hostip, usrname, pwd, dbname):
        self.conn = pymssql.connect(hostip, usrname, pwd, dbname)
    
    def fakesql(self, tablename):
        colnames = ["firstname", "lastname", "birthdate", "gender", "country", "street", "city", "stateprovince", "latitude", "rd1", "rd2", "rd3"]
        selcol = ", ".join(set([colnames[random.randint(0,len(colnames)-1)] for i in range(10)]))
        cutopt = ["gender = 'male'", "gender = 'female'", "stateprovince = 'USA'", "gender = 'PA'"]
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
    mymssqldbfakequery = mssqldbfakequery("192.168.7.85", "SA", "Helios123", "WILFRED")

    while 1:
        mymssqldbfakequery.fakequerypii(1)
        time.sleep(random.gauss(10, 3.0))
