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

                data_json = req.get(url=point_url).json()

                if data_json['status'] == 0:

                    print ('该' + point_type + '套餐接口下暂无套餐信息-->>',data_json['info'])

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

    order_info = order_info_dict['order_detail_dict']['point_type_data']

    point_detail_list = []

    for info in order_info:

        point_info = info['point_info']

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

    #转为json格式
    point_detail_dict_json = json.dumps(point_detail_dict)

    return point_detail_dict_json

    # for o1 in point_detail_list:
    #
    #     point_type = o1['point_type']
    #     point_id = o1['point_id']
    #     price = o1['price']
    #     name = o1['name']
    #
    #     print ("套餐信息分别如下：")
    #     print ("point_type-->>",point_type)
    #     print ("point_id-->>",point_id)
    #     print ("price-->>",price)
    #     print ("name-->>",name,'\n')