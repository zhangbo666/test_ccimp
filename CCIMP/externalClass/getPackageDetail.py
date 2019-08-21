# -*- coding: utf-8 -*-:

__author__ = 'zhangbo'

import json

def getPackageDetail(req):

    point_type_list = []

    orderTypeList = 'http://sale.51talk.com/api/typeList?from=web'
    orderDetailList = [{'point_package_10':'http://sale.51talk.com/api/pointList?point_type=point_package_10'},
                       {'point_package':'http://sale.51talk.com/api/pointList?point_type=point_package'},
                       {'point':'http://sale.51talk.com/api/pointList?point_type=point'},
                       {'shuagnshi':'http://sale.51talk.com/api/pointList?from=web&point_type=mix_point'}]


    # 套餐type类型
    point_type_json= req.get(url=orderTypeList).json()

    point_type_json_dict = {'point_type_json':point_type_json['data']}


    for i in orderDetailList:

        for (point_type,point_url) in i.items():

            try:

                #返回dict类型
                data_json = req.get(url=point_url).json()
                # print ("data_json-->",data_json)
                # print ("type(data_json)-->",type(data_json))

                if data_json['status'] == 0:

                    print ('该' + point_type + '套餐接口下暂无套餐信息-->>',data_json['info'])
                    # print ('data_json["data"]-->',data_json['data'])
                    # print ('data_json["data"]-->',type(data_json['data']))

                else:

                    point_type_dict = {

                        'point_type':point_type,
                        'point_info':data_json['data'],

                    }

                    point_type_list.append(point_type_dict)
                    # print ("point_type_list-->",point_type_list)

            except:

                print ("获取接口错误")

            order_detail_dict = {

                'point_type_data':point_type_list
            }

    order_info_dict = {

        'info':"获取套餐信息成功",
        'order_detail_dict':order_detail_dict,
        'point_type_json_dict':point_type_json_dict,

    }

    # print ("order_detail_dict-->",order_detail_dict)

    #返回list类型
    order_info = order_info_dict['order_detail_dict']['point_type_data']
    # print ("order_info-->",order_info)
    # print ("order_info-->",type(order_info))


    point_detail_list = []

    for info in order_info:

        point_info = info['point_info']
        # print ("point_info-->",point_info)
        # print ("point_info-->",type(point_info))
        # print (" ")

        for p_info in point_info:

            pointDetail = {

                "point_id":p_info['id'],
                "name":p_info['name'],
                "price":p_info['price'],
                "point_type":p_info['point_type'],
            }

            point_detail_list.append(pointDetail)


    point_detail_dict = {

        "status":1,
        "data":point_detail_list
    }

    #转为json格式(str)
    point_detail_dict_jsonStr = json.dumps(point_detail_dict)
    # print ("point_detail_dict_jsonStr-->",point_detail_dict_jsonStr)
    print ("point_detail_dict_jsonStr-->",type(point_detail_dict_jsonStr))
    print (" ")

    return point_detail_dict_jsonStr