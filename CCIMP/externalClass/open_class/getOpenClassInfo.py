__author__ = 'zhangbo'


import operator

from externalClass.open_class.openClassConfig import *

from db_config.talkQueryOpenClassInfo import talkplatform_course_course_query_success


def getOpenClassInfo(course_limit_sum):

    open_class_info_result = talkplatform_course_course_query_success(course_limit_sum)

    return open_class_info_result


if __name__ == '__main__':

    open_class_result_list = getOpenClassInfo(course_limit_sum)

    # print ("open_class_result_list",type(open_class_result_list))
    # print ("open_class_result_list",open_class_result_list)

    # open_class_result_json = json.dumps(open_class_result_json)
    # print ("open_class_result_json",type(open_class_result_json))
    # print ("open_class_result_json",open_class_result_json)

    open_class_info_result_dict = {}
    open_class_info_result_list = []

    open_class_id = ""
    open_class_course_type = ""
    open_class_book_id = ""
    open_class_book_name = ""
    open_class_book_type = ""
    open_class_tea_ids = ""
    open_class_start_time = ""
    open_class_end_time = ""

    for open_class_1 in open_class_result_list:

        for key, values in sorted(open_class_1.items(), key=operator.itemgetter(0)):

            if key == "id":
                open_class_id = values

            if key == "course_type":
                open_class_course_type = values

            if key == "book_id":
                open_class_book_id = values

            if key == "name":
                open_class_book_name = values

            if key == "book_type":
                open_class_book_type = values

            if key == "tea_ids":
                open_class_tea_ids = values

            if key == "start_time":

                start_time = values.strftime('%Y-%m-%d %H:%M:%S')

                open_class_start_time = start_time

            if key == "end_time":

                end_time = values.strftime('%Y-%m-%d %H:%M:%S')

                open_class_end_time = end_time

            open_class_info_result_dict = {

                "id": open_class_id,
                "course_type": open_class_course_type,
                "book_id": open_class_book_id,
                "name": open_class_book_name,
                "book_type": open_class_book_type,
                "tea_ids": open_class_tea_ids,
                "start_time": open_class_start_time,
                "end_time": open_class_end_time

            }

        open_class_info_result_list.append(open_class_info_result_dict)

    print("open_class_info_result_list", type(open_class_info_result_list))
    print(open_class_info_result_list)

    # open_class_info_result_json = json.dumps(open_class_info_result_list)
    # print ("open_class_info_result_json",type(open_class_info_result_json))
    # print (open_class_info_result_json)