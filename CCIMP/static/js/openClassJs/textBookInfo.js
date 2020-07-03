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


//初始化 “教材列表”
var SelectTextBookInit = function () {

    var cmbTextBookid1 = document.getElementById("c_cate_id1_id");
    var cmbTextBookid2 = document.getElementById("c_cate_id2_id");
    var cmbTextBookid3 = document.getElementById("book_id_id");
    var textBookDataList = [];


    // console.log("一级教材对象：",cmbTextBookid1);
    // console.log("二级教材对象：",cmbTextBookid2);
    // console.log("三级教材对象：",cmbTextBookid3);
    // console.log("初始化一级教材索引：",cmbTextBookid1.selectedIndex);
    // console.log("初始化二级教材索引：",cmbTextBookid2.selectedIndex);
    // console.log("初始化二级教材索引：",cmbTextBookid3.selectedIndex);

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

    // 清除教材下拉选项
    function clearTextBookOption(cmb) {

        l_sum = cmb.length;

        for (i = 0; i <= l_sum; i++) {

            cmb.options.remove(cmb[i]);

        }
    }

    //创建一级教材下拉选项
    function addTextBook1Option(cmbTextBookid1, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbTextBookid1.options.add(option);

        // 元素值
        option.innerHTML = obj.c_cate_id1_name;

        // 元素value值
        option.value = obj.c_cate_id1_id;

    }

    //创建二级教材下拉选项
    function addTextBook2Option(cmbTextBookid2, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbTextBookid2.options.add(option);

        // 元素值
        option.innerHTML = obj.c_cate_id2_name;

        // 元素value值
        option.value = obj.c_cate_id2_id;

    }

    //创建三级教材下拉选项
    function addTextBook3Option(cmbTextBookid3, obj) {

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmbTextBookid3.options.add(option);

        // 元素值
        option.innerHTML = obj.book_id_name;

        // 元素value值
        option.value = obj.book_id_id;

    }

    //设置二级、三级教材下拉选项默认值
    function setDefaultOption(cmbSetDefaultOption2,cmbSetDefaultOption3) {

        // 清除之前二级教材下拉数据
        clearTextBookOption(cmbTextBookid2);

        // 清除之前三级教材下拉数据
        clearTextBookOption(cmbTextBookid3);

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
    function changeTextBook1() {

        // console.log("一级教材切换后索引值：", cmbTextBookid1.selectedIndex);

        if (cmbTextBookid1.selectedIndex === -1) {

            return;
        }

        if (cmbTextBookid1.selectedIndex === 0){

            // 设置二级、三级教材默认选项
            setDefaultOption(cmbTextBookid2,cmbTextBookid3);

        }

        var c_cate_id1_id = cmbTextBookid1.options[cmbTextBookid1.selectedIndex].value;
        // console.log("c_cate_id1_id：",typeof (c_cate_id1_id));
        c_cate_id1_id = parseInt(c_cate_id1_id);
        // console.log("c_cate_id1_id：",typeof (c_cate_id1_id));
        // console.log("c_cate_id1_id：", c_cate_id1_id);

        for (var i = 0; i < textBookDataList.length; i++) {

            if (textBookDataList[i].c_cate_id1_id === c_cate_id1_id) {

                var textBookList2 = textBookDataList[i].bookBList;

                console.log("一级教材切换后展示二级教材数据：", textBookList2);

                //清除之前二级教材下拉数据
                clearTextBookOption(cmbTextBookid2);

                // 创建option标签元素
                var option1 = document.createElement("option");

                // 添加option到选项
                cmbTextBookid2.options.add(option1);

                // 元素值
                option1.innerHTML = "请选择";

                // 元素value值
                option1.value = "0";

                //清除之前三级教材下拉数据
                clearTextBookOption(cmbTextBookid3);

                // 创建option标签元素
                var option2 = document.createElement("option");

                // 添加option到选项
                cmbTextBookid3.options.add(option2);

                // 元素值
                option2.innerHTML = "请选择";

                // 元素value值
                option2.value = "0";

                for (var j = 0; j < textBookList2.length; j++) {

                    addTextBook2Option(cmbTextBookid2, textBookList2[j]);

                }

                // alert(cmbTextBookid2.length);

            }

        }

    }


    //改变二级教材list数据
    function changeTextBook2() {

        // console.log("二级教材切换后索引值：", cmbTextBookid2.selectedIndex);

        if (cmbTextBookid2.selectedIndex === -1) {

            return;
        }

        if (cmbTextBookid2.selectedIndex === 0){

            //清除之前三级教材下拉数据
            clearTextBookOption(cmbTextBookid3);

            // 创建option标签元素
            var init_option = document.createElement("option");

            // 添加option到选项
            cmbTextBookid3.options.add(init_option);

            // 元素值
            init_option.innerHTML = "请选择";

            // 元素value值
            init_option.value = "0";

        }

        var c_cate_id2_id = cmbTextBookid2.options[cmbTextBookid2.selectedIndex].value;
        // console.log("c_cate_id2_id：",typeof (c_cate_id2_id));
        c_cate_id2_id = parseInt(c_cate_id2_id);
        // console.log("c_cate_id2_id：",typeof (c_cate_id2_id));
        // console.log("c_cate_id2_id：", c_cate_id2_id);

        // if (c_cate_id2_id === 0) {
        //
        //     setDefaultOption(cmbTextBookid3,c_cate_id2_id);
        //
        //
        // }

        for (var i = 0; i < textBookDataList.length; i++) {

            var textBookList2 = textBookDataList[i].bookBList;

            for (var j = 0; j < textBookList2.length; j++) {

                if (textBookList2[j].c_cate_id2_id === c_cate_id2_id) {

                    var textBookList3 = textBookList2[j].bookCList;

                    console.log("二级教材切换后展示三级教材数据：", textBookList3);

                    //清除之前三级教材下拉数据
                    clearTextBookOption(cmbTextBookid3);

                    // 创建option标签元素
                    var option = document.createElement("option");

                    // 添加option到选项
                    cmbTextBookid3.options.add(option);

                    // 元素值
                    option.innerHTML = "请选择";

                    // 元素value值
                    option.value = "0";

                    for (var k = 0; k < textBookList3.length; k++) {

                        addTextBook3Option(cmbTextBookid3, textBookList3[k]);

                    }

                }

            }
        }

    }

    //调取select数据列表
    function getSelectTextBookData() {

        $.get('/tool/open_class/api/getSelectTextBookData', {}, function (resp) {

            textBookDataList = resp.data;

            if (resp.status === 10200) {

                console.log("教材查询结果：", textBookDataList);

                for (var i = 0; i < textBookDataList.length; i++) {

                    // console.log("教材查询结果：",textBookDataList[i]);

                    addTextBook1Option(cmbTextBookid1, textBookDataList[i]);
                }

                // console.log("defaultProjectId-->",defaultProjectId);

                // 调用默认选项
                // setDefaultOption(cmbProject,defaultProjectId);

                changeTextBook1();

                cmbTextBookid1.onchange = changeTextBook1;

                changeTextBook2();

                cmbTextBookid2.onchange = changeTextBook2;

            }

            else {

                console.log("教材查询结果：", textBookDataList);

            }

        });
    };

    getSelectTextBookData();

};
