/**
 * Created by zhangbo on 19/9/10.
 */

//处理当前账户下未完成的订单--多选操作
function processOnOrder(){

    var checkbox_on_orders = document.getElementsByName('checkbox_on_orders');

    order_id_check_val = [];

    var isCheck = false;

    var  processOnOrderDoubleClick = 0;

    if (document.getElementsByName('checkbox_on_orders').length > 0) {

        if ($('input:checked').length === 0){

            alert("当前还未选择订单！！！");

            return;

        }

        for (var i = 0; i < checkbox_on_orders.length; i++) {

            if (checkbox_on_orders[i].checked) {

                //添加到数组
                order_id_check_val.push(checkbox_on_orders[i].value);

            }
        }

        //将数组对象转化成json字符串，传到后端系统
        order_id_check_val = JSON.stringify(order_id_check_val);

        alert("订单处理开始，请等候...");

        //禁用处理未完成订单按钮点击事件
        $("#processOnOrder").attr("disabled",true);
        // $("#processOnOrder").attr("disabled","disabled");
        // window.document.getElementById('processOnOrder').setAttribute("disabled",true);


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
        data:{'order_id_check_val':order_id_check_val},
        success:function(data){

            if (data.status_code === 10101 || data.status_code === 10102) {

                alert(data.message);

                $.ajax({
                    url:'/tool/sale_order/get_rest_order_on_detail/',
                    type:'GET',
                    success:function (data) {

                        if (data.status_code === 10200) {

                            // alert(data.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1=document.getElementById("myTableUserOnOrderDetail");

                            var table1_tbody=table1.getElementsByTagName("tbody");

                            if (table1_tbody.length >0){

                                table1.removeChild(table1_tbody[0]);

                            };

                            var data = data.result;

                            //单选钮
                            // for (var i=0; i < data.length; i++){
                            //
                            //     var str = '<td>' +
                            //               '<input type="radio" name="radio_on_orders" id="radio_on_orders" value='+ data[i].id + '>' + '</td>' +
                            //               '<td>' + data[i].id + '</td>' +
                            //               '<td>' + data[i].extend_id + '</td>' +
                            //               '<td>' + data[i].order_money + '</td>' +
                            //               '<td>' + data[i].order_type + '</td>' +
                            //               '<td>' + data[i].status + '</td>';
                            //     $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
                            // }

                            //复选框
                            for (var i=0; i < data.length; i++){

                                var str = '<td>' +
                                          '<input type="checkbox" name="checkbox_on_orders" id="checkbox_on_orders" value='+ data[i].id + '>' + '</td>' +
                                          '<td>' + data[i].id + '</td>' +
                                          '<td>' + data[i].extend_id + '</td>' +
                                          '<td>' + data[i].order_money + '</td>' +
                                          '<td>' + data[i].order_type + '</td>' +
                                          '<td>' + data[i].status + '</td>';
                                $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
                            }


                            //释放处理未完成订单按钮点击事件
                            $("#processOnOrder").attr("disabled",false);
                            //$("#processOnOrder").removeAttr("disabled");
                            //window.document.getElementById('processOnOrder').removeAttribute('disabled');

                        }

                        else if (data.status_code === 10100){

                            window.alert(data.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1=document.getElementById("myTableUserOnOrderDetail");

                            var table1_tbody=table1.getElementsByTagName("tbody");

                            if (table1_tbody.length >0){

                                table1.removeChild(table1_tbody[0]);

                            };

                            //模态框延迟600毫秒后，自动关闭模态框
                            setTimeout("$('#myModalUserOnOrderDetail').modal('hide')",600);

                        }
                    }
                })

            }

            else if (data.status_code === 10200) {

                alert(data.message);

                $.ajax({
                    url:'/tool/sale_order/get_rest_order_on_detail/',
                    type:'GET',
                    success:function (data) {

                        if (data.status_code === 10200) {

                            // alert(data.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1=document.getElementById("myTableUserOnOrderDetail");

                            var table1_tbody=table1.getElementsByTagName("tbody");

                            if (table1_tbody.length >0){

                                table1.removeChild(table1_tbody[0]);

                            };

                            var data = data.result;

                            //单选钮
                            // for (var i=0; i < data.length; i++){
                            //
                            //     var str = '<td>' +
                            //               '<input type="radio" name="radio_on_orders" id="radio_on_orders" value='+ data[i].id + '>' + '</td>' +
                            //               '<td>' + data[i].id + '</td>' +
                            //               '<td>' + data[i].extend_id + '</td>' +
                            //               '<td>' + data[i].order_money + '</td>' +
                            //               '<td>' + data[i].order_type + '</td>' +
                            //               '<td>' + data[i].status + '</td>';
                            //     $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
                            // }

                            //复选框
                            for (var i=0; i < data.length; i++){

                                var str = '<td>' +
                                          '<input type="checkbox" name="checkbox_on_orders" id="checkbox_on_orders" value='+ data[i].id + '>' + '</td>' +
                                          '<td>' + data[i].id + '</td>' +
                                          '<td>' + data[i].extend_id + '</td>' +
                                          '<td>' + data[i].order_money + '</td>' +
                                          '<td>' + data[i].order_type + '</td>' +
                                          '<td>' + data[i].status + '</td>';
                                $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
                            }


                            //释放处理未完成订单按钮点击事件
                            $("#processOnOrder").attr("disabled",false);
                            //$("#processOnOrder").removeAttr("disabled");
                            //window.document.getElementById('processOnOrder').removeAttribute('disabled');

                        }

                        else if (data.status_code === 10100){

                            window.alert(data.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1=document.getElementById("myTableUserOnOrderDetail");

                            var table1_tbody=table1.getElementsByTagName("tbody");

                            if (table1_tbody.length >0){

                                table1.removeChild(table1_tbody[0]);

                            };

                            //模态框延迟600毫秒后，自动关闭模态框
                            setTimeout("$('#myModalUserOnOrderDetail').modal('hide')",600);

                        }
                    }
                })

            }

        }

        });

    }

    else{

        alert("当前订单数据列表为空！")
    }


}




//处理当前账户下未完成的订单--多选操作
// function processOnOrder(){
//
//     var radio_on_order = document.getElementsByName('radio_on_orders');
//
//     var isCheck = false;
//
//     var  processOnOrderDoubleClick = 0;
//
//     if (document.getElementsByName('radio_on_orders').length > 0) {
//
//         for (var i = 0; i < radio_on_order.length; i++) {
//
//             var checkeds = document.querySelectorAll("[name=radio_on_orders]")[i].checked;
//
//             if (checkeds === true){
//
//                 var order_id = $("input[name=radio_on_orders]:checked").val();
//
//                 alert("订单处理开始，请等候...");
//
//                 isCheck = true;
//
//                 //禁用处理未完成订单按钮点击事件
//                 $("#processOnOrder").attr("disabled",true);
// //                  $("#processOnOrder").attr("disabled","disabled");
// //                  window.document.getElementById('processOnOrder').setAttribute("disabled",true);
//
//
//                 //处理订单按钮连击，暂不考虑
// //                    if (processOnOrderDoubleClick == 0) {
// //
// //                        processOnOrderDoubleClick = 1;
// //
// //                        $("#processOnOrder").attr("disabled",true);
// //
// //                        setTimeout(function () {
// //
// //                            processOnOrderDoubleClick = 0;
// //
// //                          $("#processOnOrder").attr("disabled",false);
// //
// //                        }, 20000);
// //                    }
//
//
//                 //处理订单接口
//                 $.ajax({
//                 url:'/tool/sale_order/process_order/',
//                 type:'POST',
//                 data:{'order_id':order_id},
//                 success:function(data){
//
//                     if (data.status_code === 10101 || data.status_code === 10102) {
//
//                         alert(data.message);
//
//                     }
//
//                     else if (data.status_code === 10200) {
//
//                         alert(data.message);
//
//                         $.ajax({
//                             url:'/tool/sale_order/get_rest_order_on_detail/',
//                             type:'GET',
//                             success:function (data) {
//
//                                 if (data.status_code === 10200) {
//
//                                     // alert(data.message);
//
//                                     //每次初始化加载模态框时，清空模态框中的tbody元素
//                                     var table1=document.getElementById("myTableUserOnOrderDetail");
//
//                                     var table1_tbody=table1.getElementsByTagName("tbody");
//
//                                     if (table1_tbody.length >0){
//
//                                         table1.removeChild(table1_tbody[0]);
//
//                                     };
//
//                                     var data = data.result;
//
//                                     for (var i=0; i < data.length; i++){
//
//                                         var str = '<td>' +
//                                                   '<input type="radio" name="radio_on_orders" id="radio_on_orders" value='+ data[i].id + '>' + '</td>' +
//                                                   '<td>' + data[i].id + '</td>' +
//                                                   '<td>' + data[i].extend_id + '</td>' +
//                                                   '<td>' + data[i].order_money + '</td>' +
//                                                   '<td>' + data[i].order_type + '</td>' +
//                                                   '<td>' + data[i].status + '</td>';
//                                         $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
//                                     }
//
//                                     //释放处理未完成订单按钮点击事件
//                                     $("#processOnOrder").attr("disabled",false);
//                                     //$("#processOnOrder").removeAttr("disabled");
//                                     //window.document.getElementById('processOnOrder').removeAttribute('disabled');
//
//                                 }
//
//                                 else if (data.status_code === 10100){
//
//                                     window.alert(data.message);
//
//                                     //每次初始化加载模态框时，清空模态框中的tbody元素
//                                     var table1=document.getElementById("myTableUserOnOrderDetail");
//
//                                     var table1_tbody=table1.getElementsByTagName("tbody");
//
//                                     if (table1_tbody.length >0){
//
//                                         table1.removeChild(table1_tbody[0]);
//
//                                     };
//
//                                     //模态框延迟600毫秒后，自动关闭模态框
//                                     setTimeout("$('#myModalUserOnOrderDetail').modal('hide')",600);
//
//                                 }
//                             }
//                         })
//
//                     }
//
//                 }
//
//                 });
//
//             }
//         }
//
//         if (!isCheck){
//
//             alert("当前还未选择订单！！！");
//
//         }
//
//
//     }
//
//     else{
//
//         alert("当前订单数据列表为空！")
//     }
//
//
// }



