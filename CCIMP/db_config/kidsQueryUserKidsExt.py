#!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.dbConfig import *
import operator

#----------------------------------------------------------------------------------------------------------------------#
    # 查询kids库-->user_kids_ext表相关用户level信息字段
#----------------------------------------------------------------------------------------------------------------------#

def kids_query_user_kids_ext_info_detail_success(user_id):

    '''查询用户级别详情'''

    try:

        with conn_kids.cursor() as cursor:

            #查询状态
            sql_query  = "select id,stu_id,now_level,current_level " \
                         "from user_kids_ext where stu_id = '"+str(user_id)+"'"

            #连接中断重连
            conn_kids.ping(reconnect=True)

            cursor.execute(sql_query)

            user_kids_ext_info_result = cursor.fetchall()

            return user_kids_ext_info_result

    except Exception as e:

        conn_kids.rollback()

        print ("e-->",e)