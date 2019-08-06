__author__ = 'zhangbo'



def processOrder(req,order_id):

    processUrl = 'http://www.51talk.com/admin/order/do_deal_order.php?order_id=' + str(order_id)

    responses_result = req.get(url=processUrl)

    return responses_result

