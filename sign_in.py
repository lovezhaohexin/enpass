#!/usr/bin/env python3
#模拟用户登陆信息系统
# 1.  支持新用户注册,新用户名和密码注册到字典中
# 2.  支持老用户登陆,用户名和密码正确提示登陆成功
# 3.  主程序通过循环询问进行何种操作,根据用户的选择,执行注册或是登陆操作

#
import getpass
userdb = {}
def regiter():
    username = input('用户名：')
    passwd = input('密码：')
    if username in userdb:
        print('用户%s已经存在' % username)
    else:
        userdb[username] = passwd



def login():
    username = input('用户名：')
    passwd = getpass.getpass('密码：') #getpass.getpass 可以实现隐形输入密码
    if userdb.get(username) == passwd:
        print('\033[32;1m登陆成功！\033[0m')
    else:
        print('\033[31;1m登陆失败！\033[0m')


def show_menu():
    mds = {'0':regiter,'1':login}
    prompt = '''*********************MENU************************
    [0]regiter     [1]login       [2]quit    

请输入【0/1/2】：'''
    while True:
        choice = input(prompt).strip()
        if choice not in ['0','1','2']:
            print('\033[31;1m无效选择\033[0m')
            continue
        if choice == '2':
            break
        mds[choice]()



if __name__ == '__main__':
    show_menu()