/**
 * Created by zhangbo on 2020/6/21.
 */

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


//初始化 “青少教材列表”
var SelectJuniorBookInit = function () {

    var cmbJuniorTextBookid1 = document.getElementById("j_cate_id1_id");
    var cmbJuniorTextBookid2 = document.getElementById("j_cate_id2_id");
    var cmbJuniorTextBookid3 = document.getElementById("j_cate_id3_id");
    var textJuniorBookDataList = [];


    console.log("青少一级教材对象：",cmbJuniorTextBookid1);
    console.log("青少二级教材对象：",cmbJuniorTextBookid2);
    console.log("青少三级教材对象：",cmbJuniorTextBookid3);
    console.log("初始化青少一级教材索引：",cmbJuniorTextBookid1.selectedIndex);
    console.log("初始化青少二级教材索引：",cmbJuniorTextBookid2.selectedIndex);
    console.log("初始化青少二级教材索引：",cmbJuniorTextBookid3.selectedIndex);


    // 清除教材下拉选项
    function clearJuniorTextBookOption(cmb) {

        l_sum = cmb.length;

        for (i = 0; i <= l_sum; i++) {

            cmb.options.remove(cmb[i]);

        }
    }

    //创建一级教材下拉选项
    function addJuniorTextBook1Option(cmbJuniorTextBookid1, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbJuniorTextBookid1.options.add(option);

        // 元素值
        option.innerHTML = obj.c_cate_id1_name;

        // 元素value值
        option.value = obj.c_cate_id1_id;

    }

    //创建二级教材下拉选项
    function addJuniorTextBook2Option(cmbJuniorTextBookid2, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbJuniorTextBookid2.options.add(option);

        // 元素值
        option.innerHTML = obj.c_cate_id2_name;

        // 元素value值
        option.value = obj.c_cate_id2_id;

    }

    //创建三级教材下拉选项
    function addJuniorTextBook3Option(cmbJuniorTextBookid3, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbJuniorTextBookid3.options.add(option);

        // 元素值
        option.innerHTML = obj.book_id_name;

        // 元素value值
        option.value = obj.book_id_id;

    }

    //设置二级、三级教材下拉选项默认值
    function setDefaultOption(cmbSetDefaultOption2,cmbSetDefaultOption3) {

        // 清除之前二级教材下拉数据
        clearJuniorTextBookOption(cmbJuniorTextBookid2);

        // 清除之前三级教材下拉数据
        clearJuniorTextBookOption(cmbJuniorTextBookid3);

        // 创建option标签元素
        var text_book2_init_option = document.createElement("option");
        var text_book3_init_option = document.createElement("option");

        // 添加option到选项
        cmbSetDefaultOption2.options.add(text_book2_init_option);
        cmbSetDefaultOption3.options.add(text_book3_init_option);

        // 元素值
        text_book2_init_option.innerHTML = "请选择";
        text_book3_init_option.innerHTML = "请选择";

        // 元素value值
        text_book2_init_option.value = "0";
        text_book3_init_option.value = "0";

    }

    //改变一级教材list数据
    function changeJuniorTextBook1() {

        // console.log("青少一级教材切换后索引值：", cmbJuniorTextBookid1.selectedIndex);

        if (cmbJuniorTextBookid1.selectedIndex === -1) {

            return;
        }

        if (cmbJuniorTextBookid1.selectedIndex === 0){

            // 设置二级、三级教材默认选项
            setDefaultOption(cmbJuniorTextBookid2,cmbJuniorTextBookid3);

        }

        var j_c_cate_id1_id = cmbJuniorTextBookid1.options[cmbJuniorTextBookid1.selectedIndex].value;
        // console.log("j_c_cate_id1_id：",typeof (j_c_cate_id1_id));
        j_c_cate_id1_id = parseInt(j_c_cate_id1_id);
        // console.log("j_c_cate_id1_id：",typeof (j_c_cate_id1_id));
        // console.log("j_c_cate_id1_id：", j_c_cate_id1_id);

        for (var i = 0; i < textJuniorBookDataList.length; i++) {

            if (textJuniorBookDataList[i].c_cate_id1_id === j_c_cate_id1_id) {

                var textJuniorBookList2 = textJuniorBookDataList[i].bookBList;

                console.log("青少一级教材切换后展示青少二级教材数据：", textJuniorBookList2);

                //清除之前青少二级教材下拉数据
                clearJuniorTextBookOption(cmbJuniorTextBookid2);

                // 创建option标签元素
                var option1 = document.createElement("option");

                // 添加option到选项
                cmbJuniorTextBookid2.options.add(option1);

                // 元素值
                option1.innerHTML = "请选择";

                // 元素value值
                option1.value = "0";

                //清除之前三级教材下拉数据
                clearJuniorTextBookOption(cmbJuniorTextBookid3);

                // 创建option标签元素
                var option2 = document.createElement("option");

                // 添加option到选项
                cmbJuniorTextBookid3.options.add(option2);

                // 元素值
                option2.innerHTML = "请选择";

                // 元素value值
                option2.value = "0";

                for (var j = 0; j < textJuniorBookList2.length; j++) {

                    addJuniorTextBook2Option(cmbJuniorTextBookid2, textJuniorBookList2[j]);

                }

            }

        }

    }


    //改变二级教材list数据
    function changeJuniorTextBook2() {

        // console.log("二级教材切换后索引值：", cmbJuniorTextBookid2.selectedIndex);

        if (cmbJuniorTextBookid2.selectedIndex === -1) {

            return;
        }

        if (cmbJuniorTextBookid2.selectedIndex === 0){

            //清除之前三级教材下拉数据
            clearJuniorTextBookOption(cmbJuniorTextBookid3);

            // 创建option标签元素
            var init_option = document.createElement("option");

            // 添加option到选项
            cmbJuniorTextBookid3.options.add(init_option);

            // 元素值
            init_option.innerHTML = "请选择";

            // 元素value值
            init_option.value = "0";

        }

        var j_c_cate_id2_id = cmbJuniorTextBookid2.options[cmbJuniorTextBookid2.selectedIndex].value;
        // console.log("j_c_cate_id2_id：",typeof (j_c_cate_id2_id));
        j_c_cate_id2_id = parseInt(j_c_cate_id2_id);


        for (var i = 0; i < textJuniorBookDataList.length; i++) {

            var textJuniorBookList2 = textJuniorBookDataList[i].bookBList;

            for (var j = 0; j < textJuniorBookList2.length; j++) {

                if (textJuniorBookList2[j].c_cate_id2_id === j_c_cate_id2_id) {

                    var textJuniorBookList3 = textJuniorBookList2[j].bookCList;

                    console.log("青少二级教材切换后展示青少三级教材数据：", textJuniorBookList3);

                    //清除之前三级教材下拉数据
                    clearJuniorTextBookOption(cmbJuniorTextBookid3);

                    // 创建option标签元素
                    var option = document.createElement("option");

                    // 添加option到选项
                    cmbJuniorTextBookid3.options.add(option);

                    // 元素值
                    option.innerHTML = "请选择";

                    // 元素value值
                    option.value = "0";

                    for (var k = 0; k < textJuniorBookList3.length; k++) {

                        addJuniorTextBook3Option(cmbJuniorTextBookid3, textJuniorBookList3[k]);

                    }

                }

            }
        }

    }

    //调取select数据列表
    function getSelectJuniorTextBookData() {

        $.get('/tool/appoint_manage/api/getSelectJuniorTextBookData', {}, function (resp) {

            textJuniorBookDataList = resp.data;

            if (resp.status === 10200) {

                console.log("教材查询结果：", textJuniorBookDataList);

                for (var i = 0; i < textJuniorBookDataList.length; i++) {

                    // console.log("教材查询结果：",textBookDataList[i]);

                    addJuniorTextBook1Option(cmbJuniorTextBookid1, textJuniorBookDataList[i]);
                }

                // console.log("defaultProjectId-->",defaultProjectId);

                // 调用默认选项
                // setDefaultOption(cmbProject,defaultProjectId);

                changeJuniorTextBook1();

                cmbJuniorTextBookid1.onchange = changeJuniorTextBook1;

                changeJuniorTextBook2();

                cmbJuniorTextBookid2.onchange = changeJuniorTextBook2;

            }

            else {

                console.log("教材查询结果：", textJuniorBookDataList);

            }

        });
    };

    getSelectJuniorTextBookData();

};
