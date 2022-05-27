var token = CSRF_TOKEN;
var url = window.location.pathname;

$('.nwpa').on('blur', function(events) {
  events.preventDefault();
  var c1 = $(this), c2 = c1.val();
  if(c2){
    var val = validator(c2); 
    var elemen =  c1.parent('div').next('div.form-group').find('input');
    var elemen2 =  $('.pass_all');
    val.success ? ( c1.removeClass('is-invalid'), pst_viw = true, elemen.attr('disabled', true), elemen2.attr('disabled', true)) : (c1.addClass('is-invalid'), warning_message(val.message), elemen.attr('disabled', true), pst_viw = false, elemen2.attr('disabled', true))
    if(pst_viw){
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('option', 'password_one');
      form.append('password', c2);
      $.ajax({
        type: 'POST',
        url: url,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          elemen2.removeAttr('disabled');
          elemen.removeAttr('disabled');
        } else {
          error_message(json.message)
        }
      });
    }
  }
});
$('.pass_all').on('click', function (e){
  e.preventDefault();
  pas1 = $('.nwpa').val();
  pas2 = $('.nwpa_c').val();
  var bool = pas1 && pas2 ? true : false;
  if(bool){
    if(pas1 == pas2){
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('option', 'password_all');
      form.append('password', pas1);
      form.append('password2', pas2);
      $.ajax({
        type: 'POST',
        url: url,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          $('.pass_notify').modal('show');
        } else {
          error_message(json.message)
        }
      });
    }else{
      warning_message('Las contraseñas no son iguales.')
    }
  }else{
    warning_message('Todos los * campos son obligatorios')
  }
});

$('.login').on('click', function(e){
  setTimeout(function(){location.href = url_redirect;}, 500);
});

$('.send').on('click', function (e) {
  e.preventDefault();
  eml = $('#id_email').val();
  if (true){
    var form = new FormData();
    form.append('csrfmiddlewaretoken', token);
    form.append('email', eml);
    $.ajax({
      type: 'POST',
      url: url,
      data: form,
      contentType: false,
      processData: false,
    }).done(function (json) {
      if (json.success) {
        setTimeout(function(){location.href = url_email;}, 500);
      } else {
        error_message(json.message)
      }
    });
  }else{
    warning_message('La estructura del correo electrónico no es correcta.') 
  }
});