##!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.dbConfig import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talkplatform_teacher库-->teacher_info表老师信息字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_platform_teacher_query_teacher_info_success(limin_teacher_sum):

    '''查询老师详情'''

    try:

        with conn_talkplatform_teacher.cursor() as cursor:

            #查询
            sql_query  = "SELECT teacher_id,user_name,nick_name,`status`,project_type,qualification_status from" \
                         " talkplatform_teacher.teacher_info where status = 1 and project_type = 1 " \
                         "and qualification_status = 1 LIMIT %d" % (limin_teacher_sum)

            #连接中断重连
            conn_talkplatform_teacher.ping(reconnect=True)

            cursor.execute(sql_query)

            teacher_info_result = cursor.fetchall()

            # print ("teacher_info_result-->",teacher_info_result)
            # print ("teacher_info_result-->",type(teacher_info_result))

            return teacher_info_result

    except Exception as e:

        conn_talkplatform_teacher.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talkplatform_teacher库-->teacher_class_schedule老师开课时间表信息字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_platform_teacher_query_teacher_class_schedule_success(tid,current_now_time_y_m_d_sqlit):

    '''查询老师开课时间表'''

    try:

        with conn_talkplatform_teacher.cursor() as cursor:

            #查询
            sql_query = "SELECT teacher_id,time,date,status,appoint_status,time_slot from" \
                        " talkplatform_teacher.teacher_class_schedule where status = 'on' and appoint_status = '1' " \
                        "and teacher_id = %s and date > %s" % (tid,current_now_time_y_m_d_sqlit)


            #连接中断重连
            conn_talkplatform_teacher.ping(reconnect=True)

            cursor.execute(sql_query)

            teacher_class_schedule_result = cursor.fetchall()

            # print ("teacher_class_schedule_result-->",teacher_class_schedule_result)
            # print ("teacher_class_schedule_result-->",type(teacher_class_schedule_result))

            return teacher_class_schedule_result

    except Exception as e:

        conn_talkplatform_teacher.rollback()

        print ("e-->",e)

