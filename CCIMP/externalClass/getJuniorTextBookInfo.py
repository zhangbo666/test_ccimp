#!/usr/bin/python
# encoding:utf-8
# -*- coding:utf-8 -*-


from db_config.talkQueryJuniorTextBookInfo import textbook_series_junior_textbook_tree_depth_one_query_success
from db_config.talkQueryJuniorTextBookInfo import textbook_series_junior_textbook_tree_depth_two_query_success
from db_config.talkQueryJuniorTextBookInfo import textbook_series_junior_textbook_tree_depth_three_query_success

import operator
import json


def getJuniorTextBookInfo(current_level):

    book_id_id = 0
    book_id_name = ''

    c_cate_id1_id = 0
    c_cate_id1_name = ''

    c_cate_id2_id = 0
    c_cate_id2_name = ''

    c_cate1_dict = {}
    c_cate1_list = []

    c_cate2_dict = {}

    c_cate3_dict = {}

    t1_result = textbook_series_junior_textbook_tree_depth_one_query_success()

    t2_result = t1_result

    for aa in t2_result:

        for key,values in sorted(aa.items(),key=operator.itemgetter(0)):

            if current_level == "0":

                if key == "id":

                   if values == 769941:

                       aa.clear()

                   if values == 772051:

                       aa.clear()

                   if values == 772061:

                       aa.clear()

                   if values == 796041:

                       aa.clear()

                   if values == 797021:

                       aa.clear()

                   if values == 796051:

                       aa.clear()

            elif current_level == "1":

                if key == "id":

                    if values == 772051:

                       aa.clear()

                    if values == 772061:

                       aa.clear()

                    if values == 796041:

                       aa.clear()

                    if values == 797021:

                       aa.clear()

                    if values == 796051:

                       aa.clear()

            elif current_level == "2":

                if key == "id":

                    if values == 772061:

                        aa.clear()

                    if values == 796041:

                        aa.clear()

                    if values == 797021:

                        aa.clear()

                    if values == 796051:

                        aa.clear()

            elif current_level == "3":

                if key == "id":

                    if values == 796041:

                        aa.clear()

                    if values == 797021:

                        aa.clear()

                    if values == 796051:

                        aa.clear()

            elif current_level == "4":

                if key == "id":

                    if values == 797021:

                        aa.clear()

                    if values == 796051:

                        aa.clear()


            elif current_level == "5":

                if key == "id":

                    if values == 796051:

                        aa.clear()

            elif current_level  == "-1":

                if key == "id":

                   if values  == 773011:

                       aa.clear()

                   if values == 769941:

                       aa.clear()

                   if values == 772051:

                       aa.clear()

                   if values == 772061:

                       aa.clear()

                   if values == 796041:

                       aa.clear()

                   if values == 797021:

                       aa.clear()

                   if values == 796051:

                       aa.clear()


    print(t2_result)

    while {} in t2_result:

        t2_result.remove({})

    print(t2_result)

    # 一级教材
    for t1 in t2_result:

        for key, values in sorted(t1.items(), key=operator.itemgetter(0)):

            if key == "id":

                c_cate_id1_id = values

            if key == "name":

                c_cate_id1_name = values

            c_cate1_dict = {

                "c_cate_id1_id": c_cate_id1_id,
                "c_cate_id1_name": c_cate_id1_name
            }

        # print ("传入一级id：",c_cate_id1_id)

        # 二级教材
        t2_result = textbook_series_junior_textbook_tree_depth_two_query_success(c_cate_id1_id)
        c_cate2_list = []

        for t2 in t2_result:

            for key, values in sorted(t2.items(), key=operator.itemgetter(0)):

                if key == "id":

                    c_cate_id2_id = values

                if key == "name":

                    c_cate_id2_name = values

                c_cate2_dict = {

                    "c_cate_id2_id": c_cate_id2_id,
                    "c_cate_id2_name": c_cate_id2_name,

                }

            # print("传入二级id：", c_cate_id2_id)

            # 三级教材
            t3_result = textbook_series_junior_textbook_tree_depth_three_query_success(c_cate_id2_id)

            c_cate3_list = []

            for t3 in t3_result:

                for key, values in sorted(t3.items(), key=operator.itemgetter(0)):

                    if key == "id":

                        book_id_id = values

                    if key == "name":

                        book_id_name = values

                    c_cate3_dict = {

                        "book_id_id": book_id_id,
                        "book_id_name": book_id_name

                    }

                c_cate3_list.append(c_cate3_dict)

            # print ("c_cate3_list-->",c_cate3_list)

            c_cate2_dict['bookCList'] = c_cate3_list
            # print (c_cate2_dict)

            c_cate2_list.append(c_cate2_dict)
            # print (c_cate2_list)

        c_cate1_dict['bookBList'] = c_cate2_list
        # print (c_cate1_dict)

        c_cate1_list.append(c_cate1_dict)
        # print (c_cate1_list)

    # print (c_cate1_list)
    # print(type(c_cate1_list))

    # c_cate1_json = json.dumps(c_cate1_list)
    # print(c_cate1_json)
    # print(type(c_cate1_json))

    return c_cate1_list

if __name__ == '__main__':

    #junior_textbook_level_K = 1084111
    #junior_textbook_level_0 = 773011
    #junior_textbook_level_1 = 769941

    #junior_textbook_level_2 = 772051
    #junior_textbook_level_3 = 772061
    #junior_textbook_level_4 = 796041
    #junior_textbook_level_5 = 797021
    #junior_textbook_level_6 = 796051

    c_cate1_list = getJuniorTextBookInfo()
    print (c_cate1_list)
    # print(type(c_cate1_list))

    c_cate1_json = json.dumps(c_cate1_list)
    print(c_cate1_json)
    # print(type(c_cate1_json))