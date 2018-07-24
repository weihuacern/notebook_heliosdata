import sys
import time

import requests

#register, cgi-bin/register.py, ssn, name, phone
#course, cgi-bin/course.py, ssn, name, course
#eval, cgi-bin/eval.cgi, ssn, course, eval
#info, cgi-bin/info.py, ssn
MODE_APP_DICT = {
    "register": ("cgi-bin/register.py", "?ssn=123&name=Jack Pitts&phone=1234567890"),
    "course": ("cgi-bin/course.py", "?ssn=123&name=Jack Pitts&course=CS101"),
    "eval": ("cgi-bin/eval.cgi", "?ssn=123&course=CS101&eval=A"),
    "info": ("cgi-bin/info.py", "?ssn=123"),
}

if __name__ == "__main__":
  mode = sys.argv[1]
  print("running in mode: " + mode)
  ip = "192.168.7.100"
  try:
      app = MODE_APP_DICT[mode][0]
  except KeyError:
      print("mode not found!")
      sys.exit()
  val = "123"
  url = "http://" + ip + "/" + app + MODE_APP_DICT[mode][1]
  #http://192.168.7.100/cgi-bin/info.py?ssn=123
  print(url)
 
  while True:
    time.sleep(2) 
    r = requests.get(url)
    #r = requests.get("https://github.com/")
    print(r.content)
