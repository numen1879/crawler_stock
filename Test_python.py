#!/usr/bin/env python
# coding: utf-8

# In[122]:


from bs4 import BeautifulSoup
import requests
import time
import random
import csv
import json
import urllib3
from fake_useragent import UserAgent
import datetime


# In[177]:


#網站
url = 'https://cn.investing.com/equities/apple-computer-inc-historical-data'
#輸入日期
start_date = '2021/05/05'
end_date = '2021/05/26'
#降低Python網頁爬蟲被偵測封鎖
user_agent = UserAgent()
# 將資料加入 POST 請求中
#my_data = {'picker': '2021/05/04 - 2021/05/29'}

my_data = {
'st_date': start_date,
'end_date': end_date,
}


response = requests.post(url, data = my_data, headers={'user-agent': user_agent.random})

#爬資料
soup = BeautifulSoup(response.text, "html.parser")
table = soup.findAll("table", {"class": "genTbl closedTbl historicalTbl"})[0]
count = 0
temp_dict = {}
json_list = []

for all_info in table.findAll('td'):
    count +=1
    if count % 7 == 1:
        temp_dict['日期'] = all_info.getText()
    elif count % 7 == 2:
        temp_dict['收盤'] = all_info.getText()
    elif count % 7 == 3:
        temp_dict['開盤'] = all_info.getText()
    elif count % 7 == 4:
        temp_dict['高'] = all_info.getText()        
    elif count % 7 == 5:
        temp_dict['低'] = all_info.getText()        
    elif count % 7 == 6:
        temp_dict['交易量'] = all_info.getText()    
    elif count % 7 == 0:
        temp_dict['漲跌幅'] = all_info.getText()
        json_list.append(temp_dict)
        temp_dict = {}
        
#轉成json
jsonArr = json.dumps(json_list, ensure_ascii=False)
print(jsonArr)


# In[ ]:




