#!/usr/bin/python3.6
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import cgi
import cgitb
import json
import random

from utils import get_query, execute_query, fakesql

ms_dbname = 'hr_pii'
ms_table = 'employee'



with open('employees.json', 'r') as file:
    string = file.read()
employee_list = json.loads(string)

entry = random.choice(employee_list)
ssn = entry['ssn']
query = fakesql('employee', ['ssn', 'blood_group', 'name', 'sex', 'mail', 'phone', 'race', 'ethnic', 'religion', 'trade_union', 'health', 'sexual', 'politics', 'birthdate'], ["sex = 'M'", "sex = 'F'"])
#query = 'SELECT * FROM employee WHERE ssn = %s;' % repr(ssn)

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>EMPLOYEE INFORMATION CHECK</title>')
print('</head>')
print('<body>')
print('ssn: ' + ssn + '<br />')
print('Query results:<br />')
execute_query('mssql', 'hr_pii', query)
print('</body>')
print('</html>')
