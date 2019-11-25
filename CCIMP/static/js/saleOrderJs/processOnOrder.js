/**
 * Created by zhangbo on 19/9/10.
 */

//处理当前账户下未完成的订单
function processOnOrder(){

    var radio_on_order = document.getElementsByName('radio_on_orders');

    var isCheck = false;

    var  processOnOrderDoubleClick = 0;

    if (document.getElementsByName('radio_on_orders').length > 0) {

        for (var i = 0; i < radio_on_order.length; i++) {

            var checkeds = document.querySelectorAll("[name=radio_on_orders]")[i].checked;

            if (checkeds === true){

                var order_id = $("input[name=radio_on_orders]:checked").val();

                alert("订单处理开始，请等候...");

                isCheck = true;

                //禁用处理未完成订单按钮点击事件
                $("#processOnOrder").attr("disabled",true);
//                  $("#processOnOrder").attr("disabled","disabled");
//                  window.document.getElementById('processOnOrder').setAttribute("disabled",true);


                //处理订单按钮连击，暂不考虑
//                    if (processOnOrderDoubleClick == 0) {
//
//                        processOnOrderDoubleClick = 1;
//
//                        $("#processOnOrder").attr("disabled",true);
//
//                        setTimeout(function () {
//
//                            processOnOrderDoubleClick = 0;
//
//                          $("#processOnOrder").attr("disabled",false);
//
//                        }, 20000);
//                    }


                //处理订单接口
                $.ajax({
                url:'/tool/sale_order/process_order/',
                type:'POST',
                data:{'order_id':order_id},
                success:function(data){

                    if (data.status_code === 10101 || data.status_code === 10102) {

                        alert(data.message);

                    }

                    else if (data.status_code === 10200) {

                        alert(data.message);

                    }

                }

                });

            }
        }

        if (!isCheck){

            alert("当前还未选择订单！！！");

        }


    }

    else{

        alert("当前订单数据列表为空！")
    }


}