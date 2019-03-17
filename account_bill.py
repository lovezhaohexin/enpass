#!/usr/bin/env python3

# 记账程序
# 1.  假设在记账时,有一万元钱
# 2.  无论是开销还是收入都要进行记账
# 3.  记账内容包括时间、金额和说明等
# 4.  记账数据要求永久存储
import time
import pickle





flist = [[0,10000,'初始本金']]  #全局变量


#记录功能
def insert ():
    global flist
    storelist = []
    flistfile = 'flist.data'
    f = open(flistfile,'wb')
    pickle.dump(flist,f)
    f.close()
    it = input('你还要继续吗?[Yy/Nn]').strip()
    if it  in 'nN':
        print('Bye Bye!!!')
        exit()







#收入操作
def income():
    global flist
    account = []
    try:
        add = int(input('请输入您本次的收入:').strip())
    except ValueError:
        print('此输入只支持数字!!!,程序将退回到menu菜单')
        menu()
    except EOFError:
        print('Bye Bye!!!')
        exit()
    incomet = time.strftime('%Y-%m-%d')
    inform = input('请输入本次操作的备注:')
    print(incomet)
    list = [incomet,add,inform]
    flist.append(list)
    flist[-1][1] = add + flist[-2][1]

    insert()



#支付操作
def pay():
    global flist
    account = []
    sub = int(input('请输入您本次的支出:').strip())
    payt = time.strftime('%Y-%m-%d')
    inform = input('请输入本次操作的备注:')
    print(payt)
    list = [payt,sub,inform]
    flist.append(list)
    flist[-1][1] = flist[-2][1] - sub

    insert()

#查看功能
def view():
    readlist = []
    with open('flist.data','rb') as f:
        readlist = pickle.load(f)
    print('%-14s%-12s%-12s' % ('data','balance','info'))
    for record in readlist:
        print('%-14s%-12s%-12s' %tuple(record))






def menu():
    cmds = {'0':income,'1':pay,'2':view}
    while True:
        prompt = '''
        [0]/收入
        [1]/支出
        [2]/查询
        [3]/退出
        请输入[0/1/2/3]:'''
        try:
            data = input(prompt).strip()
        except ValueError:
            print('无效输入!,输入只能为0-3的一个数字')
        except EOFError:
            print('Bye Bye!!!')
            break
        if data not in ['0','2','3','1']:
            print('无效输入!,请输入0-3之间的一个数字')
            continue
        if data == '3':
            print('ByeBye!')
            break
        cmds[data]()

if __name__ == '__main__':
    menu()

