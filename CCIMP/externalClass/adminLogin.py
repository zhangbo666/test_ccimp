# -*- coding: utf-8 -*-:


'''
@author: zhangbo

@file: adminLogin.py

'''

import requests
from externalClass.md import mdFile

def adminLogin():
    '''
    后台登录
    使用：实例化后直接调请求方法
    '''

    admin_pwd = '123456'
    admin_pwd = mdFile(admin_pwd)

    adminLoginUrl = 'http://crm.51talk.com/admin/login.php'
    data = {
        'user_name': 'admin',
        'password': admin_pwd,
        'ref': '',
        'user_type': 'admin',
        'Submit': '登 录',
        'login_type':'tmp'
    }
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
    }
    request = requests.Session()

    aa = request.post(url=adminLoginUrl, data=data, headers=head)
    # print ("aa-->",aa)

    return request

if __name__ == '__main__':

    url = 'http://crm.51talk.com/Stu_List/index?is_buy=All&user_id=' + \
          str(800003511) + \
          '&student_id=&email=&skype_id=&qq=&mobile=&agent=&submit=Search'

    url1 = 'http://crm.51talk.com/Stu_List/index?is_buy=All&user_id=&student_id=&email=&skype_id=&qq=&mobile=' + \
          str(18611220000) + \
          '&agent=&submit=Search'

    test = adminLogin()

    info = test.get(url=url)

    print(info.text,info.status_code)