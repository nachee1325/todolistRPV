var globalID;

//validateInput
	function validateCode(id){
    var TCode = document.getElementById(id).value;
    if( /[^a-zA-Z0-9_ ]/.test( TCode ) ) {
       alert('Input is not alphanumeric.')
       return false;
    }
    else if(TCode == "")
    {
        alert('Input is required.')
    }
    return true;
 }

//get Data for Edit Modal
	var $task = $('#taskEdit');
	var $due = $('#dueEdit');
	function getData(id){
	    var e = document.getElementById("sid");
		e.id = id;
		globalID = id;
		$.getJSON('/_get_data',{taskID:id},function(data){
			$('#taskEdit').val(data.result[id].task);
			$('#dueEdit').val(data.result[id].due);

			return(e.id)
	});
}

//Display Data in Table
    function getTable(){
    	var table = document.getElementById("executeTable");
    	$.getJSON('/_get_table',{},function (data){

    		while(table.rows.length > 1){
    			table.deleteRow(1);
    		}
       	    for(var i = 0 ; i < data.jsonn.length ; i++){
							tr = $('<tr/>');
							tr.append('<td>' + data.jsonn[i].task +'</td>')
							tr.append('<td>' + data.jsonn[i].due +'</td>')
							tr.append('<td>' + '<a href="#openModal"><input name = "btnEdit" type="button" onclick="getData(this.id)" value="Edit" id='+i+'>' + '</td></a>')
							tr.append('<td>' + '<input name = "btnDelete" type="button" onclick="deleteTask(this.id)" value="Delete" id='+i+'>' + '</td>')
						$("#executeTable").append(tr);
					}
    		});


    	return false;
	}

//Refresh Things
function RefreshTable() {
       $( "#executeTable" ).load( "index.html #executeTable" );
   }

    $("btnDelete").on("click", RefreshTable);
    $("btnSave").on("click", RefreshTable);
    $("btnAdd").on("click", RefreshTable);
    $("btnEdit").on("click", RefreshTable,resetID(this.id));
    $("btnCancel").on("click", RefreshTable,resetID(this.id));
    $("x").on("click", RefreshTable,resetID(this.id));

// Delete Task
	function deleteTask(id) {
		$.getJSON('/_delete_task',{taskID:id}, function(data){
        	getTable();
		});

	}

//Edit task
	function editTask(id) {
		if (validateCode('taskEdit')){
		$.getJSON('/_edit_task',{taskID:globalID,task:$('input[name = "txtEditTitle"]').val(),due:$('input[name = "txtEditDate"]').val()}, function(data){
		});
		alert('Successfully saved!')
		getTable();}
		else{
			alert('Unable to edit task. Please check your input.')
		}
	}
//Add Task
	function myFunction() {

		if(validateCode('task')){
		$.getJSON('/_add_task',{task: $('input[name = "txtTitle"]').val(), due: $('input[name = "txtDate"]').val()}, function(data){
			$("#result").text(data.result);
			alert('Successfully Saved!')
			getTable();
			$("#task").val("");
			$("#due").val("");
			});

	}
	else{
		alert('Unable to save task. Please check your input.')
	}
    }

	function resetID(id){
		var e = document.getElementById(id);
		e.id = "sid";

	}
