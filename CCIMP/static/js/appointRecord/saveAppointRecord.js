/**
 * Created by zhangbo on 2021/3/26.
 */


/*保存1V1青少约课*/
function saveAppointRecord(){

    var uidName = document.querySelector("[name=uid_name]").value;
    var tidName = document.querySelector("[name=tid_name]").value;
    var assertSum = document.querySelector("[name=assert_sum]").value;
    var startDate = document.querySelector("[name=start_date]").value;
    var startTime = document.querySelector("[name=start_time]").value;
    var endDate = document.querySelector("[name=end_date]").value;
    var endTime = document.querySelector("[name=end_time]").value;

    var juniorBookText1Name = document.querySelector("[name=j_cate_id1_name]").value;
    var juniorBookText2Name = document.querySelector("[name=j_cate_id2_name]").value;
    var juniorBookText3Name = document.querySelector("[name=j_cate_id3_name]").value;

//        alert(uidName);
//        alert(tidName);
//        alert(assertSum);
//        alert(startDate);
//        alert(startTime);
//        alert(endDate);
//        alert(endTime);
//        alert(juniorBookText1Name);
//        alert(juniorBookText2Name);
//        alert(juniorBookText3Name);

    if(uidName === ''){

        alert("学员id为空!");
        return;
    }

    if(tidName === '0'){

        alert("1v1老师未选择!");
        return;

    }

    if(startDate === ""){

        alert("约课开始日期为空!");
        return;
    }
    else if(endDate === ""){

        alert("约课结束日期为空!");
        return;
    }

    if(startTime === "0"){

        alert("约课开始时间未选!");
        return;
    }
    else if(endTime === "0"){

        alert("约课结束时间未选!");
        return;
    }

    var startDate_replace = startDate.replace(/\-/g,'/');
    var endDate_replace = endDate.replace(/\-/g,'/');

    var startDate_unix = Date.parse(startDate_replace);
    var endDate_unix = Date.parse(endDate_replace);

    if(startDate_unix > endDate_unix || startDate_unix < endDate_unix){

        alert("青少约课开始日期和结束日期不一致!");
        return;

    }

    var newData = new Date(),newDate_str = "";
    // alert(newData.getFullYear());
    // alert(newData.getMonth());
    // alert(newData.getDate());
    // alert(newData.getHours());
    // alert(newData.getMinutes());

    newDate_str += newData.getFullYear() + '-';
    newDate_str += newData.getMonth() + 1 + '-';
    newDate_str += newData.getDate() + " ";
    newDate_str += newData.getHours() + ':';
    newDate_str += newData.getMinutes();
    // alert(newDate_str);
    var newDate_str_replace = newDate_str.replace(/\-/g,'/');
    var newDate_str_unix = Date.parse(newDate_str_replace);


    startAppointTime = startDate + " " + startTime;
    endAppointTime   = endDate   + " " + endTime;
    // alert(startAppointTime);
    // alert(endAppointTime);

    var startTime_replace = startAppointTime.replace(/\-/g,'/');
    var endTime_replace = endAppointTime.replace(/\-/g,'/');

    var startTime_unix = Date.parse(startTime_replace);
    var endTime_unix = Date.parse(endTime_replace);
    // alert(endTime_unix-startTime_unix);
    // alert(startTime_replace);
    // alert(endTime_replace);
    // alert(startTime_unix);
    // alert(endTime_unix);

    //判断用户预约大于当前时间30分钟后课程--给客户端造数据方便
    // if ((newDate_str_unix + 1800000 >= startTime_unix)){
    //
    //     alert("青少约课时间：必须大于当前时间30分钟以上才能约付费课！");
    //     return;
    // }

    if (newDate_str_unix >= startTime_unix){

        alert("青少约课时间：约课开始时间必须大于当前时间点！");
        return;

    }

    if((endTime_unix-startTime_unix) === 0){

        alert("青少约课时间：青少开始时间不能和结束时间一样！");
        return;

    }
    else if((endTime_unix-startTime_unix) > 1800000){

        alert("青少约课时间：青少约课时间不正确，只能约30分钟的课程！");
        return;

    }
    else if((endTime_unix-startTime_unix) < 0){

        alert("青少约课时间：青少约课时间不正确，请重新选择！");
        return;

    }


    if(juniorBookText1Name === "0"){

        alert("青少1v1一级教材未选择!");
        return;
    }
    else if(juniorBookText2Name === "0"){

        alert("青少1v1二级教材未选择!");
        return;
    }
    else if(juniorBookText3Name === "0"){

        alert("青少1v1三级教材未选择!");
        return;
    }


    msg_confirm = confirm("确定为该学员约课吗？");

    if(msg_confirm === true) {

        //1v1约课接口
        $.ajax({
            url: '/tool/appoint_manage/junior_appoint_add/',
            type: 'POST',
            data: {
                'uidName': uidName,
                'tidName': tidName,
                'assertSum': assertSum,
                'startDate': startDate,
                'startTime': startTime,
                'endDate': endDate,
                'endTime': endTime,
                'startAppointTime':startAppointTime,
                'endAppointTime':endAppointTime,
                'juniorBookText1Name': juniorBookText1Name,
                'juniorBookText2Name': juniorBookText2Name,
                'juniorBookText3Name': juniorBookText3Name
            },
            success: function (data) {

                if (data.status === 200) {

                    alert(data.message);
                    // window.location.replace("/tool/appoint_manage/");

                }

                else if (data.status === 10001 || data.status === 10002 || data.status === 10003 ||
                         data.status === 10004 || data.status === 10005 || data.status === 10006 ||
                         data.status === 10007 || data.status === 10008 || data.status === 10009 ||
                         data.status === 10010) {

                    alert(data.message);
                    console.log(data.message);

                }

            }
        });
    }
}
