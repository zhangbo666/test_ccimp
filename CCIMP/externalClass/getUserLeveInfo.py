#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'



import re,requests,os,sys
import operator

currentdir = os.path.dirname(os.path.realpath(__file__))
# print (currentdir)
sys.path.append(currentdir)

# parentdir = os.path.dirname(currentdir)
# print (parentdir)
# sys.path.append(parentdir)


from userInfo.login.adminLogin import adminLogin

from database.talkQueryUserInfo import talk_query_user_info_id_success,talk_query_user_info_detail_success

from database.kidsQueryUserKidsExt import kids_query_user_kids_ext_info_detail_success

def getUserLevelInfo(user_id):


    user_level_info = kids_query_user_kids_ext_info_detail_success(user_id)

    return user_level_info

if __name__ == '__main__':

    mobile = '18611220000'

    # userId    = talk_query_user_info_id_success(mobile)
    # user_level_result = getUserLevelInfo(userId)

    # print (user_level_result)
    # print (type(user_level_result))

    # for u1 in user_level_result:

    #     for key, values in sorted(u1.items(), key=operator.itemgetter(0)):

    #         if key == "current_level":

    #             print (values)


    userInfo = talk_query_user_info_detail_success(mobile)

    print (userInfo)
    print (type(userInfo))

    for u1 in userInfo:

        for key, values in sorted(u1.items(), key=operator.itemgetter(0)):

            if key == "current_level":

                print (values)
