$(".btn-insert-data").click(function(){
	var name = $("#ins_name").val();
	var email = $("#ins_email").val();
	var gender = $("#ins_gender").val();
	if(name == " "){
		$("#ins_error").text("Please Enter Name")
		$("#ins_error").show()
		return;
	}
	else if(email == " "){
		$("#ins_error").text("Please Enter Email")
		$("#ins_error").show()
		return;
	}
	else{
		$(".btn-insert-data").attr("disabled","disabled");
		$(".btn-insert-data").text("Inserting....Please Wait...");
		$.ajax({
			url:"InsertStudent/",
			type:'POST',
			data:{name:name,email:email,gender:gender}
		})
		.done(function(response){
			if (response['error'] == false){
				$('#ins_error').hide();
				$("#ins_success").text(response['errorMessage']);
				$('#ins_success').show();
				var html_data = "<tr><td>"+response['id']+"</td><td class='editable' data-type='name'>"+name+"</td><td class='editable' data-type='email'>"+email+"</td><td class='editable' data-type='gender'>"+gender+"</td><td>"+response['created_at']+"</td><td class='btn td-block'><button class='btn btn-block btn-delete btn-danger'>Delete</button></td><tr>";
				$(".table tbody").append(html_data);
			}
			else{
				$('#ins_success').hide();
				$('#ins_error').text(response['errorMessage']);
				$('#ins_error').show();
			}
		})
		.fail(function(response){
			$('#ins_success').hide();
			$('#ins_error').text("Something went wrong !");
			$('#ins_error').show();
		})
		.always(function(){
			$(".btn-insert-data").removeAttr("disabled");
			$(".btn-insert-data").text("Insert Student");
		})
	}
})

$("#update_btn").click(function(){
	$("#update_btn").hide();
	$("#save_all_btn").show();
	$(".editable").each(function(){
		$("#update_btn").hide();
		$("#save_all_btn").show();
		var value = $(this).text();
		var types = $(this).data('type');
		if(types!='gender'){
			var html_data = "<input type='text' name='"+types+"' class='form-control input_"+types+" input_data' value='"+value+"'>";
			$(this).html(html_data);
		}
		else{
			var html_data = "<select name='"+types+"' class='form-control input_"+types+" input_data'>";
			if(value == "Male"){
				html_data += "<option selected>Male</option><option>Female</option>"
			}
			else{
				html_data += "<option>Male</option><option selected>Female</option>";
			}
			html_data += "</select>";
			$(this).html(html_data);	
		}
	})
})

$("#save_all_btn").click(function(){
	$("#save_all_btn").attr("disabled","disabled");
	$("#save_all_btn").text("Saving Data....");
	var json_data = [];
	$(".input_data").each(function(){
		//console.log($(this).val())
		var value = $(this).val();
		var parent_html = $(this).parent();
		parent_html.html(value);
		$(this).remove();
	});
	$("tbody tr").each(function(){
		var id = $(this).children().eq(0).text()
		var name = $(this).children().eq(1).text()
		var email = $(this).children().eq(2).text()
		var gender = $(this).children().eq(3).text()
		console.log(gender)

		var single_data = {"id":id,"name":name,"email":email,"gender":gender};
		json_data.push(single_data);
});

var string_data = JSON.stringify(json_data)
$.ajax({
			url:"update_all/",
			type:'POST',
			data:{data:string_data}
		})
		.done(function(response){
			if (response['error'] == false){
				$('#upt_error').hide();
				$("#upt_success").text(response['errorMessage']);
				$('#upt_success').show();
			}
			else{
				$('#upt_success').hide();
				$('#upt_error').text(response['errorMessage']);
				$('#upt_error').show();
			}
		})
		.fail(function(response){
			$('#upt_success').hide();
			$('#upt_error').text("Something went wrong !");
			$('#upt_error').show();
		})
		.always(function(){
			$("#save_all_btn").removeAttr("disabled");
			$("#save_all_btn").text("Save");
			$("#update_btn").show();
			$("#save_all_btn").hide();
		})
})

$(document).on("click",".btn-delete",function(){
	var this_html = $(this);
	this_html.attr("disabled","disabled");
	this_html.text("Deleting....");
	var id = this_html.parent().parent().children().first().text();
	$.ajax({
			url:"delete_data/",
			type:'POST',
			data:{id:id}
		})
		.done(function(response){
			if (response['error'] == false){
				$('#upt_error').hide();
				$("#upt_success").text(response['errorMessage']);
				$('#upt_success').show();
			}
			else{
				$('#upt_success').hide();
				$('#upt_error').text(response['errorMessage']);
				$('#upt_error').show();
			}
		})
		.fail(function(response){
			$('#upt_success').hide();
			$('#upt_error').text("Something went wrong !");
			$('#upt_error').show();
		})
});