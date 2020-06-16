__author__ = 'zhangbo'

import hashlib

def mdFile(admin_pwd):

    a = hashlib.md5()

    a.update(admin_pwd.encode(encoding='utf-8'))

    return (a.hexdigest())