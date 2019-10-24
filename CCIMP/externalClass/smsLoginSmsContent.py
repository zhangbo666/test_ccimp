__author__ = 'zhangbo'

# -*- coding: utf-8 -*-：

import requests,re

def smsLoginSmsContent(username,password,mobile_text):

    try:

        request = requests.Session()

        sms_login_url = 'http://sms.51talk.com/Admin/Login/user_login'
        sms_login_data = {

            'username':username,
            'password':password
        }
        sms_login_after = request.post(url=sms_login_url,data=sms_login_data)
        # print ("sms_login_after-->",sms_login_after.text)

        sms_welcome_url = 'http://sms.51talk.com/Admin/Welcome/index'
        sms_welcome_after = request.get(url=sms_welcome_url)
        # print ("sms_welcome_after-->",sms_welcome_after.text)

        search_url = 'http://sms.51talk.com/Admin/SendSms/index?send_time=&mobile=' + \
                     str(mobile_text) + '&sms_id='

        #调用搜索手机号接口
        ajax_login = request.get(url=search_url)
        # print ("ajax_login-->",ajax_login.text)

        #正则表达式截取短信内容
        search_sms_text = re.findall(r'<td>(.*)</td>',ajax_login.text)
        # print ("search_sms_text-->",search_sms_text)

        for search_text in search_sms_text:

            if '系统已自动给您分配51talk账号' in search_text:

                print ("sms_content-->",search_text)

    except BaseException as e:

        print('调用短信登录接口不正确！信息：%s'%e)


if __name__ == '__main__':

    mobile = '19014000114'

    # 用户登录，查询该手机的账户与密码内容
    smsLoginSmsContent('zhangbo','zhangbo2019',mobile)
