# coding:utf-8
import urllib.request
import re


# 处理页面标签类,可复用
class Tool:
    # 去除img标签，7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeA = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将<td>替换为\t
    replaceTD =re.compile('<td>')
    # 把段落开头换为\n加空两格
    replaceP = re.compile('<p.*?>')
    # 把换行符或者双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将多余的标签删除
    removeEx = re.compile('<.*?>')
    # 

    def rep(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeA, "", x)
        x = re.sub(self.replaceLine, "", x)
        x = re.sub(self.replaceTD, "", x)
        x = re.sub(self.replaceP, "", x)
        x = re.sub(self.replaceBR, "", x)
        x = re.sub(self.removeEx, "", x)

        return x.strip()
