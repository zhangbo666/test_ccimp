__author__ = 'zhangbo'


import operator
import json

from externalClass.appoint.appointConfig import *

from db_config.talkQueryAppointInfo import talk_query_appoint_info_detail_success

def getTalkAppointInfo(user_id,limit_appoint_sum):

    talk_appoint_info_result_dict = {}
    talk_appoint_info_result_list = []

    talk_appoint_id = ""
    talk_appoint_t_id = ""
    talk_appoint_s_id = ""
    talk_appoint_course_id = ""
    talk_appoint_point_type = ""
    talk_appoint_start_time = ""
    talk_appoint_end_time = ""

    talk_appoint_result_list = talk_query_appoint_info_detail_success(user_id,limit_appoint_sum)

    for talk_appoint_1 in talk_appoint_result_list:

        for key, values in sorted(talk_appoint_1.items(), key=operator.itemgetter(0)):

            if key == "id":

                talk_appoint_id = values

            if key == "t_id":

                talk_appoint_t_id = values

            if key == "s_id":

                talk_appoint_s_id = values

            if key == "course_id":

                talk_appoint_course_id = values

            if key == "point_type":

                talk_appoint_point_type = values

            if key == "start_time":

                start_time = values.strftime('%Y-%m-%d %H:%M:%S')

                talk_appoint_start_time = start_time

            if key == "end_time":

                end_time = values.strftime('%Y-%m-%d %H:%M:%S')

                talk_appoint_end_time = end_time

            talk_appoint_info_result_dict = {

                "id": talk_appoint_id,
                "t_id": talk_appoint_t_id,
                "s_id": talk_appoint_s_id,
                "course_id": talk_appoint_course_id,
                "point_type": talk_appoint_point_type,
                "start_time": talk_appoint_start_time,
                "end_time": talk_appoint_end_time

            }

        talk_appoint_info_result_list.append(talk_appoint_info_result_dict)

    # print("talk_appoint_info_result_list", type(talk_appoint_info_result_list))
    # print(talk_appoint_info_result_list)

    # talk_appoint_info_result_json = json.dumps(talk_appoint_info_result_list)
    # print ("talk_appoint_info_result_json",type(talk_appoint_info_result_json))
    # print (talk_appoint_info_result_json)



    return talk_appoint_info_result_list


if __name__ == '__main__':

    user_id = '800021389'

    talk_appoint_result_list = getTalkAppointInfo(user_id,limit_appoint_sum)

    print ("talk_appoint_result_list",type(talk_appoint_result_list))
    print ("talk_appoint_result_list",talk_appoint_result_list)

    talk_appoint_result_json = json.dumps(talk_appoint_result_list)
    print ("talk_appoint_result_json",type(talk_appoint_result_json))
    print ("talk_appoint_result_json",talk_appoint_result_json)
