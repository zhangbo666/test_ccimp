
/**
 * Created by zhangbo on 20/07/05.
 */


var userappointRecordDoubleClike = 0;

function userAppointRecord(){

    //获取手机号
    var userMobile = $("[name='user_mobile']").val();

    //开启按钮连击模态框不能显示出来
    //获取约课记录连击
    // if (userappointRecordDoubleClike === 0) {
    //
    //    userappointRecordDoubleClike = 1;
    //
    //    $('#appointRecord').attr("disabled", true);
    //
    //    setTimeout(function () {
    //
    //        userappointRecordDoubleClike = 0;
    //
    //        $('#appointRecord').attr("disabled", false);
    //
    //    }, 2000)
    // }

    $.ajax({
        url:'/tool/appoint_manage/get_user_appoint_record/',
        type:'GET',
        data:{'userMobile':userMobile},
        success:function (data)
        {

            if (data.status_code === 10101 || data.status_code === 10102 ||
                data.status_code === 10103 || data.status_code === 10104 ||
                data.status_code === 10105 || data.status_code === 10106 ||
                data.status_code === 10107)
            {

                window.alert(data.message);

                //手机号错误时，每次初始化加载模态框时默认删除该模态框
                $("#myModalAppointRecord").empty();

                window.location.reload()

            }

            else if (data.status_code === 10200){

                appointRecords = data.appointRecords;

                //获取搜索条件list数据
                // getAppointRecordListData(userMobile);
                console.log("appointRecords-->",appointRecords);
                // window.alert(resp.message);

                //每次初始化加载模态框时，清空模态框中的tbody元素
                var table1=document.getElementById("myTableOpenClassInfo");

                var table1_tbody=table1.getElementsByTagName("tbody");

                if (table1_tbody.length >0){

                    table1.removeChild(table1_tbody[0]);

                };

                for (var i=0; i < appointRecords.length; i++){

                    var str = '<td>' +
                              '<input type="checkbox" name="checkbox_on_appoint_record" id="checkbox_on_appoint_record" value='+ appointRecords[i].id +' >' + '</td>' +
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

    //调取select数据列表
    // function getAppointRecordListData(userMobile){
    //
    //     $.get('/tool/user_info/api/getAppointRecordListData',{'userMobile':userMobile},function(resp){
    //
    //         appointRecords = resp.appointRecords;
    //
    //         if (resp.status_code === 10200){
    //
    //             console.log("appointRecords-->",appointRecords);
    //             // window.alert(resp.message);
    //
    //             //每次初始化加载模态框时，清空模态框中的tbody元素
    //             var table1=document.getElementById("myTableOpenClassInfo");
    //
    //             var table1_tbody=table1.getElementsByTagName("tbody");
    //
    //             if (table1_tbody.length >0){
    //
    //                 table1.removeChild(table1_tbody[0]);
    //
    //             };
    //
    //             for (var i=0; i < appointRecords.length; i++){
    //
    //                 var str = '<td>' +
    //                           '<input type="radio" name="radio_on_appoint_record" id="radio_on_appoint_record" value='+ appointRecords[i].id +' >' + '</td>' +
    //                           '<td>' + appointRecords[i].id + '</td>' +
    //                           '<td>' + appointRecords[i].t_id + '</td>' +
    //                           '<td>' + appointRecords[i].s_id + '</td>' +
    //                           '<td>' + appointRecords[i].course_id + '</td>' +
    //                           '<td>' + appointRecords[i].point_type + '</td>' +
    //                           '<td>' + appointRecords[i].status + '</td>' +
    //                           '<td>' + appointRecords[i].start_time + '</td>' +
    //                           '<td>' + appointRecords[i].end_time + '</td>';
    //                 $("#myTableOpenClassInfo").append('<tr>' + str + '</tr>');
    //             }
    //
    //             var cmbCourseStatus = document.getElementById("course_status");
    //
    //             cmbCourseStatus.selectedIndex = 0;
    //
    //             //释放处理未完成订单按钮点击事件
    //             // $("#processOnOrder").attr("disabled",false);
    //             //$("#processOnOrder").removeAttr("disabled");
    //             //window.document.getElementById('processOnOrder').removeAttribute('disabled');
    //
    //         }
    //
    //         else{
    //
    //             window.alert(resp.message);
    //
    //             //每次初始化加载模态框时，清空模态框中的tbody元素
    //             var table2=document.getElementById("myTableOpenClassInfo");
    //
    //             var table2_tbody=table2.getElementsByTagName("tbody");
    //
    //             if (table2_tbody.length >0){
    //
    //                 table2.removeChild(table2_tbody[0]);
    //
    //             };
    //
    //             //模态框延迟600毫秒后，自动关闭模态框
    //             setTimeout("$('#myModalAppointRecord').modal('hide')",50);
    //             }
    //
    //     });
    // }
}