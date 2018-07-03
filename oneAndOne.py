import re
import urllib.request
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Cookie": "user_trace_token=20171025133046-a75063b9-b945-11e7-9613-5254005c3644; LGUID=20171025133046-a750666a-b945-11e7-9613-5254005c3644; _ga=GA1.2.1301350500.1508909444; LG_LOGIN_USER_ID=bb5cb5245b7abcc3aba04c354d4ad1340752d9e42dd21106; _gid=GA1.2.1565293422.1530365343; JSESSIONID=ABAAABAAAGFABEF72FBF6D0B0E6607B1F64585C17D80087; _gat=1; LGSID=20180701211337-90e95d90-7d30-11e8-9856-5254005c3644; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530148244,1530365343,1530450817,1530450870; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530450874; LGRID=20180701211434-b28b5670-7d30-11e8-bab3-525400f775ce; SEARCH_ID=1a0bb8c4813a4f8d89c7a04002f83cef",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}

# 设置代理
proxy = urllib.request.ProxyHandler({'http': "114.82.109.134:8118"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

XZ =[]
Area = []
page = 1
while page <= 30:
    # print(str(page) + "页")
    url = "https://www.lagou.com/zhaopin/Python/" + str(page) + "/?filterOption=3"
    # print(url)
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    cont = resp.read().decode("utf-8")
    # print(cont)
    soup = BeautifulSoup(cont, "lxml")
    text = soup.select("div.main_container")
    # print(text)
    result = re.findall('<li class="con_list_item default_list".*?data-company="(.*?)".*?<h3.*?>(.*?)</h3>.*?<em>(.*?)</em>.*?<span class="money">(.*?)</span>.*?-->(.*?)                              </div>.*?<div class="industry">(.*?)</div>', str(text), re.S)
    # print(result)
    page += 1

    for xz in result:
        XZ.append(xz[3])

    for area in result:
        Area.append(area[2])
# print(XZ)
# 去重，为了获取各个薪资水平
# xzSet = list(set(XZ))
# print(len(xzSet))
# 去重，区
# areaSet = list(set(Area))
# print(areaSet)
# 怎么作图、、、、
# wt = sorted(xzSet)

# a代表20k以下的，b代表20k到40k的，c代表40k到80k的
a = 0
b = 0
c = 0
d = 0
for x in XZ:
    if int(x[-3:-1]) <= 20:
        a += 1
    elif 21 <= int(x[-3:-1]) <= 40:
        b += 1
    elif 41 <= int(x[-3:-1]) <= 60:
        c += 1
    elif 61 <= int(x[-3:-1]) <= 80:
        d += 1

print(a, b, c, d)



# 条形图 数据
value = [a, b, c, d]
index = ["<=20k", "20K-40k", "40k-60k", "60k-80k"]
# 饼状图 数据
labels = "<=20k", "20K-40k", "40k-60k", "60k-80k"
fracs = [a, b, c, d]

plt.bar(left = index, height = value, color = "green", width = 0.5)
plt.show()
# 饼状图
plt.subplot(224)
plt.axes(aspect = 1)

explode = [0, 0.05, 0, 0]
plt.pie(x = fracs, labels = labels, autopct = "%0f%%", explode = explode)

plt.show()
