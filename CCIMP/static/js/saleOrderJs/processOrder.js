/**
 * Created by zhangbo on 19/9/7.
 */


//处理订单
function processOrder(){

    var radio_order = document.getElementsByName('radio_orders');

    var isCheck = false;

    //处理订单按钮连击
    var processOrderDoubleClick = 0;

    if ($("#radio_orders").length > 0) {

        for (var i = 0; i < radio_order.length; i++) {

//                if (radio_order[i].checked){
//
//                    userid = radio_order[i].value;
//
//                    isCheck = true;
//
//                }
            var checkeds = document.querySelectorAll("[name=radio_orders]")[i].checked;

            if (checkeds === true){

                var order_id = $("input[name=radio_orders]:checked").val();

                alert("订单处理开始，请等候...");

                isCheck = true;

                //禁用按钮点击事件
                $("#processOrder").attr("disabled",true);
                //$("#processOrder").attr("disabled","disabled");
                //window.document.getElementById('processOrder').setAttribute("disabled",true);


                //处理订单按钮连击，暂不考虑
//                    if (processOrderDoubleClick == 0) {
//
//                        processOrderDoubleClick = 1;
//
//                        $("#processOrder").attr("disabled",true);

//                        setTimeout(function () {
//
//                            processOrderDoubleClick = 0;
//
//                          $("#processOrder").attr("disabled",false);
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

                        alert("该订单处理成功！");

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
