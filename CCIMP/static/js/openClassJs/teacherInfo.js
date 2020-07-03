/**
 * Created by zhangbo on 2020/6/18.
 */

// 获取项目列表
// var projectInit = function(_cmbProject){
//
//     var cmbProject = document.getElementById(_cmbProject);
//
//     function getProjectListInfo(){
//
//         $.get("/project/get_project_list/",{},function (resp) {
//
//             if (resp.status === 10200) {
//
//                 console.log(resp.data);
//
//                 dataList = resp.data;
//
//                 for(var i = 0; i < dataList.length; i++){
//
//                     cmbAddOption(cmbProject,dataList[i]);
//
//                 }
//
//                 $('#project_name').selectpicker("refresh");
//
//             }
//         })
//     }
//
//     // 调用getProjectListInfo
//     getProjectListInfo();
//
// };


// 获取某一个项目的模块列表
// var ModuleInit = function(_cmbModule,pid){
//
//     var cmbModule = document.getElementById(_cmbModule);
//
//     function getModuleListInfo(){
//
//         $.post("/module/get_module_list/",{"pid":pid},function (resp) {
//
//             if (resp.status === 10200) {
//
//                 console.log(resp.data);
//
//                 dataList = resp.data;
//
//                 //清除之前modules下拉数据
//                 clearOption(cmbModule);
//
//                 for(i = 0; i < dataList.length; i++){
//
//                     cmbAddOption(cmbModule,dataList[i]);
//
//                 }
//
//                 //改变事件后刷新modules下拉列表数据
//                 $("#module_name").selectpicker("refresh");
//
//             }
//
//             else {
//
//                 // window.alert(resp.message);
//                 console.log(resp.message);
//
//                 //清除之前modules下拉数据
//                 clearOption(cmbModule);
//
//                 options2 = document.querySelectorAll("#module_name > option");
//
//                 if (options2.length === 0) {
//
//                     // 创建option标签元素
//                     var option = document.createElement("option");
//
//                     // 添加option到选项
//                     cmbModule.options.add(option);
//
//                     // 元素值
//                     option.innerHTML = "请选择";
//
//                     // 元素value值
//                     option.value = "";
//
//                     //查询定位该类元素text赋值
//                     document.querySelectorAll(".filter-option-inner-inner")[1].innerText = "请选择";
//
//                     //改变事件后刷新modules下拉列表数据
//                     $("#module_name").selectpicker("refresh");
//                 }
//
//             }
//
//         })
//     }
//
//     // 调用getModuleListInfo
//     getModuleListInfo();
//
// };




// 获取下拉框模块列表所有option的list数据
// var SelectModule = function(mid){
//
//     options2 = document.querySelectorAll("#module_name > option");
//
// 	for (i = 0; i < options2.length; i++){
//
//         v2 = options2[i].value;
//
// 		if (v2 === mid){
//
// 			options2[i].selected = true;
//
// 			text = options2[i].text;
//
// 			document.querySelectorAll(".filter-option-inner-inner")[1].innerText = text;
//
// 		}
// 	}
// };





//------------------------------------select2 js二级联动菜单------------------------------------//


/**
 * select2
*/

// 获取用例信息
// var TestCaseInit = function() {
//
//     // 获取当前url地址
//     var url = document.location;
//
//     console.log("url",url.pathname.split("/")[3]);
//
//     var cid = url.pathname.split("/")[3];
//
//     $.post("/testcase/get_case_info",
//         {
//             cid:cid
//         },
//         function(resp) {
//
//             console.log("返回的结果", resp.data);
//
//             // 请求URL
//             document.querySelector("#req_url").value = resp.data.url;
//
//             // 用例名称
//             document.getElementById("case_name").value = resp.data.name;
//
//             // 请求方法
//             if (resp.data.method === 1) {
//
//                 document.querySelector("#get").setAttribute("checked", "");
//             }
//
//             else if (resp.data.method === 2) {
//
//                 document.querySelector("#post").setAttribute("checked", "");
//
//             }
//
//             else if (resp.data.method === 3) {
//
//                 document.querySelector("#put").setAttribute("checked", "");
//
//             }
//
//             else if (resp.data.method === 4) {
//
//                 document.querySelector("#delete").setAttribute("checked", "");
//
//             }
//
//             // 请求头
//             document.getElementById("header").value = resp.data.header;
//
//             // 请求类型
//             if (resp.data.parameter_type === 1) {
//
//                 document.querySelector("#form").setAttribute("checked", "");
//
//             }
//
//             else if (resp.data.parameter_type === 2) {
//
//                 document.querySelector("#json").setAttribute("checked", "");
//
//             }
//
//             // 请求参数
//             document.getElementById("req_parameter").value = resp.data.parameter_body;
//
//             // 断言类型
//             if (resp.data.assert_type === 1) {
//
//                 document.querySelector("#contains").setAttribute("checked", "");
//
//             }
//
//             else if (resp.data.assert_type === 2) {
//
//                 document.querySelector("#mathches").setAttribute("checked", "");
//
//             }
//
//             // 断言文本
//             document.getElementById("assert").value = resp.data.assert_text;
//
//             //调用js初始化下拉框数据
//             // console.log(resp.data.project_id,resp.data.module_id);
//             // console.log(typeof(resp.data.project_id),typeof(resp.data.module_id));
//             SelectInit(resp.data.project_id,resp.data.module_id);
//
//         }
//     )
//
// };


//初始化 “公开课老师列表”
var SelectTeacherInit = function () {

    var cmbTeacher = document.getElementById("c_tea_ids_id");
    var teachDataList = [];


     //console.log("项目对象：",cmbProject);
     //console.log("模块对象：",cmbModule);
     //console.log("初始化项目前索引：",cmbProject.selectedIndex);
     //console.log("初始化模块前索引：",cmbModule.selectedIndex);


    // //设置默认选项
    // function setDefaultOption(obj,id){
    //
    //     console.log("默认list长度：",obj.options.length);
    //     // console.log("select默认项目id：",id);
    //     // console.log("select默认项目id类型：",typeof(id));
    //     // console.log("select项目value值索引：",obj.options[obj.selectedIndex].value);
    //
    //     if (id === 0 ){
    //
    //         clearModuleOption(cmbModule);
    //
    //         // 创建option标签元素
    //         var option = document.createElement("option");
    //
    //         // 添加option到选项
    //         cmbModule.options.add(option);
    //
    //         // 元素值
    //         option.innerHTML = "请选择";
    //
    //         // 元素value值
    //         option.value = "0";
    //
    //     }
    //
    //     for(var i = 0; i < obj.options.length; i++) {
    //
    //         // console.log("obj.options[i].value：",typeof(obj.options[i].value));
    //
    //         if (obj.options[i].value === id ){
    //
    //             obj.selectedIndex = i;
    //
    //             // console.log("项目默认索引为：",obj.selectedIndex);
    //
    //             return;
    //         }
    //     }
    //
    // }
    //
    // // 清除下拉选项
    // function clearModuleOption(cmb){
    //
    //     for(i=0; i<= cmb.length+1; i++){
    //
    //         cmb.options.remove(cmb[i]);
    //
    //     }
    // }
    //
    //创建下拉选项
    function addOption(cmbTeacher,obj){

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbTeacher.options.add(option);

        // 元素值
        option.innerHTML = obj.nick_name;

        // 元素value值
        option.value = obj.teacher_id;

    }

    //改变项目
    function changeTeacher(){

        // cmbModule.options.length = 0;

        // console.log("老师列表索引值为：",cmbTeacher.selectedIndex);

        if (cmbTeacher.selectedIndex === -1){

            return;
        }

        var teacher_id = cmbTeacher.options[cmbTeacher.selectedIndex].value;
        // console.log("pid：",typeof (pid));
        teacher_id = parseInt(teacher_id);
        // console.log("teacher_id：",typeof (teacher_id));
        // console.log("teacher_id：",teacher_id);

        // if (teacher_id === 0) {

            // setDefaultOption(cmbModule,pid);


        // }

        // for (var i = 0 ; i < datalist.length; i++){
        //
        //     if (datalist[i].id === pid) {
        //
        //         var modules = datalist[i].moduleList;
        //
        //         console.log("改变后模块信息：",modules);
        //
        //         //清除之前modules下拉数据
        //         clearModuleOption(cmbModule);
        //
        //         // 创建option标签元素
        //         var option = document.createElement("option");
        //
        //         // 添加option到选项
        //         cmbModule.options.add(option);
        //
        //         // 元素值
        //         option.innerHTML = "请选择";
        //
        //         // 元素value值
        //         option.value = "0";
        //
        //         for (var j = 0 ; j < modules.length; j++){
        //
        //             addOption(cmbModule,modules[j]);
        //
        //         }
        //
        //     }
        //
        // }
        //
        // setDefaultOption(cmbModule,defaultModuleId);

    }


    //调取select数据列表
    function getSelectTeacherData(){

        $.get('/tool/open_class/api/getSelectTeacherData',{},function(resp){

            teachDataList = resp.data;

            if (resp.status === 10200){

                // console.log("公开课老师结果：",teachDataList);

                for (var i = 0; i < teachDataList.length; i++){

                    // console.log("公开课老师结果：",teachDataList[i]);

                    addOption(cmbTeacher,teachDataList[i]);
                }

                // console.log("defaultProjectId-->",defaultProjectId);

                // 调用默认选项
                // setDefaultOption(cmbProject,defaultProjectId);

                changeTeacher();

                cmbTeacher.onchange = changeTeacher;

            }

            else{

                console.log("公开课老师结果：",teachDataList);

            }

        });
    };

    getSelectTeacherData();

};
