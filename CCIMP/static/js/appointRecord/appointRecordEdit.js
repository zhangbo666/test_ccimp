/**
 * Created by zhangbo on 20/7/5.
 */


//约课记录修改
function appointRecordEdit(){

    var radio_appoint_record = document.getElementsByName('radio_on_appoint_record');

    // console.log(radio_appoint_record);

    var isCheck = false;

    //修改约课记录按钮连击
    var appointRecordEditDoubleClick = 0;

    if ($("#radio_on_appoint_record").length > 0) {

        for (var i = 0; i < radio_appoint_record.length; i++) {

//                if (radio_appoint_record[i].checked){
//
//                    userid = radio_appoint_record[i].value;
//
//                    isCheck = true;
//
//                }
            var checkeds = document.querySelectorAll("[name=radio_on_appoint_record]")[i].checked;

            var courseStatus = $("select[id='course_status']").val();

            if (courseStatus === '0'){

                window.alert("课程状态还未选择");
                return;

            }

            if (checkeds === true){

                var appointRecordID = $("input[name=radio_on_appoint_record]:checked").val();


                // console.log(appointRecordID);

                isCheck = true;

                //禁用修改按钮点击事件
                // $("#appointRecordEdit").attr("disabled",true);
                //$("#appointRecordEdit").attr("disabled","disabled");
                //window.document.getElementById('appointRecordEdit').setAttribute("disabled",true);


                //处理订单按钮连击，暂不考虑
//                    if (appointRecordEditDoubleClick == 0) {
//
//                        appointRecordEditDoubleClick = 1;
//
//                        $("#processOrder").attr("disabled",true);

//                        setTimeout(function () {
//
//                            appointRecordEditDoubleClick = 0;
//
//                          $("#processOrder").attr("disabled",false);
//
//                        }, 20000);
//                    }



                //修改课程状态接口
                $.ajax({
                url:'/tool/user_info/api/appoint_record',
                type:'POST',
                data:{'appointRecordID':appointRecordID,'courseStatus':courseStatus},
                success:function(data){

                    if (data.status_code === 10101 || data.status_code === 10102) {

                        alert(data.message);

                    }

                    else if (data.status_code === 10200) {

                        alert(data.message);

                    }

                }

                });

            }
        }

        if (!isCheck){

            alert("请选择约课记录！！！");

        }


    }

    else{

        alert("当前约课数据列表为空！")
    }


}
