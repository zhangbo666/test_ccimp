__author__ = 'zhangbo'


from db_config.talkQueryAppointInfo import talk_query_appoint_info_appoint_id_success


#通过平台库约课id查询php约课表约课id
def getTalkAppointId(appoint_id):

    talk_appoint_id_result = talk_query_appoint_info_appoint_id_success(appoint_id)

    return talk_appoint_id_result


if __name__ == '__main__':

    appoint_id = "52681278"

    talk_appoint_id_result = getTalkAppointId(appoint_id)

    print (talk_appoint_id_result)
    print (type(talk_appoint_id_result))