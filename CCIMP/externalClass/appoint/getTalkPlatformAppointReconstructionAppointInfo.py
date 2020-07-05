__author__ = 'zhangbo'


import operator
import json

from externalClass.appoint.appointConfig import *

from db_config.talkQueryAppointInfo import talkplatform_appoint_reconstruction_query_appoint_info_detail_success

def getTalkPlatformAppointReconstructionAppointInfo(user_id,limit_appoint_sum):

    talkplatform_appoint_reconstruction_appoint_info_result_dict = {}
    talkplatform_appoint_reconstruction_appoint_info_result_list = []

    talkplatform_appoint_reconstruction_appoint_id = ""
    talkplatform_appoint_reconstruction_appoint_t_id = ""
    talkplatform_appoint_reconstruction_appoint_s_id = ""
    talkplatform_appoint_reconstruction_appoint_course_id = ""
    talkplatform_appoint_reconstruction_appoint_point_type = ""
    talkplatform_appoint_reconstruction_appoint_start_time = ""
    talkplatform_appoint_reconstruction_appoint_end_time = ""

    talkplatform_appoint_reconstruction_result_list = talkplatform_appoint_reconstruction_query_appoint_info_detail_success(user_id,limit_appoint_sum)

    for talkplatform_appoint_reconstruction_appoint_1 in talkplatform_appoint_reconstruction_result_list:

        for key, values in sorted(talkplatform_appoint_reconstruction_appoint_1.items(), key=operator.itemgetter(0)):

            if key == "id":

                talkplatform_appoint_reconstruction_appoint_id = values

            if key == "t_id":

                talkplatform_appoint_reconstruction_appoint_t_id = values

            if key == "s_id":

                talkplatform_appoint_reconstruction_appoint_s_id = values

            if key == "course_id":

                talkplatform_appoint_reconstruction_appoint_course_id = values

            if key == "point_type":

                talkplatform_appoint_reconstruction_appoint_point_type = values

            if key == "start_time":

                start_time = values.strftime('%Y-%m-%d %H:%M:%S')

                talkplatform_appoint_reconstruction_appoint_start_time = start_time

            if key == "end_time":

                end_time = values.strftime('%Y-%m-%d %H:%M:%S')

                talkplatform_appoint_reconstruction_appoint_end_time = end_time

            talkplatform_appoint_reconstruction_appoint_info_result_dict = {

                "id": talkplatform_appoint_reconstruction_appoint_id,
                "t_id": talkplatform_appoint_reconstruction_appoint_t_id,
                "s_id": talkplatform_appoint_reconstruction_appoint_s_id,
                "course_id": talkplatform_appoint_reconstruction_appoint_course_id,
                "point_type": talkplatform_appoint_reconstruction_appoint_point_type,
                "start_time": talkplatform_appoint_reconstruction_appoint_start_time,
                "end_time": talkplatform_appoint_reconstruction_appoint_end_time

            }

        talkplatform_appoint_reconstruction_appoint_info_result_list.append(talkplatform_appoint_reconstruction_appoint_info_result_dict)

    # print("talkplatform_appoint_reconstruction_appoint_info_result_list", type(talkplatform_appoint_reconstruction_appoint_info_result_list))
    # print(talkplatform_appoint_reconstruction_appoint_info_result_list)

    # talkplatform_appoint_reconstruction_appoint_info_result_json = json.dumps(talkplatform_appoint_reconstruction_appoint_info_result_list)
    # print ("talkplatform_appoint_reconstruction_appoint_info_result_json",type(talkplatform_appoint_reconstruction_appoint_info_result_json))
    # print (talkplatform_appoint_reconstruction_appoint_info_result_json)

    return talkplatform_appoint_reconstruction_appoint_info_result_list


if __name__ == '__main__':

    user_id = '800021389'

    talkplatform_appoint_reconstruction_result_list = getTalkPlatformAppointReconstructionAppointInfo(user_id,limit_appoint_sum)

    print ("talkplatform_appoint_reconstruction_result_list",type(talkplatform_appoint_reconstruction_result_list))
    print ("talkplatform_appoint_reconstruction_result_list",talkplatform_appoint_reconstruction_result_list)

    talkplatform_appoint_reconstruction_result_json = json.dumps(talkplatform_appoint_reconstruction_result_list)
    print ("talkplatform_appoint_reconstruction_result_json",type(talkplatform_appoint_reconstruction_result_json))
    print ("talkplatform_appoint_reconstruction_result_json",talkplatform_appoint_reconstruction_result_json)