/**
 * Created by zhangbo on 2020/5/20.
 */


//获取手机号验证按钮连击
var mobileStatusDoubleClick = 0;

//获取手机号验证方法
function mobileStatus() {

    var userMobile = $("[name='user_mobile']").val();
    var isCheck = $("[name='is_check']").val();

    //获取手机号验证按钮连击锁定超时时间
    if (mobileStatusDoubleClick === 0) {

        mobileStatusDoubleClick = 1;

        $("#mobileStatus").attr("disabled",true);

        setTimeout(function () {

            mobileStatusDoubleClick = 0;

            $("#mobileStatus").attr("disabled",false);

        }, 3000);
    }

    if (isCheck === '0'){

        alert("手机号状态还未选择");

        return;

    }

    //获取手机号验证接口
    $.ajax({
    url:'/tool/user_info/mobile_status/',
    type:'POST',
    data:{'userMobile':userMobile,'isCheck':isCheck},
    success:function (data) {

        if (data.status_code === 10200) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.message);

        }

        else{

            window.alert(data.message);

            window.location.reload()

        }

    }

    })

};
