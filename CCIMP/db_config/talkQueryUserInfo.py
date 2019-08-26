##!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->user表相关用户信息字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_info_detail_success(user_mobile):

    '''查询用户详情'''

    try:

        with conn_talk.cursor() as cursor:

            #查询
            sql_query  = "select id,real_name,nick_name,mobile,is_trail,is_buy,current_level,now_level,city," \
                         "parent_id from user where mobile = '"+str(user_mobile)+"'"

            #连接中断重连
            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            user_info_result = cursor.fetchall()

            # print ("user_info_result-->",user_info_result)
            # print ("user_info_result-->",type(user_info_result))

            return user_info_result

    except Exception as e:

        conn_talk.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talk库-->user表id字段
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_info_id_success(user_mobile):

    '''查询用户userId'''

    return_value = []

    try:

        with conn_talk.cursor() as cursor:

            #查询
            sql_query  = "SELECT id from user where mobile = '"+str(user_mobile)+"'"

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