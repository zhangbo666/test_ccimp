__author__ = 'zhangbo'

import time

import json

import requests

from externalClass.adminLogin import adminLogin

from db_config.talkQueryUserInfo import talk_query_user_info_id_success


def courseStatusTalkPlatform(course_status_data,appoint_id_check_val):

    '''
    账号状态
    :param course_status_data:课程状态数据
    :param appoint_id_data:约课ID
    :return:返回账号状态数据
    '''

    appiont_url = "http://172.16.16.97/talkplatform_appointone_consumer/v1/appoint/update"

    appoint_id_check_val_list = json.loads(appoint_id_check_val)

    appoint_id_check_val_length = len(appoint_id_check_val_list)

    for i in range(0,appoint_id_check_val_length):

        appiont_data = {

            "id": appoint_id_check_val_list[i],
            "status": course_status_data
        }

        appiont_update_result = requests.post(url=appiont_url, data=json.dumps(appiont_data))
        # print (appiont_update_result.json())

        appoint_id_result = str(appiont_update_result.json()["code"])

        if (i == appoint_id_check_val_length -1 ):

            if appoint_id_result == "10000":

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

    appoint_id = '52680177'

    appiont_url = "http://172.16.16.97/talkplatform_appointone_consumer/v1/appoint/update"

    appiont_data = {

        "id": appoint_id,
        "status": course_status_data
    }

    appiont_update_result = requests.post(url=appiont_url, data=json.dumps(appiont_data))
    print(appiont_update_result.json())

    appoint_id_result = str(appiont_update_result.json()["code"])



