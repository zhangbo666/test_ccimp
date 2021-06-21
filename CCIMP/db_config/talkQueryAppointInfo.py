#!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.dbConfig import *
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
    # 查询talkplatform_appoint_reconstruction库-->appoint_hot表相关用户约课信息字段
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_query_appoint_hot_info_detail_success(user_id, limit_appoint_sum):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query = "select id,t_id,s_id,start_time,end_time,course_id,point_type,status " \
                        "from appoint_hot where s_id = " \
                        "'" + str(user_id) + "' and status = 'on'" \
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
    # 查询talkplatform_appoint_reconstruction库-->appoint_t_xx（老师分库表）相关用户约课信息字段
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_query_appoint_t_xx_info_detail_success(t_id, t_id_xx, user_id,
                                                                               limit_appoint_sum):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query = "select id,t_id,s_id,start_time,end_time,course_id,point_type,status " \
                        "from appoint_t_'" + str(t_id_xx)+"' where s_id = " \
                        "'" + str(user_id) + "' and '" + str(t_id) + "' and status = 'on'" \
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
    # 查询talkplatform_appoint_reconstruction库-->appoint_s_xx（学员分库表）相关用户约课信息字段
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_query_appoint_s_xx_info_detail_success(s_id, s_id_xx, user_id,
                                                                               limit_appoint_sum):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query = "select id,t_id,s_id,start_time,end_time,course_id,point_type,status " \
                        "from appoint_s_'" + str(s_id_xx)+"' where s_id = " \
                        "'" + str(user_id) + "' and status = 'on'" \
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


# ----------------------------------------------------------------------------------------------------------------------#
    # 更新talkplatform_appoint_reconstruction库-->通过appoint_hot表的约课id字段更新课程开始时间与结束时间
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_update_appoint_hot_info_start_time_end_time_success(appoint_Id, start_time,
                                                                                            end_time):

    '''查询约课id的开始时间与结束时间'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            # sql_query = "select id from appoint where appoint_Id = '" + str(appoint_Id) + "'"

            # 更新
            sql_upate = "update appoint_hot set start_time = '" + start_time + "',end_time = '" + end_time + \
                        "' where id = '" + str(appoint_Id) + "'"

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_upate)

            conn_talkplatform_appoint_reconstruction.commit()

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


# ----------------------------------------------------------------------------------------------------------------------#
    # 更新talkplatform_appoint_reconstruction库-->通过appoint_s_xx（学员分库表）的约课id字段更新课程开始时间与结束时间
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_update_appoint_s_xx_info_start_time_end_time_success(appoint_Id, s_id_xx,
                                                                                             start_time, end_time):

    '''查询约课id的开始时间与结束时间'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            # sql_query = "select id from appoint where appoint_Id = '" + str(appoint_Id) + "'"

            # 更新
            sql_upate = "update appoint_s_ '" + s_id_xx
            "' + set start_time = '" + start_time + "',end_time = '" + end_time + \
            "' where id = '" + str(appoint_Id) +"'"

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_upate)

            conn_talkplatform_appoint_reconstruction.commit()

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


# ----------------------------------------------------------------------------------------------------------------------#
     # 更新talkplatform_appoint_reconstruction库-->通过appoint_t_xx（老师分库表）的约课id字段更新课程开始时间与结束时间
# ----------------------------------------------------------------------------------------------------------------------#

    def talkplatform_appoint_reconstruction_update_appoint_t_xx_info_start_time_end_time_success(appoint_Id,t_id,t_id_xx,
                                                                                                 start_time, end_time):

        '''查询约课id的开始时间与结束时间'''

        try:

            with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

                # 查询
                # sql_query = "select id from appoint where appoint_Id = '" + str(appoint_Id) + "'"

                # 更新
                sql_upate = "update appoint_t_ '" + t_id_xx
                "' + set start_time = '" + start_time + "',end_time = '" + end_time + \
                "' where id = '" + str(appoint_Id) + "' and t_id = '" +str(t_id) +"'"

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


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->appoint表appoint_id约课信息字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_appoint_info_appoint_id_success(appoint_id):

    '''查询约课id'''

    try:

        with conn_talk.cursor() as cursor:

            # 查询
            sql_query = "select id from appoint where id = '" + str(appoint_id) + "'"

            # 连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            return appoint_info_result

    except Exception as e:

        conn_talk.rollback()

        print("e-->", e)


# ----------------------------------------------------------------------------------------------------------------------#
    # 查询talkplatform_appoint_reconstruction库-->appoint表appoint_id约课信息字段
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_appoint_info_appoint_id_success(date_time):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query = "select id from appoint where date_time = '" + str(date_time) + "'"

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            return appoint_info_result

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


# ----------------------------------------------------------------------------------------------------------------------#
# 查询talkplatform_appoint_reconstruction库-->appoint表所有数据
# ----------------------------------------------------------------------------------------------------------------------#

def talkplatform_appoint_reconstruction_query_appoint_info_detail2_success(appoint_id):

    '''查询约课详情'''

    try:

        with conn_talkplatform_appoint_reconstruction.cursor() as cursor:

            # 查询
            sql_query = "select * from appoint where id = '" + str(appoint_id) + "'"

            # 连接中断重连
            conn_talkplatform_appoint_reconstruction.ping(reconnect=True)

            cursor.execute(sql_query)

            appoint_info_result = cursor.fetchall()

            return appoint_info_result

    except Exception as e:

        conn_talkplatform_appoint_reconstruction.rollback()

        print("e-->", e)


#----------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
