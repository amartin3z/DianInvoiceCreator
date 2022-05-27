var token = CSRF_TOKEN;
var url = 'options/';

//fiscal data
$('.edit_fiscaldata').on('click', function (event) {
  event.preventDefault();
  $('#pills-fiscal div.fiscal input, select').removeAttr('disabled');
  $('#pills-fiscal div.fiscal input.disabled, select.disabled').attr('disabled', true);
  $(this).hide();
  $('.save_fiscaldata').show();
  $('.cancel_fiscaldata').show();
});

$('.cancel_fiscaldata').on('click', function (event) {
  event.preventDefault();
  $('#data_fiscal div.has-error').removeClass('has-error');
  $('#pills-fiscal div.fiscal input, select').attr('disabled', true);
  $('.edit_fiscaldata').show();
  $('.save_fiscaldata').hide();
  $(this).hide();
  cancel_btn(container);
});

$('.save_fiscaldata').on('click', function (event) {
  event.preventDefault();
  
  var name_company = $('#name_company').val();
  // var tax_regime = $('#tax_regime').val();
  var email = $('#email').val();
  var phone = $('#phone').val();
  var country = $('#country').val();
  var states = $('#states').val();
  var locality = $('#locality').val();
  var zipcode = $('#zipcode').val();
  // var municipality = $('#municipality').val();
  // var town = $('#town').val();
  var street = $('#Street_name').val();

  var schemeID = $('#schemeID').val();
  var organization_id = $('#organization_id').val();
  var seller_elect_address = $('#s_e_a').val();

  // var street_aditional = $('#Additional_StreetName').val();
  // var address_line = $('#address_line').val();
  
  var ext_num = $('#external_number').val();
  var int_num = $('#internal_number').val();

  var form = new FormData();
  form.append('csrfmiddlewaretoken', token);
  form.append('option', 'upd_fisdata');
  form.append('name_company', name_company);
  // form.append('tax_regime', tax_regime);
  form.append('country', country);
  form.append('email', email);
  form.append('phone', phone);
  form.append('states', states);
  form.append('locality', locality);
  // form.append('municipality', municipality);
  // form.append('town', town);
  form.append('street', street);
  form.append('zipcode', zipcode);  
  // form.append('street_aditional', street_aditional);
  // form.append('address_line', address_line);
  
  form.append('schemeID', schemeID);
  form.append('organization_id', organization_id);
  form.append('seller_elect_address', seller_elect_address);

  form.append('ext_num', ext_num);
  form.append('int_num', int_num);

  var vals = validation()
  if (vals.success) {
    var success = true;
    if (email) {
      success = validate_email(email)
    }
    if (success) {
      if(__address__().success){
        $.ajax({
          type: 'POST',
          url: PROFILE_OPTIONS,
          data: form,
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false,
        }).done(function (json) {
          if (json.success) {
            success_message('Actualizados correctamente.');
            setTimeout(function(){location.reload(1);}, 2000);
            $('#pills-fiscal div.container input, select').removeAttr('disabled');
            $(this).hide();
            $('.save_fiscaldata').show();
            $('.cancel_fiscaldata').show();        
          } else {
            error_message(json.message)
          }
        });
      }else{
        warning_message(__address__().message)
      }
    } else {
      warning_message('La estructura del correo electronico es erronea.')
    }
  }
});

//password
$('#new_password').on('keyup', function (event) {
  event.preventDefault();
  keyup_pass($(this).val());
})

$('#new_password_confirm').on('keyup', function (event) {
  event.preventDefault();
  if ($(this).val() !== $('#new_password').val()) {
    $('div.confirm span.confirm').addClass('val_danger');
  } else {
    $('div.confirm span.confirm').removeClass('val_danger');
  }
});

$('.pass_update').on('click', function (event) {
  event.preventDefault();
  $('#pills-settings div.pass input').removeAttr('disabled', true);
  $(this).hide();
  $('.save_pass').show();
  $('.cancel_pass').show();
  $('div.validation .number, .length, .capital, .tiny, .character').addClass('text-danger');
});

$('.cancel_pass').on('click', function (event) {
  event.preventDefault();
  $('div.pass').parent().closest('div').removeClass('has-error');
  $('#pills-settings div.pass input').attr('disabled', true).val('');
  $('div.pass div.has-error').removeClass('has-error');
  $('.pass_update').show();
  $('.save_pass').hide();
  $(this).hide();
  $('div.validation .number, .length, .capital, .tiny, .character, .space').removeClass('text-danger').removeClass('val_success');
  $('div.confirm span.confirm').removeClass('val_danger');
});

$('.save_pass').on('click', function (event) {
  event.preventDefault();
  var last_pass = $('#last_password').val();
  var pass1 = $('#new_password').val();
  var pass2 = $('#new_password_confirm').val();
  if (empty_password().success) {
    var val = pass_validations(pass1, pass2);
    if (val.success) {
      if (pass1 != last_pass) {
        var form = new FormData();
        form.append('csrfmiddlewaretoken', token);
        form.append('pass1', pass1);
        form.append('pass2', pass2);
        form.append('last_pass', last_pass);
        form.append('option', 'upd_pass');
        $.ajax({
          type: 'POST',
          url: PROFILE_OPTIONS,
          data: form,
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false,
        }).done(function (json) {
          if (json.success) {
            // success_message('¡Contraseña Actualizada!, Debe ingresar al sistema nuevamente, el cambio de contraseña cerrar la sesión en todos los dispositivos.');
            $('#pills-settings div.container input').attr('disabled', true).val('');
            $('.pass_update').show();
            $('.cancel_pass').hide();
            $('.password_notify').modal('show');
            $(this).hide();
            // setTimeout(function(){location.reload(1);}, 5000);
            // location.reload();
          } else {
            $('div.pass').parent().closest('div').addClass('has-error');
            error_message(json.message)
          }
        });
      } else {
        warning_message('La contraseña no debe ser la misma que la anterior.')
      }
    } else {
      warning_message(val.message)
    }
  }
});

$('.pass_acept_n').on('click', function (e) {
  e.preventDefault();
  location.reload();
});

//logo
$('.btn_edit_logo').click(function (e) {
  modals_editserie({
    'title':'Selecciona el logotipo',
    'text': '',
    'id': 'newlogo',
    'attr': 'file',
    'bsucces': 'succes_logo'
  });
});

$('.btn_acept').on('click', function (events) {
  var id_butt = $(this).attr('id');
  events.preventDefault();
  if(id_butt == 'succes_logo'){
    var newlogo = $('#newlogo')[0].files[0];
    if (newlogo) {
      img_format_ = img_format(newlogo.name);
      if (img_format_.success) {
        var data = new FormData();
        data.append('option', 'edit_logo');
        data.append('logo', newlogo);
        data.append('csrfmiddlewaretoken', token);
        $.ajax({
          type: 'POST',
          url: PROFILE_OPTIONS,
          data: data,
          contentType: false,
          processData: false,
        }).done(function (json) {
          if (json.success) {
            success_message('Imagen Actualizada con exito');
            $('.img_logo').attr('src', json.object + '?' + new Date().getTime());
            var modal = $('div.modal_series');
            modal.find('input').val('');
            modal.modal('hide');
          } else {
            error_message(json.message)
          }
        });
      } else {
        warning_message("El archivo seleccionado no corresponde a ninguna extencion permitida: JPG, PNG, JPGE.")
      }
    } else {
      warning_message("No seleccionaste ninguna imagen")
    }
  }else if (id_butt ==  'successs_series'){
    var attr2 = $(this).attr('data1');
    var new_folio = $('#series_edit').val();
    if(new_folio) {
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('option', 'edit_serie');
      form.append('data1', attr2);
      form.append('data2', new_folio);
      $.ajax({
        type: 'POST',
        url: PROFILE_OPTIONS,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          success_message('El folio de la serie actualizo de manera correcta.')
          $('#dt_serie').DataTable().ajax.reload();
          var modal = $('div.modal_series'); 
          modal.find('input').val('');
          modal.modal('hide');
        } else {
          error_message(json.message)
        }
      });
    } else {
      warning_message('No puedo ingresar datos vacios.')
    }
  }
});

// //email
// $('.new_mails').on('click', function (event) {
//   event.preventDefault();
//   $(this).hide();
//   $('div.div_add input').removeAttr('disabled')
//   $('div.div_add button.hiddem').show();
// });

// $('.cancel_mails').on('click', function (event) {
//   event.preventDefault();
//   $('div.div_add input').attr('disabled', true).val('');
//   $('div.div_add button.hiddem').hide();
//   $('.new_mails').show();
// });

$('div.div_mail span.btn-reset_email').on('click', function (event) {
  event.preventDefault();
  $('div.div_add input').val('');
});

$('.add_mails').on('click', function (event) {
  event.preventDefault();
  var email = $('div.div_mail input').val();
  if (validate_email(email) && email !== '') {
    var form = new FormData();
    form.append('csrfmiddlewaretoken', token);
    form.append('option', 'add_emails');
    form.append('email', email);
    $.ajax({
      type: 'POST',
      url: PROFILE_OPTIONS,
      data: form,
      contentType: false,
      processData: false,
    }).done(function (json) {
      if (json.success) {
        success_message('El correo se agrego de manera correcta.');
        $('div.div_mail input').val('');
        // $('div.div_add input').attr('disabled', true).val('');
        // $('div.div_add button.hiddem').hide();
        // $('.new_mails').show();
        $('#dt_email').DataTable().ajax.reload();
      } else {
        error_message(json.message)
      }
    });
  } else {
    warning_message("La estructura del correo electronico es erronea.")
  }
});

$(document).on("click", "#delect_email", function (event) {
  event.preventDefault();
  var email = $(this).attr('data');
  var form = new FormData();
    form.append('csrfmiddlewaretoken', token);
    form.append('option', 'delect_email');
    form.append('email', email);
    $.ajax({
      type: 'POST',
      url: PROFILE_OPTIONS,
      data: form,
      contentType: false,
      processData: false,
    }).done(function (json) {
      if (json.success) {
        success_message('El correo se elimino de manera correcta.');
        $('#dt_email').DataTable().ajax.reload();
      } else {
        error_message(json.message)
      }
    });
});

$(document).on("click", "#edit_email", function(event) {
  event.preventDefault();
  var last_email = $(this).attr('data');
  var elemt = $('.notify_edit');
  elemt.modal('show');
  elemt.find('h2.title').text('Modificación');
  elemt.find('h4.text').text('del correo '+ last_email);
  $('.notify_edit input.input_content').val(last_email).addClass('text-center');
});

$('.notify_edit button.successs').on('click', function(event){
  event.preventDefault();
  var last_email = $('#edit_email').attr('data');
  var new_email = $('.notify_edit input.input_content'); 
  if(new_email.val()){
    if(validate_email(new_email.val())){
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('sub', 'edit');
      form.append('option', 'add_emails');
      form.append('email', last_email);
      form.append('new_email', new_email.val());
      $.ajax({
        type: 'POST',
        url: PROFILE_OPTIONS,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          success_message('El correo se actualizo de manera correcta.');
          $('.notify_edit').modal('hide');
          new_email.val('').addClass('text-center');
          $('#dt_email').DataTable().ajax.reload();
        } else {
          error_message(json.message)
        }
      });  
    }else{
      warning_message("La estructura del correo electronico es erronea.")
    }
  }else{
    warning_message("No puedo ingresar datos vacios.")
  }
});

$('.notify_edit button.cancels').on('click', function(event){
  event.preventDefault();
  $('.notify_edit').modal('hide');
  $('.notify_edit input.input_content').val(''); 
});

//csd
$('.add_csd').on('click', function (event) {
  event.preventDefault();
  var Key = $('#add_csd_0')[0].files[0];
  var Cer = $('#add_csd_1')[0].files[0];
  var pass = $.trim($('input.pass').val());
  if (empty_csd().success) {
    var ext_cer = exts_cer(Cer.name);
    var ext_key = exts_key(Key.name);
    if (ext_cer.success && ext_key.success) {
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('cer', Cer);
      form.append('key', Key);
      form.append('pass', pass);
      form.append('option', 'add_csd');
      $.ajax({
        type: 'POST',
        url: PROFILE_OPTIONS,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          success_message('El certificado se agrego exitosamente.');
          $('div.contents').hide().find('input').val('');
          $('div.btns').find('button').hide();
          $('div.btns').find('button.new_csd').show();
          $('#dt_csd').DataTable().ajax.reload();
        } else {
          $('div.contents').find('input').each(function () { $(this).parent().closest('div').addClass('has-error'); });
          error_message(json.message)
        }
      });
    } else {
      var message = 'El archivo debe ser de tipo .cer .key', success = ext_cer.message && ext_key.message ? false : true;
      success ? (message = !ext_cer.message ? message = ext_key.message : message = ext_cer.message) : message;
      warning_message(message)
    }
  }
});

$(document).on("click", "#default", function (event) {
  event.preventDefault();
  var attr1 = $(this).attr('data_0');
  var attr2 = $(this).attr('data_1');
  var elemt = $(this).attr('serial');
  var form = new FormData();
  form.append('csrfmiddlewaretoken', token);
  form.append('option', 'csd_default');
  form.append('data0', attr1);
  form.append('data1', attr2);
  $.ajax({
    type: 'POST',
    url: PROFILE_OPTIONS,
    data: form,
    contentType: false,
    processData: false,
  }).done(function (json) {
    if (json.success) {
      success_message('Se establecio correctamente el certificado.');
      $('#dt_csd').DataTable().ajax.reload();
    } else {
      error_message(json.message)
    }
  });
});

//series
$('.add_serie').on('click', function (event) {
  event.preventDefault();
  var serie = $('.serie').val();
  var folio = $('.folio').val();
  var length = serie_and_folio_length()
  if (empty_series().success) {
    if(length.success1 && length.success2){
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('folio', folio);
      form.append('serie', serie);
      form.append('option', 'add_serie');
      $.ajax({
        type: 'POST',
        url: PROFILE_OPTIONS,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        var elements_div = $('div.contents_serie');
        if (json.success) {
          success_message('La serie se agrego exitosamente.');
          elements_div.hide().find('input').val('');
          var elements_buttons = $('div.btns_series');
          elements_buttons.find('button').hide();
          elements_buttons.find('button.new_serie').show();
          $('#dt_serie').DataTable().ajax.reload();
        } else {
          error_message(json.message)
          elements_div.find('input').each(function () { $(this).parent().closest('div').addClass('has-error'); });
        }
      });
    }else{
      var message = length.success1 ? 'El Folio solo puede tener 40 caracteres.' : 'La serie solo puede tener 25 caracteres.';
      warning_message(message)   
    } 
  }
});

$(document).on("click", "#defecto_serie", function (event) {
  event.preventDefault();
  var attr1 = $(this).attr('data0');
  var attr2 = $(this).attr('data1');
  var elemt = $(this).attr('serie');
  var form = new FormData();
  form.append('csrfmiddlewaretoken', token);
  form.append('option', 'default_serie');
  form.append('data0', attr1);
  form.append('data1', attr2);
  $.ajax({
    type: 'POST',
    url: PROFILE_OPTIONS,
    data: form,
    contentType: false,
    processData: false,
  }).done(function (json) {
    if (json.success) {
      success_message('Se establecio correctamente la serie.')
      $('#dt_serie').DataTable().ajax.reload();
    } else {
      error_message(json.message)
    }
  });
});

$(document).on("click", "#deactive_serie", function (event) {
  event.preventDefault();
  var attr1 = $(this).attr('data0');
  var attr2 = $(this).attr('data1');
  var elemt = $(this).attr('serie');
  var form = new FormData();
  form.append('csrfmiddlewaretoken', token);
  form.append('option', 'activ/deact');
  form.append('optionsub', 'deactivate');
  form.append('data0', attr1);
  form.append('data1', attr2);
  
  $.ajax({
    type: 'POST',
    url: PROFILE_OPTIONS,
    data: form,
    contentType: false,
    processData: false,
  }).done(function (json) {
    if (json.success) {
      success_message('Se desactivo la serie correctamente.')
      $('#dt_serie').DataTable().ajax.reload();
    } else {
      error_message(json.message)
    }
  });
});

$(document).on("click", "#activar_serie", function (event) {
  event.preventDefault();
  var attr1 = $(this).attr('data0');
  var attr2 = $(this).attr('data1');
  var elemt = $(this).attr('serie');
  var form = new FormData();
  form.append('csrfmiddlewaretoken', token);
  form.append('option', 'activ/deact');
  form.append('data0', attr1);
  form.append('data1', attr2);
  $.ajax({
    type: 'POST',
    url: PROFILE_OPTIONS,
    data: form,
    contentType: false,
    processData: false,
  }).done(function (json) {
    if (json.success) {
      success_message('Se activo la serie correctamente.')
      $('#dt_serie').DataTable().ajax.reload();
    } else {
      error_message(json.message)
    }
  });
});

$(document).on("click", "#edit_serie", function (event) {
  event.preventDefault();
  var attr2 = $(this).attr('data1');
  var elemt = $(this).attr('serie');
  var last_folio = $(this).attr('folio');
  modals_editserie({
    'title':'Modificación',
    'text': 'del folio de la serie ' + elemt,
    'id': 'series_edit',
    'last_folio': last_folio,
    'data1':attr2,
    'attr': 'text',
    'bsucces': 'successs_series'
  });
});

$('.delete_account').on('click', function(events){
  events.preventDefault();
  $('.form_DelecteAccount').modal('show');
});

//in proccess
$('.desactivate').on('click', function(events) {
  events.preventDefault();
  var why_account = $('.the_why').val();
  var name = $('.name_account').val();
  var email = $('.email_account').val();
  var phone = $('.phone_account').val();
  var empty = input_deleteaccount()
  if(empty.success){
    var succ_email =  email ? validate_email(email) : true; 
    if(succ_email){
      var form = new FormData();
      form.append('csrfmiddlewaretoken', token);
      form.append('option', 'add_ticket');
      form.append('why_account', why_account);
      form.append('name', name);
      form.append('email', email);
      form.append('phone', phone);
      $.ajax({
        type: 'POST',
        url: PROFILE_OPTIONS,
        data: form,
        contentType: false,
        processData: false,
      }).done(function (json) {
        if (json.success) {
          success_message('Solicitud enviada');
          $('.form_DelecteAccount').modal('hide');
          $('.form_DelecteAccount div.info_contact').find('input, textarea').val('');
          setTimeout(function(){location.reload(1);}, 2000);
        } else {
          error_message(json.message)
        }
      });
    }else{
      warning_message('La estructura del email es correcta.');
    }

  }else{
    warning_message(empty.message);
  }
});


// blur_change();
// function blur_change(){
//   var elemt = $('div.fiscal').find('input.not_only_numbers').each(function(event){
//     $(this).on('blur', function (e) {
//       __address__();
//     }); 
//   });
// }

