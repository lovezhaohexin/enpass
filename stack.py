# 1.  栈是一个后进先出的结构
# 2.  编写一个程序,用列表实现栈结构
# 3.  需要支持压栈、出栈、查询功能


#/usr/bin/env python3
#出栈
stack = []
def push_it():
    data = input('data to push').strip()
    if data:
        stack.append(data)


#压栈
def pop_it():
    if stack:
        print('from stack,poped \033[31;1m%s\033[0m' % stack.pop())
    else:
        print('\033[31;1mEmpty stack\033[0m')

#查看栈
def view_it():
    print('\033[32;1m%s\033[0m' % stack)

#与用户交互的菜单，也是整个程序的主程序
def show_menu():
    prompt = '''
    (0) push it
    (1) pop it
    (2) view it
    (3) quit'''
    while True:
        cmds = {'0':push_it,'1':pop_it,'2':view_it}
        choice = input(prompt).strip()
        #判断输入是否符合菜单，然后根据用户输入的选项，来调取与之对应的功能
        if choice not in ['0','1','2','3']:
            print('\033[31;1m%s\033[0m' % 'Ivalid choice,please try again!')
            continue


        cmds[choice]() #应用字典简化程序，0--->push_it  1---> pop_it  2---> view_it

        # if choice == '3':
        #     break
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()


if __name__ == '__main__':
    show_menu()