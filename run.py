# coding:utf-8

import re
import urllib.request
# import tool
url = "https://www.lagou.com/"

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
# print(resp.read().decode('utf-8'))


cont = resp.read().decode('utf-8')
pattern = re.findall('<div class="category-list">.*?h2>(.*?)</h2>.*?<div class="menu_sub dn".*?<dt>*?<span>(.*?)</span>.*?</dt>.*?<dd>(.*?)</dd>', cont, re.S)
print(pattern[0])
#for item in pattern:

    #for i in item[2]:
    #    list1 = []
    #    url2 = re.findall('<a href="(.*?)".*?d.*?d.*?d.*?c.*?>(.*?)</a>', i, re.S)
    #    reqq = urllib.request.Request(url)
    #    respp = urllib.request.urlopen(req)

    #    contt = respp.read().decode('utf-8')
    #    patternA = re.findall('')
