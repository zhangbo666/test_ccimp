__author__ = 'zhangbo'

from db_config.talkQueryUserInfo import talk_query_user_info_id_success
from externalClass.adminLogin import adminLogin

def accountStatus(account_status_data,user_id):

    '''
    账号状态
    :param account_status_data:账号状态数据
    :param user_id:用户ID
    :return:返回账号状态数据
    '''

    print ("account_status_data-->",account_status_data)
    print ("user_id-->",user_id)

    accountStatusUrl = "http://crm.51talk.com/admin/user/freezeUser.php?user_id=" \
                       + str(user_id) + "&type=" + str(account_status_data)

    #调取后台登录接口
    admin_login = adminLogin()

    accountstatus = admin_login.get(url=accountStatusUrl)

    if accountstatus.ok == True:

        return True

    else:

        return False

if __name__ == '__main__':

    mobile = '18611221275'

    # account_status_data = 'freeze'
    account_status_data = 'on'

    user_id = '1587373327'

    accountStatusUrl = "http://crm.51talk.com/admin/user/freezeUser.php?user_id=" \
                       + str(user_id) + "&type=" + str(account_status_data)

    print (accountStatusUrl)

    #调取后台登录接口
    admin_login = adminLogin()

    accountstatus = admin_login.get(url=accountStatusUrl)

    if accountstatus.ok == True:

        print (True)
        print (type(True))




