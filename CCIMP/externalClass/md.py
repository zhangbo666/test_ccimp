__author__ = 'zhangbo'

import hashlib
from Crypto.Cipher import AES
import base64

def mdFile(admin_pwd):

    a = hashlib.md5()

    a.update(admin_pwd.encode(encoding='utf-8'))

    return (a.hexdigest())


def base64File(admin_pwd):

    b = base64.b64encode(admin_pwd.encode())  # 加密
    result = b.decode()
    print(result,type(result))

    b = base64.b64decode(result)  # 解密
    print(b,type(b.decode()))


if __name__ == '__main__':

    # password = '51talkgc'
    # password_result = mdFile(password)
    # print (password_result,type(password_result))


    # password = 'e761bbb1575e7de297f90f0f36628b66'
    # password = '51talkgc'
    password = '111111'
    # print (password,type(password))

    password_result = base64File(password)