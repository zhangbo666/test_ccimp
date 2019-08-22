__author__ = 'zhangbo'


def getCheckCartInfo(req,point_id):

    '''
    是否该套餐可以被下单
    :param pointId:套餐id
    :return:req
    '''

    #查看套餐是否可以被下单接口
    checkCart_Url = 'http://sale.51talk.com/ajax/checkCart?&cart={"cart":["' + str(point_id) + '"]}'

    req_s = req.get(url=checkCart_Url)

    #返回为0，不能下该套餐、返回为1可以下单
    checkCartList_status = req_s.json()['status']
    # print ("checkCartList_status-->",checkCartList_status)

    if checkCartList_status == 0:

        return False

    else:

        return True