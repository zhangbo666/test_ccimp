__author__ = 'zhangbo'

# -*- coding: utf-8 -*-：

import requests,re
from externalClass.smsLoginSmsContent import smsLoginSmsContent


def smsLoginCode(username,password,mobile_text):

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
        search_code_text = re.findall(r'<td>(.*)</td>',ajax_login.text)
        # print ("search_code_text-->",search_code_text)

        for search_code in search_code_text:

            if '【51Talk】' in search_code:

                if search_code[13:21] == '是您的手机验证码':

                    return (search_code[8:13])

                elif search_code[14:22] == '是您的手机验证码':

                    return (search_code[8:14])



            elif '是您的手机验证码' in search_code:

                #团购
                if search_code[0:6].isdigit():

                    return (search_code[0:6])

                #非团购
                else:

                    return (search_code[0:5])

            elif '中华少年说' in search_code:

                    return (search_code[6:12])

            else:

                pass

    except BaseException as e:

        print('调用短信登录接口不正确！信息：%s'%e)


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

            elif '亲爱的学员感谢注册51Talk！' in search_text:

                print ("sms_content-->",search_text)

    except BaseException as e:

        print('调用短信登录接口不正确！信息：%s'%e)


if __name__ == '__main__':

    mobile = '18611221831'

    # 用户登录，查询短信验证码
    sms_code = smsLoginCode('zhangbo','zhangbo2019',mobile)

    if sms_code == None:

        print ("未找到该手机的短信验证码！")

    else:

        print ('sms_code-->',sms_code)

    smsLoginSmsContent('zhangbo','zhangbo2019',mobile)