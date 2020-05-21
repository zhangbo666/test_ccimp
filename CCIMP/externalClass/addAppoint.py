
import time

import requests
import json


'''
@method:addAppoint
'''
def addAppoint():

    '''
    获取约课自增ID
    return:返回约课自增ID
    '''
    appointIDUrl = "http://172.16.16.97/talkplatform_idgenerator_consumer/genId?keyName=appoint.id"

    appointIDResult = requests.get(url=appointIDUrl)
    appointIDResult_json = appointIDResult.json()
    # print (appointIDResult_json)
    appoint_id_result   = str(appointIDResult_json["id"])



    appoint_currery_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (currery_time)
    # print (type(currery_time))

    '''
    1v1约课接口
    '''
    addAppointUrl = "http://172.16.16.97/talkplatform_appointone_consumer/v1/appoint/add"

    head = {

        'Content-Type':'application/json'
    }

    addAppointData = {

        'id':appoint_id_result,
        't_id':'4814',
        's_id':'800037593',
        'tag_id':'87703151451772984943',
        'start_time':'2020-05-21 21:00:00',
        'end_time':'2020-05-21 21:25:00',
        'date_time':'20200521_43',
        'status':'on',
        'date':'2020-05-21',
        'time':'43',
        'week':'1',
        'add_time':appoint_currery_time,
        'course_id':'793021',
        'appoint_type':'ios',
        'point_type':'point',
        'cost_num':'1',
        'teach_type':'51TalkAC',
        'use_point':'buy',
        'cancel_operator':'0',
        'use_skype_id':'0',
        'need_oral':'0',
        'course_top_id':'773011',
        'course_sub_id':'793011',
        'course_type':'1',
        'tea_salary':'0',
        'package_id':'0',
        'category':'ph_buy'
    }

    add_appoint_result = requests.post(url=addAppointUrl,data=json.dumps(addAppointData),headers=head)

    print (add_appoint_result.json())


if __name__ == '__main__':

    '''
    获取约课自增ID
    return:返回约课自增ID
    '''
    appointIDUrl = "http://172.16.16.97/talkplatform_idgenerator_consumer/genId?keyName=appoint.id"

    appointIDResult = requests.get(url=appointIDUrl)
    appointIDResult_json = appointIDResult.json()
    # print (appointIDResult_json)
    appoint_id_result   = str(appointIDResult_json["id"])

    appoint_currery_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print (currery_time)
    # print (type(currery_time))

    '''
    1v1约课接口
    '''
    addAppointUrl = "http://172.16.16.97/talkplatform_appointone_consumer/v1/appoint/add"

    head = {

        'Content-Type':'application/json'
    }

    addAppointData = {

        'id':appoint_id_result,
        't_id':'4814',
        's_id':'800037593',
        'tag_id':'87703151451772984943',
        'start_time':'2020-05-21 21:00:00',
        'end_time':'2020-05-21 21:25:00',
        'date_time':'20200521_43',
        'status':'on',
        'date':'2020-05-21',
        'time':'43',
        'week':'1',
        'add_time':appoint_currery_time,
        'course_id':'793021',
        'appoint_type':'ios',
        'point_type':'point',
        'cost_num':'1',
        'teach_type':'51TalkAC',
        'use_point':'buy',
        'cancel_operator':'0',
        'use_skype_id':'0',
        'need_oral':'0',
        'course_top_id':'773011',
        'course_sub_id':'793011',
        'course_type':'1',
        'tea_salary':'0',
        'package_id':'0',
        'category':'ph_buy'
    }

    add_appoint_result = requests.post(url=addAppointUrl,data=json.dumps(addAppointData),headers=head)

    print (add_appoint_result.json())