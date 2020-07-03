/**
 * Created by zhangbo on 19/9/7.
 */


//下单
function saleOrder(){

    var userMobile = $("[name='mobile_name']").val();
    var userPasword = $("[name='password_name']").val();

    //选用这种方式获取单选钮集合，var radio_statu = document.all('radio_status');
    //单选钮为1个时，radio_statu.length，获取不到值

    //只能选用这种方法获取：document.getElementsByName('radio_status')

    //下单按钮连击
    var saleOrderDoubleClick = 0;

    var radio_statu = document.getElementsByName('radio_status');

    var isCheck = false;

    if ($("#radio_status").length > 0) {

        for (var i = 0; i < radio_statu.length; i++) {

                //if (radio_statu[i].checked){

                    //userid = radio_statu[i].value;

                    //isCheck = true;

                //}

            var checkeds = document.querySelectorAll("[name=radio_status]")[i].checked;

            if (checkeds === true){

                var point_id = $("input[name=radio_status]:checked").val();

//                    alert("获取到单选钮的value值为：" + point_id);

                isCheck = true;

                //下单按钮连击
                if (saleOrderDoubleClick === 0) {

                    saleOrderDoubleClick = 1;

                    //下单按钮置灰色状态不能点击
                    $("#saleOrder").attr("disabled",true);

                    setTimeout(function () {

                        saleOrderDoubleClick = 0;

                      $("#saleOrder").attr("disabled",false);

                    }, 20000);
                }


                //下单接口
                $.ajax({
                url:'/tool/sale_order/order_pay_success/',
                type:'POST',
                data:{'userMobile':userMobile,'userPasword':userPasword,'point_id':point_id},
                success:function(data){

                    if (
                            data.status_code === 10101 ||
                            data.status_code === 10102 ||
                            data.status_code === 10103 ||
                            data.status_code === 10104 ||
                            data.status_code === 10105
                        ) {

                        alert(data.message);

                    }

                    else if (data.status_code === 10200) {

                        alert(data.message + "，生成的订单号为：" + data.result);

                        //释放按钮点击事件
                        //$("#processOrder").attr("disabled",false);
//                            $("#processOrder").removeAttr("disabled");
                        window.document.getElementById("processOrder").removeAttribute("disabled");

                        //读取订单数据
                        $.ajax({
                        url:'/tool/sale_order/get_order_detail/',
                        type:'POST',
                        data:{'order_id':data.result},
                        success:function(data){

                            console.log("data-->",data);
                            console.log("data-->",data.result);

                            if (data.status_code === 10101) {

                                alert(data.message);

                            }

                            else if (data.status_code === 10200) {

                                //alert(data.message);

                                var table2=document.getElementById("myTableGetOrderDetail");

                                var table2_tbody=table2.getElementsByTagName("tbody");

                                if (table2_tbody.length >0){

                                    table2.removeChild(table2_tbody[0]);

                                };

                                var data = data.result;

                                for (var i=0; i<data.length; i++){

                                    var str ='<td>' +
                                             '<input type="radio" name="radio_orders" id="radio_orders" value=' + data[i].id + '>' +
                                             '</td>' +
                                             '<td>' + data[i].id + '</td>' +
                                             '<td>' + data[i].extend_id + '</td>' +
                                             '<td>' + data[i].order_money + '</td>' +
                                             '<td>' + data[i].pay_method + '</td>' +
                                             '<td>' + data[i].order_type + '</td>';

                                    console.log(data[i].id,data[i].extend_id,data[i].order_money,data[i].pay_method,data[i].order_type);

                                    $("#myTableGetOrderDetail").append('<tr>' + str + '</tr>');
                                }


//                                    var obj = eval(date.result);
//                                    var tbody =$('<tbody></tbody>');
//
//                                    $(obj).each(function (index){
//
//                                        var val=obj[index];
//                                        var tr=$('<tr></tr>');
//                                        tr.append('<td>' + val.id + '</td>' + '<td>' + val.order_money + '</td>' +
//                                                  '<td>' + val.pay_method + '</td>' + '<td>' + val.order_type + '</td>');
//                                        tbody.append(tr);
//                                    });

                            }
//                            $('#myTableGetOrderDetail tbody').replaceWith(tbody);

                        }

                        });

                    }

                }

                });

            }
        }

        if (!isCheck){

            alert("还未选择套餐！");

        }

//            else {
//
//                alert("获取到单选钮到value值为：" + checked_value);
//            }

    }

    else{

        alert("当前没有套餐数据，不能下单！")
    }

}
