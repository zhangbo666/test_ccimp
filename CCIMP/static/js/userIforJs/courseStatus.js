/**
 * Created by zhangbo on 2020/5/31.
 */


//获取课程状态按钮连击
var courseStatusDoubleClick = 0;

//获取用户昵称方法
function courseStatus() {

    var userMobile = $("[name='user_mobile']").val();
    var courseStatus = $("select[id='course_status']").val();

    //获取课程状态按钮连击锁定超时时间
    if (courseStatusDoubleClick === 0) {

        courseStatusDoubleClick = 1;

        $("#courseStatus").attr("disabled",true);

        setTimeout(function () {

            courseStatusDoubleClick = 0;

            $("#courseStatus").attr("disabled",false);

        }, 3000);
    }

    if (courseStatus === '0'){

        alert("课程状态还未选择");

        return;

    }

    //获取课程状态接口
    $.ajax({
    url:'/tool/user_info/course_status/',
    type:'GET',
    data:{'userMobile':userMobile,'courseStatus':courseStatus},
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

