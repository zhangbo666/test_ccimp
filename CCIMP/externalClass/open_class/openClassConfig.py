__author__ = "zhangbo"


from ccimp_systemSettings_app.models.WebConfigModels import WebConfig
import json


def openClassTeacherConfig():

    # 公开课老师查询数量
    openClassTeacheConfig = "OpenClassTeacheConfig"

    # 调取默认配置表(configKey=OpenClassTeacheConfig)
    webConfigs = WebConfig.objects.all()

    for w1 in webConfigs:

        if (w1.keyConfig == openClassTeacheConfig):

            dict_data = w1.valueConfig

            # src转dict
            w1 = json.loads(dict_data)

            limin_teacher_sum = int(w1["sum"])

            return limin_teacher_sum

        else:

            #默认返回
            limin_teacher_sum = 10

def openClassOneTextBookConfig():

    # 一级教材查询数量
    openClassOneTextBookConfig = "OpenClassOneTextBookConfig"

    # 调取默认配置表(configKey=OpenClassOneTextBookConfig)
    webConfigs = WebConfig.objects.all()

    for w1 in webConfigs:

        if (w1.keyConfig == openClassOneTextBookConfig):

            dict_data = w1.valueConfig

            # src转dict
            w1 = json.loads(dict_data)

            c_cate1_textbook_limit_sum = int(w1["sum"])

            return c_cate1_textbook_limit_sum

        else:

            # 默认返回
            c_cate1_textbook_limit_sum = 10


def openClassTwoTextBookConfig():

    # 二级教材查询数量
    openClassTwoTextBookConfig = "OpenClassTwoTextBookConfig"

    # 调取默认配置表(configKey=OpenClassTwoTextBookConfig)
    webConfigs = WebConfig.objects.all()

    for w1 in webConfigs:

        if (w1.keyConfig == openClassTwoTextBookConfig):

            dict_data = w1.valueConfig

            # src转dict
            w1 = json.loads(dict_data)

            c_cate2_textbook_limit_sum = int(w1["sum"])

            return c_cate2_textbook_limit_sum

        else:

            # 默认返回
            c_cate2_textbook_limit_sum = 10

def openClassThreeTextBookConfig():

    # 三级教材查询数量
    openClassThreeTextBookConfig = "OpenClassThreeTextBookConfig"

    # 调取默认配置表(configKey=OpenClassThreeTextBookConfig)
    webConfigs = WebConfig.objects.all()

    for w1 in webConfigs:

        if (w1.keyConfig == openClassThreeTextBookConfig):

            dict_data = w1.valueConfig

            # src转dict
            w1 = json.loads(dict_data)

            c_cate3_textbook_limit_sum = int(w1["sum"])

            return c_cate3_textbook_limit_sum

        else:

            # 默认返回
            c_cate3_textbook_limit_sum = 10


def openClassCourseConfig():

    # 公开课开课查询数量
    openClassCourseListConfig = "OpenClassCourseListConfig"

    # 调取默认配置表(configKey=OpenClassCourseListConfig)
    webConfigs = WebConfig.objects.all()

    for w1 in webConfigs:

        if (w1.keyConfig == openClassCourseListConfig):

            dict_data = w1.valueConfig

            # src转dict
            w1 = json.loads(dict_data)

            course_limit_sum = int(w1["sum"])

            return course_limit_sum

        else:

            # 默认返回
            course_limit_sum = 10