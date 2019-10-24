/**
 * Created by zhangbo on 19/9/20.
 */


//获取用户信息详情按钮连击
var userInfoDetailDoubleClick = 0;

//获取用户信息详情数据
function userInfoDetail() {

    var userMobile = $("[name='user_mobile']").val();
//        var userPasword = $("[name='password_name']").val();

    //获取用户信息详情按钮连击
    if (userInfoDetailDoubleClick == 0) {

        userInfoDetailDoubleClick = 1;

        $("#userInfoDetail").attr("disabled",true);

        setTimeout(function () {

            userInfoDetailDoubleClick = 0;

          $("#userInfoDetail").attr("disabled",false);

        }, 6000);
    }

    //获取用户信息详情接口
    $.ajax({
    url:'/tool/user_info/get_userinfo_detail/',
    type:'POST',
    data:{'userMobile':userMobile},
    success:function (data) {

        if (data.status_code === 10200) {

            console.log("data-->", data);
            console.log("data-->result.user_list-->", data.result.user_list);
            console.log("data-->result.enable_wealth_list-->", data.result.enable_wealth_list);
            console.log("data-->result.disable_wealth_list-->",data.result.disable_wealth_list);
            console.log("data-->result.userRole-->",data.result.userRole);

            alert(data.message);

            //区域元素显示出来
            document.getElementById('hide_cancle').style.display = "inline";
//                document.getElementById('hide_cancle').style.display="block";
//                document.getElementById('hide_cancle').removeAttribute('class');
//                document.getElementById('hide_cancle').style.visibility="visible";

            //释放处理订单按钮点击事件
//                $("#processOrder").attr("disabled",false);
//                $("#processOrder").removeAttr("disabled");
//                window.document.getElementById('processOrder').removeAttribute('disabled');

//                var obj = eval(data.result);
//                var tbody =$('<tbody></tbody>');
//
//                $(obj).each(function (index){
//
//                    var val=obj[index];
//                    var tr=$('<tr></tr>');
//                    tr.append('<td>' +
//                              '<input type="radio" name="radio_status" id="radio_status" value=' + val.point_id + '>' +
//                              '</td>' +
//                              '<td>' + val.point_id + '</td>' + '<td>' + val.name + '</td>' +
//                              '<td>' + val.price + '</td>' + '<td>' + val.point_type + '</td>');
//                    tbody.append(tr);
//                });

            //清空创建到元素内容
//                $(myTablePlaceOrder).empty();
//                $(myTableGetOrderDetail).empty();

            //清空tbody元素
            var table1 = document.getElementById("myTableUserInfo");
//                var table2=document.getElementById("myTableGetOrderDetail");

            var table1_tbody = table1.getElementsByTagName("tbody");
//                var table2_tbody=table2.getElementsByTagName("tbody");

            if (table1_tbody.length > 0) {

                table1.removeChild(table1_tbody[0]);

            }
            ;

//                if (table2_tbody.length >0){
//
//                    table2.removeChild(table2_tbody[0]);
//
//                };

            var user_list_data = data.result.user_list;
            var enable_wealth_list_data = data.result.enable_wealth_list;
            var disable_wealth_list_data = data.result.disable_wealth_list;
            var str1;
            var str2;
            var str3;

            for (var i = 0; i < user_list_data.length; i++) {

                str1 = '<td>' + user_list_data[i].id + '</td>' + '<td>' + user_list_data[i].real_name + '</td>' +
                       '<td>' + user_list_data[i].nick_name + '</td>' + '<td>' + user_list_data[i].mobile + '</td>' +
                       '<td>' + user_list_data[i].is_trail + '</td>' + '<td>' + user_list_data[i].is_buy + '</td>' +
                       '<td>' + user_list_data[i].now_level + '</td>' + '<td>' + user_list_data[i].current_level + '</td>' +
                       '<td>' + user_list_data[i].parent_id + '</td>' + '<td>' + user_list_data[i].city + '</td>';
//                    $("#myTableUserInfo").append('<tr>' + str1 + '</tr>');

            }


            //当前财富：成人与青少
            if (data.result.userRole === 14 || data.result.userRole === 11) {

                //当前财富
                if (enable_wealth_list_data.length > 0) {

                    for (var y = 0; y < enable_wealth_list_data.length; y++) {

                        if (enable_wealth_list_data[y].point === undefined) {

                            str2 = str1 + '<td>' + '次卡：' + 0 + '；' + '课时：' + enable_wealth_list_data[y].classtime + '</td>';

                        }

                        else if (enable_wealth_list_data[y].classtime === undefined) {

                            str2 = str1 + '<td>' + '次卡：' + enable_wealth_list_data[y].point + '；' + '课时：' + 0 + '</td>';

                        }

                        else {

                            str2 = str1 + '<td>' + '次卡：' + enable_wealth_list_data[y].point + '；' + '课时：' + enable_wealth_list_data[y].classtime + '</td>';

                        }
                    }

                }
                else {

                    str2 = str1 + '<td>' + '次卡：' + 0 + '；' + '课时：' + 0 + '</td>';

                }

                //未开启财富
                if (disable_wealth_list_data.length > 0) {

                    for (var y = 0; y < disable_wealth_list_data.length; y++) {


                        if (disable_wealth_list_data[y].point_count === null && disable_wealth_list_data[y].classtime_count === null){

                            str3 = str2 + '<td>' + '次卡：' + 0 + '；' + '课时：' + 0 + '</td>';

                        }

                        else if (disable_wealth_list_data[y].point_count === null) {

                            str3 = str2 + '<td>' + '次卡：' + 0 + '；' + '课时：' + parseInt(disable_wealth_list_data[y].classtime_count) + '</td>';

                        }

                        else if (disable_wealth_list_data[y].classtime_count === null) {

                            str3 = str2 + '<td>' + '次卡：' + parseInt(disable_wealth_list_data[y].point_count) + '；' + '课时：' + 0 + '</td>';

                        }

                        else {

                            str3 = str2 + '<td>' + '次卡：' + parseInt(disable_wealth_list_data[y].point_count) + '；' + '课时：' + parseInt(disable_wealth_list_data[y].classtime_count) + '</td>';

                        }
                    }

                }

                else {

                    str3 = str2 + '<td>' + '次卡：' + 0 + '；' + '课时：' + 0 + '</td>';

                }

            }

             //当前财富：美小
            else if (data.result.userRole === 12 ) {

                //当前财富
                if (enable_wealth_list_data.length > 0) {

                    for (var y = 0; y < enable_wealth_list_data.length; y++) {

                        if (enable_wealth_list_data[y].na_pri === undefined) {

                            str2 = str1 + '<td>' + '北美课时：' + 0 + '；' + '北美绘本课：' + enable_wealth_list_data[y].na_open + '</td>';

                        }

                        else if (enable_wealth_list_data[y].na_open === undefined) {

                            str2 = str1 + '<td>' + '北美课时：' + enable_wealth_list_data[y].na_pri + '；' + '北美绘本课：' + 0 + '</td>';

                        }

                        else {

                            str2 = str1 + '<td>' + '北美课时：' + enable_wealth_list_data[y].na_pri + '；' + '北美绘本课：' + enable_wealth_list_data[y].na_open + '</td>';

                        }
                    }

                }
                else {

                    str2 = str1 + '<td>' + '北美课时：' + 0 + '；' + '北美绘本课：' + 0 + '</td>';

                }

                //未开启财富
                if (disable_wealth_list_data.length > 0) {

                    for (var y = 0; y < disable_wealth_list_data.length; y++) {


                        if (disable_wealth_list_data[y].na_pri_count === null && disable_wealth_list_data[y].na_open_count === null){

                            str3 = str2 + '<td>' + '北美课时：' + 0 + '；' + '北美绘本课：' + 0 + '</td>';

                        }

                        else if (disable_wealth_list_data[y].na_pri_count === null) {

                            str3 = str2 + '<td>' + '北美课时：' + 0 + '；' + '北美绘本课：' + parseInt(disable_wealth_list_data[y].na_open_count) + '</td>';

                        }

                        else if (disable_wealth_list_data[y].na_open_count === null) {

                            str3 = str2 + '<td>' + '北美课时：' + parseInt(disable_wealth_list_data[y].na_pri_count) + '；' + '北美绘本课：' + 0 + '</td>';

                        }

                        else {

                            str3 = str2 + '<td>' + '北美课时：' + parseInt(disable_wealth_list_data[y].na_pri_count) + '；' + '北美绘本课：' + parseInt(disable_wealth_list_data[y].na_open_count) + '</td>';

                        }
                    }

                }

                else {

                    str3 = str2 + '<td>' + '北美课时：' + 0 + '；' + '课时：' + 0 + '</td>';

                }


            }


            $("#myTableUserInfo").append('<tr>' + str3 + '</tr>');

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

        else{

            window.alert(data.message);

            window.location.reload()

        }
//        $('#myTablePlaceOrder tbody').replaceWith(tbody);


    }

    })

};
