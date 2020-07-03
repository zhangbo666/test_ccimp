__author__ = 'zhangbo'

from externalClass.open_class.openClassConfig import *

from db_config.talkQueryTeacherInfo import talk_platform_teacher_query_teacher_info_success

import json



def getTeacherInfo(limin_teacher_sum):

    teacher_info_result_list = talk_platform_teacher_query_teacher_info_success(limin_teacher_sum)

    return teacher_info_result_list



if __name__ == '__main__':

    teacher_info_result_list = talk_platform_teacher_query_teacher_info_success(limin_teacher_sum)
    teacher_info_result_json = json.dumps(teacher_info_result_list)

    # print (teacher_info_result_list)
    # print (type(teacher_info_result_list))
    #
    # print (json.dumps(teacher_info_result_json))
    # print (type(json.dumps(teacher_info_result_json)))

    for i in range(len(teacher_info_result_list)):

        # print (teacher_info_result_list[i])
        nick_name = teacher_info_result_list[i]['nick_name']
        teacher_id = teacher_info_result_list[i]['teacher_id']


        # print (nick_name,teacher_id)