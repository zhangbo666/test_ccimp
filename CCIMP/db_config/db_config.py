#!usr/bin/python
#encoding:utf-8

__author__ = 'zhangbo'

from pymysql import connect,cursors

'''###############################################################################'''

# 连接172.16.70.20--teanew数据库
# conn_teanew = connect(host='172.16.70.20',
#                       user='rd_user',
#                       password='NTHXDF7czYwi',
#                       port=3306,
#                       db='teanew',
#                       charset='utf8',
#                       cursorclass=cursors.DictCursor)
# 连接teanew数据库游标
# cursor_teanew = conn_teanew.cursor()

'''###############################################################################'''


'''###############################################################################'''

# 连接172.16.70.20--talk测试数据库
conn_talk = connect(host='172.16.70.20',
                          user='rd_user',
                          password='NTHXDF7czYwi',
                          port=3306,
                          db='talk',
                          charset='utf8',
                          cursorclass=cursors.DictCursor)
# 连接talk数据库游标
cursor_talk = conn_talk.cursor()

'''###############################################################################'''


'''###############################################################################'''

# 连接172.16.70.20--point测试数据库
conn_point = connect(host='172.16.70.20',
                          user='rd_user',
                          password='NTHXDF7czYwi',
                          port=3306,
                          db='point',
                          charset='utf8',
                          cursorclass=cursors.DictCursor)
# 连接point数据库游标
cursor_point = conn_point.cursor()

'''###############################################################################'''


'''###############################################################################'''

# 连接172.16.70.20--talkplatform_appoint_reconstruction测试数据库
conn_talkplatform_appoint_reconstruction = connect(host='172.16.70.20',
                          user='rd_user',
                          password='NTHXDF7czYwi',
                          port=3306,
                          db='talkplatform_appoint_reconstruction',
                          charset='utf8',
                          cursorclass=cursors.DictCursor)
# 连接talkplatform_appoint_reconstruction数据库游标
cursor_talkplatform_appoint_reconstruction = conn_talkplatform_appoint_reconstruction.cursor()

'''###############################################################################'''


'''###############################################################################'''

# 连接172.16.70.20--talkdata_php测试数据库
conn_talkdata_php = connect(host='172.16.70.20',
                          user='rd_user',
                          password='NTHXDF7czYwi',
                          port=3306,
                          db='talkdata_php',
                          charset='utf8',
                          cursorclass=cursors.DictCursor)
# 连接talkdata_php数据库游标
cursor_talkdata_php = conn_talkdata_php.cursor()

'''###############################################################################'''


# 连接本地测试数据库
# conn_test = connect(host='127.0.0.1',
#                     user='root',
#                     password='123456',
#                     port=3306,
#                     db='test',
#                     charset='utf8',
#                     cursorclass=cursors.DictCursor)
# 连接本地测试数据库游标
# cursor_test = conn_test.cursor()


# 连接线上测试数据库
# conn_onlie_test = connect(host='127.0.0.1',
#                           user='root',
#                           # password='123456',
#                           password='1234qwer',
#                           port=3306,
#                           db='onlie_test',
#                           charset='utf8',
#                           cursorclass=cursors.DictCursor)
# 连接线上测试数据库游标
# cursor_onlie_test = conn_onlie_test.cursor()