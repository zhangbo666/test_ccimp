__author__ = 'zhangbo'

from externalClass.adminLogin import adminLogin


def userIdentity(user_identity_data,user_id):

    '''
    获取手机号验证状态
    :param user_identity_data:用户身份
    :param user_id:用户ID
    :return:返回用户身份状态数据
    '''

    print (user_identity_data)
    print (user_id)

    userIdentityUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    userIdentityTata = {

        'field': 'is_buy',
        'id': user_id,
        'is_buy': user_identity_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    useridentity = admin_login.post(url=userIdentityUrl,data=userIdentityTata)

    print ("返回-->",useridentity.text)

    return useridentity.text

if __name__ == '__main__':

    mobile = '18611221275'

    user_identity_data = 'free'
    # user_identity_data = 'buy'

    user_id = '800021389'

    userIdentityUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    userIdentityTata = {

        'field': 'is_buy',
        'id': user_id,
        'is_buy': user_identity_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    useridentity = admin_login.post(url=userIdentityUrl,data=userIdentityTata)

    print ("返回-->",useridentity.text)



