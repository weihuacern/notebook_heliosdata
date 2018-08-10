#!/usr/bin/python3.6
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import cgi
import cgitb
import random
import json

from utils import execute_query

EMPLOYEE_LIST = ['ssn', 'blood_group', 'name', 'sex', 'mail', 'phone', 'race', 'ethnic', 'religion', 'trade_union', 'health', 'sexual', 'politics', 'birthdate']
with open('employees.json', 'r') as file:
    string = file.read()
employee_list = json.loads(string)

columns = '('
values = '('
entry = random.choice(employee_list)
for key, value in entry.items():
    if key in EMPLOYEE_LIST and value:
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
print('employee: ' + str(entry) + '<br />')

query = 'INSERT INTO employee ' + columns + ' VALUES ' + values + ';'

execute_query('mssql', 'hr_pii', query)

query = 'IF NOT EXISTS ( SELECT * FROM dbo.key_table WHERE ssn = %s )INSERT dbo.key_table (ssn) VALUES (%s)' % (repr(entry['ssn']), repr(entry['ssn']))


execute_query('mssql', 'hr_pii', query)

print('</body>')
print('</html>')
