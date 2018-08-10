#!/usr/bin/python3.6
import sys
import cgi
import cgitb
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
import pymssql
import pymysql

def insert_entry_mysql(hostip, usrname, pwd, dbname, cid, contact, trade):
    conn = pymysql.connect(host=hostip, user=usrname, password=pwd, db=dbname)
    c = conn.cursor()
    try:
        print("insert: " + cid + "," + contact + "," + trade)
        val = "(" + cid + ", '" + contact + "', '" + trade + "');"
        c.execute("insert into customers values " + val)
        print("success")
    except:
        print("insert failed")
    conn.commit()
    conn.close()

my_ip = "192.168.8.74"
my_usrname = "root"
my_pwd = "Helios123"
my_port = 3306
my_dbname = "customers_info"

cgitb.enable()
form = cgi.FieldStorage()
cid = form.getvalue('cid')
contact= form.getvalue('contact')
trade = form.getvalue('trade')
print("Content-Type: text/html;charset=utf-8")

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<body>')
print("cid: " + cid)
print("Insert results: ")
insert_entry_mysql(my_ip, my_usrname, my_pwd, my_dbname, cid, contact, trade)
print('</body>')
print('</html>')
