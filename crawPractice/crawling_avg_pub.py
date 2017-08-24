'''
Created on 2017-08-23 14:04

@ product name : PyCharm Community Edition

@ author : yoda


Aug24, 2017. 17:28
JB

Work Done


'''

from requests.packages import urllib3
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import scipy as sp
import scipy.stats as stats
from bs4 import BeautifulSoup
import re
import datetime, time, sys
from multiprocessing import Process, Queue
import pymysql as pms
from urllib.error import *
from socket import *
import requests
ids = []
dates = []
models = []
krnames = []
prices = []
contracts = []
agencies = []
guarantees = []
changes = []
conditions = []
components = []
srcs = []

def crawl(startpno, endpno, counter):
    con = pms.connect(host="localhost", port=3306, user="root", password="11111", db="test", charset="UTF8")
    cursor = con.cursor()
    try:
        for pno in range(startpno, endpno):
            url_code = requests.get("http://market.cetizen.com/market.php?q=info&pno="+str(pno) )
            plain_text = url_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            # ids
            # dates
            try:
                soupSel01 = soup.select('div > div > div')  
                temp =[]
                for divs in soupSel01:
                    try:
                        pkrname = divs.find(name="span", attrs={"class":"p18 clr100 b ln22"}).text
                    except AttributeError as phoneNameError:
#                         pkrname = 'N/A'
                        pass
                    try:
                        tempModel = divs.find(name="span", attrs={"class":"b p16"}).text
                        agentLetter = tempModel.split(' ')[0][-1]
                        
                        if agentLetter == 'L' or agentLetter == 'K' or agentLetter == 'S':
                            tempList = tempModel.split(' ')
                            tempList[0] = tempList[0][0:-1]
                            pModel = " ".join(str(s) for s in tempList)
                        else:
                            pModel = tempModel
                    except AttributeError as phoneModelError:
#                         pModel = 'N/A'
                        pass
                    try:
                        pPublishedDate = divs.find(name="div", attrs={"style":"float:left;overflow:hidden"}).text
                    except AttributeError as pPublishedDateError:
#                         pPublishedDate = 'N/A'
                        pass
                    try:
                        pPublishedPrice = divs.find(name="div", attrs={"style":"float:left"}).text
                    except AttributeError as pPublishedPriceError:
#                         pPublishedPrice = 'N/A'
                        pass
                    
                    ######### pAvg, pLow, pHigh, 
                    ###?????? 중고시세변동, 출고가 변동.
                    
                print(pno,'::',pPublishedPrice)
                    
                    ## mariaDB insert DATA.
#                     try:
#                         cursor.execute("""CREATE TABLE IF NOT EXISTS PHONE (
#                             `id` TEXT NULL DEFAULT NULL,
#                             `date` TEXT NULL DEFAULT NULL,
#                             `model` TEXT NULL DEFAULT NULL,
#                             `krname` TEXT NULL DEFAULT NULL,
#                             `price` TEXT NULL DEFAULT NULL,
#                             `contract` TEXT NULL DEFAULT NULL,
#                             `agency` TEXT NULL DEFAULT NULL,
#                             `guarantee` TEXT NULL DEFAULT NULL,
#                             `change` TEXT NULL DEFAULT NULL,
#                             `condition` TEXT NULL DEFAULT NULL,
#                             `component` TEXT NULL DEFAULT NULL,
#                             `src` TEXT NULL DEFAULT NULL,
#                             `sold` TEXT NULL DEFAULT NULL
#                         )
#                         COLLATE='utf8_general_ci'
#                         """)
#                         con.commit()
#                     except:
#                         print("error", sys.exc_info())
#                         con.rollback()
#                     print(str(pno)+" inserting sql completed")
                    
            except AttributeError as e:
                print(str(pno) + "데이터 존재하지 않음")
                continue
            except IndexError as index:
                print(str(pno)+" IndexError  :: ", index)
            except URLError as e:
                print(str(pno)+"URLError")
            except HTTPError as http:
                pass
            except WindowsError as win:
                pass
            # except socket.timeout:
            #     print(str(pno)+" timeout")
    except gaierror as gai:
        print("#############################process" + str(counter) + " : " + str(pno) + "gaierror##############################")
        pno += 1
        crawl(pno, endpno, counter)
    except TimeoutError as time:
        print("#############################process" + str(counter)+" : " + str(pno) + "TimeoutError##############################")
        pno += 1
        crawl(pno, endpno, counter)
    except urllib3.exceptions.ProtocolError:
        print("##############################process" + str(counter)+" : " + str(pno) + " requests.packages.urllib3.exceptions.ProtocolError##############################")
        pno += 1
    except requests.exceptions.ChunkedEncodingError:
        print("##############################process" + str(counter)+" : " + str(pno) + " requests.exceptions.ChunkedEncodingError##############################")
        pno += 1
        crawl(pno, endpno, counter)
    log("saving that to mysql..")
    print("process" + str(counter) + " success")





def log(message):
   ts = time.time()
   sts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
   print ("%s : %s"% (sts, message))

log("start crawl..")

if __name__ == '__main__':
    start_time = time.time()
    result = Queue()
    pr1 = Process(target=crawl, args=(6538, 6600, 1))
#     pr2 = Process(target=crawl, args=(17207493, 17400000, 2)) # error
#     pr3 = Process(target=crawl, args=(17406521, 17600000, 3))
    # pr5 = Process(target=crawl, args=(15566320, 16065000, 5))
    # pr6 = Process(target=crawl, args=(16066320, 16565000, 6))
    # pr7 = Process(target=crawl, args=(16566320, 17065000, 7))
    # 17421646

    pr1.start()
#     pr2.start()
#     pr3.start()
    # pr5.start()
    # pr6.start()
    # pr7.start()


    pr1.join()
#     pr2.join()
#     pr3.join()
    # pr5.join()
    # pr6.join()
    # pr7.join()


    result.put('STOP')

    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
    log("data crawling completed..")
    log("complete!")
    end_time = time.time()
    print((end_time - start_time)/60)
