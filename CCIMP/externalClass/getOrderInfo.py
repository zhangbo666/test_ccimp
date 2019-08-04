__author__ = 'zhangbo'


def getOrderInfo(req,point_id) -> str:
    '''
    用户下单
    :param pointId:套餐id
    :param is_Process: 是否处理订单
    :return:订单id
    '''

    signUrl = 'http://sale.51talk.com/ajax/getOrderInfo?&web=1&cart={"cart":["' + str(point_id) + '"]}'
    s = req.get(url=signUrl)
    try:
        sign = s.json()['data']['data_sign']
        print('获取签名：{}'.format(sign))

    except:

        return False

    payUrl = 'http://sale.51talk.com/orderPay'
    payData = {
        'is_cash_down': '0',
        'sign': sign,
        'gateway': '99online',
        'point_id': str(point_id),
        'agreement': '1',
        'payMethod': 'bank'
    }
    pay = req.post(url=payUrl,data=payData,verify=False)

    orderId = str(pay.url).split('order_id=')[1]

    # print('接口返回code：{}，返回的url：{}，订单id：{}'.format(pay.status_code,pay.url,orderId))
    # return '接口返回code：{}，返回的url：{}，订单id：{}'.format(pay.status_code,pay.url,orderId)

    return orderId
    # try:
    #
    #
    #     if is_Process :
    #         processOrder(orderId)
    #         return '订单%s处理成功！'%(orderId)
    #     else:
    #         return '订单%s未处理！'%(orderId)
    # except:
    #     return '订单id获取失败！'
