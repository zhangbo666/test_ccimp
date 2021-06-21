#!usr/bin/python
#encoding:utf-8

from time import sleep
from db_config.dbConfig import *
import operator

#----------------------------------------------------------------------------------------------------------------------#
    # 插入talk库-->appoint表约课数据
#----------------------------------------------------------------------------------------------------------------------#

def talk_insert_appoint_info_success(id_values,t_id_values,s_id_values,date_time_values,tag_id_values,
                                     start_time_values,end_time_values,status_values,date_values,time_values,
                                     week_values,add_time_values,course_id_values,appoint_type_values,point_type_values,
                                     cost_num_values,teach_type_values,use_point_values,now_level_values,
                                     cancel_operator_values,use_skype_id_values,need_oral_values,course_top_id_values,
                                     course_sub_id_values,course_type_values,tea_salary_values,update_time_values,
                                     package_id_values,category_values):

    '''插入数据表记录'''

    try:

        with conn_talk.cursor() as cursor:

            #单条插入
            # sql_insert  = "INSERT into appoint(id,t_id,s_id,date_time,tag_id,start_time,end_time,status,date,time," \
            #               "week,add_time,course_id,appoint_type,point_type,cost_num,teach_type,use_point,now_level" \
            #               "cancel_operator,use_skype_id,need_oral,course_top_id,course_sub_id,course_type,tea_salary" \
            #               "update_time,package_id,category) VALUES (id_values,t_id_values,s_id_values,date_time_values," \
            #               "tag_id_values,start_time_values,end_time_values,status_values,date_values,time_values," \
            #               "week_values,add_time_values,course_id_values,appoint_type_values,point_type_values," \
            #               "cost_num_values,teach_type_values,use_point_values,now_level_values,cancel_operator_values," \
            #               "use_skype_id_values,need_oral_values,course_top_id_values,course_sub_id_values,course_type_values," \
            #               "tea_salary_values,update_time_values,package_id_values,category_values)"

            sql_insert  = "INSERT into appoint(id,t_id,s_id,date_time,tag_id,start_time,end_time,status,date,time," \
                          "week,add_time,course_id,appoint_type,point_type,cost_num,teach_type,use_point,now_level," \
                          "cancel_operator,use_skype_id,need_oral,course_top_id,course_sub_id,course_type,tea_salary," \
                          "update_time,package_id,category) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cursor.execute(sql_insert,(id_values,t_id_values,s_id_values,date_time_values,tag_id_values,
                                     start_time_values,end_time_values,status_values,date_values,time_values,
                                     week_values,add_time_values,course_id_values,appoint_type_values,point_type_values,
                                     cost_num_values,teach_type_values,use_point_values,now_level_values,
                                     cancel_operator_values,use_skype_id_values,need_oral_values,course_top_id_values,
                                     course_sub_id_values,course_type_values,tea_salary_values,update_time_values,
                                     package_id_values,category_values))

            conn_talk.commit()

            sleep(2)

    except Exception as e:

        conn_talk.rollback()

        print (e)

    finally:

        cursor.close()

        conn_talk.close()