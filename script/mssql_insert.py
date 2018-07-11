from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pymssql
import pymysql
import names
import random
import time
import uuid

#firstname, lastname, phone number, email
class fakepiientry:

    def __init__(self):
        self.domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
        self.letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.genders = ["male", "female"]
        self.countries = ["CHN", "USA", "SOV", "JAP", "GER"]
        self.cities = ["New York", "Los Angeles", "San Francisco", "Boston", "Riverside", "Seattle"]
        self.stateprovinces = ["CA", "NY", "WA", "IL", "IN"]
        
    def generate_phonenumber(self):
        first = str(random.randint(100,999))
        second = str(random.randint(1,888)).zfill(3)
        last = (str(random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last = (str(random.randint(1,9998)).zfill(4))
        return ('{}-{}-{}'.format(first,second, last))
    
    def generate_random_email(self):
        namelen = random.randint(10,20)
        one_name = str(''.join([self.letters[random.randint(0,len(self.letters)-1)] for i in range(namelen)]))         
        one_domain = str(self.domains[random.randint(0, len(self.domains)-1)])
        return(one_name  + "@" + one_domain)

    def generate_random_gender(self):
        return self.genders[random.randint(0, len(self.genders)-1)]
        
    def generate_random_country(self):
        return self.countries[random.randint(0, len(self.countries)-1)]
    
    def generate_random_city(self):
        return self.cities[random.randint(0, len(self.cities)-1)]
    
    def generate_random_stateprovince(self):
        return self.stateprovinces[random.randint(0, len(self.stateprovinces)-1)]

    def pii_2nd_entry_gen(self, uid):
        return (uid, names.get_first_name(), names.get_last_name(), self.generate_random_gender(), random.randint(0, 10), random.randint(10, 100))
    
    def pii_3rd_entry_gen(self, uid):
        return (uid, self.generate_phonenumber(), self.generate_random_email(), random.randint(0, 10), random.randint(10, 100))

    def pii_4th_entry_gen(self, uid):
        return (uid, self.generate_random_country(), self.generate_random_city(), self.generate_random_stateprovince(), random.randint(0, 10), random.randint(10, 100))
    

class mssqldbprocess:

    def __init__(self, hostip, usrname, pwd, dbname):
        self.hostip = hostip
        self.usrname = usrname
        self.pwd = pwd
        self.dbname = dbname
    
    def createpii(self):
        conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        c1 = conn.cursor()
        # table 1 for uid
        c1.execute("IF OBJECT_ID('pii_1st', 'U') IS NOT NULL DROP TABLE pii_1st")
        c1.execute("CREATE TABLE pii_1st (uid INT NOT NULL, tab1col1 INT, tab1col2 INT)")
        c1.execute("IF OBJECT_ID('pii_2nd', 'U') IS NOT NULL DROP TABLE pii_2nd")
        c1.execute("CREATE TABLE pii_2nd (uid INT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100), gender VARCHAR(100), tab2col1 INT, tab2col2 INT)")
        c1.execute("IF OBJECT_ID('pii_3rd', 'U') IS NOT NULL DROP TABLE pii_3rd")
        c1.execute("CREATE TABLE pii_3rd (uid INT NOT NULL, phonenumber VARCHAR(100), email VARCHAR(100), tab3col1 INT, tab3col2 INT)")
        c1.execute("IF OBJECT_ID('pii_4th', 'U') IS NOT NULL DROP TABLE pii_4th")
        c1.execute("CREATE TABLE pii_4th (uid INT NOT NULL, country VARCHAR(100), city VARCHAR(100), stateprovince VARCHAR(100), tab4col1 INT, tab4col2 INT)")
        conn.commit()
        conn.close()
        return 
        
    def fillpii(self, uid_beg, uid_end):
        conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        
        c = conn.cursor()
        entries_1st = []
        entries_2nd = []
        entries_3rd = []
        entries_4th = []
        
        for i in range(uid_beg, uid_end):
            #print(i)
            entries_1st.append((i, random.randint(0, 10), random.randint(10, 100)))
            entries_2nd.append(myfakepiientry.pii_2nd_entry_gen(i))
            entries_3rd.append(myfakepiientry.pii_3rd_entry_gen(i))
            entries_4th.append(myfakepiientry.pii_4th_entry_gen(i))            
        
        c.executemany("INSERT INTO pii_1st VALUES (%d, %d, %d)", entries_1st)
        c.executemany("INSERT INTO pii_2nd VALUES (%d, %s, %s, %s, %d, %d)", entries_2nd)
        c.executemany("INSERT INTO pii_3rd VALUES (%d, %s, %s, %d, %d)", entries_3rd)
        c.executemany("INSERT INTO pii_4th VALUES (%d, %s, %s, %s, %d, %d)", entries_4th)
        
        conn.commit()
        conn.close()
        return

if __name__ == '__main__':

    mymssqldbprocess = mssqldbprocess("192.168.7.73", "SA", "Helios12$", "huaPIITest")
    mymssqldbprocess.createpii()
    batch_size = 50
    for i in range(0, 2):
        mymssqldbprocess.fillpii(i*batch_size , (i+1)*batch_size)
