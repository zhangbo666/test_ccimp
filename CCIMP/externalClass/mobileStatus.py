__author__ = 'zhangbo'

from externalClass.adminLogin import adminLogin


def mobileStatus(mobile_status_data,user_id):

    '''
    获取手机号验证状态
    :param mobile_status_data:手机状态
    :param user_id:用户ID
    :return:返回手机号验证后状态数据
    '''

    # print (mobile_status_data)
    # print (user_id)

    mobileStatusUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    mobileStatusTata = {

        'field': 'is_check',
        'id': user_id,
        'is_check': mobile_status_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    mobilestatus = admin_login.post(url=mobileStatusUrl,data=mobileStatusTata)

    print ("返回-->",mobilestatus.text)

    return mobilestatus.text

if __name__ == '__main__':

    mobile = '18611221275'

    mobile_status_data = 'y'
    # mobile_status_data = 'n'

    userId = '800021389'

    mobileStatusUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    mobileStatusTata = {

        'field': 'is_check',
        'id': userId,
        'is_check': mobile_status_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    mobilestatus = admin_login.post(url=mobileStatusUrl,data=mobileStatusTata)

    data_mobilestatus = mobilestatus.text

    print (data_mobilestatus)




