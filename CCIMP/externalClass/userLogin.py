# -*- coding: utf-8 -*-：  

'''
@author: andong

@file: userLogin.py

@time: 2019/7/26 14:46
'''
import requests,re
from externalClass.publicKeyRsa import publicKeyRsa
from externalClass.getPackageDetail import getPackageDetail
from externalClass.public_configure import global_configure

def userLogin(mobile,password):
    '''
    用户登录函数
    使用方法：直接实例化此函数即可，实例化的对象直接调用请求方法
    :param mobile: 用户手机，默认参数
    :param password: 用户加密后的密码，默认参数
    :return: 返回的是requests.sessions.Session
    '''
    try:
        request = requests.Session()
        url_sso = 'http://login.51talk.com/sso/prelogin?callback=preLoginCallBack&client=1'
        la = request.get(url=url_sso)
        laList = re.findall(r'"la":"(.*)"',la.text)
        # print ("laList-->",laList)
        ajax_login_url = 'http://login.51talk.com/ajax/login'
        ajax_data = {
            'auto_login':'1',
            'user_name': mobile,
            'la': laList[0],
            'password': password,
            'client': '1',
            'group': '0',
            'from_url': ''
        }
        #调用登录接口
        ajax_login = request.post(url=ajax_login_url,data=ajax_data)
        print ("ajax_login-->",ajax_login.json())

        try:
            form_url = ajax_login.json()['res']['from_url']
            # print ("form_url-->",form_url)

            #sso重定向跳转autologin
            sso_autologin = request.get(url=form_url)
            # print ("sso_autologin-->",sso_autologin.text)

            #sso重定向调转用户中心
            index_url = 'http://www.51talk.com/sso/index'
            indxe = request.get(url=index_url)
            # print ("indxe-->",indxe.text)

            return request

        except:

            # print(global_configure.login_error_message)

            return global_configure.login_error_message

    except BaseException as e:

        print('调用登录方法报错！信息：%s'%e)

    # else:
    #     return request

if __name__ == '__main__':

    # 密码进行加密
    pwd = publicKeyRsa('123456')

    # 用户登录
    req = userLogin('18611772708',pwd)

    # 获取该账户下可启用的套餐详情
    pointDetailNewJson = getPackageDetail(req)

    print ("该账户下所有套餐信息：",pointDetailNewJson)