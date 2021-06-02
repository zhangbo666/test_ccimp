__author__ = 'zhangbo'

import time

import json

from externalClass.adminLogin import adminLogin

from db_config.talkQueryUserInfo import talk_query_user_info_id_success


#更改php库和平台库约课状态
def courseStatus(course_status_data,appoint_id_check_val):

    '''
    账号状态
    :param course_status_data:课程状态数据
    :param appoint_id_data:约课ID
    :return:返回账号状态数据
    '''

    appoint_id_check_val_list = json.loads(appoint_id_check_val)

    appoint_id_check_val_length = len(appoint_id_check_val_list)

    for i in range(0,appoint_id_check_val_length):

        courseStatusUrl = "https://www.51talk.com/Admin/Masy/masy_mysql_update_appoint_status?id=" \
                           + str(appoint_id_check_val_list[i]) + "&status=" + str(course_status_data)

        #调取后台登录接口
        admin_login = adminLogin()

        coursestatus = admin_login.get(url=courseStatusUrl)

        time.sleep(1)

        if (i == appoint_id_check_val_length -1 ):

            if coursestatus.ok == True:

                return True

            else:

                return False

if __name__ == '__main__':

    mobile_data = '18611222465'

    # course_status_data = 'on'
    course_status_data = 'end'
    # course_status_data = 's_absent'
    # course_status_data = 't_absent'
    # course_status_data = 'cancel'

    appoint_id = '52680179'

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



