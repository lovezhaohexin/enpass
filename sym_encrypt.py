#!/usr/bin/env python3

import sys, os


# 用户没有输入路径地址,则设置
def sym_encrpt(src_file=None):
    # 用户没有输入文件路径,如果路径为None
    # print(type(src_file))
    if not src_file:
        print('清输入要加密的文件路径')
        return None

    # 用户输入的文件不存在,如果文件不存在,返回None并退出
    if not os.path.exists(src_file):
        print('你输入的文件不存在,请重新输入')
        return None
    if src_file.endswith('.en'):
        dst_file = src_file.rsplit('.', 1)[0]
    else:
        dst_file = src_file + '.en'

    with open(src_file, 'r') as rf:
        with open(dst_file, 'w') as wf:
            while True:
                data = rf.readline()
                # print(data)
                if not data:
                    break

                # data-->list(每个字符 --> 加密后的字符)
                # ROT13  加密应射表
                en_dict = {}
                for i in 65, 97:
                    for j in range(26):
                        en_dict[chr(i + j)] = chr(i + (j + 13) % 26)

                data_en = ''.join([en_dict.get(c, c) for c in data])
                # print(data_en)
                wf.write(data_en)
    # 删除源文件
    os.remove(src_file)

    # 返回目标文件路径地址
    return dst_file


if __name__ == '__main__':
    # if sys.argv[0]:
    #     print('清输入要家密的文件路径')
    try:
        receive_path = sys.argv[1]
    except IndexError:
        print('+' + '*' * 48 + '+')
        print('+{:^48}+'.format("Usage:  ./sym_encrypt.py  file_path"))
        print('+' + '*' * 48 + '+')
    else:
        # print(receive_path)
        path = sym_encrpt(receive_path)
        if path:
            if path.endswith('.en'):
                print("加密文件路径:%s" % path)
            else:
                print("解密文件路径:%s" % path)
