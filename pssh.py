#!/usr/bin/env python3


import paramiko
import sys
import getpass
import threading


def rcmd(host,password=None,command=None,user='root',port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user,password=password,port=port)
    stdin,stdout,stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('\033[32;1m[OUT] %s\033[0m :\n\033[35;1m%s\033[0m' % (host,out.decode()))
    if err:
        print('\033[31;1m[ERR] %s\033[0m :\n\033[35;1m%s\033[0m' % (host,err.decode()))
    ssh.close()


if __name__ == '__main__':
    #rcmd('192.168.4.100',password='123456',command='id root;id tom')
    if len(sys.argv) != 3:
        print('Usage: %s <ipfile> "command"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file!:',sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    command = sys.argv[2]
    password = getpass.getpass()

    with open(ipfile) as fobj:
        for line in ipfile:
            ip = line.strip()
            t = threading.Thread(target=rcmd,args=(ip,password,command))
            t.start()
            