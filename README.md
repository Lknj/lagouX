# 使用手册
## 安装依赖
- windows
<pre>
pip install flask
pip install pymysql
pip install bs4
</pre>
- python3,mysql,[echart](http://echarts.baidu.com/download.html)去官网安装即可
## 数据库
- 执行sql脚本文件
  - 使用cmd命令执行
  
  - <pre>
    "C:Program Files\mysql 5.6\bin\mysql" –uroot –ppassword <d:lagoux\lagoux.sql
    </pre>
  
- 进入mysql控制台，使用source命令执行

<pre>

 source d:lagoux\lagoux.sql
 or
 \. d:lagoux\lagoux.sql
 
</pre>

## 以调试模式启动

<pre>

python debug.py
open http://127.0.0.1:5000/ in your browser.

</pre>
- 截图展示：
  - ![image](https://raw.githubusercontent.com/Lknj/Temp/master/image.png)
  - ![image](https://raw.githubusercontent.com/Lknj/Temp/master/image%20(1).png)
  - ![image](https://raw.githubusercontent.com/Lknj/Temp/master/image%20(2).png)
  - ![image](https://raw.githubusercontent.com/Lknj/Temp/master/image%20(3).png)
  - ![image](https://raw.githubusercontent.com/Lknj/Temp/master/image%20(4).png)
  
