


/**
 * Created by Jing on 2020/06/05.
 */

function userRegister() {

    //读取注册手机号
    var new_mobile = $("[name='new_mobile']").val();

    //读取注册密码
    var new_password = $("[name='new_password']").val();

    //读取注册推荐人手机号
    var recommen_mobile = $("[name='recommen_mobile']").val();

    //手机是否注册，1可以注册，0已注册
    var mobile_check_status = '';

    //校验注册手机号 和 密码 填写规范
    if(!checkPhone(new_mobile)){
        return
    }else if(!checkPassword(new_password)){
        return
    };

    //获取手机号是否注册接口
    $.ajax({
    url:'/tool/user_info/register_mobile_check/',
    type:'POST',
    data:{'new_mobile':new_mobile},
        success:function (data) {

            if (data.status_code === 10200) {
                mobile_check_status = 1

                //初始化蒙层
                createMask();

                //注册接口调用
                $.ajax({
                    url:'/tool/user_info/post_registerInfo/',
                    type:'POST',
                    data:{'new_mobile':new_mobile,'new_password':new_password,'recommen_mobile':recommen_mobile},
                    beforeSend:function(){
                        showMask();
                    },
                    success:function (data) {

                        closeMask();

                        if (data.status_code === 10200) {
                            window.alert(data.message)
                        } else if (data.status_code === 10101){
                            mobile_check_status = 0
                            window.alert(data.message);
                            window.location.reload()
                        }else if (data.status_code === 10102){
                            mobile_check_status = 0
                            window.alert(data.message);
                            window.location.reload()
                        }else {
                            window.alert('发生出了其他错误，咱也不知道，咱们不敢问，请联系波波');
                            window.location.reload()
                        }

                    },

                    complete:function(){
                        closeMask();
                    }
               })

            } else if (data.status_code === 10101){
                mobile_check_status = 0
                window.alert(data.message);
                window.location.reload()
            }else if (data.status_code === 10102){
                mobile_check_status = 0
                window.alert(data.message);
                window.location.reload()
            }else {
                window.alert('发生出了其他错误，咱也不知道，咱们不敢问，请联系波波');
                window.location.reload()
            }

        }
   })

    // if(mobile_check_status === 1){
    //     $.ajax({
    //     url:'/tool/user_info/post_registerInfo/',
    //     type:'POST',
    //     data:{'new_mobile':new_mobile,'new_password':new_password,'recommen_mobile':recommen_mobile},
    //         success:function (data) {
    //
    //             if (data.status_code === 10200) {
    //                 window.alert(data.message)
    //             } else if (data.status_code === 10101){
    //                 mobile_check_status = 0
    //                 window.alert(data.message);
    //                 window.location.reload()
    //             }else if (data.status_code === 10102){
    //                 mobile_check_status = 0
    //                 window.alert(data.message);
    //                 window.location.reload()
    //             }else {
    //                 window.alert('发生出了其他错误，咱也不知道，咱们不敢问，请联系波波');
    //                 window.location.reload()
    //             }
    //
    //         }
    //    })
    // }


}

//校验手机号是否正确
function checkPhone(phoneNumber) {
    if(phoneNumber === '') {
        alert('手机号不能为空');
        return false
    }
    else if(phoneNumber.length !== 11){
        alert('手机号的长度不符合中国规则');
        return false
    }else if(isNaN(phoneNumber)){
        alert('手机号包含非数字字符');
        return false
    }else {
        return true;
    }
}

//校验密码
function checkPassword(userPassword) {
    if(userPassword === ''){
        alert('密码不能为空');
        return false
    }
    else if(userPassword.length < 6){
        alert('密码长度不能小于6位');
        return false
    }else{
        return true
    }
}

//创建遮罩层函数体
function createMask(){
    var node=document.createElement('div');
        node.setAttribute('id','backdrop');
        node.style="position:fixed;top:0;left:0;right:0;bottom:0;z-index:1000;background-color:rgba(0,0,0,0.6);";
        node.style.display="none";
    var html='<div style="position: fixed; top: 38%; left: 38%; z-index: 1001;">';
        html+='<div style="text-align:center;">';
        html+='<img src="/static/image/loading.gif" style="width:60px;height:60px;">';
        html+='<div style="padding-left:10px;font-size:14px;color:#FFF;">网络请求中...</div>';
        html+='</div>';
        html+='</div>';
        node.innerHTML=html;
    var body=document.querySelector('body');
        body.appendChild(node);
}

//开启遮罩层函数体
function showMask() {
    var backdrop=document.getElementById('backdrop');
    backdrop.style.display='block';
}

//关闭遮罩层函数体
function closeMask(){
    var backdrop=document.getElementById('backdrop');
    backdrop.style.display='none';
}

