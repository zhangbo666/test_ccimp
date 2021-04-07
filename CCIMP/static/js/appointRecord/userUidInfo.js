/**
 * Created by zhangbo on 2021/3/31.
 */


function SelectJuniorTextBookData() {

    var cmbJuniorTextBookid1 = document.getElementById("j_cate_id1_id");
    var cmbJuniorTextBookid2 = document.getElementById("j_cate_id2_id");
    var cmbJuniorTextBookid3 = document.getElementById("j_cate_id3_id");
    var textJuniorBookDataList = [];


    // console.log("青少一级教材对象：",cmbJuniorTextBookid1);
    // console.log("青少二级教材对象：",cmbJuniorTextBookid2);
    // console.log("青少三级教材对象：",cmbJuniorTextBookid3);
    // console.log("初始化青少一级教材索引：",cmbJuniorTextBookid1.selectedIndex);
    // console.log("初始化青少二级教材索引：",cmbJuniorTextBookid2.selectedIndex);
    // console.log("初始化青少二级教材索引：",cmbJuniorTextBookid3.selectedIndex);

    // 每次查询后，清除青少一级教材
    clearJuniorTextBookOption(cmbJuniorTextBookid1);
    clearJuniorTextBookOption(cmbJuniorTextBookid2);
    clearJuniorTextBookOption(cmbJuniorTextBookid3);

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

    //设置一级教材下拉选项默认值
    function setDefaultOption1(cmbSetDefaultOption1) {

        // 创建option标签元素
        var text_book1_init_option = document.createElement("option");

        // 添加option到选项
        cmbSetDefaultOption1.options.add(text_book1_init_option);

        // 元素值
        text_book1_init_option.innerHTML = "请选择";

        // 元素value值
        text_book1_init_option.value = "0";

    }

    //设置二级、三级教材下拉选项默认值
    function setDefaultOption(cmbSetDefaultOption2,cmbSetDefaultOption3) {

        // 清除之前二级教材下拉数据
        clearJuniorTextBookOption(cmbJuniorTextBookid2);
        // clearJuniorTextBookOption(cmbJuniorTextBookid1);

        // 清除之前三级教材下拉数据
        clearJuniorTextBookOption(cmbJuniorTextBookid3);

        // 创建option标签元素
        // var text_book1_init_option = document.createElement("option");
        var text_book2_init_option = document.createElement("option");
        var text_book3_init_option = document.createElement("option");

        // 添加option到选项
        // cmbSetDefaultOption1.options.add(text_book1_init_option);
        cmbSetDefaultOption2.options.add(text_book2_init_option);
        cmbSetDefaultOption3.options.add(text_book3_init_option);

        // 元素值
        // text_book1_init_option.innerHTML = "请选择";
        text_book2_init_option.innerHTML = "请选择";
        text_book3_init_option.innerHTML = "请选择";

        // 元素value值
        // text_book1_init_option.value = "0";
        text_book2_init_option.value = "0";
        text_book3_init_option.value = "0";

    }

    //改变一级教材list数据
    function changeJuniorTextBook1() {

        console.log("青少一级教材切换后索引值：", cmbJuniorTextBookid1.selectedIndex);

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

                // 设置一级教材默认选项
                setDefaultOption1(cmbJuniorTextBookid1);

                // clearJuniorTextBookOption(cmbJuniorTextBookid1);

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

    getSelectJuniorTextBookData()

}







function UserUidIfon() {

    var userAppointMobile = $("[name='user_appoint_mobile']").val();

    //查询手机对应Uid

    $.ajax({
        url:'/tool/appoint_manage/api/get_user_query_uid',
        type:'POST',
        data:{'userAppointMobile':userAppointMobile},
        success:function (data)
        {
            if (data.status_code === 10101 || data.status_code === 10102 ||
                data.status_code === 10103 || data.status_code === 10104 ||
                data.status_code === 10105 || data.status_code === 10106 ||
                data.status_code === 10107) {

                alert(data.message);

                window.location.reload();

            }

            else if (data.status_code === 10200) {

                alert("当前约课用户UID为：" + data.uid + ";" +"  当前约课用户角色为：" + data.userRole + ";");

                SelectJuniorTextBookData();


            }

        }
    });

};
