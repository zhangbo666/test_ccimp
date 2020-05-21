/**
 * Created by zhangbo on 20/05/11.
 */


//获取用户昵称按钮连击
var userNickNameDoubleClick = 0;

//获取用户昵称方法
function userNickName() {

    var userMobile = $("[name='user_mobile']").val();
    var nickName = $("[name='nick_name']").val();

    //获取用户昵称按钮连击锁定超时时间
    if (userNickNameDoubleClick === 0) {

        userNickNameDoubleClick = 1;

        $("#userNickName").attr("disabled",true);

        setTimeout(function () {

            userNickNameDoubleClick = 0;

            $("#userNickName").attr("disabled",false);

        }, 3000);
    }

    //获取用户昵称接口
    $.ajax({
    url:'/tool/user_info/user_nick_name/',
    type:'POST',
    data:{'userMobile':userMobile,'nickName':nickName},
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
