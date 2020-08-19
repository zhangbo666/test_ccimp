# -*- coding: utf-8 -*-：  

'''
@author: zhangbo

@file: wapUserLogin.py

@time: 2020/08/19 13:44
'''


import re,requests

from externalClass.publicKeyRsa import publicKeyRsa


def wapUserLogin(mobile,password):
    '''
    用户登录函数
    使用方法：直接实例化此函数即可，实例化的对象直接调用请求方法
    :param mobile: 用户手机，默认参数
    :param password: 用户加密后的密码，默认参数
    :return: 返回的是requests.sessions.Session
    '''
    try:
        request = requests.Session()
        wapUrl_sso = 'http://login.51talk.com/sso/prelogin?client=2&callback=__jp1'
        la = request.get(url=wapUrl_sso)
        print ("laList-->",la.text)
        laList = re.findall(r'"la":"(.*)"',la.text)
        print ("laList-->",laList)
        ajax_wap_login_url = 'http://login.51talk.com/ajax/login'
        ajax_data = {
            'user_name': mobile,
            'la': laList[0],
            'password': password,
            'client': '2',
            # 'from_url': ''
            'from_url': 'http://sale.51talk.com/wap/mall?redirect=sso'
        }
        #调用登录接口
        ajax_wap_login = request.post(url=ajax_wap_login_url,data=ajax_data)
        print ("ajax_wap_login-->",ajax_wap_login.json())
        
        form_url = ajax_wap_login.json()['res']['from_url']
        print ("form_url-->",form_url)

        #sso重定向跳转autologin
        sso_autologin = request.get(url=form_url)
        print ("sso_autologin-->",sso_autologin.text)

        return request

    except BaseException as e:

        print('调用登录方法报错！信息：%s'%e)


if __name__ == '__main__':

    # 密码进行加密
    pwd = publicKeyRsa('111111')

    # 用户登录
    req = wapUserLogin('18611221275',pwd)

    baseInfo_url = 'http://sale.51talk.com/api/mall/goodsList?page=1&goods_type=1'

    baseInfo_result = req.get(url=baseInfo_url)

    print (baseInfo_result.json())