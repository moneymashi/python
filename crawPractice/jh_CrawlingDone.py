'''
Created on 2017-08-23 14:04

@ product name : PyCharm Community Edition

@ author : yoda


Aug24, 2017. 17:28
JB

Work Done

 ## programming TODO:: 
-------- Aug 22, 2017
00. 가독성증가용 :: 함수/ 클래스화. 제발 ㅜㅜ
5. 인기가 없거나 "데이터가 많은걸 저장"하고, 웹페이지에서 필터적용할수 있게끔.
4. 슬슬 데이터 -> matplot사용해서 그래프그리기.
5. word clouding



 ## Project TODO:: 
0. 각기종의 첫 판매시기, 판매시기 전 가장 최근10개 기종 가격변동 확인.
1. 웹페이지 연동.
2. 해킹 - 페이지에 나타나지 않는 데이터 

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
import datetime, time
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
def mariaDB():
    try:
        con = pms.connect(host="localhost", port=3306, user="root", password="11111", db="test", charset="UTF8")
        cursor = con.cursor()
        for i in range(0, len(ids)):
            cursor.execute("INSERT INTO CETIZEN2 VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            ids[i], dates[i], models[i], krnames[i], prices[i], contracts[i], agencies[i],
            guarantees[i], changes[i], conditions[i], components[i], srcs[i]))
        con.commit()
        print("success")
    except:
        print("error", sys.exc_info())
        con.rollback()
    finally:
        con.close()

def crawl(startno, endno, counter):
    con = pms.connect(host="localhost", port=3306, user="root", password="11111", db="test", charset="UTF8")
    cursor = con.cursor()
    try:
        for no in range(startno, endno):
            url_code = requests.get("http://market.cetizen.com/market.php?q=view&auc_no="+str(no)+"&auc_wireless=5")
            plain_text = url_code.text
            soup = BeautifulSoup(plain_text, "lxml")
            # ids
            id = no
            # dates
            try:
                try:
                    date = soup.find(name="span", attrs={"class":"p12 ls-0"}).text
                    date = date[1:11]
                except AttributeError as datesError:
                    date = "N/A"
                # models
                try:  ## model 통신사 캐릭터 제거.
                    tempModel = soup.find(name="span", attrs={"class":"clr02 bn p15 ls-0"}).text.strip()
                    agentLetter = tempModel.split(' ')[0][-1]
                    
                    if agentLetter == 'L' or agentLetter == 'K' or agentLetter == 'S':
                        tempList = tempModel.split(' ')
                        tempList[0] = tempList[0][0:-1]
                        model = " ".join(str(s) for s in tempList)
                    else:
                        model = tempModel
                        
                except AttributeError as modelsError:
                    model = "N/A"
                try:
                    krname = soup.find(name="li", attrs={"class":"viewright_box_wide p17 clr100 b"}).text
                    krname = str.split(krname, "\xa0")[0]
                    krname = str.replace(krname, "\xa0", "")
                except AttributeError as krnamesError:
                    krname = "N/A"
                # prices
                try:
                    price = soup.find(name="span", attrs={"class":"clr03 p21"}).text
                    price = re.sub('[^0-9]', "", price)
                except AttributeError as pricesError:
                    price = "N/A"
                # contracts
                try:
                    contract = soup.find(name="span", attrs={"onmouseout":"OnIconHide('opt"+str(no)+"');"}).text
                except AttributeError as contractsError:
                    contract = "N/A"
                # agencies
                try:
                    agency = soup.find(name="li", attrs={"class":"viewright_box_wide clr04"}).text
                    agency = str.replace(agency, "\xa0", "")
                except AttributeError as agenciesError:
                    agency = "N/A"
                # guarantees
                try:
                    guarantee = soup.find(name="li", attrs={"class":"viewright_box clr04 "}).text
                except AttributeError as guaranteesError:
                    guarantee = "N/A"
                # changes
                try:
                    change = soup.find(name="span", attrs={"onmouseout":"OnIconHide('usim"+str(no)+"');"}).text
                except AttributeError as changesError:
                    change = "N/A"
                # conditions
                try:
                    condition = soup.find_all(name="li", attrs={"class":"viewright_box clr04 "})[1].text
                except AttributeError as conditionsError:
                    condition = "N/A"
                # components
                try:
                    component = soup.find_all(name="li", attrs={"class":"viewright_box1 clr04"})[1].text
                except AttributeError as componentError:
                    component = "N/A"
                try:
                    src = soup.find(name="img", attrs={"width":"220", "vspace":"1"}).get("src")
                except AttributeError as srcsError:
                    src = "N/A"
                try:
                    sold = soup.find(name="span", attrs={"class":"p13 clr100 b"}).text
                except AttributeError as soldError:
                    sold = "N/A"
                print(str(no)+" crawling completed")
                try:
                    cursor.execute("""CREATE TABLE IF NOT EXISTS CETIZEN (
                        `id` TEXT NULL DEFAULT NULL,
                        `date` TEXT NULL DEFAULT NULL,
                        `model` TEXT NULL DEFAULT NULL,
                        `krname` TEXT NULL DEFAULT NULL,
                        `price` TEXT NULL DEFAULT NULL,
                        `contract` TEXT NULL DEFAULT NULL,
                        `agency` TEXT NULL DEFAULT NULL,
                        `guarantee` TEXT NULL DEFAULT NULL,
                        `change` TEXT NULL DEFAULT NULL,
                        `condition` TEXT NULL DEFAULT NULL,
                        `component` TEXT NULL DEFAULT NULL,
                        `src` TEXT NULL DEFAULT NULL,
                        `sold` TEXT NULL DEFAULT NULL
                    )
                    COLLATE='utf8_general_ci'
                    """)
                    cursor.execute("INSERT INTO CETIZEN VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                            id, date, model, krname, price, contract, agency, guarantee,
                            change, condition, component, src, sold))
                    con.commit()
                except:
                    print("error", sys.exc_info())
                    con.rollback()
                print(str(no)+" inserting sql completed")
            except AttributeError as e:
                print(str(no) + "데이터 존재하지 않음")
                continue
            except IndexError as index:
                print(str(no)+" IndexError  :: ", index)
            except URLError as e:
                print(str(no)+"URLError")
            except HTTPError as http:
                pass
            except WindowsError as win:
                pass
            # except socket.timeout:
            #     print(str(no)+" timeout")
    except gaierror as gai:
        print("#############################process" + str(counter) + " : " + str(no) + "gaierror##############################")
        no += 1
        crawl(no, endno, counter)
    except TimeoutError as time:
        print("#############################process" + str(counter)+" : " + str(no) + "TimeoutError##############################")
        no += 1
        crawl(no, endno, counter)
    except urllib3.exceptions.ProtocolError:
        print("##############################process" + str(counter)+" : " + str(no) + " requests.packages.urllib3.exceptions.ProtocolError##############################")
        no += 1
    except requests.exceptions.ChunkedEncodingError:
        print("##############################process" + str(counter)+" : " + str(no) + " requests.exceptions.ChunkedEncodingError##############################")
        no += 1
        crawl(no, endno, counter)
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
    pr1 = Process(target=crawl, args=(17425928, 17425950, 1))
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
