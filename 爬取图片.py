#/!/usr/bin/env python3

from urllib import request
import os
import re
import threading


#下载网页文件,以及图片,提供下载功能
def download(url,fname):

    html = request.urlopen(url)
    with open(fname,'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)





#获取图片地址,并保存为一个列表

def get_urls(fname,patt,encoding=None):
    patt_list = []
    cpatt = re.compile(patt)        #定义正则匹配规则
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:                 #判断m是否存在
                patt_list.append(m.group())

    return patt_list              #返回一个列表








if __name__ == '__main__':
    path = '/tmp/myimg'
    if not os.path.exists(path):     #如果路径不存在,则创建路径
        os.mkdir(path)
    url_163 = 'http://www.tmooc.cn'
    fname_163 = os.path.join(path,'tmooc.html')
    download(url_163,fname_163)       #下载网易首页
    img_patt = '(http|https)://[-/.\w]+\.(png|jpg|gif|jpeg)'
    img_list = get_urls(fname_163,img_patt)
    for line in img_list:             #遍历图片地址列表,遍历的每一项是一个字符串
         fname = os.path.basename(line)  #对字符串进行切割,获取图片的名字
        #fname = line.split('/')[-1]
         fname = os.path.join(path,fname) #将获取的名字与路径拼接



         # 多线程执行图片下载
         t = threading.Thread(target=download,args=(line,fname))
         t.start()


