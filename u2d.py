#!/usr/bin/env python3
# 写unix2dos的程序
# 1.  Windows文本文件的行结束标志是\r\n
# 2.  类unix文本文件的行结束标志是\n
# 3.  编写程序,将unix文本文件格式转换为windows文
# 本文件的格式


import sys
# import os
#
def unix2dos(fname):
#     if not os.path.exists(fname):
#         print('')

    dst_fname = fname+'.txt'
    with open(fname) as src_fobj:
        with open(dst_fname,'w') as dst_fobj:
            for line in src_fobj:

                line = line.rstrip('\n\r')+'\r\n'
                dst_fobj.write(line)

if __name__ == '__main__':

    try:
        unix2dos(sys.argv[1])
    except IndexError:
        print('*******Usage: ./u2d  <filename>********')
    