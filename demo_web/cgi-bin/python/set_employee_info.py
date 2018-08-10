#!/usr/bin/python3.6

import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import cgi
import cgitb

from utils import insert_entry


ms_dbname = "hr_pii"
ms_table = 'employee'

cgitb.enable()
form = cgi.FieldStorage()
eid = form.getvalue('eid')
name = form.getvalue('name')
phone = form.getvalue('phone')
value = "('" + eid + "', '" + name + "', '" + phone + "');"

print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>INSERT EMPLOYEE INFO</title>')
print('</head>')
print('<body>')
print('eid: ' + eid + '<br />')
print("Insert results:<br />")
insert_entry('mssql', ms_dbname, ms_table, value)
print('</body>')
print('</html>')
