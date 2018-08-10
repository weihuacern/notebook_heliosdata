#!/usr/bin/python3.6
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import cgi
import cgitb
import json
import random

from utils import get_query, execute_query, fakesql

my_dbname = "customers_info"
my_table = 'customer'

with open('customers.json', 'r') as file:
    string = file.read()
customer_list = json.loads(string)

entry = random.choice(customer_list)
ssn = entry['ssn']
query = fakesql('customer', ['ssn', 'job', 'company', 'blood_group', 'name', 'sex', 'mail', 'zipcode', 'city', 'state', 'phone', 'race', 'ethnic', 'religion', 'trade_union', 'health', 'sexual', 'politics', 'birthdate'], ["sex = 'M'", "sex = 'F'", "state = 'CA'", "state = 'WA'"])
#query = 'SELECT * FROM customer WHERE ssn = %s;' % repr(ssn)

cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>CUSTOMER INFORMATION CHECK</title>')
print('</head>')
print('<body>')
print('ssn: ' + ssn + '<br />')
print('Query results:<br />')
execute_query('mysql', 'customers_info', query)
print('</body>')
print('</html>')
