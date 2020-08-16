


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

        window.location.reload();
        return;

    }else if(!checkPassword(new_password)){

        window.location.reload();
        return;

    };

    //获取手机号是否注册接口
    $.ajax({
    url:'/tool/user_info/register_mobile_check/',
    type:'POST',
    data:{'new_mobile':new_mobile},
        success:function (data) {

            $('#myRolecontent').modal('hide');

            if (data.status_code === 10200) {

                mobile_check_status = 1;

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

                            window.alert(data.message);
                            $('#myRolecontent').modal('show');

                        } else if (data.status_code === 10101){

                            mobile_check_status = 0;
                            window.alert(data.message);
                            window.location.reload();

                        }else if (data.status_code === 10102){

                            mobile_check_status = 0;
                            window.alert(data.message);
                            window.location.reload();

                        }else {
                            window.alert('发生出了其他错误，咱也不知道，咱们不敢问，请联系波波');
                            window.location.reload();
                        }

                    },

                    complete:function(){
                        closeMask();
                    }
               })

            } else if (data.status_code === 10101 || data.status_code === 10102){

                mobile_check_status = 0;

                window.alert(data.message);

                // $('#myRolecontent').modal('hide');

                //模态框延迟100毫秒后，自动关闭模态框
                // setTimeout("$('#myRolecontent').modal('hide')",1);//5s延时自动关闭

                window.location.reload();

            }else {

                window.alert('发生出了其他错误，咱也不知道，咱们不敢问，请联系波波');
                window.location.reload()
            }

        }
   })

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


//青少按钮点击监听
// $("#teenagers_Role").click(function() {
// })

//成人按钮点击监听
// $("#adult_Role").click(function() {
// })


//身份确认弹窗
function userLevelconfirm(){
    var data={'occup': '7', 'grade': '-4', 'purpose': '0', 'english_level': '1', 'age': '0', 'sex': 'man'};

    if($("#teenagers_Role option:selected").val() === 'teenagers001'){
        data = {
            'occup': '7',
            'grade': '-4',
            'purpose': '0',
            'english_level': '1',
            'age': '0',
            'sex': 'man'
        }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers002'){
        data = {
                'occup': '7',
                'grade': '-4',
                'purpose': '0',
                'english_level': '4',
                'age': '0',
                'sex': 'man'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers003'){
        data = {
                'occup': '7',
                'grade': '-3',
                'purpose': '0',
                'english_level': '2',
                'age': '0',
                'sex': 'woman'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers004'){
        data = {
                'occup': '7',
                'grade': '-2',
                'purpose': '0',
                'english_level': '3',
                'age': '0',
                'sex': 'woman'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers005'){
        data = {
                'occup': '7',
                'grade': '-1',
                'purpose': '21',
                'english_level': '1',
                'age': '0',
                'sex': 'woman'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers006'){
        data = {
                'occup': '4',
                'grade': '1',
                'purpose': '21',
                'english_level': '1',
                'age': '0',
                'sex': 'woman'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers007'){
        data = {
                'occup': '6',
                'grade': '8',
                'purpose': '20',
                'english_level': '11',
                'age': '0',
                'sex': 'man'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers008'){
        data = {
                'occup': '5',
                'grade': '0',
                'purpose': '14',
                'english_level': '2',
                'age': '0',
                'sex': 'man'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers009'){
        data = {
                'occup': '2',
                'grade': '0',
                'purpose': '12',
                'english_level': '4',
                'age': '0',
                'sex': 'man'
            }
    }else if($("#teenagers_Role option:selected").val() === 'teenagers010'){
        data = {
                'occup': '1',
                'grade': '0',
                'purpose': '7',
                'english_level': '1',
                'age': '0',
                'sex': 'man'
            }
    }

     $.ajax({
           url:'/tool/user_info/post_UpUserOccupInfo/',
           type:'POST',
           data:data,
           success:function (data) {

               if (data.status_code === 10200) {

                    window.alert(data.message);

               }

           },

          complete:function(){

          }
     })
}




