import re
import urllib.request
from bs4 import BeautifulSoup
import random
import time
from tool import Tool
from first_db import insert_db
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

def position_dict():
    url = "https://www.lagou.com/"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    cont = resp.read().decode("utf-8")
    soup = BeautifulSoup(cont, "lxml")
    text = soup.select("div.mainNavs")
    some_url = re.findall('<div class="category-list">(.*?)</div>', str(text), re.S)
    position_dict = {}
    position_url = []
    g = 0
    for urla in some_url:
        all_name = re.findall('<a.*?>(.*?)</a>', str(urla), re.S)
        soup = BeautifulSoup(str(urla), "lxml")

        for link in soup.find_all('a'):
            position_url.append(link.get('href'))
        for name in all_name:
            position_dict[name] = position_url[g]
            g += 1
    return position_dict
print(position_dict())
def getData(url):
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, "lxml")
    text = soup.select("div.s_position_list ul")
    result = re.findall('<li class="con_list_item default_list".*?data-company="(.*?)".*?<h3.*?>(.*?)</h3>.*?<span class="add".*?<em>(.*?)</em>.*?<span class="money">(.*?)</span>.*?-->(.*?)                              </div>.*?<div class="industry">(.*?)</div>', str(text), re.S)
    return result
def get_result(url):
    small = []
    page = 1
    while page <= 30:
        new_url = url + str(page) + "/?filterOption=3"
        data = getData(new_url)
        for it in data:
            small.append([it[0], it[1], it[2], it[3], Tool().rep(it[4]), Tool().rep(it[5]), datetime.date.today()])
            insert_db(it[0], it[1], it[2], it[3], Tool().rep(it[4]), Tool().rep(it[5]), datetime.date.today())
        page += 1
        time.sleep(5)
    return small
def salaryData(url):
    salary = []
    a = 0
    b = 0
    c = 0
    d = 0
    for salarys in get_result(url):
        salary.append(salarys[3])

    for sal in salary:
        if int(sal[-3:-1]) <= 10:
            a += 1
        elif 11 <= int(sal[-3:-1]) <= 20:
            b += 1
        elif 21 <= int(sal[-3:-1]) <= 40:
            c += 1
        elif 41 <= int(sal[-3:-1]) <= 60:
            d += 1
    A = [a, b, c, d]
    return A

def areaData(url):
    allArea = []
    for area in get_result(url):
        allArea.append(area[2][0:2])

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
