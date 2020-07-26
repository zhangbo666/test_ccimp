__author__ = 'zhangbo'

import re

from externalClass.adminLogin import adminLogin
from externalClass.public_configure import global_configure

from db_config.talkQueryUserInfo import talk_query_user_info_id_success


def getUserRole(user_id):

    userRole = ''

    getrole_url = 'http://www.51talk.com/Admin/Sso/getrole?uid=' + str(user_id)
    # print (getrole_url)

    #调取后台登录接口
    admin_login = adminLogin()
    # print ("admin_login",admin_login)

    roleResult = admin_login.get(url=getrole_url)
    # print ("roleResult.text-->",roleResult.text)

    try :

        role_sso_text = re.findall(r'"data":"(.*)"', roleResult.text)[0]
        # print ("role_sso_text-->",role_sso_text)

        role_sso_text = role_sso_text.split(',')
        # print ("用户角色为：",role_sso_text)

        #11 菲小, 12 美小, 13 B2S, 14 成人, 15 达拉斯, 16 B2B, 17 美小达拉斯, 18 一对多班课, 19 1+2项目
        #新注册学员，还未选身份，sso返回为空，默认为成人（14）
        for user_role in role_sso_text:

            if user_role == '11':

                    userRole = 11

            elif user_role == '12':

                    userRole = 12

            elif user_role == '14':

                    userRole = 14

            elif user_role == '19':

                    userRole = 19

            elif user_role == '18':

                    userRole = 18

            elif user_role == '13':

                    userRole = 13

            elif user_role == '':

                    userRole = 14

    except:

        error_text = "请重新登录4"

        try:

            for error_text in roleResult.text:

                userRole = global_configure.login_error_message

        except:

                userRole = global_configure.query_role_message

    return userRole

if __name__ == '__main__':

    mobile = '18611222647'

    userRole = ''

    userId = talk_query_user_info_id_success(mobile)

    getrole_url = 'https://www.51talk.com/Admin/Sso/getrole?uid=' + str(userId)

    #调取后台登录接口
    admin_login = adminLogin()

    roleResult = admin_login.get(url=getrole_url)
    # print (roleResult.text)

    role_sso_text = re.findall(r'"data":"(.*)"', roleResult.text)[0]
    # print (role_sso_text)

    role_sso_text = role_sso_text.split(',')
    # print (role_sso_text)
