#!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->appoint表相关用户约课信息字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_appoint_info_detail_success(user_id,limit_appoint_sum):

    '''查询约课详情'''

    try:

        with conn_talk.cursor() as cursor:

            #查询状态
            sql_query  = "select id,t_id,s_id,start_time,end_time,course_id,point_type,status " \
                         "from appoint where s_id = " \
                         "'"+str(user_id)+"' and start_time > '2020-01-01 00:00:00' and status = 'on'" \
                         "ORDER BY start_time DESC LIMIT %d" % (limit_appoint_sum)

            #连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            return appoint_info_result

    except Exception as e:

        conn_talk.rollback()

        print ("e-->",e)


# ----------------------------------------------------------------------------------------------------------------------#
    # 查询talkplatform_appoint_reconstruction库-->appoint表相关用户约课信息字段
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_query_appoint_info_detail_success(user_id,limit_appoint_sum):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query  = "select id,t_id,s_id,start_time,end_time,course_id,point_type,status " \
                         "from appoint where s_id = " \
                         "'"+str(user_id)+"' and start_time > '2020-01-01 00:00:00' and status = 'on'" \
                         "ORDER BY start_time DESC LIMIT %d" % (limit_appoint_sum)

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            return appoint_info_result

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


# ----------------------------------------------------------------------------------------------------------------------#
    # 更新talk库-->通过appoint表的约课id字段更新课程开始时间与结束时间
# ----------------------------------------------------------------------------------------------------------------------#

def talk_update_appoint_info_start_time_end_time_success(appoint_Id,start_time,end_time):

    '''查询约课id的开始时间与结束时间'''

    try:

        with conn_talk.cursor() as cursor:

            # 查询
            # sql_query = "select start_time,end_time from appoint where s_id = '" + str(appoint_Id) + "'"

            # 更新
            sql_upate = "update appoint set start_time = '" + start_time + "',end_time = '" + end_time +\
                        "' where id = '" + str(appoint_Id) + "'"


            # 连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_upate)

            conn_talk.commit()

    except Exception as e:

        conn_talk.rollback()

        print("e-->", e)

# ----------------------------------------------------------------------------------------------------------------------#
    # 更新talkplatform_appoint_reconstruction库-->通过appoint表的约课id字段更新课程开始时间与结束时间
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_update_appoint_info_start_time_end_time_success(appoint_Id,start_time,end_time):

    '''查询约课id的开始时间与结束时间'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            # sql_query = "select id from appoint where appoint_Id = '" + str(appoint_Id) + "'"

            # 更新
            sql_upate = "update appoint set start_time = '" + start_time + "',end_time = '" + end_time +\
                        "' where id = '" + str(appoint_Id) + "'"

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_upate)

            conn_talkplatform_appoint_reconstruction.commit()

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->appoint表约课id字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_appoint_info_id_success(user_id):

    '''查询约课id'''

    try:

        with conn_talk.cursor() as cursor:

            # 查询
            sql_query = "select id from appoint where s_id = '" + str(user_id) + "'"

            # 连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            # print ("appoint_info_result-->",appoint_info_result)
            # print ("appoint_info_result-->",type(appoint_info_result))

            if appoint_info_result == ():

                return appoint_info_result

            else:

                for appointid in appoint_info_result:

                    for key,value in appointid.items():

                        if key == "id":

                            return value

    except Exception as e:

        conn_talk.rollback()

        print("e-->", e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->user表id字段的冻结状态
#----------------------------------------------------------------------------------------------------------------------#
def talk_query_user_info_id_account_status_success(user_mobile):

    '''查询用户userID的冻结状态'''

    return_value = []

    try:

        with conn_talk.cursor() as cursor:

            #查询
            sql_query  = "SELECT id from user where mobile = '%s'" % (user_mobile)

            #连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            user_id_result = cursor.fetchall()

            # print ("user_id-->",user_id_result)
            # print ("user_id-->",type(user_id_result))

            if user_id_result == ():

                return user_id_result

            else:

                for userid in user_id_result:

                    for key,valuse in userid.items():

                        if key == "id":

                            return  valuse

    except Exception as e:

        conn_talk.rollback()

        print ("e-->",e)


