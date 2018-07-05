# coding:utf-8
import re
import urllib.request

fp = open("thebigproxylist-18-07-05.txt", 'r')
lines = fp.readlines()


for ip in lines:
    try:
        print('当前代理IP:' + ip)
        proxy = urllib.request.ProxyHandler({'http': "ip"})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        url = 'https://www.lagou.com/'
        data = urllib.request.urlopen(url).read().decode('utf-8')
        print('通过！')
        print('-' * 150)
        fpT = open("proxy_list.txt", 'a')
        fpT.writelines(ip)
    except Exception as err:
        print(err)
        print('*' * 150)
fp.close()
fpT.close()
