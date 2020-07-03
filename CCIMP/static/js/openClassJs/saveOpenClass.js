/**
 * Created by zhangbo on 2020/6/25.
 */

/*保存公开课开课*/
function saveOpenClass(){

    var openClassName = document.querySelector("[name=open_class_name]").value;
    var capacityName = document.querySelector("[name=capacity_name]").value;
    var teacherName = document.querySelector("[name=c_tea_ids_name]").value;
    var costTypeName = document.querySelector("[name=cost_type_name]").value;
    var codeItemIdName = document.querySelector("[name=code_item_id_name]").value;
    var codeNumName = document.querySelector("[name=code_num_name]").value;
    var priorityName = document.querySelector("[name=priority_name]").value;
    var courseTypeName = document.querySelector("[name=course_type_name]").value;
    var bookTypeName = document.querySelector("[name=book_type_name]").value;
    var bookText1Name = document.querySelector("[name=c_cate_id1_name]").value;
    var bookText2Name = document.querySelector("[name=c_cate_id2_name]").value;
    var bookText3Name = document.querySelector("[name=book_id_name]").value;

    var openClassStartTime = document.querySelector("[name=start_time]").value;
    var openClassEndTime = document.querySelector("[name=end_time]").value;

//        alert(openClassName);
//        alert(capacityName);
//        alert(teacherName);
//        alert(costTypeName);
//        alert(codeItemIdName);
//        alert(codeNumName);
//        alert(priorityName);
//        alert(courseTypeName);
//        alert(bookTypeName);
//        alert(bookText1Name);
//        alert(bookText2Name);
//        alert(bookText3Name);
//        alert(openClassStartTime);
//        alert(openClassEndTime);

    if(openClassName === ''){

        alert("公开课名称为空!");
        return;
    }

    if(capacityName === ''){

        alert("公开课上课人数为空!");
        return;

    }

    if(teacherName === '0'){

        alert("公开课老师未选择!");
        return;

    }

    if( costTypeName === "free" && codeItemIdName === "19" ||
        costTypeName === "free" && codeItemIdName === "1" ||
        costTypeName === "free" && codeItemIdName === "15"){

        alert("免费公开课必须对应免费商品类型!");
        return;

    }

    else if(costTypeName === "class_time" && codeItemIdName === "14" ||
            costTypeName === "point" && codeItemIdName === "14" ||
            costTypeName === "money" && codeItemIdName === "14"){

        alert("付费公开课必须对应付费商品类型!");
        return;

    }

    if (costTypeName === "class_time"){

        if (codeItemIdName !== "19"){

            alert("课时公开课必须对应课时商品类型!");
            return;

        }

    }

    else if(costTypeName === "point"){

        if(codeItemIdName !== "1"){

            alert("次卡公开课必须对应次卡商品类型!");
            return;

        }
    }

    else if(costTypeName === "money"){

        if(codeItemIdName !== "15"){

            alert("现金公开课必须对应现金商品类型!");
            return;

        }
    }

    if(codeItemIdName === "19" || codeItemIdName === "1" || codeItemIdName === "15"){

        if(codeNumName === '0'){

            alert("付费公开课财富量不能为空");
            return;
        }

    }

    if(bookText1Name === "0"){

        alert("一级教材未选择!");
        return;
    }
    else if(bookText2Name === "0"){

        alert("二级教材未选择!");
        return;
    }
    else if(bookText3Name === "0"){

        alert("三级教材未选择!");
        return;
    }

    if(openClassStartTime === ""){

        alert("公开课开始时间为空!");
        return;
    }
    else if(openClassEndTime === ""){

        alert("公开课结束时间为空!");
        return;
    }

    var startTime = openClassStartTime;
    var endTime   = openClassEndTime;

    var startTime_replace = startTime.replace(/\-/g,'/');
    var endTime_replace = endTime.replace(/\-/g,'/');

    var startTime_unix = Date.parse(startTime_replace);
    var endTime_unix = Date.parse(endTime_replace);

    if(startTime_unix >= endTime_unix){

        alert("公开课开始时间必须小于结束时间!");
        return;

    }

    msg_confirm = confirm("确定创建该节公开课吗？");

    if(msg_confirm === true) {

        //公开课开课接口
        $.ajax({
            url: '/tool/open_class/open_class_add/',
            type: 'POST',
            data: {
                'openClassName': openClassName,
                'capacityName': capacityName,
                'teacherName': teacherName,
                'costTypeName': costTypeName,
                'codeItemIdName': codeItemIdName,
                'codeNumName': codeNumName,
                'priorityName': priorityName,
                'courseTypeName': courseTypeName,
                'bookTypeName': bookTypeName,
                'bookText1Name': bookText1Name,
                'bookText2Name': bookText2Name,
                'bookText3Name': bookText3Name,
                'openClassStartTime': openClassStartTime,
                'openClassEndTime': openClassEndTime
            },
            success: function (data) {

                if (data.status === 200) {

                    alert(data.message);
                    window.location.replace("/tool/open_class/");

                }

                else if (data.status === 10000 || data.status === 10001 || data.status === 10002 || data.status === 10003) {

                    alert(data.message);

                }

            }
        });
    }
}
