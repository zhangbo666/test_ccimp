/**
 * Created by zhangbo on 19/9/7.
 */


//获取用户未完成的订单
function userOnOrderDetail(){

    var userMobile = $("[name='mobile_name']").val();
    var userPasword = $("[name='password_name']").val();

    $.ajax({
    url:'/tool/sale_order/get_order_on_detail/',
    type:'POST',
    data:{'userMobile':userMobile,'userPasword':userPasword},
    success:function(data){

        if (data.status_code === 10200){

            console.log("data-->",data);
            console.log("result.result-->",data.result);

            window.alert(data.message);

            //每次初始化加载模态框时，清空模态框中的tbody元素
            var table1=document.getElementById("myTableUserOnOrderDetail");

            var table1_tbody=table1.getElementsByTagName("tbody");

            if (table1_tbody.length >0){

                table1.removeChild(table1_tbody[0]);

            };

            var data = data.result;

            for (var i=0; i < data.length; i++){

                var str = '<td>' +
                          '<input type="radio" name="radio_on_orders" id="radio_on_orders" value='+ data[i].id + '>' + '</td>' +
                          '<td>' + data[i].id + '</td>' +
                          '<td>' + data[i].extend_id + '</td>' +
                          '<td>' + data[i].order_money + '</td>' +
                          '<td>' + data[i].order_type + '</td>' +
                          '<td>' + data[i].status + '</td>';
                $("#myTableUserOnOrderDetail").append('<tr>' + str + '</tr>');
            }

            //释放处理未完成订单按钮点击事件
            $("#processOnOrder").attr("disabled",false);
            //$("#processOnOrder").removeAttr("disabled");
            //window.document.getElementById('processOnOrder').removeAttribute('disabled');

        }

        else if(data.status_code === 10103){

            window.alert(data.message);

            //每次初始化加载模态框时，清空模态框中的tbody元素
            var table1=document.getElementById("myTableUserOnOrderDetail");

            var table1_tbody=table1.getElementsByTagName("tbody");

            if (table1_tbody.length >0){

                table1.removeChild(table1_tbody[0]);

            };

            //模态框延迟600毫秒后，自动关闭模态框
            setTimeout("$('#myModalUserOnOrderDetail').modal('hide')",600);

        }

        else{

            window.alert(data.message);

            //手机号或密码错误时，每次初始化加载模态框时默认删除该模态框
            $("#myModalUserOnOrderDetail").empty();

            window.location.reload()

        }
    }

    });
};