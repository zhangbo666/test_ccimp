__author__ = 'zhangbo'

import requests
import re
import json

from externalClass.adminLogin import adminLogin
from externalClass.ssoIdentityPhpSessidConfig import phpsessid_data
from requests.exceptions import ReadTimeout,HTTPError,RequestException


def ssoIdentity(sso_identity_data, user_id):
    '''
    sso身份修改
    :param sso_identity_data:sso数据
    :param user_id:用户ID
    :return:返回修改后sso数据
    '''

    ssoIdentityUrl = "http://www.51talk.com/Admin/Sso/roleset"
    # getURl = "http://www.51talk.com/Admin/sso/role"
    ssoIdentityTata = {

        'uid': user_id,
        'role_set': sso_identity_data

    }

    # 调取后台登录接口
    admin_login = adminLogin()

    # 获取cookies
    # res_cookies = requests.utils.dict_from_cookiejar(admin_login.cookies)
    # print (res_cookies)

    # tms_training_sso = res_cookies['tms_training_sso']
    # price_show_type  = res_cookies['price_show_type']
    # admin_code        = res_cookies['admin_code']
    # PHPSESSID        = res_cookies['PHPSESSID']
    # PHPSESSID = '3234vhktom7jt4kdnkce9murs1'

    # r1 = requests.get(url=getURl,verify=False)

    res_cookies = {

        'PHPSESSID': phpsessid_data,
    }

    # cookies_str = 'rmbUser=true; username=admin; password=123456; PHPSESSID=p_str; price_show_type=pst_str; admin_code=ac_str; tms_training_sso=tts_str; gr_user_id=e21062de-2309-45c9-9975-7d316d26aca2; b71258c4284e7d6f_gr_session_id=f813a46c-78b3-4cc5-9210-9f9bb301895b; b71258c4284e7d6f_gr_session_id_f813a46c-78b3-4cc5-9210-9f9bb301895b=true; grwng_uid=cf6b5344-9ffa-46d3-8312-940708b6a1b1; from_url=crm.51talk.com%2Cocm.51talk.com; PHPSESSID_51Talk=eyJpdiI6IlwvbENhMCtreFprODBrVDZiMlFHWXRnPT0iLCJ2YWx1ZSI6IkNxZTNsYUtwU2krd3NDWmhGZ3RZNHd1Smt4YmdTSGlWY09ZRDdyZjF6bUxwRjVWRmloeFoxQnFEOG1pSVwvb3VZeEh4czd1NHZidFwvSG9URXlYdEsyM3c9PSIsIm1hYyI6IjNlZGIyYWQzMmFkNDIzZmU4MDEzOWQ3YjI2Zjk5MDQ0MTBmMGUwMjc5MzljZTczOTVhNjVlOTRjZjY4YWEyYjAifQ%3D%3D'

    # cookies_str_ = cookies_str

    # str_a = ['p_str','tts_str','pst_str','ac_str']
    # str_a = ['p_str','tts_str','pst_str']

    # str_b = ""

    # for str_b in str_a:

    #     if str_b == 'p_str':

    #         cookies_str_ = cookies_str_.replace(str_b, PHPSESSID)

    #     elif str_b == 'tts_str':

    #         cookies_str_ = cookies_str_.replace(str_b,tms_training_sso)

    #     elif str_b == 'pst_str':

    #         cookies_str_ = cookies_str_.replace(str_b,price_show_type)

    # elif str_b == 'ac_str':

    #     cookies_str_ = cookies_str_.replace(str_b,admin_code)

    # cookies_str_ = cookies_str_
    # print (cookies_str_)
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #     'Connection': 'keep-alive',
    #     'Content-Length': '26',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Cookie':res_cookies,
    #     'Host': 'www.51talk.com',
    #     'Origin': 'http://www.51talk.com',
    #     'Referer': 'http://www.51talk.com/Admin/sso/role',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    #     'X-Requested-With': 'XMLHttpRequest'
    # }

    try:

        # ssoidentity = admin_login.post(url=ssoIdentityUrl,data=ssoIdentityTata,headers=headers)
        ssoidentity = admin_login.post(url=ssoIdentityUrl, data=ssoIdentityTata, cookies=res_cookies)

        return ssoidentity

    except HTTPError:

        return ('httperror')

    except RequestException:

        return ('requesterror')


if __name__ == '__main__':

    sso_identity_data = '12'

    user_id = '1587375078'

    sso_identity_result = ssoIdentity(sso_identity_data, user_id)
    print("返回的该sso身份为：", sso_identity_result.text)
    print ("返回的该sso身份为：",sso_identity_result.json())