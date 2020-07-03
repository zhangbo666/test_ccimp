#!/usr/bin/python
# encoding:utf-8
# -*- coding:utf-8 -*-


from time import sleep
from db_config.db_config import *
import operator


#----------------------------------------------------------------------------------------------------------------------#
    # 查询textbook库-->series_textbook一级教材信息
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_textbook_tree_depth_one_query_success(c_cate1_limit_sum):

    '''查询一级教材表信息'''

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id, \
                          tree_depth from series_textbook where is_used = 1 and tree_depth = 1 LIMIT %d" % (c_cate1_limit_sum)

            #连接中断重连
            conn_textbook.ping(reconnect=True)

            cursor.execute(sql_query)

            text_book_result = cursor.fetchall()

            # print ("text_book_result-->",text_book_result)
            # print ("text_book_result-->",type(text_book_result))

            return text_book_result

    except Exception as e:

        conn_textbook.rollback()

        print ("e-->",e)

#----------------------------------------------------------------------------------------------------------------------#
    # 查询textbook库-->series_textbook二级教材表信息
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_textbook_tree_depth_two_query_success(one_tree_depth_id,c_cate2_limit_sum):

    '''查询二级教材表信息'''

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id," \
                         "tree_depth from series_textbook where is_used = 1 and tree_depth = 2 " \
                         "and tree_parent_id = '"+str(one_tree_depth_id)+"' LIMIT %d" % (c_cate2_limit_sum)

            #连接中断重连
            conn_textbook.ping(reconnect=True)

            cursor.execute(sql_query)

            text_book_result = cursor.fetchall()

            # print ("text_book_result-->",text_book_result)
            # print ("text_book_result-->",type(text_book_result))

            return text_book_result

    except Exception as e:

        conn_textbook.rollback()

        print ("e-->",e)

#----------------------------------------------------------------------------------------------------------------------#
    # 查询textbook库-->series_textbook三级教材表信息
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_textbook_tree_depth_three_query_success(two_tree_depth_id,c_cate3_limit_sum):

    '''查询三级教材表信息'''

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id," \
                         "tree_depth from series_textbook where is_used = 1 and tree_depth = 3 " \
                         "and tree_parent_id = '"+str(two_tree_depth_id)+"' LIMIT %d" % (c_cate3_limit_sum)

            #连接中断重连
            conn_textbook.ping(reconnect=True)

            cursor.execute(sql_query)

            text_book_result = cursor.fetchall()

            # print ("text_book_result-->",text_book_result)
            # print ("text_book_result-->",type(text_book_result))

            return text_book_result

    except Exception as e:

        conn_textbook.rollback()

        print ("e-->",e)


#----------------------------------------------------------------------------------------------------------------------#
    # 查询talkplatform_course库-->course公开课开课记录
#----------------------------------------------------------------------------------------------------------------------#
def talkplatform_course_course_query_success(course_limit_sum):

    '''查询公开课开课信息'''

    try:

        with conn_talkplatform_course.cursor() as cursor:

            #查询
            sql_query  = "select id,name,book_type,book_id,tea_ids,course_type,start_time,end_time \
                          from course where course_type = '6' ORDER BY id DESC LIMIT %d" % (course_limit_sum)

            #连接中断重连
            conn_talkplatform_course.ping(reconnect=True)

            cursor.execute(sql_query)

            open_class_info_result = cursor.fetchall()

            # print ("open_class_info_result-->",open_class_info_result,type(open_class_info_result))

            return open_class_info_result

    except Exception as e:

        conn_talkplatform_course.rollback()

        print ("e-->",e)


