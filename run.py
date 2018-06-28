# coding:utf-8

import re
import urllib.request
from bs4 import BeautifulSoup
# import tool
url = "https://www.lagou.com/"

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
# print(resp.read().decode('utf-8'))


cont = resp.read().decode('utf-8')
pattern = re.findall('<div class="category-list">.*?h2>(.*?)</h2>.*?<div class="menu_sub dn">(.*?)</div>', cont, re.S)
# print(pattern[0])
for items in pattern:


    for item in items:

        #url2 = re.findall('<a href="(.*?)".*?d.*?d.*?d.*?c.*?>(.*?)</a>', i, re.S)
        #print(item)
        patternA = re.findall('<dl.*?dt.*?<span>(.*?)</span>.*?<dd>(.*?)</dd>', item, re.S)
        #print(patternA)
