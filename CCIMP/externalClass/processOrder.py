from externalClass.adminLogin import adminLogin

__author__ = 'zhangbo'


def processOrder(req,order_id):

    processUrl = 'http://www.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    responses_result = req.get(url=processUrl)

    return responses_result


if __name__ == '__main__':

    #调取后台登录接口
    admin_login = adminLogin()

    order_id = "1801568487"

    #调取后台处理订单接口
    processUrl = 'http://www.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    info = admin_login.get(url=processUrl)

    print(info.text,info.status_code)



