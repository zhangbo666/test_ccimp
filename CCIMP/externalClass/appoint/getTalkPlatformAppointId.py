__author__ = 'zhangbo'

import operator

from db_config.talkQueryAppointInfo import talkplatform_appoint_reconstruction_appoint_info_appoint_id_success


#获取通过datatime时间查询平台约课表约课id
def getTalkPlatformAppointId(date_time):

    appoint_id = ""

    talkplatfrom_appoint_id_result = talkplatform_appoint_reconstruction_appoint_info_appoint_id_success(date_time)

    if talkplatfrom_appoint_id_result == () or talkplatfrom_appoint_id_result == None:

        return 0

    for result_list in talkplatfrom_appoint_id_result:

        for key, values in sorted(result_list.items(), key=operator.itemgetter(0)):

            if key == "id":

                appoint_id = values

    return appoint_id


if __name__ == '__main__':

    date_time = '20210611_43'

    talkplatfrom_appoint_id_result = getTalkPlatformAppointId(date_time)
    # print (talkplatfrom_appoint_id_result)
    # print (type(talkplatfrom_appoint_id_result))