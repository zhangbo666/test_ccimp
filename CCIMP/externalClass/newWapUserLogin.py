# -*- coding: utf-8 -*-：

'''
@author: zhangbo

@file: newWapUserLogin.py

@time: 2020/09/11 14:00
'''


import re,requests

from externalClass.publicKeyRsa import publicKeyRsa


def newWapUserLogin(mobile,password):
    '''
    用户登录函数
    使用方法：直接实例化此函数即可，实例化的对象直接调用请求方法
    :param mobile: 用户手机，默认参数
    :param password: 用户加密后的密码，默认参数
    :return: 返回的是requests.sessions.Session
    '''
    try:
        request = requests.Session()
        wapUrl_sso = 'https://login.51talk.com/ajax/access/ticket?client=1&callback=__jp0004978618940560331'
        at = request.get(url=wapUrl_sso)
        # print ("at-->",at.text)
        atList = re.findall(r'"at":"(.*)"',at.text)
        # print ("atList-->",atList)
        ajax_wap_login_url = 'https://login.51talk.com/ajax/student/signin'
        ajax_data = {
            'at': atList[0],
            'client': '1',
            'ufu':'dapan_newlanjie',
            'username': mobile,
            'data_type':'json',
            'password': password,
        }

        headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '136',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie':'PHPSESSID=gugsrib7gl37fkcdamfdpfue11; uuid=6f2b2cc2-83b5-4180-aa44-b7cc68c4f16a; servChkFlag=sso; SpMLdaPx_poid=1; SpMLdaPx_pvid=1592007587997; SpMLdaPx_uuid=8205672434; SpMLdaPx_sid=8221223284; Hm_lvt_cd5cd03181b14b3269f31c9cc8fe277f=1592007588; Hm_lpvt_cd5cd03181b14b3269f31c9cc8fe277f=1592007588; Hm_lvt_12bb113d16ba4f5e8689b4a441a1d6a2=1592007588; Hm_lpvt_12bb113d16ba4f5e8689b4a441a1d6a2=1592007588',
        'Host': 'login.51talk.com',
        'Origin': 'http://login.51talk.com',
        # 'Referer': 'http://login.51talk.com/wap/user?from_url=http%3A%2F%2Fsale.51talk.com%2Fwap%2Fmall%3Fredirect%3Dsso%26redirect%3Dsso%26redirect%3Dsso',
        # 'Referer':'http://login.51talk.com/web/register',
        'Upgrade-Insecure-Requests': '1',
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

        #调用登录接口
        ajax_wap_login = request.post(url=ajax_wap_login_url,data=ajax_data,headers=headers)
        # print ("ajax_wap_login-->",ajax_wap_login.json())

        return request

    except BaseException as e:

        print('调用登录方法报错！信息：%s'%e)


if __name__ == '__main__':

    # 密码进行加密
    pwd = publicKeyRsa('816944')

    # 用户登录
    req = newWapUserLogin('18611222888',pwd)

    # baseInfo_url = 'http://sale.51talk.com/api/mall/baseInfo'

    baseInfo_url = 'https://igateway.51talk.com/talkplatform_page_router/v1/router/config?appkey=fx_h5&timestamp=1599803606178&id=111111111111001001'

    baseInfo_result = req.get(url=baseInfo_url)

    print (baseInfo_result.text)