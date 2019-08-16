##!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询user表mobile,password
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_order_success(orderId):

    '''查询订单详情'''

    return_value = []

    try:

        with conn_talk.cursor() as cursor:

            #查询
            sql_query  = "select id,extend_id,order_money,pay_method,order_type from user_order where id = %s" % (orderId)

            conn_talk.ping(reconnect=True)

            cursor.execute(sql_query)

            user_order_info_result = cursor.fetchall()

            print ("user_order_info_result-->",user_order_info_result)
            print ("user_order_info_result-->",type(user_order_info_result))

            if user_order_info_result == ():

                return user_order_info_result

            else:

                return user_order_info_result

    except Exception as e:

        conn_talk.rollback()

        print ("e-->",e)