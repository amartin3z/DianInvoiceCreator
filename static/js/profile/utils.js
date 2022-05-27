// ======  funciones de acciones  ======== //
$(function() {
  bs_input_file();
  input_pass();
  buttons();
  form_delecteaccount();

  $('#perfil').addClass('active');
});
// ======  funciones de acciones  ======== //

var container = get_info();
function get_info(){
  var data = [];
  $('div[id^="data_"]').find('input, select').each(function(){ 
    data.push($(this).attr('id')+':'+ $(this).val());
  });
  return data;
}

function cancel_btn(data){ return block_container(data, 'A'); }

function block_container(data, option){
  if(option == 'A'){
    var data_ = data;
    data.forEach(function(input){
      a = input.split(':');
      $('#'+a[0]+'').val(a[1]);
    });
  }
}

function validation(){
  var message = '', success = true, response = {};
  $('div[id^="data_"]').find('input.required, select.required').each(function(){
    var Proof = $(this).val();
    if(Proof === "N" || Proof === ''){
      $(this).parent().closest('div').addClass('has-error');
      success = false; message = 'Datos requeridos vacios.'; 
    }else{
      $(this).parent().closest('div').removeClass('has-error');
    }
  });
  return  response = { 'success': success, 'message': message } ;
}

$('div input.number').on('input', function(){ this.value = this.value.replace(/[^0-9]/g,''); });
$('.serie').on('input', function(){ this.value = this.value.replace(/[^A-Za-z0-9]/g,'') });

function validate_email(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function pass_validations(pass1, pass2){
  var success = false, message = '', data = {}
  var inputpass = $('#new_password').parent().closest('div'); 
  var last_inputpass = $('#new_password_confirm').parent().closest('div'); 
  var val = pass1 == pass2 ? true : false;
  !val ? (inputpass.removeClass('has-error'), last_inputpass.addClass('has-error'), message = 'Las contraseñas no son iguales.'): (inputpass.removeClass('has-error'), last_inputpass.removeClass('has-error'))
  if(val){
    var val_inter = validator(pass1);
    val_inter.success ? (inputpass.removeClass('has-error'), last_inputpass.removeClass('has-error'), success=true):(inputpass.addClass('has-error'), last_inputpass.addClass('has-error'), message = val_inter.message)
  }
  return data = {'success': success, 'message': message} 
}

function empty_password(){
  var message = '', success = true, response = {};
  $('div.pass').find('input').each(function() { 
    var element = $(this).parent().closest('div'), input = $(this).val();
    !input ?(element.addClass('has-error'), success = false, message = 'Todos los campos * son requeridos.') : element.removeClass('has-error');
  });
  return response = {'success': success, 'message':message}
}

function validator(pass){
  var data = {}, success = false, message = '', space = /\s/
  if(pass.length < 8){ message = 'La contraseñas debe tener mínimo 8 carácteres.'
  }else if(space.test(pass)){ message = 'La contraseñas no debe tener espacios.'
  }else if(!pass.match(/\d/)){ message = 'La contraseñas debe tener minimo un numero.'
  }else if(!pass.match(/[A-Z]/)){ message = 'La contraseñas debe tener minimo una mayúscula.'
  }else if(!pass.match(/[a-z]/)){ message = 'La contraseñas debe tener minimo una minúscula.'
  }else if(!pass.match(/[.$@#!%*?&_/()^{}¿="]/)){ message = 'La contraseñas debe tener mínimo una carácter especial.'
  }else{success = true}
  return data = {'success': success, 'message': message}
}

function keyup_pass(pass){
  var parent_element = $('div.validation')
  var length = parent_element.find('.length'), number = parent_element.find('.number'), tiny = parent_element.find('.tiny'); 
  var character = parent_element.find('.character'), capital = parent_element.find('.capital'), space = parent_element.find('.space'), space_rex = /\s/;
  pass.length >= 8 ? length.addClass('val_success') : length.removeClass('val_success');
  pass.match(/\d/) ? number.addClass('val_success') : number.removeClass('val_success');
  pass.match(/[A-Z]/) ? capital.addClass('val_success') : capital.removeClass('val_success');
  pass.match(/[a-z]/) ? tiny.addClass('val_success') : tiny.removeClass('val_success');
  pass.match(/[.$@#!%*?&_/()^{}¿="]/) ? character.addClass('val_success') : character.removeClass('val_success')
  space_rex.test(pass) ? space.addClass('text-danger') : space.removeClass('text-danger');
}

function img_format(img){
  var dict_success = {}, message = '', success = true;
  var Extpict = img.split('.').pop();
  var exts = ['png', 'jpg', 'jpeg', 'PNG', 'JPG', 'JPEG'];
  if (!exts.includes(Extpict)){
    message = 'El archivo debe ser de tipo .png, jpg o jpeg';
    success = false;
  }  
  return dict_success = { 'success': success , 'message':  message}
}

var lenaguaje = {
  "sProcessing":     "Procesando...",
  "sLengthMenu":     "Mostrar _MENU_ registros",
  "sZeroRecords":    "No se encontraron resultados",
  "sEmptyTable":     "Ningún dato disponible en esta tabla",
  "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
  "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
  "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
  "sInfoPostFix":    "",
  "sSearch":         "Buscar:",
  "sUrl":            "",
  "sInfoThousands":  ",",
  "sLoadingRecords": "Cargando...",
  "oPaginate": {
    "sFirst":    "Primero",
    "sLast":     "Último",
    "sNext":     "Siguiente",
    "sPrevious": "Anterior"
  },
  "oAria": {
    "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
    "sSortDescending": ": Activar para ordenar la columna de manera descendente"
  }
}

function input_pass(){
  var element = $("div.input-pass");
  element.find(".btn-reset").on('click', function(event){
    element.find('input').val('');
  });
}
function bs_input_file(){
  $(".input-file").before( function(index){
    if (!$(this).prev().hasClass('input-ghost')) { 
      var element = $("<input type='file' class='input-ghost' id='add_csd_"+index+"' style='visibility:hidden; height:0'>");
      element.attr("name",$(this).attr("name"));
      element.change(function(){ 
        element.next(element).find('input').val((element.val()).split('\\').pop());
        var id = element.attr('id')
        if(id === 'add_csd_0' && element){
          var exts = exts_key(element[0].files[0].name); 
          exts.success ? $(this).parent().closest('div').removeClass('has-error') : ($(this).parent().closest('div').addClass('has-error'),  warning_message(exts.message))
        }else{
          var exts = exts_cer(element[0].files[0].name); 
          exts.success ? $(this).parent().closest('div').removeClass('has-error') : ($(this).parent().closest('div').addClass('has-error'), warning_message(exts.message))
        }
      });
      $(this).find("span.btn-choose").click(function(){
        element.click();
      });
      $(this).find("span.btn-reset").click(function(){
        element.val(null);
        $(this).parents(".input-file").find('input').val('');
      });
      $(this).find('input').css("cursor","pointer");
      $(this).find('input').mousedown(function() {
        $(this).parents('.input-file').prev().click();
        return false;
      });
      return element;
    }
  });
}

function buttons(){
  var elements_buttons = $('div.btns');
  var add = elements_buttons.find('button.new_csd').click(function(event){
    $(this).hide();
    $('div.contents').show();
    elements_buttons.find('button.add_csd, button.cancel_csd').show();
  });
  elements_buttons.find('button.cancel_csd').click(function(){
    $('div.contents').hide().find('input').val('');
    elements_buttons.find('button').hide();
    elements_buttons.find('button.new_csd').show();
    $('div.contents').find('input').each(function(){ $(this).parent().closest('div').removeClass('has-error'); });
  });
}

function empty_csd(){
  var message = '', success = true, response = {};
  var empty = $('div.contents').find('input').each(function() { 
    var input = $(this).val();
    if (input === ''){
      $(this).parent().closest('div').addClass('has-error');
      success = false; message = 'Todos los campos * son requeridos.';
    }else{
      $(this).parent().closest('div').removeClass('has-error');
    }
  });
  return response = {'success': success, 'message':message}
}

function exts_cer(cfile) {
  var response = {}, message = '', success = true;
  var ext = cfile.split('.').pop(), exts = ['cer'];
  if(!exts.includes(ext)){
    message = 'El archivo debe ser de tipo .cer'; success = false;
  }
  return response = { 'success': success , 'message':  message}  
}

function exts_key(cfile) {
  var response = {}, message = '', success = true;
  var ext = cfile.split('.').pop(), exts = ['key'];
  if(!exts.includes(ext)){
    message = 'El archivo debe ser de tipo .key'; success = false;
  }
  return response = { 'success': success , 'message':  message}  
}
//series
buttons_series();
function buttons_series(){
  var elements_buttons = $('div.btns_series');
  var add = elements_buttons.find('button.new_serie').click(function(event){
    elements_buttons.find('button').show();
    $('div.contents_serie').show();
    $(this).hide();
  });
  elements_buttons.find('button.cancel_serie').click(function(){
    $('div.contents_serie').hide().find('input').val('');
    elements_buttons.find('button').hide();
    elements_buttons.find('button.new_serie').show();
    $('div.contents_serie').find('input').each(function(){ $(this).parent().closest('div').removeClass('has-error'); });
  });
}

function empty_series(){
  var message = '', success = true, response = {};
  $('div.contents_serie').find('input').each(function() { 
    var element = $(this).parent().closest('div'), input = $(this).val();
    !input ?(element.addClass('has-error'), success = false, message = 'Todos los campos * son requeridos.') : element.removeClass('has-error');
  });
  return response = {'success': success, 'message':message}
}

function serie_and_folio_length() {
  var serie_elem = $('.serie').val(), folio_elem = $('.folio').val(), response = {};
  var success1 = (serie_elem.length <= 25 && serie_elem.length > 0 ) ? true : false;
  var success2 = (folio_elem.length <= 40 && folio_elem.length > 0) ? true : false;
  return response = {'success1':success1, 'success2':success2}
}

function form_delecteaccount(){
  var elements_buttons = $('div.form_DelecteAccount');
  elements_buttons.find('button.cancel').click(function(event){
    event.preventDefault();
    $('.form_DelecteAccount').modal('hide');
    $('div.datasss_').find('input, textarea').val('');
    $('div.datasss_').find('input, textarea').each(function () { $(this).parent().closest('div').removeClass('has-error'); });
  });
}

function input_deleteaccount(){
  var message = '', success = true, response = {};
  $('div.datasss_').find('input.requerid, textarea').each(function() { 
    var element = $(this).parent().closest('div'), input = $(this).val();
    !input ?(element.addClass('has-error'), success = false, message = 'Todos los campos * son requeridos.') : element.removeClass('has-error');
  });
  return response = {'success': success, 'message':message}
}


function modals_editserie(data){
  var modal = $('div.modal_series');
  modal.modal('show');
  modal.find('h2.title').text(data.title);
  modal.find('h4.text').text(data.text);
  modal.find('input').attr("type", data.attr).attr("id", data.id).val(data.last_folio).addClass('text-center');
  modal.find('button.btn_acept').attr('id', data.bsucces);
  if(data.data1){
    modal.find('button.btn_acept').attr("data1", data.data1);
  }
  modal.find('button.cancel_series').click(function(){
    modal.find('input').val('');
    modal.modal('hide');
  });
  modal.find('button #'+data.bsucces).click(function(){
    alert(data.title);
  });
}

function __address__(){
  var message = '', success = false;
  $('div.fiscal').find('input.not_only_numbers').each(function(){
    if ($(this).val() !== undefined){
      var input = $(this).val();
      success = !input ? true : false;
      (!success && !isNaN(input))?($(this).parent().closest('div').addClass('has-error'), message = 'Los campos no pueden contener solo números.'):($(this).parent().closest('div').removeClass('has-error'), success = true);
    }
  }); 
  return {'success': success, 'message': message}
}


//========    toas    ===== ////
function warning_message(message){
  $.toast({
      heading: "Advertencia",
      text: message,
      showHideTransition: "fade",
      icon: "warning",
      position: "top-right",
  });
}

function error_message(message){
  $.toast({
      heading: "Error",
      text: message,
      showHideTransition: "fade",
      icon: "error",
      position: "top-right",
  });
}

function success_message(message){
$.toast({
  heading: "Correcto",
  text: message,
  showHideTransition: "fade",
  icon: "success",
  position: "top-right",
});
}
