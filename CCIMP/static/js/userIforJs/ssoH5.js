/**
 * Created by zhangbo on 2020/8/20.
 */


//获取h5标签按钮连击
var ssoH5DoubleClick = 0;

//获取sso身份方法
function ssoH5() {

    var userMobile = $("[name='user_mobile']").val();
    var h5Label = $("[name='h5_label']").val();

    //获取sso身份按钮连击锁定超时时间
    if (ssoH5DoubleClick === 0) {

        ssoH5DoubleClick = 1;

        $("#ssoH5").attr("disabled",true);

        setTimeout(function () {

            ssoH5DoubleClick = 0;

            $("#ssoH5").attr("disabled",false);

        }, 3000);
    }

    if (h5Label === '-1'){

        alert("H5标签选项未选！");

        return;

    }
    else if (h5Label === '2'){

        alert("巧虎标签暂时不能改！");

        return;

    }

    //修改h5标签接口
    $.ajax({
    url:'/tool/user_info/sso_h5/',
    type:'POST',
    data:{'userMobile':userMobile,'h5Label':h5Label},
    success:function (data) {

        if (data.status_code === 10200) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.message);

        }

        else if (data.status_code === 10101 || data.status_code === 10102 || data.status_code === 10103) {

            console.log("data-->", data);
            console.log("data.message-->", data.message);

            window.alert(data.message);
        }

    }

    })

};

