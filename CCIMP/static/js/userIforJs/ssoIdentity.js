/**
 * Created by zhangbo on 2020/7/25.
 */


//获取sso身份按钮连击
var ssoIdentityDoubleClick = 0;

//获取sso身份方法
function ssoIdentity() {

    var userMobile = $("[name='user_mobile']").val();
    var ssoIdentity = $("[name='sso_identity']").val();

    //获取sso身份按钮连击锁定超时时间
    if (ssoIdentityDoubleClick === 0) {

        ssoIdentityDoubleClick = 1;

        $("#ssoIdentity").attr("disabled",true);

        setTimeout(function () {

            ssoIdentityDoubleClick = 0;

            $("#ssoIdentity").attr("disabled",false);

        }, 3000);
    }

    if (ssoIdentity === '0'){

        alert("sso身份还未选择");

        return;

    }

    //修改sso身份接口
    $.ajax({
    url:'/tool/user_info/sso_identity/',
    type:'POST',
    data:{'userMobile':userMobile,'ssoIdentity':ssoIdentity},
    success:function (data) {

        if (data.status_code === 10200) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.result);

        }

        else if (data.status_code === 10104) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.result);
        }

        else if (data.status_code === 10105){

            window.alert(data.message);

            window.location.reload()

        }

        else if (data.status_code === 10106 || data.status_code === 10107){

            window.alert(data.message);

        }

    }

    })

};
