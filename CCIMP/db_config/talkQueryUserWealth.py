__author__ = 'zhangbo'

##!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->stu_point表
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_list_info = []
    wealth_list_result = []

    wealth_dict = {}
    wealth_dict_result = {}

    user_wealth_result = {}

    type_point = ""
    type_content = ""

    point_class = ""
    point_caifu = ""

    classtime_class = ""
    classtime_caifu = ""

    try:

        with conn_point.cursor() as cursor:

            #查询
            sql_query  = "select content,type from stu_point where stu_id = '%s'" % (user_id)
            # print ("sql_query-->",sql_query)

            #连接中断重连
            conn_point.ping(reconnect=True)

            cursor.execute(sql_query)

            user_wealth_result = cursor.fetchall()

            if user_wealth_result == ():

                return user_wealth_result

            else:

                for user_wealth in user_wealth_result:

                    # print ("user_wealth-->",user_wealth)

                    for key, valuse in sorted(user_wealth.items(), key=operator.itemgetter(0)):


                        if key == "type":

                            type_point = valuse

                        if key == "content":

                            type_content = valuse

                        wealth_dict = {

                            type_point:type_content

                        }
                    wealth_list_info.append(wealth_dict)

                # print ("wealth_list_info-->",wealth_list_info)
                # print ("type(wealth_list_info)-->",type(wealth_list_info))


                # [{"point":'22',"classtime":'30'}]
                for wealth_list_info_one in wealth_list_info:

                    for w1 in wealth_list_info_one:

                        if w1 == "point":

                            point_class = w1

                            point_caifu = int (wealth_list_info_one[w1])

                        elif w1 == "classtime":

                            classtime_class = w1

                            classtime_caifu = int (wealth_list_info_one[w1])

                wealth_dict_result = {

                    point_class:point_caifu,
                    classtime_class:classtime_caifu
                }

                wealth_list_result.append(wealth_dict_result)

                # print ("wealth_list_result-->",wealth_list_result)
                # print ("type(wealth_list_result)-->",type(wealth_list_result))

                return wealth_list_result

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)

