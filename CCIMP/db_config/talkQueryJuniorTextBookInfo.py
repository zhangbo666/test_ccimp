#!/usr/bin/python
# encoding:utf-8
# -*- coding:utf-8 -*-


from time import sleep
from db_config.dbConfig import *
import operator




#----------------------------------------------------------------------------------------------------------------------#
    # 查询textbook库-->series_textbook（青少5.0一级教材信息）
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_junior_textbook_tree_depth_one_query_success():

    '''青少5.0一级教材信息'''

    #junior_textbook_level_K =
    #junior_textbook_level_0 = 773011
    #junior_textbook_level_1 = 769941

    #junior_textbook_level_2 = 772051
    #junior_textbook_level_3 = 772061
    #junior_textbook_level_4 = 796041
    #junior_textbook_level_5 = 797021
    #junior_textbook_level_6 = 796051
    #经典英语青少版 Level K（第五版）
    #经典英语青少版 Level 0（第五版）
    #经典英语青少版 Level 1（第五版）
    #经典英语青少版 Level 2（第五版）
    #经典英语青少版 Level 3（第五版）
    #经典英语青少版 Level 4（第五版）
    #经典英语青少版 Level 5（第五版）
    #经典英语青少版 Level 6（第五版）

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id," \
                         "tree_depth from series_textbook where name_zh_cn = '经典英语青少版'" \
                         " and is_used = 1 and tree_parent_id = 0 and tg = 'on' and id in " \
                         "('1084111','773011','769941','772051','772061','796041','797021','796051')"

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
    # 查询textbook库-->series_textbook（青少5.0二级教材信息）
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_junior_textbook_tree_depth_two_query_success(two_books_id):

    '''青少5.0一级教材信息'''

    #junior_textbook_level_K = 773011
    #junior_textbook_level_0 = 773011
    #junior_textbook_level_1 = 769941

    #junior_textbook_level_2 = 772051
    #junior_textbook_level_3 = 772061
    #junior_textbook_level_4 = 796041
    #junior_textbook_level_5 = 797021
    #junior_textbook_level_6 = 796051
    #经典英语青少版 Level K（第五版）
    #经典英语青少版 Level 0（第五版）
    #经典英语青少版 Level 1（第五版）
    #经典英语青少版 Level 2（第五版）
    #经典英语青少版 Level 3（第五版）
    #经典英语青少版 Level 4（第五版）
    #经典英语青少版 Level 5（第五版）
    #经典英语青少版 Level 6（第五版）

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id," \
                         "tree_depth from series_textbook where is_used = 1 and tg = 'on' and tree_parent_id = '"+str(two_books_id)+"'"

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
    # 查询textbook库-->series_textbook（青少5.0三级教材信息）
#----------------------------------------------------------------------------------------------------------------------#
def textbook_series_junior_textbook_tree_depth_three_query_success(three_books_id):

    '''青少5.0一级教材信息'''

    #junior_textbook_level_K = 773011
    #junior_textbook_level_0 = 773011
    #junior_textbook_level_1 = 769941

    #junior_textbook_level_2 = 772051
    #junior_textbook_level_3 = 772061
    #junior_textbook_level_4 = 796041
    #junior_textbook_level_5 = 797021
    #junior_textbook_level_6 = 796051
    #经典英语青少版 Level K（第五版）
    #经典英语青少版 Level 0（第五版）
    #经典英语青少版 Level 1（第五版）
    #经典英语青少版 Level 2（第五版）
    #经典英语青少版 Level 3（第五版）
    #经典英语青少版 Level 4（第五版）
    #经典英语青少版 Level 5（第五版）
    #经典英语青少版 Level 6（第五版）

    try:

        with conn_textbook.cursor() as cursor:

            #查询
            sql_query  = "select id,name_en_us,name_zh_cn,name,tree_path,tree_parent_id," \
                         "tree_depth from series_textbook where is_used = 1 and tg = 'on' and tree_parent_id = '"+str(three_books_id)+"'"

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


