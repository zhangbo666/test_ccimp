__author__ = 'zhangbo'

from externalClass.adminLogin import adminLogin

from db_config.talkQueryUserInfo import talk_query_user_info_id_success

def courseStatus(course_status_data,appoint_id_data):

    '''
    账号状态
    :param course_status_data:课程状态数据
    :param appoint_id_data:约课ID
    :return:返回账号状态数据
    '''

    # print ("course_status_data-->",course_status_data)
    # print ("appoint_id_data-->",appoint_id_data)

    # course_appoint_id_data = talk_query_user_info_id_success(mobile_data)

    courseStatusUrl = "https://www.51talk.com/Admin/Masy/masy_mysql_update_appoint_status?id=" \
                       + str(appoint_id_data) + "&status=" + str(course_status_data)

    #调取后台登录接口
    admin_login = adminLogin()

    coursestatus = admin_login.get(url=courseStatusUrl)

    if coursestatus.ok == True:

        return True

    else:

        return False

if __name__ == '__main__':

    mobile_data = '18611222465'

    course_status_data = 'on'
    # course_status_data = 'end'
    # course_status_data = 's_absent'
    # course_status_data = 't_absent'

    appoint_id = '52663928'

    course_appoint_id_data = talk_query_user_info_id_success(mobile_data)

    courseStatusUrl = "https://www.51talk.com/Admin/Masy/masy_mysql_update_appoint_status?id=" \
                       + str(appoint_id) + "&status=" + str(course_status_data)

    #调取后台登录接口
    admin_login = adminLogin()

    coursestatus = admin_login.get(url=courseStatusUrl)

    print (coursestatus.text)
    print (type(coursestatus.text))

    if coursestatus.ok == True:

        print ("true")



