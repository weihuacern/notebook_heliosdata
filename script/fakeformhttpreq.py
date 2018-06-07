import os
import random
import time

class formhttpfakeget:

    def __init__(self, hostip, directory, filelist):
        self.hostip = hostip
        self.directory = directory
        self.filelist = filelist
        #"http://192.168.7.155/PIIFormTest/"

    def fakecurl(self, fname):
        curlcmd = "curl -O http://" + self.hostip + "/" + self.directory + "/" + fname
        return curlcmd

    def fakehttppii(self, cnt):
        for i in range(cnt):
            thishttpreq = self.fakecurl(self.filelist[random.randint(0, len(self.filelist)-1)])
            #print(thishttpreq)
            os.system(thishttpreq)
            time.sleep(abs(random.gauss(1, 0.3)))

if __name__ ==  "__main__":

    myformhttpfakeget = formhttpfakeget("192.168.7.155", "PIIFormTest", ["form1.pdf", "form2.pdf", "form3.pdf", "form4.pdf", "form5.pdf"])

    while 1:
        myformhttpfakeget.fakehttppii(random.randint(1, 10))
        time.sleep(abs(random.gauss(10, 3.0)))
