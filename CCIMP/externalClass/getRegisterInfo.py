import requests,re
import datetime

#校验手机号是否已注册
def is_used_phoneNumber(phoneNumber):

    #请求地址
    mobileValiDateUrl = 'http://www.51talk.com/Ajax/homeMobilEvalidate'

    #请求参数手机号
    check_mobile = {"mobile": phoneNumber}

    status_code = ''

    try:
        res = requests.request('Post',url=mobileValiDateUrl,data=check_mobile)

        #获取是否注册状态 1 未注册  0 已注册
        status_code = res.text[10]

        #返回注册状态
        return status_code

    except BaseException as e:

        print('调用短信登录接口不正确！信息：%s'%e)



if __name__ == '__main__':

    mobile = '18911666666'

    # 用户登录，查询该手机的账户与密码内容
    is_used_phoneNumber(mobile)