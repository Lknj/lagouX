import re
import urllib.request
from bs4 import BeautifulSoup
import random
import time
from data import getData, allData

headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Cookie": "user_trace_token=20171025133046-a75063b9-b945-11e7-9613-5254005c3644; LGUID=20171025133046-a750666a-b945-11e7-9613-5254005c3644; _ga=GA1.2.1301350500.1508909444; LG_LOGIN_USER_ID=bb5cb5245b7abcc3aba04c354d4ad1340752d9e42dd21106; _gid=GA1.2.1565293422.1530365343; JSESSIONID=ABAAABAAAGFABEF72FBF6D0B0E6607B1F64585C17D80087; _gat=1; LGSID=20180701211337-90e95d90-7d30-11e8-9856-5254005c3644; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530148244,1530365343,1530450817,1530450870; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530450874; LGRID=20180701211434-b28b5670-7d30-11e8-bab3-525400f775ce; SEARCH_ID=1a0bb8c4813a4f8d89c7a04002f83cef",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}

# 先爬取后端开发的各职位url
url = "https://www.lagou.com/"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
cont = resp.read().decode("utf-8")
some_url = re.findall('<span>后端开发</span>(.*?)<span>移动开发</span>', cont, re.S)
# print(some_url)
# 获取所有a标签  href
soup = BeautifulSoup(str(some_url), "lxml")
all_data = []
for link in soup.find_all('a'):
    # print(link.get('href'))
    page = 1
    while page <= 30:
        # 设置代理
        fp = open("proxy_list.txt", 'r')
        lines = fp.readlines()
        ip = lines[0:random.randint(0, len(lines))]
        proxy = urllib.request.ProxyHandler({'http': "114.82.109.134:8118"})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)

        new_url = str(link.get('href')) + str(page) + "/?filterOption=3"
        # print(new_url)
        data = getData(new_url)
        all_data.append(data)
        page += 1
        time.sleep(5)
        print(data)
        print("-" * 100)
