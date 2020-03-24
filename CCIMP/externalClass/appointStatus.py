# -*- coding: utf-8 -*-：

__author__ = 'zhangbo'



from externalClass.adminLogin import adminLogin

def appointStatus(req,appointID):

    #调取后台约课至状态接口
    appointStatusUrl = 'http://www.51talk.com/Admin/Masy/masy_mysql_update_appoint_status?id=' + str(appointID) +'&status=end'

    responses_result = req.get(url=appointStatusUrl)

    return responses_result


if __name__ == '__main__':

    #调取后台登录接口
    admin_login = adminLogin()

    appointID = "52660905"

    #调取后台约课至状态接口
    appointStatusUrl = 'http://www.51talk.com/Admin/Masy/masy_mysql_update_appoint_status?id=' + str(appointID) +'&status=end'

    info = admin_login.get(url=appointStatusUrl)

    print(info.text,info.status_code)


