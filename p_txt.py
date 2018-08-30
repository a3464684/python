import urllib.request
import re
url_qsbk = "https://www.qiushibaike.com/text/page/1/"
user_agent = " Chrome/4.0(compatible; MSIE 5.5; Windows NT)"#模仿浏览器打开网页
req = urllib.request.Request(url_qsbk,headers={"User-Agent":user_agent}) #请求网页
page = urllib.request.urlopen(req)
html = page.read().decode("utf-8")
r1 = r"<div\s.*>\s<span>\s*(.*)?\s*</span>"
r2 = r"<h2>\s*(.*?)\s*</h2>"
r3 = r"<span class.*?>\s*<i class=.*?>([0-9]+)</i>"

a = re.findall(r1,html,re.M)
c = re.findall(r2,html,re.M)
d = re.findall(r3,html,re.M)
for i in range(len(a)):
    print('昵称：{}\n段子：{}\n点赞数：{}'.format(c[i],a[i],d[i]))



