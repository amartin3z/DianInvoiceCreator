/**
 * Function to display a message to the user. The message is styled 
 * in colors and icons according to its type.
 * @param {String} message: The message to display.
 * @param {String} type: The type of message to display.
 */


  var div = document.getElementById('wis-message');
  var interval = setInterval(function(message){
    $.ajax({
      url: '/app/session/verify/',
      type: 'post',
      data: {
        action: 'check_session_timeout'
      },
      dataType: 'json',
      success: function(data) {
        if (data.success) {
          if (data.message != '') {
            $('#wis-message').html('<strong>¡Importante! </strong> ' + data.message);
            div.style.display = '';
          }
        } else {
          window.location = '/logout/';
        }
        
      },
      error: ()=>{
        clearInterval(interval);
        $('#inactividad-session').modal('show');
      }
    })
  }, 30000);
  // }, 60000);

  document.querySelector('#seccion_close').addEventListener('click', ()=>{
    window.location = '/logout/';
  }, false)


//var showMessage = function(message, type) {
//    if (!message) {
//      alert(gettext('The message could not be show because no message text was given'));
//      return false;
//    }
//    if (!type) {
//      type = 'info';
//    }
//    $('#wis-message').html(message);
//    //$('#wis-message').removeClass()
//    //    .addClass(type + '-message')
//    //    .show();
//  }
//var showWarningMessage = function(message) {
//    showMessage(message);
//}

//var hideMessage = function() {
//$('#wis-message .wis-message-text').html('');
//$('#wis-message').removeClass().hide();
//}