i = 1

while i < 10:
    print("加加加")
    i += 1
import re
import urllib.request
from bs4 import BeautifulSoup

headers = {
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Cookie": "user_trace_token=20171025133046-a75063b9-b945-11e7-9613-5254005c3644; LGUID=20171025133046-a750666a-b945-11e7-9613-5254005c3644; _ga=GA1.2.1301350500.1508909444; LG_LOGIN_USER_ID=bb5cb5245b7abcc3aba04c354d4ad1340752d9e42dd21106; _gid=GA1.2.1565293422.1530365343; JSESSIONID=ABAAABAAAGFABEF72FBF6D0B0E6607B1F64585C17D80087; _gat=1; LGSID=20180701211337-90e95d90-7d30-11e8-9856-5254005c3644; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%8C%97%E4%BA%AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530148244,1530365343,1530450817,1530450870; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530450874; LGRID=20180701211434-b28b5670-7d30-11e8-bab3-525400f775ce; SEARCH_ID=1a0bb8c4813a4f8d89c7a04002f83cef",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}

url = "https://www.lagou.com/zhaopin/Python/" 
# print(url)
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
cont = resp.read().decode("utf-8")
# print(cont)
soup = BeautifulSoup(cont, "lxml")
text = soup.select("div.s_position_list")

result = re.findall('<li class="con_list_item default_list".*?data-company="(.*?)".*?<h3.*?>(.*?)</h3>.*?<em>(.*?)</em>.*?<span class="money">(.*?)</span>.*?-->(.*?)                              </div>.*?<div class="industry">(.*?)</div>', str(text), re.S)
print(result)
