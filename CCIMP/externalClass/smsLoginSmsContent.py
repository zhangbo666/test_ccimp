__author__ = 'zhangbo'

# -*- coding: utf-8 -*-：

import requests,re
import datetime


'''
authon:郭靖
'''
def is_contain_chinese(check_str):

    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:

        if u'\u4e00' <= ch <= u'\u9fff':

            return True

    return False

def smsLoginSmsContent(username,password,mobile_text,search_content):

    try:

        request = requests.Session()

        #获取当前时间（天）
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')

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

        #张波
        # search_url = 'http://sms.51talk.com/Admin/SendSms/index?send_time=&mobile=' + \
        #              str(mobile_text) + '&sms_id='

        #郭靖
        search_url = 'http://sms.51talk.com/Admin/SendSms/index?send_time=' + \
                     str(now_time) + '&mobile=' + \
                     str(mobile_text) + '&sms_id=' + '&msg=' + \
                     str(search_content)

        #调用搜索手机号接口
        ajax_login = request.get(url=search_url)
        # print ("ajax_login-->",ajax_login.text)

        #正则表达式截取短信内容
        search_sms_text = re.findall(r'<td>(.*)</td>',ajax_login.text)
        # print ("search_sms_text-->",search_sms_text)

        #返回短信内容 默认为空
        respondContent = "今日最新消息："

        #张波
        '''
        for search_text in search_sms_text:

            if '系统已自动给您分配51talk账号' in search_text:

                # print ("sms_content-->",search_text)
                return search_text

            elif '亲爱的学员感谢注册51Talk！' in search_text:

                # print ("sms_content-->",search_text)
                return search_text
        '''

        #郭靖
        for search_text in search_sms_text:

            if is_contain_chinese(search_text):

                respondContent = respondContent + '\n' + search_text

        return respondContent

    except BaseException as e:

        print('调用短信登录接口不正确！信息：%s'%e)


if __name__ == '__main__':

    mobile = '15102700011'

    content_text = "用户"

    # 用户登录，查询该手机的账户与密码内容
    smsLoginSmsContent('zhangbo','zhangbo2019',mobile,content_text)
