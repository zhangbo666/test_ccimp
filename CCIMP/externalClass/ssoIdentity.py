__author__ = 'zhangbo'

import requests
import re
from externalClass.adminLogin import adminLogin
import json


def ssoIdentity(sso_identity_data, user_id):
    '''
    sso身份修改
    :param sso_identity_data:sso数据
    :param user_id:用户ID
    :return:返回修改后sso数据
    '''

    # print (sso_identity_data)
    # print (user_id)

    ssoIdentityUrl = "http://www.51talk.com/Admin/Sso/roleset"

    ssoIdentityTata = {

        'uid': user_id,
        'role_set': sso_identity_data

    }

    # 调取后台登录接口
    admin_login = adminLogin()
    # print (admin_login.cookies)

    res_cookies = requests.utils.dict_from_cookiejar(admin_login.cookies)
    # print(res_cookies)

    tms_training_sso = res_cookies['tms_training_sso']
    price_show_type = res_cookies['price_show_type']
    PHPSESSID = res_cookies['PHPSESSID']

    cookies_str = 'rmbUser=true; password=123456; username=admin; global=787d57ad-28f6-49cc-a019-ef6584385c9c; SpMLdaPx_uuid=7869567572; uuid=eyJpdiI6IkR3VlwvR3FwV3VtYkZKK0RoRGVSZVpnPT0iLCJ2YWx1ZSI6IjFpTmlcL0lqTmF3a2xkMExoZmczRDRTXC9jYU1WOGI2UTJTc2kzek4raVA1U1hGYzErVFd3bHBOVFVxMFdwcXYyQSIsIm1hYyI6IjRmNzk0NzRlODI2NzQ1OGQwN2NhNjMyNTkzMWQwYjRlNjNiOGRhYWMwOTU1MDVkNTAyYTg0MmQ2NzUzZjU4NjUifQ%3D%3D; _pykey_=bde0614d-ec18-5123-8329-36524716885e; __utma=108070726.1807357615.1594622322.1594622322.1594974741.2; __utmz=108070726.1594974741.2.2.utmcsr=51talk.com|utmccn=(referral)|utmcmd=referral|utmcct=/user/index; 51talkpassuser=; price_show_type=pst_str; from_url=www.51talk.com%2Ccrm.51talk.com; PHPSESSID=p_str; servChkFlag=sso; Hm_lvt_cd5cd03181b14b3269f31c9cc8fe277f=1595091009,1595093317,1595215175,1595301436; Hm_lvt_12bb113d16ba4f5e8689b4a441a1d6a2=1594974743,1595097508,1595216209,1595302584; visitid=2925CF309C1C13F944166749FE0D57D4MNTTUF40NYzWMx3rNMTjEA3xNMwQO0O0OO0O0OO0O0OO0O0O; PHPSESSID_51talk=eyJpdiI6ImlaN0R0QzUwQnZwbHlwRkJGbWtcL1pBPT0iLCJ2YWx1ZSI6IkJoSmpIZnZlbDFNQzNIS2ZZM2tuRE5Eb0gycGw3bUwwWitaZmF0U2llTDcrK2JTUFdiM2pTY1IyYlI1VUFqVUFlZGN1bjl3ZVBSSVB4T0JseDcyOHF3PT0iLCJtYWMiOiJmOWZjYzVkNDRjYmZhMjlmN2I4OGY1YzA4MDQ5MGI1YjI1MjA2NThkOWU4NGQ4NjdkZDFhMjRmNTk1ZTZkMWU0In0%3D; unique_id=24672ffd9800868a3d5c6500b9a5d104; SpMLdaPx_sid=4831267554; home_captcha=15953144407041; pt_6f1ebac9=uid=eHqYfV-lni/ibtB5wCKqiQ&nid=0&vid=DPU0KCygGDF0RSFq2nuJfw&vn=34&pvn=1&sact=1595314454074&to_flag=0&pl=Alw12N2ud5Hn69BFWu8a0w*pt*1595314454074; pt_s_6f1ebac9=vt=1595314454074&cad=; SpMLdaPx_poid=1547; Hm_lpvt_cd5cd03181b14b3269f31c9cc8fe277f=1595314673; Hm_lpvt_12bb113d16ba4f5e8689b4a441a1d6a2=1595314673; admin_code=826a7ee4b213db94bfdf092db5e2411c; tms_training_sso=tts_str; SpMLdaPx_pvid=1595314786383'

    str_a = ['p_str', 'tts_str', 'pst_str']

    cookies_str_ = cookies_str

    for str_b in str_a:

        if str_b == 'p_str':

            cookies_str_ = cookies_str_.replace(str_b, PHPSESSID)

        elif str_b == 'tts_str':

            cookies_str_ = cookies_str_.replace(str_b,tms_training_sso)

        elif str_b == 'pst_str':

            cookies_str_ = cookies_str_.replace(str_b,price_show_type)

        cookies_str_ = cookies_str_

    # print (cookies_str_)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '26',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies_str_,
        'Host': 'www.51talk.com',
        'Origin': 'http://www.51talk.com',
        'Referer': 'http://www.51talk.com/Admin/sso/role',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    ssoidentity = admin_login.post(url=ssoIdentityUrl,data=ssoIdentityTata,
    							   headers=headers)

    return ssoidentity


if __name__ == '__main__':

    sso_identity_data = '11'

    user_id = '1587375078'

    sso_identity_result = ssoIdentity(sso_identity_data, user_id)
    # print ("返回的该sso身份为：",sso_identity_result.text)
    print ("返回的该sso身份为：",sso_identity_result.json())

    # data_result = sso_identity_result.json()['data']
    # print ("data返回值为：",data_result)