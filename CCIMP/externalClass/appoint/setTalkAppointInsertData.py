__author__ = 'zhangbo'

import operator

from db_config.talkInsertAppointInfo import talk_insert_appoint_info_success
from externalClass.appoint.getTalkPlatformAppointData import getTalkPlatformAppointData


#获取通过datatime时间查询php约课表约课id
def setTalkAppointInsertData(talkplatform_appoint_info_list):

    talk_appoint_info_list = talkplatform_appoint_info_list

    id_values = ""
    t_id_values = ""
    s_id_values = ""
    date_time_values = ""
    tag_id_values = ""
    start_time_values = ""
    end_time_values = ""
    status_values = ""
    date_values = ""
    time_values = ""
    week_values = ""
    add_time_values = ""
    course_id_values = ""
    appoint_type_values = ""
    point_type_values = ""
    cost_num_values = ""
    teach_type_values = ""
    use_point_values = ""
    now_level_values = ""
    cancel_operator_values = ""
    use_skype_id_values = ""
    need_oral_values = ""
    course_top_id_values = ""
    course_sub_id_values = ""
    course_type_values = ""
    tea_salary_values = ""
    update_time_values = ""
    package_id_values = ""
    category_values = ""


    for talk_appoint_info_list_1 in talk_appoint_info_list:

        for key, values in sorted(talk_appoint_info_list_1.items(), key=operator.itemgetter(0)):

            if key == "id":

                id_values = str(values)

            if key == "t_id":

                t_id_values = str(values)

            if key == "s_id":

                s_id_values = str(values)

            if key == "date_time":

                date_time_values = str(values)

            if key == "tag_id":

                tag_id_values = str(values)

            if key == "start_time":

                start_time_values = str(values)

            if key == "end_time":

                end_time_values = str(values)

            if key == "status":

                status_values = str(values)

            if key == "date":

                date_values = str(values)

            if key == "time":

                time_values = str(values)

            if key == "week":

                week_values = str(values)

            if key == "add_time":

                add_time_values = str(values)

            if key == "course_id":

                course_id_values = str(values)

            if key == "appoint_type":

                appoint_type_values = str(values)

            if key == "point_type":

                point_type_values = str(values)

            if key == "cost_num":

                cost_num_values = str(values)

            if key == "teach_type":

                teach_type_values = str(values)

            if key == "use_point":

                use_point_values = str(values)

            if key == "now_level":

                now_level_values = str(values)

            if key == "cancel_operator":

                cancel_operator_values = str(values)

            if key == "use_skype_id":

                use_skype_id_values = str(values)

            if key == "need_oral":

                need_oral_values = str(values)

            if key == "course_top_id":

                course_top_id_values = str(values)

            if key == "course_sub_id":

                course_sub_id_values = str(values)

            if key == "course_type":

                course_type_values = str(values)

            if key == "tea_salary":

                tea_salary_values = str(values)

            if key == "update_time":

                update_time_values = str(values)

            if key == "package_id":

                package_id_values = str(values)

            if key == "category":

                category_values = str(values)

    talk_insert_appoint_info_success(id_values,t_id_values,s_id_values,date_time_values,tag_id_values,
                                     start_time_values,end_time_values,status_values,date_values,time_values,
                                     week_values,add_time_values,course_id_values,appoint_type_values,point_type_values,
                                     cost_num_values,teach_type_values,use_point_values,now_level_values,
                                     cancel_operator_values,use_skype_id_values,need_oral_values,course_top_id_values,
                                     course_sub_id_values,course_type_values,tea_salary_values,update_time_values,
                                     package_id_values,category_values)

    # return talk_appoint_info_list


if __name__ == '__main__':

    appoint_id = "52681375"

    talkplatform_appoint_info_list = getTalkPlatformAppointData(appoint_id)

    print (talkplatform_appoint_info_list)

    setTalkAppointInsertData(talkplatform_appoint_info_list)