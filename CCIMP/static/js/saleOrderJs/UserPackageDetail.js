/**
 * Created by zhangbo on 19/9/7.
 */


//获取套餐详情数据
function userPackageDetail() {

    //获取用户套餐详情按钮连击
    var userPackageDetailDoubleClick = 0;

    var userMobile = $("[name='mobile_name']").val();
    var userPasword = $("[name='password_name']").val();

    //获取用户套餐详情按钮连击
    if (userPackageDetailDoubleClick == 0) {

        userPackageDetailDoubleClick = 1;

        //用户套餐详情与用户未完成订单按钮置灰色状态不能点击
        $("#userPackageDetail").attr("disabled", true);
        $("#userOnOrderDetail").attr("disabled", true);

        setTimeout(function () {

            userPackageDetailDoubleClick = 0;

            //用户套餐详情与用户未完成订单按钮状态恢复为点击
            $("#userPackageDetail").attr("disabled", false);
            $("#userOnOrderDetail").attr("disabled", false);

        }, 10000);
    }

    //获取套餐详情接口
    $.ajax({
        url: '/tool/sale_order/get_package_detail/',
        type: 'POST',
        data: {'userMobile': userMobile, 'userPasword': userPasword},
        success: function (data) {

            if (data.status_code === 10200) {

                console.log("data-->", data);
                console.log("data.result-->", data.result);
                console.log("data.user_role-->",data.user_role);

                alert(data.message);

                //区域元素显示出来
                document.getElementById('hide_cancle').style.display = "inline";
//                document.getElementById('hide_cancle').style.display="block";
//                document.getElementById('hide_cancle').removeAttribute('class');
//                document.getElementById('hide_cancle').style.visibility="visible";

                //释放处理订单按钮点击事件
                $("#processOrder").attr("disabled", false);
//                $("#processOrder").removeAttr("disabled");
//                window.document.getElementById('processOrder').removeAttribute('disabled');

                //清空该元素下面的所有元素内容
//                $(myTablePlaceOrder).empty();
//                $(myTableGetOrderDetail).empty();

                //清空tbody元素
                var table1 = document.getElementById("myTablePlaceOrder");
                var table2 = document.getElementById("myTableGetOrderDetail");

                var table1_tbody = table1.getElementsByTagName("tbody");
                var table2_tbody = table2.getElementsByTagName("tbody");

                if (table1_tbody.length > 0) {

                    table1.removeChild(table1_tbody[0]);

                }
                ;

                if (table2_tbody.length > 0) {

                    table2.removeChild(table2_tbody[0]);

                }
                ;


                var data = data.result;

                for (var i = 0; i < data.length; i++) {

                    if (data[i].point_type === 'mix_point'){

                        var str = '<td>' +
                        '<input type="radio" name="radio_status" id="radio_status" value=' + data[i].point_id + '>' +
                        '</td>' +
                        '<td>' + data[i].point_id + '</td>' + '<td>' + data[i].name + '</td>' +
                        '<td>' + "" + '</td>' + '<td>' + "" + '</td>' +
                        '<td>' + data[i].price + '</td>' + '<td>' + "" + '</td>' +
                        '<td>' + "" + '</td>' + '<td>' + data[i].point_type + '</td>';

                    }

                    else {

                        var str = '<td>' +
                            '<input type="radio" name="radio_status" id="radio_status" value=' + data[i].point_id + '>' +
                            '</td>' +
                            '<td>' + data[i].point_id + '</td>' + '<td>' + data[i].name + '</td>' +
                            '<td>' + data[i].point_value + '</td>' + '<td>' + data[i].class_time_value + '</td>' +
                            '<td>' + data[i].price + '</td>' + '<td>' + data[i].point_gift_package + '</td>' +
                            '<td>' + data[i].point_press_book + '</td>' + '<td>' + data[i].point_type + '</td>';
                    }

                    $("#myTablePlaceOrder").append('<tr>' + str + '</tr>');
                }




                //释放获取用户套餐详情按钮点击事件
//                $("#userPackageDetail").attr("disabled",false);

//                for (var i in data){
//
//                    var str = '<td>' +
//                              '<input type="radio" name="radio_status" id="radio_status" value=' + data[i].point_id + '>' +
//                              '</td>' +
//                              '<td>' + data[i].point_id + '</td>' + '<td>' + data[i].name + '</td>' +
//                              '<td>' + data[i].price + '</td>' + '<td>' + data[i].point_type + '</td>';
//                    $("#myTablePlaceOrder").append('<tr>' + str + '</tr>');
//                }

//                $.each(data,function(index,item){
//
//                    var str = '<td>' +
//                              '<input type="radio" name="radio_status" id="radio_status" value=' + item.point_id + '>' +
//                              '</td>' +
//                              '<td>' + item.point_id + '</td>' + '<td>' + item.name + '</td>' +
//                              '<td>' + item.price + '</td>' + '<td>' + item.point_type + '</td>';
//                    $("#myTablePlaceOrder").append('<tr>' + str + '</tr>');
//                });

            }

            else {

                window.alert(data.message);

                window.location.reload()

            }
//        $('#myTablePlaceOrder tbody').replaceWith(tbody);


        }

    });

};