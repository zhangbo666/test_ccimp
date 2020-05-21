/**
 * Created by zhangbo on 19/11/22.
 */


var userSmsContentDoubleClike = 0;

function userSmsConnent(){

    var userMobile = $("[name='user_mobile']").val();

    //获取短信内容连击
    //if (userSmsContentDoubleClike === 0) {
    //
    //    userSmsContentDoubleClike = 1;
    //
    //    $('#userSmsConnent').attr("disabled", true);
    //
    //    setTimeout(function () {
    //
    //        userSmsContentDoubleClike = 0;
    //
    //        $('#userSmsConnent').attr("disabled", false);
    //
    //    }, 2000)
    //}

    $.ajax({
    url:'/tool/user_info/get_user_sms_connent/',
    type:'POST',
    data:{'userMobile':userMobile},
    success:function (data){

        if (data.status_code === 10100 || data.status_code === 10101){

            window.alert(data.message);

            //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
            $("#myModalUserSmsContent").empty();

            window.location.reload()

        }

        else if (data.status_code === 10200){

            console.log("data-->", data);
            console.log("data-->result_sms_code-->", data.result_sms_code);
            console.log("data-->result_sms_content-->", data.result_sms_content);


            $("[name='sms_code']").val(data.result_sms_code);
            $("[name='sms_content']").val(data.result_sms_content);


            setTimeout(function(){

                alert(data.message);

            },250);

            //模态框延迟2000毫秒后，自动关闭模态框
            setTimeout("$('#myModalUserSmsContent').modal('hide')",1500);

        }

        else if (data.status_code === 10300){

            $('#myModalUserSmsContent').modal('show');

            $("[name='sms_code']").val("");
            $("[name='sms_content']").val("");

            setTimeout(function(){

                alert(data.message);

            },250);

            //setTimeout(function(){
            //
            //    //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
            //    $("#myModalUserSmsContent").empty();
            //
            //    $('#myModalUserSmsContent').modal('hide');
            //
            //},5000);

            //模态框延迟500毫秒后，自动关闭模态框
            setTimeout("$('#myModalUserSmsContent').modal('hide')",2000);

        }
    }

    })

};