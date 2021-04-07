/**
 * Created by zhangbo on 2021/3/25.
 */


//------------------------------------select2 js二级联动菜单------------------------------------//


/**
 * select2
*/


//初始化 “约课开始时间”
var SelectStartTimeInit = function () {

    var cmbStartTime = document.getElementById("start_time_id");
    var startTimeList = [];

    //创建下拉选项
    function addOption(cmbStartTime,obj){

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbStartTime.options.add(option);

        // 元素值
        option.innerHTML = obj.start_time_id;

        // 元素value值
        option.value = obj.start_time_value;

    }

    //改变项目
    function changeStartTime(){

        if (cmbStartTime.selectedIndex === -1){

            return;
        }

        var startTime_id = cmbStartTime.options[cmbStartTime.selectedIndex].value;
        // console.log("pid：",typeof (pid));
        startTime_id = parseInt(startTime_id);
        // console.log("startTime_id：",typeof (startTime_id));
        // console.log("startTime_id：",startTime_id);


    }


    //调取select数据列表
    function getSelectStartTimeData(){

        $.get('/tool/appoint_manage/api/getSelectStartTimeData',{},function(resp){

            startTimeList = resp.data;

            if (resp.status === 10200){

                // console.log("开始时间结果：",startTimeList);

                for (var i = 0; i < startTimeList.length; i++){

                    // console.log("开始时间结果：",startTimeList[i]);

                    addOption(cmbStartTime,startTimeList[i]);
                }

                changeStartTime();

                cmbStartTime.onchange = changeStartTime;

            }

            else{

                console.log("开始时间结果：",startTimeList);

            }

        });
    };

    getSelectStartTimeData();

};



//初始化 “约课结束时间”
var SelectEndTimeInit = function () {

    var cmbEndTime = document.getElementById("end_time_id");
    var endTimeList = [];

    //创建下拉选项
    function addOption(cmbEndTime,obj){

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbEndTime.options.add(option);

        // 元素值
        option.innerHTML = obj.end_time_id;

        // 元素value值
        option.value = obj.end_time_value;

    }

    //改变项目
    function changeEndTime(){


        if (cmbEndTime.selectedIndex === -1){

            return;
        }

        var endTime_id = cmbEndTime.options[cmbEndTime.selectedIndex].value;
        endTime_id = parseInt(endTime_id);
        // console.log("endTime_id：",typeof (endTime_id));
        // console.log("endTime_id：",endTime_id);


    }


    //调取select数据列表
    function getSelectEndTimeData(){

        $.get('/tool/appoint_manage/api/getSelectEndTimeData',{},function(resp){

            endTimeList = resp.data;

            if (resp.status === 10200){

                // console.log("结束时间结果：",endTimeList);

                for (var i = 0; i < endTimeList.length; i++){

                    // console.log("结束时间结果：",endTimeList[i]);

                    addOption(cmbEndTime,endTimeList[i]);
                }

                changeEndTime();

                cmbEndTime.onchange = changeEndTime;

            }

            else{

                console.log("结束时间结果：",endTimeList);

            }

        });
    };

    getSelectEndTimeData();

};

