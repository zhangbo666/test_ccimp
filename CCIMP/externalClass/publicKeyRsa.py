# -*- coding: utf-8 -*-：

'''
@__author__ = 'zhangbo'

@file: publicKeyRsa.py
'''

import requests,re
import base64
import os

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


def publicKeyRsa(password):

    '''
    获取密码加密
    :param password: 用户加密后的密码，默认参数
    :return: 返回的是加密后的密码
    '''

    #字符串转为bytes
    pwd = bytes(password,encoding='utf8')
    # print ("pwd-->",pwd)
    url = 'http://login.51talk.com/sso/publickey?callback=pubkeyCallBack&client=1'

    #获取加密公钥
    public_key_info = requests.get(url=url)
    info = r'%s' % public_key_info.text.strip()
    # print ("info-->",info)

    #正则提取公钥
    public_key = re.findall(r'"rsa_pub":"(.*)"', info)[0]
    # print ("public_key-->",public_key)

    #将公钥写入文件
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    BASE_FILE_DIR = BASE_DIR + '/public_key/' + 'key.txt'

    with open(BASE_FILE_DIR, 'w') as f:
        f.write(public_key.replace("\\n", "\n").replace("\\/", "/"))

    rsa_public_key = open(BASE_FILE_DIR, 'r').read()

    #将密码加密
    rsakey = RSA.importKey(rsa_public_key)
    # print ("rsakey-->",rsakey)

    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # print ("cipher-->",cipher)

    cipher_text = base64.b64encode(cipher.encrypt(pwd))
    # print ("cipher_text-->",cipher_text)

    #bytes转为字符串
    pwd = bytes.decode(cipher_text, encoding='utf8')
    # print ("pwd-->",pwd)

    return pwd

if __name__ == '__main__':

    pwd = publicKeyRsa('111111')
    print (pwd)