'''
Created on 2017. 8. 7.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

## visualization
#import matplotlib.pyplot as plt
#from matplotlib import font_manager, rc
#font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
#rc('font', family = font_name)

## timeseries
from datetime import datetime

from bs4 import BeautifulSoup as Soup, Tag

import requests


response = requests.get("http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=")
soup = Soup(response.content)

births_span = soup.find("span", {"id": "Births"})
births_ul = births_span.parent.find_next_sibling()



print('#' * 30 ,"")




