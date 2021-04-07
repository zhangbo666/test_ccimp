__author__ = 'zhangbo'


from externalClass.open_class.openClassConfig import *

from db_config.talkQueryOpenClassInfo import textbook_series_textbook_tree_depth_one_query_success
from db_config.talkQueryOpenClassInfo import textbook_series_textbook_tree_depth_two_query_success
from db_config.talkQueryOpenClassInfo import textbook_series_textbook_tree_depth_three_query_success

import operator
import json



def getTextBookInfo(c_cate1_textbook_limit_sum,c_cate2_textbook_limit_sum,c_cate3_textbook_limit_sum):

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

    t1_result = textbook_series_textbook_tree_depth_one_query_success(c_cate1_textbook_limit_sum)

    # print (t1_rusult)
    # print (type(t1_rusult))


    # t1_json = json.dumps(t1_rusult)
    # print (t1_json)
    # print (type(t1_json))

    # 一级教材
    for t1 in t1_result:

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
        t2_result = textbook_series_textbook_tree_depth_two_query_success(c_cate_id1_id, c_cate2_textbook_limit_sum)
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
            t3_result = textbook_series_textbook_tree_depth_three_query_success(c_cate_id2_id, c_cate3_textbook_limit_sum)

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


    c_cate1_list = getTextBookInfo(c_cate1_textbook_limit_sum,c_cate2_textbook_limit_sum,c_cate3_textbook_limit_sum)

    # print (c_cate1_list)
    # print(type(c_cate1_list))

    c_cate1_json = json.dumps(c_cate1_list)
    # print(c_cate1_json)
    # print(type(c_cate1_json))