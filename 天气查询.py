#!/usr/bin/env python3
#天气预报查询


import re
import pprint
from urllib import request
import json



def city_num():                 #导入中国天气网所有城市码,存入字典使城市名称和城市码对应
    dict = {}
    with open('/tmp/weather.txt') as fobj:
        for line in fobj:
            if line.strip():
                data = re.split('=',line.strip())
                # print(data)
                dict[data[1]] = data[0]

    return dict

#实况信息
def sk(city):
    url = 'http://www.weather.com.cn/data/sk/%s.html' % city
    r = request.urlopen(url)
    data = r.read()
    bj = json.loads(data)
    bj = bj['weatherinfo']
    for key,val in bj.items():
        print('%-12s: %-12s\r\n' % (key,val))

#城市信息
def cityinfo(city):
    url = 'http://www.weather.com.cn/data/cityinfo/%s.html' % city
    r = request.urlopen(url)
    data = r.read()
    bj = json.loads(data)
    bj = bj['weatherinfo']
    for key, val in bj.items():
        print('%-12s: %-12s\r\n' % (key, val))


#详细指数
def zs(city):
    url = 'http://www.weather.com.cn/data/zs/%s.html' % city
    r = request.urlopen(url)
    data = r.read()
    bj = json.loads(data)
    bj = bj['zs']

    for key, val in bj.items():
        print('%-12s: %-12s\r\n' % (key, val))



def menu():
    chose = {'0':sk,'1':cityinfo,'2':zs}
    while True:
        try:
            city = input('请输入您要查询的城市:').strip()   #菜单选项,为主程序
        except (KeyboardInterrupt,EOFError):
            print('Bye Bye!')
            exit()                                       #输入城市并做一系列判断
        if city_num().get(city):
            city = city_num().get(city)
            break
        else:
            print('对不起,没有这样的城市,请重新输入!')
    prompt='''\n\n************MENU***************
    [0]:天气实况
    [1]:城市信息
    [2]:详细指数
    [3]:退出
    >>>'''


    while True:
        try:                                        #输入菜单选项,来选择功能
            ch = input(prompt).strip()
        except (KeyboardInterrupt,EOFError):
            print('Bye Bye!')
            exit()
        if ch not in chose:
            continue

        if ch == '3':
            print('Bye Bye!')
            exit()

        chose[ch](city)



if __name__ == '__main__':
    menu()






