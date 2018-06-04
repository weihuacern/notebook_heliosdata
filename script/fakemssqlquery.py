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
        self.hostip = hostip
        self.usrname = usrname
        self.pwd = pwd
        self.dbname = dbname
        if self.mode == "mssql":
            self.conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        elif self.mode == "mysql":
            self.conn = pymysql.connect(host=self.hostip, user=self.usrname, password=self.pwd, db=self.dbname)
    
    def fakesql(self, tablename, colnames, cutopt):
        #if self.mode == "mssql":
        #    colnames = ["firstname", "lastname", "birthdate", "gender", "country", "street", "city", "stateprovince", "latitude", "rd1", "rd2", "rd3"]
        #    cutopt = ["gender = 'male'", "gender = 'female'", "stateprovince = 'USA'", "gender = 'PA'"]
        #elif self.mode == "mysql":
        #    colnames = ["firstname", "lastname", "birthdate", "gender", "country", "street", "city", "stateprovince", "latitude", "rd1", "rd2", "rd3"]
        #    cutopt = ["gender = 'male'", "gender = 'female'", "stateprovince = 'USA'", "gender = 'PA'"]

        selcol = ", ".join(set([colnames[random.randint(0, len(colnames)-1)] for i in range(3)]))
        if cutopt:
            cutstr = " where " + cutopt[random.randint(0, len(cutopt)-1)]
        else:
            cutstr = ""
        sqlstr = "select " + selcol + " from " + tablename + cutstr
        print(sqlstr)
        return sqlstr
    
    def fakequerypii(self, cnt):
        c = self.conn.cursor()
        tabnames = ["pii_2nd", "pii_3rd", "pii_4th"]
        sqlparas = {"pii_2nd": (["firstname", "lastname", "gender"], ["gender = 'male'", "gender = 'female'"]), "pii_3rd": (["phonenumber", "email"], []), "pii_4th": (["country", "city", "stateprovince"], ["country = 'CHN'", "country = 'USA'"])}
        for i in range(cnt):
            thistabstr = tabnames[random.randint(0, len(tabnames)-1)]
            #self.fakesql(thistabstr, sqlparas[thistabstr][0], sqlparas[thistabstr][1])
            c.execute(self.fakesql(thistabstr, sqlparas[thistabstr][0], sqlparas[thistabstr][1]))
        return
    
if __name__ == "__main__":
    mysqldbfakequery = sqldbfakequery("mssql", "192.168.7.155", "SA", "Helios123", "huaPIITest")
    #mysqldbfakequery = sqldbfakequery("mysql", "192.168.7.21", "root", "Helios123", "huaPIITest")
    while 1:
        mysqldbfakequery.fakequerypii(1)
        time.sleep(abs(random.gauss(10, 3.0)))
        #time.sleep(abs(random.gauss(1, 0.3)))
