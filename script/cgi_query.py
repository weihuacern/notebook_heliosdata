import sys
import time

import requests

MODE_TAGS_DICT = {
    "HR": ["set_employee", "set_payroll", "set_performance", "check_employee", "check_payroll", "check_performance"],
    "SALES_MANAGER": ["set_sales", "set_customer", "check_sales", "check_customer", \
                      "set_employee", "check_employee", "check_payroll"],
    "SALES_GENERAL": ["set_customer", "check_sales", "check_customer", \
                      "check_employee", "check_payroll"],
}

TAG_APP_DICT = {
    "set_employee": 'post_employee.py',
    "set_payroll": 'set_payroll.py',
    "set_performance": 'set_performance.py',
    "set_sales": 'set_sales.py',
    "set_customer": 'post_customer.py',
    "check_employee": 'check_employee_info.py',
    "check_payroll": 'check_payroll.py',
    "check_performance": 'check_performance.py',
    "check_sales": 'check_sales.py',
    "check_customer": 'check_customer.py'
}

if __name__ == "__main__":
    mode = sys.argv[1]
    print("Script is running in mode: " + mode)
    print("Valid run modes are: " + ", ".join(MODE_TAGS_DICT.keys()))
    if mode == "HR":
        ip = "192.168.7.100"
    else:
        ip = "192.168.7.173"
    try:
        tag_list = MODE_TAGS_DICT[mode]
    except KeyError:
        print("Not a valid mode!")
        print("Valid run modes are: " + ", ".join(MODE_TAGS_DICT.keys()))
        sys.exit()

    round_index = 0
    while True:
        round_index += 1
        print("Round " + str(round_index) + ":" )
        for tag in tag_list:
            url = "http://" + ip + "/cgi-bin/" + TAG_APP_DICT[tag]
            print(url)
            r = requests.get(url)
            print(r.content)
            time.sleep(1)

        time.sleep(5)
