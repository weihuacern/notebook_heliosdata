#!/usr/bin/python3.6
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import cgi
import cgitb
import json
import random

from utils import get_query, execute_query, fakesql

with open('employees.json', 'r') as file:
    string = file.read()
employee_list = json.loads(string)

entry = random.choice(employee_list)
ssn = entry['ssn']
query = fakesql('sales', ['ssn', 'name', 'customer_ssn', 'customer_name'], [])
#query = 'SELECT * FROM sales WHERE ssn = %s;' % repr(ssn)

print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>SALES INFORMATION CHECK</title>')
print('</head>')
print('<body>')
print('salesman ssn: ' + ssn + '<br />')
print('Query results:<br />')
execute_query('mysql', 'sales_info', query)
print('</body>')
print('</html>')
