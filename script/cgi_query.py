import sys
import time

import requests

MODE_TAGS_DICT = {
    "HR": ["set_employee", "set_payroll", "set_performance", "check_employee", "check_payroll", "check_performance"],
    "SALES_MANAGER": ["set_sales", "set_customer", "check_sales", "check_customer", \
                      "set_employee", "check_employee", "check_payroll"],
    "SALES_GENERAL": ["set_customer", "check_sales", "check_customer", \
                      "set_employee", "check_employee", "check_payroll"],
}

TAG_APP_DICT = {
    "set_employee": ("cgi-bin/set_employee_info.py", "?eid=123&name=Jack Pitts&phone=1234567890"),
    "set_payroll": ("cgi-bin/set_payroll.py", "?eid=123&payment=10000&title=SDE"),
    "set_performance": ("cgi-bin/set_performance.py", "?eid=123&bonus=5000&attendance=50"),
    "set_sales": ("cgi-bin/set_sales.py", "?eid=123&name=Jack Pitts&cids=1001"),
    "set_customer": ("cgi-bin/set_customer.py", "?cid=123&contact=2345678901&trade=book"),
    "check_employee": ("cgi-bin/check_employee_info.py", "?eid=123"),
    "check_payroll": ("cgi-bin/check_payroll.py", "?eid=123"),
    "check_performance": ("cgi-bin/check_performance.py", "?eid=123"),
    "check_sales": ("cgi-bin/check_sales.py", "?eid=123"),
    "check_customer": ("cgi-bin/check_customer.py", "?cid=123"),
}

if __name__ == "__main__":
    mode = sys.argv[1]
    print("Script is running in mode: " + mode)
    print("Valid run modes are: " + ",".join(MODE_TAGS_DICT.keys()))
    ip = "192.168.7.100"
    try:
        tag_list = MODE_TAGS_DICT[mode]
    except KeyError:
        print("Not a valid mode!")
        print("Valid run modes are: " + ",".join(MODE_TAGS_DICT.keys()))
        sys.exit()

    round_index = 0
    while True:
        round_index += 1
        print("Round " + str(round_index) + ":" )
        for tag in tag_list:
            url = "http://" + ip + "/" + TAG_APP_DICT[tag][0] + TAG_APP_DICT[tag][1]
            print(url)
            r = requests.get(url)
            print(r.content)
            time.sleep(2)
