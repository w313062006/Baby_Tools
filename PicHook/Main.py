# -*- coding: utf-8 -*-

import urllib2
#from bs4 import BeautifulSoup
import re
import requests
import time
import os
import cStringIO
import Image
#增加多线程支持
import threading


#保存文件夹地址
PicDir   = ''
#保存当前时间戳
time_tmp = str(time.time())

def ty(temp):
    print type(temp)
    return
def getFileName(n,filename):

    path_dir = 'C:\\Users\\wushuang\\Desktop\\mk\\' + time_tmp + '\\'

    if os.path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)

    PicDir = path_dir + str(n)  + '__' + filename
    return PicDir


def checkPicSize(pic_binary):
    temp  = cStringIO.StringIO(pic_binary)
    img   = Image.open(temp)
    #img = Image.open(pic_binary)

    if (img.size[0] > 400) and (img.size[1] > 400):
        return True
    else:
        return False

def getImgThread(tmp_n,tmp_filename,tem_r):

    print tmp_filename
    with open(getFileName(tmp_n,tmp_filename),'wb') as fd:
        for chunk in tem_r:
               fd.write(chunk)
    fd.close()


page = urllib2.urlopen("http://item.secoo.com/12517614.shtml")
#print page
context = page.read()
#模式定义
#pattern = re.compile(r'"https?://.*?\.jpe?g"')

pattern = re.compile(r'"https?://[\w/\.\-/]*\.jpe?g"')

#放弃使用beautifulsoup 因为它主要用途是建立网站源码的树形结构。
#soup = BeautifulSoup(context,'html.parser')

pic_list = []
match = re.findall(pattern,context)
#print match
for url_tmp in match:
    index_tmp = url_tmp.index('http')
    if index_tmp != -1:
        pic_list.append(url_tmp)

#
# 开始处理图片下载
#
n = 1

task_threads = []
for a in pic_list:
    a = a[1:-1]
    #倒着取文件名
    filename = a.split('/')[-1]
    #存储线程

    r = requests.get(a,stream = True)
    #判断文件的大小，确定是否要处理
    if checkPicSize(r.content):
        pass
    else:
        n = n + 1
        continue

    #with open(getFileName(n,filename),'wb') as fd:
    #    for chunk in r.iter_content(8 * 1024):
    #        fd.write(chunk)
    #    fd.close()
    #增加线程操作
    t = threading.Thread(target = getImgThread,args = (n,filename,r))
    task_threads.append(t)
    n = n + 1

for t in task_threads:
    t.start()
for t in task_threads:
    t.join()


print 'end'






