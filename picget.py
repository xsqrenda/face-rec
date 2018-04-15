# xp1024.com 日本騎兵 最新合集
from bs4 import BeautifulSoup
#import urllib.request
# import lxml.html
import requests
import os
from urllib.parse import urljoin
import re
from img_face_rec import find_face

# rooturl为首页地址，m为起始页，n为结束页
# key:keyword
# url='http://1024.c2048ao.pw/pw/thread.php?fid=83'
# url = 'https://www.wulinpai.com/18686.html'
# url = "http://1024.c2048ao.pw/pw/htm_data/3/1802/1021470.html"
# rooturl = 'http://s2.91sgc.rocks/pw/thread.php?fid=3'
# LXVS,39
# 259LUXU,71
# prestige,81
# LXV0,81 'F:\\My Documents\\My Pictures\\'
rooturl = 'http://1024.c2048ao.pw/'
avkeylist = ['259LUXU','LXV0','prestige','LXVS','古装','OL']
clkeylist = ['最新合集']
# clkey1 = '日本騎兵'
urlkey = 'thread'
m = 1
n = 10
rtpath = "E:\\xsq\\AV\\zz"
r = requests.get(rooturl)
r.encoding='utf-8'
soup = BeautifulSoup(r.text, "lxml")
atags = soup.select('a[href*="thread"]')
urllist = [urljoin(r.url, item.get('href')) \
        for item in atags \
         if item.get('target') is None \
         and item.text in clkeylist \
         ]#and item.text == clkey1

def downlaodimg(url,m,n,key,rtpath):
    # 创建搜索关键字命名的目录    
    os.chdir(rtpath)
    isExists = os.path.exists(key)
    if isExists:
        print(key, '文件夹已经存在了，不再创建')
    else:
        os.makedirs(key)
    os.chdir(key)
    keypath = os.getcwd()
    # 逐页查找目标
    for x in range(n-m+1):
        # os.chdir(keypath)
        # 拼接完整的带页码目标网址
        crurl=url + "&page=" + str(m+x)
        r = requests.get(crurl)
        print(crurl)
        r.encoding='utf-8'        
        soup = BeautifulSoup(r.text, "lxml")
        temp1= soup.find_all('h3')
        # newpath = os.getcwd()
        for title in temp1:
            os.chdir(keypath)
            t = 1
            if title.find('a') is None:
                continue
            temp2= title.find('a')['href']
            urlt=urljoin(url, temp2)
            r = requests.get(urlt)
            soup = BeautifulSoup(r.text, "lxml")
            # 查找网页文本中是非存在所找关键字
            if key not in r.text:
                continue
            # 创建保存目录            
            print(urlt)
            rstr = r"[\/\\\:\*\?\"\<\>\|]"
            new_title = re.sub(rstr,"_",title.text)
            isExists = os.path.exists(new_title)
            if isExists:
                print(new_title, '文件夹已经存在了，不再创建')
                continue
            os.makedirs(new_title)
            os.chdir(new_title)
            print(new_title)
            # 查找图片            
            ilist = soup.find_all('div',class_="tpc_content")
            for myimg in ilist:
                if myimg.find("img") is None:
                    continue
                temp3 = myimg.find_all("img")
                for temp4 in temp3:
                    temp5 = temp4["src"]
                    temp6 = find_face(temp5)
                    ir = requests.get(temp5)
                    if ir.status_code == 200:
                        pic_name = str(t) + temp6 +'.jpg'
                        open(pic_name, 'wb').write(ir.content)
                        print("Success!" + temp5)
                        t += 1     
for url in urllist:
    for key in avkeylist:
        downlaodimg(url,m,n,key,rtpath)
