/**
 * Created by zhangbo on 2020/5/19.
 */


//获取账号状态按钮连击
var accountStatusDoubleClick = 0;

//获取用户昵称方法
function accountStatus() {

    var userMobile = $("[name='user_mobile']").val();
    var accountStatus = $("select[id='account_status']").val();

    //获取用户昵称按钮连击锁定超时时间
    if (accountStatusDoubleClick === 0) {

        accountStatusDoubleClick = 1;

        $("#accountStatus").attr("disabled",true);

        setTimeout(function () {

            accountStatusDoubleClick = 0;

            $("#accountStatus").attr("disabled",false);

        }, 3000);
    }

    if (accountStatus === '0'){

        alert("账号状态还未选择");

        return;

    }

    //获取账号状态接口
    $.ajax({
    url:'/tool/user_info/account_status/',
    type:'GET',
    data:{'userMobile':userMobile,'accountStatus':accountStatus},
    success:function (data) {

        if (data.status_code === 10200) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.message);

        }

        else{

            window.alert(data.message);

            // window.location.reload()

        }

    }

    })

};
