/**
 * Created by zhangbo on 2020/5/21.
 */


//获取用户身份按钮连击
var userIdentityDoubleClick = 0;

//获取用户身份方法
function userIdentity() {

    var userMobile = $("[name='user_mobile']").val();
    var isBuy = $("[name='is_buy']").val();

    //获取用户身份按钮连击锁定超时时间
    if (userIdentityDoubleClick === 0) {

        userIdentityDoubleClick = 1;

        $("#userIdentity").attr("disabled",true);

        setTimeout(function () {

            userIdentityDoubleClick = 0;

            $("#userIdentity").attr("disabled",false);

        }, 3000);
    }

    if (isBuy === '0'){

        alert("用户身份还未选择");

        return;

    }

    //获取用户身份验证接口
    $.ajax({
    url:'/tool/user_info/user_identity/',
    type:'POST',
    data:{'userMobile':userMobile,'isBuy':isBuy},
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
