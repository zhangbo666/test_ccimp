
import time

import requests
import json

keyNameUrl = "http://172.16.16.58/talkplatform_idgenerator_consumer/genId?keyName=appoint.id"


result = requests.get(keyNameUrl)
result_text = result.json()
print (result_text)
result_id   = str(result_text["id"])



currery_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print (currery_time)
print (type(currery_time))

appointAddUrl = "http://172.16.16.97/talkplatform_appointone_consumer/v1/appoint/add"

head = {

    'Content-Type':'application/json'
}

appointAddTata = {

    'id':result_id,
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
    'add_time':currery_time,
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


# appointAddTata = {
#
#     "id":result_id,
#     "tag_id":"87703151451772984943",
#     "t_id":"4814",
#     "s_id":"800037593",
#     "date_time":"20200521_39",
#     "start_time":"2020-05-21 19:00:00",
#     "end_time":"2020-05-21 19:25:00",
#     "status":"on",
#     "date":"2020-05-21",
#     "time":"39",
#     "week":"5",
#     "add_time":currery_time,
#     "course_id":"793021",
#     "appoint_type":"ios",
#     "point_type":"point",
#     "cost_num":"1",
#     "teach_type":"51TalkAC",
#     "use_point":"buy",
#     "cancel_operator":"0",
#     "use_skype_id":"0",
#     "need_oral":"0",
#     "course_top_id":"773011",
#     "course_sub_id":"793011",
#     "course_type":"1",
#     "tea_salary":"0",
#     "package_id":"0",
#     "category":"ph_buy"
# }


# appointAddTata = {
#
#     "id":result_id,
#     "tag_id":"87703151451772984942",
#     "t_id":"4814",
#     "s_id":"800037593",
#     "date_time":"20200521_39",
#     "start_time":"2020-05-21 19:00:00",
#     "end_time":"2020-05-21 19:25:00",
#     "status":"on",
#     "date":"20200521",
#     "time":"39",
#     "week":"1",
#     "add_time":currery_time,
#     "course_id":"793021",
#     "course_info":"测试课程",
#     "course_desc":"20200521",
#     "opinion":"5",
#     "appoint_type":"ios",
#     "cancel_time":"20200521",
#     "point_type":"point",
#     "cost_num":"1",
#     "now_level":"0",
#     "teach_type":"51TalkAC",
#     "use_point":"buy",
#     "cancel_operator":"0",
#     "cancel_reason":"测试课程",
#     "use_skype_id":"0",
#     "need_oral":"0",
#     "course_top_id":"773011",
#     "course_sub_id":"793011",
#     "course_type":"1",
#     "tea_salary":"0",
#     "package_id":"0",
#     "category":"ph_buy",
#
# }

appoint_result = requests.post(url=appointAddUrl,data=json.dumps(appointAddTata),headers=head)

print (appoint_result.json())