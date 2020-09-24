$(document).ready(function (){ 
    
    $('#submit').click(function (e){
        $('#message').text('');
        e.preventDefault()
        // $("input").prop('required',true);
          //validate fields
          var fail = false;
          var fail_log = '';
          var name;
          $( '#create-portfolio' ).find( 'select, textarea, input' ).each(function(){
              if( ! $( this ).prop( 'required' )){
  
              } else {
                  if ( ! $( this ).val() ) {
                      fail = true;
                      name = $( this ).attr( 'name' );
                      fail_log += '<p>' +name + " is required \n"+ '</p>';
                  }
  
              }
          });
  
          //submit if fail never got set to true
          if ( ! fail ) {
                $.ajax({
                    headers: { "X-CSRFToken": $.cookie("csrftoken") },
                    type: 'POST',
                    url: 'createPortfolio',
                    data: $('#create-portfolio').serialize(),
        
                    success:function(data){
                        console.log(data);
                        $('#message').text(data);
                        $('.success').show();
                        $('.error').hide();
                        $('#create-portfolio').find("input, textarea, select").val("");
                        
                        $('#btn').click(function(){
                            $('#message').text('');
                            $('.success').hide();
                        });
                        // $('.dt').ajax.reload(null, false);
                    },
                    error:function(error){
                        console.log(error);
                    }
                });
            } else {
                    $('#error').html(fail_log);
                    $('.error').show();
                    $('.success').hide();
                    
                    $('#btn2').click(function(){
                        $('#error').text('');
                        $('.error').hide();
                    });
                // alert( fail_log );
            }
    });
});