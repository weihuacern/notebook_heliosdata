#!/usr/bin/python3.6

import random
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import json
import cgi
import cgitb

from utils import execute_query

with open('customers.json', 'r') as file:
    string = file.read()
customer_list = json.loads(string)

columns = '('
values = '('
entry = random.choice(customer_list)
for key, value in entry.items():
    if value:
        columns = columns + key + ', '
        values = values + repr(value) + ', '

columns = columns[:-2] + ')'
values = values[:-2] + ')'

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>INSERT EMPLOYEE INFO</title>')
print('</head>')
print('<body>')
print('customer: ' + str(entry) + '<br />')

query = 'INSERT INTO customer ' + columns + ' VALUES ' + values + ';'

execute_query('mysql', 'customers_info', query)


query = 'INSERT INTO key_table VALUES (' + repr(entry['ssn']) + ') ON DUPLICATE KEY UPDATE ssn=ssn'

execute_query('mysql', 'customers_info', query)

print('</body>')
print('</html>')
