import urllib.request
import random

ip_list=['119.6.136.122','114.106.77.14']
#使用一组ip调用random函数来随机使用其中一个ip
url = "http://www.ip181.com/"
proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})
#参数是一个字典{'类型':'代理ip:端口号'}
opener = urllib.request.build_opener(proxy_support)
#定制opener
opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
#add_handler给加上伪装
urllib.request.install_opener(opener)
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
