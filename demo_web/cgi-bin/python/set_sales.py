#!/usr/bin/python3.6

import random
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import json
import cgi
import cgitb

from utils import execute_query
SALES_LIST = ['ssn', 'name', 'customer_ssn', 'customer_name']
with open('employees.json', 'r') as file:
    string = file.read()
employee_list = json.loads(string)

columns = '('
values = '('
entry = random.choice(employee_list)
for key, value in entry.items():
    if key in SALES_LIST and value:
        columns = columns + key + ', '
        values = values + repr(value) + ', '

columns = columns[:-2] + ')'
values = values[:-2] + ')'

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>INSERT SALES INFO</title>')
print('</head>')
print('<body>')
print('salesperson: ' + str(entry['ssn']) + '<br />')

query = 'INSERT INTO sales ' + columns + ' VALUES ' + values + ';'
print(query + '<br />')

execute_query('mysql', 'sales_info', query)

query = 'INSERT INTO key_table VALUES (' + repr(entry['ssn']) + ') ON DUPLICATE KEY UPDATE ssn=ssn'

execute_query('mysql', 'sales_info', query)

print('</body>')
print('</html>')
