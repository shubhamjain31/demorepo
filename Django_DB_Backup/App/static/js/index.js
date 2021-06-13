 // create backup function
 function user_backup(_id){

  $.ajax(
  {
      type:"POST",
      url: "/create_backup/",
      data:{
            '_id':_id
      },
      success: function( data ) 
      {
          var msg = data["msg"];
          alert(msg);
      }
    })
}

 // restore backup function
 function user_restore_backup(_id){

  $.ajax(
  {
      type:"POST",
      url: "/restore_backup/",
      data:{
            '_id':_id
      },
      success: function( data ) 
      {
          var msg = data["msg"];
          alert(msg);
      }
    })
}