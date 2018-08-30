import re
import urllib.request
user_input = int(input("请输入您要爬取几页图片:"))
print("正在爬取数据...")
x = 1
for i in range(1,user_input+1):
    url_qsbk = "https://www.qiushibaike.com/pic/{}/".format(i)
    user_agent = "Chrome/4.0(compatible; MSIE 5.5; Windows NT)"
    req = urllib.request.Request(url_qsbk,headers={"User-Agent":user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    r = r'''<div\s.*>\s*<a\s.*>\s*<img\ssrc="(.*)?" alt.*?>'''
    a = re.findall(r,html)
    for j in a:
        #try:
        urllib.request.urlretrieve("http:"+j,'%s.jpg'%x) 
        x +=1
        #except:
            #pass
print("爬取结束！！")
