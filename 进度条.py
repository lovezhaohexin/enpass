#!/usr/bin/env python3

# 案例3:编写类进度条程序
# 1.  在屏幕上打印20个#号
# 2.  符号@从20个#号穿过
# 3.  当@符号到达尾部,再从头开始

import sys
import time
def ppy():
    conunter = 19
    n = 0
    while True:
        n+=1
        print('\r%s@%s' % ('#'*n,'#'*(conunter-n)),end='')
        time.sleep(0.3)
        if n == 19:
            n = 0

if __name__ == '__main__':
    ppy()