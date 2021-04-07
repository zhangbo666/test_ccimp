__author__ = 'zhangbo'

##!usr/bin/python
#encoding:utf-8

from db_config.dbConfig import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->stu_point表
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_stu_point_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_list_info = []
    wealth_list_result = []

    wealth_dict = {}
    wealth_dict_result = {}
    user_wealth_result = {}

    type_valuse = ""
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

                            type_valuse = valuse

                        if key == "content":

                            type_content = valuse

                        wealth_dict = {

                            type_valuse:type_content

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


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->user_assets表开启的财富
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_assets_enable_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_list_info = []
    wealth_list_result = []
    wealth_dict = {}
    wealth_dict_result = {}
    user_wealth_result = {}

    type_valuse = ""

    point_class = ""
    point_caifu = ""

    classtime_class = ""
    classtime_caifu = ""

    na_pri_class = ""
    na_pri_caifu = ""

    na_open_class = ""
    na_open_caifu = ""

    try:

        with conn_point.cursor() as cursor:

            #查询开启的财富
            sql_query  = "select count,sku_type from user_assets where stu_id = '%s' " \
                         "and status = 'enable' ORDER BY add_time" % (user_id)
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


                        if key == "sku_type":

                            type_valuse = valuse

                        if key == "count":

                            type_count = valuse

                        wealth_dict = {

                            type_valuse:type_count

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

                        elif w1 == "na_pri":

                            na_pri_class = w1

                            na_pri_caifu = int (wealth_list_info_one[w1])

                        elif w1 == "na_open":

                            na_open_class = w1

                            na_open_caifu = int (wealth_list_info_one[w1])

                if point_class == "point" or classtime_class == "classtime":

                    wealth_dict_result = {

                        point_class:point_caifu,
                        classtime_class:classtime_caifu
                    }

                else:

                    wealth_dict_result = {

                        na_pri_class:na_pri_caifu,
                        na_open_class:na_open_caifu
                    }

                wealth_list_result.append(wealth_dict_result)

                # print ("wealth_list_result-->",wealth_list_result)
                # print ("type(wealth_list_result)-->",type(wealth_list_result))

                return wealth_list_result

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->user_assets表未开启的次卡财富
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_assets_disable_point_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_dict = {}
    user_wealth_result = {}

    try:

        with conn_point.cursor() as cursor:

            #查询未开启次卡财富
            point_sql_query  = "select SUM(count) as point_count from user_assets " \
                               "where stu_id = %s and status = 'disable' and sku_type = 'point' ORDER BY add_time" % (user_id)
            # print ("point_sql_query-->",point_sql_query)


            #连接中断重连
            conn_point.ping(reconnect=True)

            cursor.execute(point_sql_query)

            user_wealth_result = cursor.fetchall()

            for user_wealth in user_wealth_result:

                # print ("user_wealth-->",user_wealth)

                for key, valuse in sorted(user_wealth.items(), key=operator.itemgetter(0)):


                    if key == "point_count":

                        point_count_valuse = valuse

                    wealth_dict = {

                        "point_count":point_count_valuse

                    }

            return wealth_dict

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->user_assets表未开启的课时财富
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_assets_disable_classtime_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_dict = {}
    user_wealth_result = {}


    try:

        with conn_point.cursor() as cursor:

            #查询未开启课时财富
            classtime_sql_query  = "select SUM(count) as classtime_count from user_assets " \
                         "where stu_id = %s and status = 'disable' and sku_type = 'classtime' ORDER BY add_time" % (user_id)

            # print ("classtime_sql_query-->",classtime_sql_query)

            #连接中断重连
            conn_point.ping(reconnect=True)

            cursor.execute(classtime_sql_query)

            user_wealth_result = cursor.fetchall()

            for user_wealth in user_wealth_result:

                # print ("user_wealth-->",user_wealth)

                for key, valuse in sorted(user_wealth.items(), key=operator.itemgetter(0)):


                    if key == "classtime_count":

                        classtime_count_valuse = valuse

                    wealth_dict = {

                        "classtime_count":classtime_count_valuse

                    }

            return wealth_dict

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->user_assets表未开启的北美课时财富
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_assets_disable_na_pri_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_dict = {}
    user_wealth_result = {}


    try:

        with conn_point.cursor() as cursor:

            #查询未开启北美课时财富
            na_pri_sql_query  = "select SUM(count) as na_pri_count from user_assets " \
                         "where stu_id = %s and status = 'disable' and sku_type = 'na_pri' ORDER BY add_time" % (user_id)

            # print ("classtime_sql_query-->",classtime_sql_query)

            #连接中断重连
            conn_point.ping(reconnect=True)

            cursor.execute(na_pri_sql_query)

            user_wealth_result = cursor.fetchall()

            for user_wealth in user_wealth_result:

                # print ("user_wealth-->",user_wealth)

                for key, valuse in sorted(user_wealth.items(), key=operator.itemgetter(0)):


                    if key == "na_pri_count":

                        na_pri_count_valuse = valuse

                    wealth_dict = {

                        "na_pri_count":na_pri_count_valuse

                    }

            return wealth_dict

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询point库-->user_assets表未开启的北美绘本课财富
#----------------------------------------------------------------------------------------------------------------------#

def talk_query_user_assets_disable_na_open_user_wealth_success(user_id):

    '''查询用户财富'''

    wealth_dict = {}
    user_wealth_result = {}


    try:

        with conn_point.cursor() as cursor:

            #查询未开启北美课时财富
            na_open_sql_query  = "select SUM(count) as na_open_count from user_assets " \
                         "where stu_id = %s and status = 'disable' and sku_type = 'na_open' ORDER BY add_time" % (user_id)

            # print ("classtime_sql_query-->",classtime_sql_query)

            #连接中断重连
            conn_point.ping(reconnect=True)

            cursor.execute(na_open_sql_query)

            user_wealth_result = cursor.fetchall()

            for user_wealth in user_wealth_result:

                # print ("user_wealth-->",user_wealth)

                for key, valuse in sorted(user_wealth.items(), key=operator.itemgetter(0)):


                    if key == "na_open_count":

                        na_open_count_valuse = valuse

                    wealth_dict = {

                        "na_open_count":na_open_count_valuse

                    }

            return wealth_dict

    except Exception as e:

        conn_point.rollback()

        print ("e-->",e)

