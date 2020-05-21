__author__ = 'zhangbo'

from db_config.talkQueryUserInfo import talk_query_user_info_id_success
from externalClass.adminLogin import adminLogin

def nickName(nick_name_data,user_id):

    '''
    获取用户昵称
    :param nick_name_data:用户昵称数据
    :param user_id:用户ID
    :return:返回用户昵称nickName获取的状态数据
    '''

    print (nick_name_data)
    print (user_id)

    nickNameUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    nickNameTata = {

        'field': 'nick_name',
        'id': user_id,
        'nick_name': nick_name_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    nickname = admin_login.post(url=nickNameUrl,data=nickNameTata)

    print ("返回-->",nickname.text)

    return nickname.text

if __name__ == '__main__':

    mobile = '18611221275'

    nick_name_data = '1275'

    userId = '800021389'

    # userId = talk_query_user_info_id_success(mobile)

    nickNameUrl = 'http://crm.51talk.com/admin/user/do_update_email.php'

    nickNameTata = {

        'field': 'nick_name',
        'id': userId,
        'nick_name': nick_name_data,

    }

    #调取后台登录接口
    admin_login = adminLogin()

    nickname = admin_login.post(url=nickNameUrl,data=nickNameTata)

    data_nickname = nickname.text

    print (data_nickname)




