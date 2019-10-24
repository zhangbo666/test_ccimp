__author__ = 'zhangbo'

import re
from externalClass.adminLogin import adminLogin
from db_config.talkQueryUserInfo import talk_query_user_info_id_success

def getUserRole(user_id):

    getrole_url = 'https://www.51talk.com/Admin/Sso/getrole?uid=' + str(user_id)

    #调取后台登录接口
    admin_login = adminLogin()

    roleResult = admin_login.get(url=getrole_url)

    role_sso_text = re.findall(r'"data":"(.*)"', roleResult.text)[0]

    role_sso_text = role_sso_text.split(',')

    # print (role_sso_text)

    #11 菲小, 12 美小, 13 B2S, 14 成人, 15 达拉斯, 16 B2B, 17 美小达拉斯, 18 一对多班课, 19 1+2项目
    for user_role in role_sso_text:

        if user_role == '11':

                userRole = 11

        elif user_role == '12':

                userRole = 12

        elif user_role == '14':

                userRole = 14

        elif user_role == '19':

                userRole = 19


    return userRole

if __name__ == '__main__':

    mobile = '18611220000'

    userId = talk_query_user_info_id_success(mobile)

    getrole_url = 'https://www.51talk.com/Admin/Sso/getrole?uid=' + str(userId)

    #调取后台登录接口
    admin_login = adminLogin()

    roleResult = admin_login.get(url=getrole_url)

    # print (roleResult.text)

    role_sso_text = re.findall(r'"data":"(.*)"', roleResult.text)[0]

    # print (role_sso_text)

    role_sso_text = role_sso_text.split(',')

    print (role_sso_text)
