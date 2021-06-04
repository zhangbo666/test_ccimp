#!/usr/bin/python
# encoding:utf-8
# -*- coding:utf-8 -*-

import operator
import json
from datetime import datetime
from db_config.talkQueryTeacherInfo import talk_platform_teacher_query_teacher_class_schedule_success




def getTeacherOpenTimeInfo(teacher_id,current_now_time_y_m_d_sqlit):

    time_info = ""
    time_list = []
    time_flag = False

    teacher_open_time_result = talk_platform_teacher_query_teacher_class_schedule_success\
                                (teacher_id,current_now_time_y_m_d_sqlit)

    return teacher_open_time_result


if __name__ == '__main__':

    teacher_id = "4774"

    current_now_time = datetime.now()
    current_now_time_y_m_d = current_now_time.strftime('%Y-%m-%d %H:%M:%S')

    # 截取当前时间之后老师开课时间数据
    current_now_time_y_m_d_sqlit = current_now_time_y_m_d.split(" ")[0]

    teacher_info_result_list = getTeacherOpenTimeInfo(teacher_id,current_now_time_y_m_d_sqlit)
    print (teacher_info_result_list)
    print(type(teacher_info_result_list))