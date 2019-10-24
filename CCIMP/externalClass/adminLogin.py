# -*- coding: utf-8 -*-:


'''
@author: zhangbo

@file: adminLogin.py

'''

import requests

def adminLogin():
    '''
    后台登录
    使用：实例化后直接调请求方法
    '''
    adminLoginUrl = 'http://www.51talk.com/admin/login.php'
    data = {
        'user_name': 'admin',
        'password': '123456',
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

    return request

if __name__ == '__main__':

    url = 'http://crm.51talk.com/admin/user/stu_list.php?is_buy=All&user_id=' + \
          str(800003511) + \
          '&student_id=&email=&skype_id=&qq=&mobile=&agent=&submit=Search'

    test = adminLogin()

    info = test.get(url=url)

    print(info.text,info.status_code)