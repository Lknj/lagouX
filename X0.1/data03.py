import re
import urllib.request
from bs4 import BeautifulSoup
import random
import time
from tool import Tool
from first_db import insert_db, query_db
import datetime

headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Cookie": "user_trace_token=20171025133046-a75063b9-b945-11e7-9613-5254005c3644; LGUID=20171025133046-a750666a-b945-11e7-9613-5254005c3644; _ga=GA1.2.1301350500.1508909444; LG_LOGIN_USER_ID=bb5cb5245b7abcc3aba04c354d4ad1340752d9e42dd21106; _gid=GA1.2.1111296397.1531706780; LGSID=20180716100623-d68b4839-889c-11e8-9dec-5254005c3644; JSESSIONID=ABAAABAAAGGABCBD210DB7C182F795D880F2E5908FF2965; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531361501,1531578826,1531706780,1531709242; X_HTTP_TOKEN=8b22e1485a68b272410b9924577036d9; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=a540f44e0dba487ba1b34b0e1250cd46; _gat=1; LGRID=20180716110937-ac4e8e68-88a5-11e8-9dec-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531710576",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}

url = "https://www.lagou.com/"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
cont = resp.read().decode("utf-8")
soup = BeautifulSoup(cont, "lxml")
text = soup.select("div.mainNavs")
some_url = re.findall('<div class="category-list">(.*?)</div>', str(text), re.S)


def soup_text(text):
    txt = BeautifulSoup(str(text), "lxml")
    return txt
technology_url = soup_text(some_url[0])
product_url = soup_text(some_url[1])
design_url = soup_text(some_url[2])
operation_url = soup_text(some_url[3])
sales_url = soup_text(some_url[4])
function_url = soup_text(some_url[5])
financial_url = soup_text(some_url[6])

def getData(url):
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, "lxml")
    text = soup.select("div.s_position_list ul")
    result = re.findall('<li class="con_list_item default_list".*?data-company="(.*?)".*?<h3.*?>(.*?)</h3>.*?<span class="add".*?<em>(.*?)</em>.*?<span class="money">(.*?)</span>.*?-->(.*?)                              </div>.*?<div class="industry">(.*?)</div>', str(text), re.S)
    return result
big = []
def get_result(soup_x):
    for link in soup_x.find_all('a'):
        # print(link.get('href'))
        small = []
        page = 1
        while page <= 30:
            # 设置代理
            new_url = str(link.get('href')) + str(page) + "/?filterOption=3"
            # print(new_url)
            data = getData(new_url)
            #print(data)
            for it in data:
                small.append([it[0], it[1], it[2], it[3], Tool().rep(it[4]), Tool().rep(it[5]), datetime.date.today()])
            page += 1
            print("-" * 90 + "完成")
            time.sleep(5)
        big.append(small)
        print("*" * 180)
        return big
def industry_result():
    try:
        technology_result = get_result(technology_url)
        #product_result = get_result(product_url)
        #design_result = get_result(design_url)
        #operation_result = get_result(operation_url)
        #sales_result = get_result(sales_url)
        #function_result = get_result(function_url)
        #financial_result = get_result(financial_url)

    except urllib.error.URLError as e:
        print(e.reason)
    return technology_result
def salaryData():
    XZ = []
    a = 0
    b = 0
    c = 0
    d = 0
    for xz in industry_result():
        for x in xz:
            XZ.append(x[3])

    for x in XZ:
        if int(x[-3:-1]) <= 10:
            a += 1
        elif 11 <= int(x[-3:-1]) <= 20:
            b += 1
        elif 21 <= int(x[-3:-1]) <= 40:
            c += 1
        elif 41 <= int(x[-3:-1]) <= 60:
            d += 1
    A = [a, b, c, d]
    return A

def areaData():
    allArea = []
    for area in industry_result():
        for x in area:
            allArea.append(x[2][0:2])

    area = list(set(allArea))
    area_result = []
    for a in area:
        time = 0
        for A in allArea:
            if A == a:
                time += 1
        area_result.append([a,time])
    name = []
    num = []
    for x in area_result:
        name.append(x[0])
        num.append(x[1])
    return name,num
