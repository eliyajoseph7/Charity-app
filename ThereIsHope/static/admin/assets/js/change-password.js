$(document).ready(function(){
    $('#password-form input[type="password"]').blur(function(){
        if(!$(this).val()){
            $(this).addClass("err");
        } else{
            $(this).removeClass("err");
        }
    });

    $('#changePassword').click(function(e){
        $('#info').text('');
        $('#currPass').text('');
        $('#conferror').text('');
        $('#passerror').text('');
        e.preventDefault()

        var fail = false;
        var fail_log = '';
        var name;

        $('#password-form').find('input').each(function(){
            if(! $(this).prop('required')) {

            }else {
                if(! $(this).val()){
                    fail = true;
                    name = $(this).attr('name');
                    fail_log += '<p>' + name + ' is required!</p>';
                }
            }
        });


        // Submit iffail is false

        if(! fail){
            var full_url = document.URL; // Get current url
            var url_array = full_url.split('/'); // Split the string into an array with / as separator
            var id = url_array[url_array.length-1];  // Get the last part of the array (-1)
            $.ajax({
                headers: { "X-CSRFToken": $.cookie("csrftoken") },
                type: 'POST',
                url: 'updatePassword/'+ id,
                data: $('#password-form').serialize(),

                success:function(data){
                    $('#currPass').text(data.mismatch);
                    $('#conferror').text(data.confError);
                    $('#passerror').text(data.passError);

                    if($('#currPass').text().length == 0 &&  $('#conferror').text().length == 0 && $('#passerror').text().length == 0)
                    {
                        $('#msg').text(data.success);
                        $('.success').show();
                        $('#password-form').find('input').val('');
                        
                    }
                        $('.error').hide();
                        $('#closeSuccess').click(function (){
                            $('.success').hide();
                            $('#msg').text('');
                        });
                },
                error:function(error){
                    console.log(error);
                    $('#info').text(error.statusText + ', contact the administrator for help');
                    $('.error').show();
                    $('.success').hide();

                    $('#closeError').click(function(){
                        $('.error').hide();
                        $('#info').text('');
                    });
                }
            });
        }
        else {
            $('#info').html(fail_log);
            $('.error').show();
            $('.success').hide();

            $('#closeError').click(function(){
                $('.error').hide();
                $('#info').text('');
            });
        }
    });
});