/**
 * Created by zhangbo on 20/7/5.
 */


//处理当前账户下为on约课记录信息--多选操作
//约课记录修改
function appointRecordEdit(){

    var checkbox_on_appoint_record = document.getElementsByName('checkbox_on_appoint_record');
    // console.log(checkbox_on_appoint_record);

    appoint_id_check_val = [];

    //修改约课记录按钮连击
    var appointRecordEditDoubleClick = 0;

    if ($("#checkbox_on_appoint_record").length > 0) {

        if ($('input:checked').length === 0){

            alert("请选择约课记录！！！");

            return;

        }

        for (var i = 0; i < checkbox_on_appoint_record.length; i++) {

            if (checkbox_on_appoint_record[i].checked) {

                //添加到数组
                appoint_id_check_val.push(checkbox_on_appoint_record[i].value);

            }
        }

        //将数组对象转化成json字符串，传到后端系统
        appoint_id_check_val = JSON.stringify(appoint_id_check_val);

        var courseStatus = $("select[id='course_status']").val();

        if (courseStatus === '0'){

            window.alert("课程状态还未选择");

            return;

        }

        //禁用修改课程状态按钮点击事件
        $("#appointRecordEdit").attr("disabled",true);
        //$("#appointRecordEdit").attr("disabled","disabled");
        //window.document.getElementById('appointRecordEdit').setAttribute("disabled",true);

        //修改课程状态按钮连击，暂不考虑
//                    if (appointRecordEditDoubleClick == 0) {
//
//                        appointRecordEditDoubleClick = 1;
//
//                        $("#processOrder").attr("disabled",true);

//                        setTimeout(function () {
//
//                            appointRecordEditDoubleClick = 0;
//
//                          $("#processOrder").attr("disabled",false);
//
//                        }, 20000);
//                    }



        //约课记录状态变更接口
        $.ajax({
        url:'/tool/appoint_manage/api/appoint_record',
        type:'POST',
        data:{'appoint_id_check_val':appoint_id_check_val,'courseStatus':courseStatus},
        success:function(data) {

            if (data.status_code === 10100 || data.status_code === 10101 || data.status_code === 10102) {

                alert(data.message);

                $.ajax({
                    url: '/tool/appoint_manage/get_user_rest_appoint_record/',
                    type: 'GET',
                    success: function (data) {

                        if (data.status_code === 10100 || data.status_code === 10101) {

                            window.alert(data.message);

                            //手机号错误时，每次初始化加载模态框时默认删除该模态框
                            $("#myModalAppointRecord").empty();

                            window.location.reload()

                        }

                        else if (data.status_code === 10200) {

                            appointRecords = data.appointRecords;

                            //获取搜索条件list数据
                            // getAppointRecordListData(userMobile);
                            console.log("appointRecords-->", appointRecords);
                            // window.alert(resp.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1 = document.getElementById("myTableOpenClassInfo");

                            var table1_tbody = table1.getElementsByTagName("tbody");

                            if (table1_tbody.length > 0) {

                                table1.removeChild(table1_tbody[0]);

                            };

                            //单选钮
                            // for (var i = 0; i < appointRecords.length; i++) {
                            //
                            //     var str = '<td>' +
                            //         '<input type="radio" name="radio_on_appoint_record" id="radio_on_appoint_record" value=' + appointRecords[i].id + ' >' + '</td>' +
                            //         '<td>' + appointRecords[i].id + '</td>' +
                            //         '<td>' + appointRecords[i].t_id + '</td>' +
                            //         '<td>' + appointRecords[i].s_id + '</td>' +
                            //         '<td>' + appointRecords[i].course_id + '</td>' +
                            //         '<td>' + appointRecords[i].point_type + '</td>' +
                            //         '<td>' + appointRecords[i].status + '</td>' +
                            //         '<td>' + appointRecords[i].start_time + '</td>' +
                            //         '<td>' + appointRecords[i].end_time + '</td>';
                            //     $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
                            // }

                            //复选框
                            for (var i = 0; i < appointRecords.length; i++) {

                                var str = '<td>' +
                                    '<input type="checkbox" name="checkbox_on_appoint_record" id="checkbox_on_appoint_record" value=' + appointRecords[i].id + ' >' + '</td>' +
                                    '<td>' + appointRecords[i].id + '</td>' +
                                    '<td>' + appointRecords[i].t_id + '</td>' +
                                    '<td>' + appointRecords[i].s_id + '</td>' +
                                    '<td>' + appointRecords[i].course_id + '</td>' +
                                    '<td>' + appointRecords[i].point_type + '</td>' +
                                    '<td>' + appointRecords[i].status + '</td>' +
                                    '<td>' + appointRecords[i].start_time + '</td>' +
                                    '<td>' + appointRecords[i].end_time + '</td>';
                                $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
                            }

                            var cmbCourseStatus = document.getElementById("course_status");

                            cmbCourseStatus.selectedIndex = 0;

                            //禁用修改课程状态按钮点击事件
                            $("#appointRecordEdit").attr("disabled",false);
                            //$("#appointRecordEdit").removeAttr("disabled");
                            //window.document.getElementById('appointRecordEdit').removeAttribute('disabled');

                        }

                        //
                        //    //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
                        //    $("#myModalUserSmsContent").empty();
                        //
                        //    $('#myModalUserSmsContent').modal('hide');
                        //
                        //},5000);

                        //模态框延迟500毫秒后，自动关闭模态框
                        // setTimeout("$('#myModalUserSmsContent').modal('hide')",1000);

                        // }

                    }

                });



            }

            else if (data.status_code === 10200) {

                alert(data.message);

                $.ajax({
                    url: '/tool/appoint_manage/get_user_rest_appoint_record/',
                    type: 'GET',
                    success: function (data) {

                        if (data.status_code === 10100 || data.status_code === 10101) {

                            window.alert(data.message);

                            //手机号错误时，每次初始化加载模态框时默认删除该模态框
                            $("#myModalAppointRecord").empty();

                            window.location.reload()

                        }

                        else if (data.status_code === 10200) {

                            appointRecords = data.appointRecords;

                            //获取搜索条件list数据
                            // getAppointRecordListData(userMobile);
                            console.log("appointRecords-->", appointRecords);
                            // window.alert(resp.message);

                            //每次初始化加载模态框时，清空模态框中的tbody元素
                            var table1 = document.getElementById("myTableOpenClassInfo");

                            var table1_tbody = table1.getElementsByTagName("tbody");

                            if (table1_tbody.length > 0) {

                                table1.removeChild(table1_tbody[0]);

                            };

                            //单选钮
                            // for (var i = 0; i < appointRecords.length; i++) {
                            //
                            //     var str = '<td>' +
                            //         '<input type="radio" name="radio_on_appoint_record" id="radio_on_appoint_record" value=' + appointRecords[i].id + ' >' + '</td>' +
                            //         '<td>' + appointRecords[i].id + '</td>' +
                            //         '<td>' + appointRecords[i].t_id + '</td>' +
                            //         '<td>' + appointRecords[i].s_id + '</td>' +
                            //         '<td>' + appointRecords[i].course_id + '</td>' +
                            //         '<td>' + appointRecords[i].point_type + '</td>' +
                            //         '<td>' + appointRecords[i].status + '</td>' +
                            //         '<td>' + appointRecords[i].start_time + '</td>' +
                            //         '<td>' + appointRecords[i].end_time + '</td>';
                            //     $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
                            // }

                            //复选框
                            for (var i = 0; i < appointRecords.length; i++) {

                                var str = '<td>' +
                                    '<input type="checkbox" name="checkbox_on_appoint_record" id="checkbox_on_appoint_record" value=' + appointRecords[i].id + ' >' + '</td>' +
                                    '<td>' + appointRecords[i].id + '</td>' +
                                    '<td>' + appointRecords[i].t_id + '</td>' +
                                    '<td>' + appointRecords[i].s_id + '</td>' +
                                    '<td>' + appointRecords[i].course_id + '</td>' +
                                    '<td>' + appointRecords[i].point_type + '</td>' +
                                    '<td>' + appointRecords[i].status + '</td>' +
                                    '<td>' + appointRecords[i].start_time + '</td>' +
                                    '<td>' + appointRecords[i].end_time + '</td>';
                                $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
                            }

                            var cmbCourseStatus = document.getElementById("course_status");

                            cmbCourseStatus.selectedIndex = 0;

                            //禁用修改课程状态按钮点击事件
                            $("#appointRecordEdit").attr("disabled",false);
                            //$("#appointRecordEdit").removeAttr("disabled");
                            //window.document.getElementById('appointRecordEdit').removeAttribute('disabled');

                        }

                        //
                        //    //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
                        //    $("#myModalUserSmsContent").empty();
                        //
                        //    $('#myModalUserSmsContent').modal('hide');
                        //
                        //},5000);

                        //模态框延迟500毫秒后，自动关闭模态框
                        // setTimeout("$('#myModalUserSmsContent').modal('hide')",1000);

                        // }

                    }

                });

            }
        }

        });

    }

    else{

        alert("当前约课数据列表为空！")
    }


}





//处理当前账户下为on约课记录信息--单选操作
//约课记录修改
// function appointRecordEdit(){
//
//     var radio_appoint_record = document.getElementsByName('radio_on_appoint_record');
//
//     // console.log(radio_appoint_record);
//
//     var isCheck = false;
//
//     //修改约课记录按钮连击
//     var appointRecordEditDoubleClick = 0;
//
//     if ($("#radio_on_appoint_record").length > 0) {
//
//         for (var i = 0; i < radio_appoint_record.length; i++) {
//
// //                if (radio_appoint_record[i].checked){
// //
// //                    userid = radio_appoint_record[i].value;
// //
// //                    isCheck = true;
// //
// //                }
//             var checkeds = document.querySelectorAll("[name=radio_on_appoint_record]")[i].checked;
//
//             var courseStatus = $("select[id='course_status']").val();
//
//             if (courseStatus === '0'){
//
//                 window.alert("课程状态还未选择");
//                 return;
//
//             }
//
//             if (checkeds === true){
//
//                 var appointRecordID = $("input[name=radio_on_appoint_record]:checked").val();
//
//
//                 // console.log(appointRecordID);
//
//                 isCheck = true;
//
//                 //禁用修改按钮点击事件
//                 // $("#appointRecordEdit").attr("disabled",true);
//                 //$("#appointRecordEdit").attr("disabled","disabled");
//                 //window.document.getElementById('appointRecordEdit').setAttribute("disabled",true);
//
//
//                 //处理订单按钮连击，暂不考虑
// //                    if (appointRecordEditDoubleClick == 0) {
// //
// //                        appointRecordEditDoubleClick = 1;
// //
// //                        $("#processOrder").attr("disabled",true);
//
// //                        setTimeout(function () {
// //
// //                            appointRecordEditDoubleClick = 0;
// //
// //                          $("#processOrder").attr("disabled",false);
// //
// //                        }, 20000);
// //                    }
//
//
//
//                 //约课记录状态变更接口
//                 $.ajax({
//                 url:'/tool/appoint_manage/api/appoint_record',
//                 type:'POST',
//                 data:{'appointRecordID':appointRecordID,'courseStatus':courseStatus},
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
//                             url:'/tool/appoint_manage/get_user_rest_appoint_record/',
//                             type:'GET',
//                             success:function (data)
//                             {
//
//                                 if (data.status_code === 10100 || data.status_code === 10101 ||
//                                     data.status_code === 10102 || data.status_code === 10103)
//                                 {
//
//                                     window.alert(data.message);
//
//                                     //手机号错误时，每次初始化加载模态框时默认删除该模态框
//                                     $("#myModalAppointRecord").empty();
//
//                                     window.location.reload()
//
//                                 }
//
//                                 else if (data.status_code === 10200){
//
//                                     appointRecords = data.appointRecords;
//
//                                     //获取搜索条件list数据
//                                     // getAppointRecordListData(userMobile);
//                                     console.log("appointRecords-->",appointRecords);
//                                     // window.alert(resp.message);
//
//                                     //每次初始化加载模态框时，清空模态框中的tbody元素
//                                     var table1=document.getElementById("myTableOpenClassInfo");
//
//                                     var table1_tbody=table1.getElementsByTagName("tbody");
//
//                                     if (table1_tbody.length >0){
//
//                                         table1.removeChild(table1_tbody[0]);
//
//                                     };
//
//                                     for (var i=0; i < appointRecords.length; i++){
//
//                                         var str = '<td>' +
//                                                   '<input type="radio" name="radio_on_appoint_record" id="radio_on_appoint_record" value='+ appointRecords[i].id +' >' + '</td>' +
//                                                   '<td>' + appointRecords[i].id + '</td>' +
//                                                   '<td>' + appointRecords[i].t_id + '</td>' +
//                                                   '<td>' + appointRecords[i].s_id + '</td>' +
//                                                   '<td>' + appointRecords[i].course_id + '</td>' +
//                                                   '<td>' + appointRecords[i].point_type + '</td>' +
//                                                   '<td>' + appointRecords[i].status + '</td>' +
//                                                   '<td>' + appointRecords[i].start_time + '</td>' +
//                                                   '<td>' + appointRecords[i].end_time + '</td>';
//                                         $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
//                                     }
//
//                                     var cmbCourseStatus = document.getElementById("course_status");
//
//                                     cmbCourseStatus.selectedIndex = 0;
//
//                                 }
//
//                                     //
//                                     //    //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
//                                     //    $("#myModalUserSmsContent").empty();
//                                     //
//                                     //    $('#myModalUserSmsContent').modal('hide');
//                                     //
//                                     //},5000);
//
//                                     //模态框延迟500毫秒后，自动关闭模态框
//                                     // setTimeout("$('#myModalUserSmsContent').modal('hide')",1000);
//
//                                 // }
//
//                             }
//
//                         });
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
//             alert("请选择约课记录！！！");
//
//         }
//
//
//     }
//
//     else{
//
//         alert("当前约课数据列表为空！")
//     }
//
// }
