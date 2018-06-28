# coding:utf-8

import re
import urllib.request
from bs4 import BeautifulSoup
import tool

url = "https://www.lagou.com/"
headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Cookie": "user_trace_token=20171025133046-a75063b9-b945-11e7-9613-5254005c3644; LGUID=20171025133046-a750666a-b945-11e7-9613-5254005c3644; _ga=GA1.2.1301350500.1508909444; LG_LOGIN_USER_ID=bb5cb5245b7abcc3aba04c354d4ad1340752d9e42dd21106; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1660238457.1530102456; JSESSIONID=ABAAABAAADEAAFI5300B9A07FE2F206C32A6A58B2425CCB; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1529626234,1529888160,1530102456,1530148244; TG-TRACK-CODE=index_navigation; _gat=1; LGSID=20180628155232-36cef9bb-7aa8-11e8-b207-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2FJava%2F%3FlabelWords%3Dlabel; X_HTTP_TOKEN=8b22e1485a68b272410b9924577036d9; LGRID=20180628155305-4a6b0689-7aa8-11e8-975a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530172445; SEARCH_ID=478e32d7560a4540af362ad1a457aa4d",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
# print(resp.read().decode('utf-8'))

HY = []
cont = resp.read().decode('utf-8')
pattern = re.findall('<div class="category-list">.*?h2>(.*?)</h2>.*?<div class="menu_sub dn">(.*?)</div>', cont, re.S)
# print(pattern[0][0])
for h in pattern:
    HY.append(h[0])

# print(HY)
listA = []
for items in pattern:
    for item in items:

        #print(item)
        patternA = re.findall('<dl.*?dt.*?<span>(.*?)</span>.*?<dd>(.*?)</dd>', item, re.S)
        if patternA == []:
            pass
        else:
            listA.append(patternA)

listB = []
for industy in listA:
    for position in industy:
        result = re.findall('<a href="(.*?)".*?d.*?d.*?d.*?c.*?>(.*?)</a>', position[1], re.S)
        listB.append(result)


for result in listB:
    print("-" * 100)
    for Zurl in result:
        print(Zurl[1])
        reqA = urllib.request.Request(Zurl[0], headers = headers)
        respA = urllib.request.urlopen(reqA)
        contA = respA.read().decode("utf-8")
        # print(contA)
        soup = BeautifulSoup(contA, "lxml")
        text = soup.select("div.s_position_list")
        # print(text)
        # print(Zurl[0])
        patternB = re.findall('<li class="con_list_item default_list".*?data-salary="(.*?)".*?data-company="(.*?)".*?data-positionname="(.*?)"', str(text), re.S)
        print(patternB)
