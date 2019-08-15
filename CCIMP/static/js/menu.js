$(document).ready(function() {

//document.getElementById('div11').style.display="block";

//绑定元素点击事件
$(".menu_list ul li").click(function() {

	//判断对象是显示还是隐藏
	if($(this).children(".div1").is(":hidden")){
		//表示隐藏
		if(!$(this).children(".div1").is(":animated")) {

			$(this).children(".xiala").css({'transform': 'rotate(360deg)'});
			//如果当前没有进行动画，则添加新动画
			$(this).children(".div1").animate({
					height: 'show'
				}, 200)
				//siblings遍历div1的元素
				.end().siblings().find(".div1").hide(200);
		}

	} else {
		//表示显示
		if(!$(this).children(".div1").is(":animated")) {

			$(this).children(".xiala").css({'transform': 'rotate(360deg)'});
			$(this).children(".div1").animate({
				height: 'hide'
			}, 200)
				.end().siblings().find(".div1").hide(200);

		}
	}
});

//阻止事件冒泡，子元素不再继承父元素的点击事件
$('.div1').click(function(e){
	e.stopPropagation();
});

//点击子菜单为子菜单添加样式，并移除所有其他子菜单样式
$(".menu_list ul li .div1 a .zcd span").click(function() {
	//设置当前菜单为选中状态的样式，并移除同类同级别的其他元素的样式
	$(this).addClass("removes").siblings().removeClass("removes");
	//遍历获取所有父菜单元素
	  $(".div1").each(function(){
	  		//判断当前的父菜单是否是隐藏状态
	  		if($(this).is(":hidden")){
	  			//如果是隐藏状态则移除其样式
	  			$(this).children(".zcd").removeClass("removes");
		  		}
	  });
	});
});
