#!/usr/bin/python3.6
import sys
import cgi
import cgitb
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
import random
import json

from utils import execute_query

PERFORM_LIST = ['ssn', 'attendence', 'KPI', 'bonus']
with open('employees.json', 'r') as file:
    string = file.read()
employee_list = json.loads(string)

columns = '('
values = '('
entry = random.choice(employee_list)
for key, value in entry.items():
    if key in PERFORM_LIST and value:
        columns = columns + key + ', '
        values = values + repr(value) + ', '

columns = columns[:-2] + ')'
values = values[:-2] + ')'

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>INSERT PERFORMANCE INFO</title>')
print('</head>')
print('<body>')
print('employee: ' + str(entry['ssn']) + '<br />')

query = 'INSERT INTO performance ' + columns + ' VALUES ' + values + ';'

print(query + '<br />')

execute_query('mssql', 'hr_pii', query)

query = 'IF NOT EXISTS ( SELECT * FROM dbo.key_table WHERE ssn = %s )INSERT dbo.key_table (ssn) VALUES (%s)' % (repr(entry['ssn']), repr(entry['ssn']))


execute_query('mssql', 'hr_pii', query)

print('</body>')
print('</html>')
