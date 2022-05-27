// const { Console } = require("console");

receiverColumns = [{
  'sWidth': '1%',
  'bSortable': false
}, {
  'sWidth': '19%',
  'bSortable': false,
}, {
  'sWidth': '20%',
  'bSortable': false,
}, {
  'sWidth': '20%',
  'bSortable': false,
}, {
  'sWidth': '20%',
  'bSortable': false,
}, {
  'sWidth': '20%',
  'bSortable': false,
}];

//var datatable_language = {
//  "sProcessing": (gettext("Procesando...")),
//  "sLengthMenu": (gettext("Mostrar _MENU_ registros")),
//  "sZeroRecords": (gettext("No se encontraron resultados")),
//  "sEmptyTable": (gettext("Ningún dato disponible en esta tabla")),
//  "sInfo": (gettext("Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros")),
//  "sInfoEmpty": (gettext("Mostrando registros del 0 al 0 de un total de 0 registros")),
//  "sInfoFiltered": (gettext("(filtrado de un total de _MAX_ registros)")),
//  "sInfoPostFix": "",
//  "sSearch": (gettext("Buscar:")),
//  "sUrl": "",
//  "sInfoThousands": ",",
//  "sLoadingRecords": (gettext("Cargando...")),
//  "oPaginate": {
//      "sFirst": (gettext("Primero")),
//      "sLast": (gettext("Último")),
//      "sNext": (gettext("Siguiente")),
//      "sPrevious": (gettext("Anterior"))
//  },
//  "oAria": {
//      "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
//      "sSortDescending": ": Activar para ordenar la columna de manera descendente"
//  }
//}

if (role != 'A') {
  receiverColumns.splice(4, 1)
}else{
  receiverColumns.splice(4, 1)
}

function validate_email(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

function clearAddReceiverForm() {
  $('#formReceiver input:not([type=submit], [type=button], [type=hidden]), textarea').val("");
  $('#id_emails').val("");
  $('#id_emails').tagsinput('removeAll');
  $('#taxpayer_id option').remove();
}

/*Este contador se utiliza para que no se esten añadiendo en cada click los valores de 
USO CFDI en el dialog Editar Receptor
 */
var cont_stop_prepend = 0;

var use_cfdi, receiver_status, add_use_cfdi;

$(document).ready(function () {
  $('#receptores').addClass('active');
  var receiverTable = $('#invoicing-receiver').DataTable({
    "responsive": true,
    "searching": false,
    "bProcessing": true,
    "bServerSide": true,
    'ordering': false,
    //"stateSave": true,
    // "language": datatable_language,
    "language": language_datatable,
    "columns": receiverColumns,
    "columnDefs": [
      {
        className: "text-center",
        "targets": "_all",
      },],
    "PagingType": "full_numbers",
    "sAjaxSource": urlReceiver,
    fnServerData: function callback(sSource, aoData, fnCallback) {
      
      aoData.push({
        "name": "csrfmiddlewaretoken",
        "value": getCookie('csrftoken')
      });
      aoData.push({
        "name": "oper",
        "value": "list-receivers"
      });
      if ($("#identifier_number").val()) {
        aoData.push({
          "name": "identifier_number",
          "value": $("#identifier_number").val()
        });
      }
      if ($("#organizacion_id").val()) {
        aoData.push({
          "name": "organizacion_id",
          "value": $("#organizacion_id").val()
        });
      }
      if ($("#emails").val()) {
        aoData.push({
          "name": "emails",
          "value": $("#emails").val()
        });
      }
      if ($("#name").val()) {
        aoData.push({
          "name": "name",
          "value": $("#name").val()
        });
      }
      if ($('#owner').val()) {
        aoData.push({
          'name': 'owner_filter',
          'value': $('#owner').val(),
        })
      }
      if ($("#date-from-val").val() && $("#date-to-val").val()) {
        aoData.push({
          "name": "date-from",
          "value": $("#date-from-val").val()
        });

        aoData.push({
          "name": "date-to",
          "value": $("#date-to-val").val()
        });
      }
      

      $.ajax({
        "dataType": "json",
        "type": "POST",
        "url": sSource,
        "data": aoData,
        "success": function (json) {
          fnCallback(json);
        }
      });
    }
  });

  receiverTable.on('draw.dt', function () {
    var pageInfo = receiverTable.page.info();

    receiverTable.column(0, { page: 'current' }).nodes().each(function (cell, i) {
      cell.innerHTML = i + 1 + pageInfo.start;
    });
  });

  $('#identifier_number').keyup(function (e) {
    var pLength = $(this).val().length;
    if ((pLength > 2 || pLength == 0) && is_valid_key(e.which)) {
      e.preventDefault();
      receiverTable.draw();
    }
  });

  $("#emails, #name, #owner").keyup(function (e) {
    if ($(this).val().length >= 5) {
      e.preventDefault();
      receiverTable.draw();
    }
    else {
      receiverTable.ajax.reload();
    }
  });

  $("#organizacion_id").keyup(function (e) {
    receiverTable.draw();
  });

  $("#date-from").datetimepicker({
    locale: "es",
    format: "DD MMMM YYYY",
    sideBySide: true
  });

  $("#date-to").datetimepicker({
    locale: "es",
    format: "DD MMMM YYYY",
    sideBySide: true
  });

  $("#date-from").on("dp.change", function (e) {
    $("#date-to").data("DateTimePicker").minDate(e.date);
    if ($("#date-from-val").val() && $("#date-to-val").val()) {
      receiverTable.ajax.reload();
    }
  });

  $("#date-to").on("dp.change", function (e) {
    $("#date-from").data("DateTimePicker").maxDate(e.date);
    if ($("#date-to-val").val() && $("#date-from-val").val()) {
      receiverTable.ajax.reload();
    }
  });

  $(document).on('click', '.anr', function (e) {
    e.preventDefault();
    //clearAddReceiverForm();
    $('#modal-add-receiver').modal('show');
  });

  $(document).on('click', '.canr', function (e) {
    $('#modal-add-receiver').modal('toggle');
    $('#formRecipient input:not([type=submit], [type=button], [type=hidden])').val("");
    $('#id_emails').val("");
    $('#id_emails').tagsinput('removeAll');
    $('#receiver-status').attr('checked', false);
  });

  $(document).on('click', '.sr', function (e) {
    e.preventDefault();
    var editData = new FormData();
    editData.append('receiver', $(this).data('receiver'));

    editData.append('oper', 'activate-receiver');
    editData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: editData,
      success: function (response) {
        var send_message = response['success'] ? success_message : error_message;
        send_message(response['message']);
        receiverTable.draw();
      }
    });
  });

  $(document).on('click', '.sdr', function (e) {
    e.preventDefault();
    var show_receiver_data = new FormData();
    show_receiver_data.append('receiver', $(this).data('receiver'));
    show_receiver_data.append('oper', 'get-info-details');
    show_receiver_data.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: show_receiver_data,
      success: function (response) {
        if (response['success']) {
          $.each(response['receivers-info'], function (id, value) {
            //if (id == 'receiver_emails') {
            //  emails = []
            //  $.each(value, function(key, value) {
            //      emails.push('<span class="label label-emails">' + value + '</span>')
            //  });
            //  emails = emails.join(' ');
            //  $('#receiver_emails').html(emails);
            //} else {
            $('#' + id + '_details').val(value);
            //}
          });
        } else {
          $.toast({
            heading: 'Error',
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
          });
        }
      }
    });
    $('#modal-show-receiver-details').modal('show');
  });

  $(document).on('click', '.er', function (e) {
    e.preventDefault();
    $('#modal-edit-receiver').modal('show');
    var edit_receiver_data = new FormData();
    edit_receiver_data.append('receiver', $(this).data('receiver'));
    edit_receiver_data.append('oper', 'get-info-edit');
    edit_receiver_data.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: edit_receiver_data,
      success: function (response) {
        if (response['success']) {
          cont_stop_prepend = cont_stop_prepend + 1;
          $.each(response['receivers-info'], function (id, value) {
            //if(id == "use_cfdi_values" && cont_stop_prepend == 1){
            //  for(i=0; i<value.length; i++){
            //    $('.use_cfdi_sel').prepend($('<option>', {value:value[i].clave, text:value[i].clave + ' - ' + value[i].descripcion}));
            //  }
            // $('.use_cfdi_sel').selectpicker({
            //    liveSearch: true,
            //    showSubtext: true
            // });
            //}
            //else if(id == 'receiver_use_cfdi_val'){
            //  $('.use_cfdi_sel').val(response['receivers-info']['receiver_use_cfdi_val']).trigger('change');
            //  //$('.use_cfdi_sel').selectpicker('val', response['receivers-info']['receiver_use_cfdi_val']);
            //}
            //else if(id == 'receiver_status'){
            //  $('.receiver_status').selectpicker('val', response['receivers-info']['receiver_status']);
            //} else if(id == 'receiver_emails') {
            //if(id == 'receiver_emails') {
            //  emails = response['receivers-info']['receiver_emails'];
            //  $('#buyer_emails_edit').tagsinput('removeAll');
            //  for (var i = 0; i < emails.length; i++) {
            //    $('#buyer_emails_edit').tagsinput('add', emails[i]);
            //  }
            //}
            //else{
            $('#' + id + '_edit').val(value);
            //}
          });
        }
        else {
          $.toast({
            heading: 'Error',
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
          });
        }
      }
    });
  });


  $('.use_cfdi_sel').change(function () {
    use_cfdi = $(this).val();
  });

  $('.receiver_status').change(function (e) {
    receiver_status = $(this).val();
  });
  $(document).on('click', '.edit_receiver', function (e) {
    e.preventDefault();
    var edit_receiver_values = new FormData();
    var name_edit = $('#receiver_name_edit').val();

    edit_receiver_values.append('receiver_status', receiver_status);
    edit_receiver_values.append('receiver_use_cfdi', use_cfdi);
    edit_receiver_values.append('receiver_id_val', $('#receiver_id_edit').val());
    edit_receiver_values.append('receiver_name_val', name_edit);
    edit_receiver_values.append('receiver_taxpayer_id_val', $('#receiver_taxpayer_id_edit').val());
    edit_receiver_values.append('receiver_emails_val', $('#receiver_emails_edit').val());
    edit_receiver_values.append('oper', 'edit-receiver');
    edit_receiver_values.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    if (!$('.use_cfdi_sel').val()) {
      $('.use_cfdi_sel').focus()
      $('.use_cfdi_sel').attr('placeholder', 'Este campo es obligatorio');
      return;
    }
    if (!$('#receiver_emails_edit').tagsinput('items').length) {
      $('.bootstrap-tagsinput input').focus();
      $('.bootstrap-tagsinput input').attr('placeholder', 'Es necesario ingresar al menos un correo electrónico');
      return;
    }


    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: edit_receiver_values,
      success: function (response) {
        if (response['success']) {
          $.toast({
            heading: gettext('Success'),
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'success',
            position: 'top-right',
          });
          $('#modal-edit-receiver').modal('hide');
          receiverTable.ajax.reload();
        }
        else {
          $.toast({
            heading: 'Error',
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
          });
        }
      }
    });
  });

  $('#add_use_cfdi').on('change', function (e) {
    add_use_cfdi = $(this).val();
  });

  $(document).on('click', '.addreceiver', function (e) {
    e.preventDefault();
    var edit_receiver_values = new FormData();
    //var name_edit = $('#receiver_name_edit').val();

    edit_receiver_values.append('identifier_number', $('#identifier_number_add').val());
    edit_receiver_values.append('organizacion_id', $('#organizacion_id_add').val());
    edit_receiver_values.append('custom_name', $('#custom_name').val());
    edit_receiver_values.append('address_name', $('#address_name').val());
    edit_receiver_values.append('city_name', $('#city_name').val());
    edit_receiver_values.append('id_province', $('#id_province').val());
    edit_receiver_values.append('postal_zone', $('#postal_zone').val());
    // edit_receiver_values.append('id_country', $('#id_country').val());
    edit_receiver_values.append('id_language', $('#id_language').val());
    edit_receiver_values.append('id_currency', $('#id_currency').val());
    edit_receiver_values.append('id_full_name', $('#id_full_name').val());
    edit_receiver_values.append('id_department', $('#id_department').val());
    edit_receiver_values.append('id_email', $('#id_email').val());
    edit_receiver_values.append('id_telephone', $('#id_telephone').val());
    edit_receiver_values.append('id_web', $('#id_web').val());
    edit_receiver_values.append('id_category', $('#id_category').val());
    edit_receiver_values.append('id_method', $('#id_method').val());
    edit_receiver_values.append('payment_method', $('#payment_method').val());
    edit_receiver_values.append('term', $('#term').val());
    edit_receiver_values.append('oper', 'add-buyer');
    edit_receiver_values.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    //if (!$('.use_cfdi_sel').val()) { 
    //  $('.use_cfdi_sel').focus()
    //  $('.use_cfdi_sel').attr('placeholder', 'Este campo es obligatorio'); 
    //  return; 
    //}
    //if (!$('#receiver_emails_edit').tagsinput('items').length) {
    //  $('.bootstrap-tagsinput input').focus();
    //  $('.bootstrap-tagsinput input').attr('placeholder', 'Es necesario ingresar al menos un correo electrónico'); 
    //  return;
    //}


    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: edit_receiver_values,
      success: function (response) {
        if (response['success']) {
          $.toast({
            heading: gettext('Success'),
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'success',
            position: 'top-right',
          });
          $('#modal-add-receiver').modal('toggle');
          //$('#modal-edit-receiver').modal('hide');
          //receiverTable.ajax.reload();
        }
        else {
          $.toast({
            heading: 'Error',
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
          });
        }
      }
    });
  });

  $(document).on('click', '.editbuyer', function (e) {
    e.preventDefault();
    var edit_receiver_values = new FormData();
    //var name_edit = $('#receiver_id').val();
    //edit_receiver_values.append('receiver', $(this).data('receiver'));
    edit_receiver_values.append('receiver_id', $('#receiver_id_edit').val());
    edit_receiver_values.append('buyer_name_edit', $('#buyer_name_edit').val());
    edit_receiver_values.append('identifier_number_edit', $('#identifier_number_edit').val());
    edit_receiver_values.append('organizacion_id_edit', $('#organizacion_id_edit').val());
    edit_receiver_values.append('buyer_emails_edit', $('#buyer_emails_edit').val());
    edit_receiver_values.append('buyer_telephone_edit', $('#id_telephone_edit').val());
    edit_receiver_values.append('buyer_address_name_edit', $('#address_name_edit').val());
    edit_receiver_values.append('buyer_city_name_edit', $('#city_name_edit').val());
    // edit_receiver_values.append('buyer_country_edit', $('#id_country_edit').val());
    edit_receiver_values.append('oper', 'edit-buyer');
    edit_receiver_values.append('csrfmiddlewaretoken', getCookie('csrftoken'));

    //if (!$('.use_cfdi_sel').val()) { 
    //  $('.use_cfdi_sel').focus()
    //  $('.use_cfdi_sel').attr('placeholder', 'Este campo es obligatorio'); 
    //  return; 
    //}
    //if (!$('#receiver_emails_edit').tagsinput('items').length) {
    //  $('.bootstrap-tagsinput input').focus();
    //  $('.bootstrap-tagsinput input').attr('placeholder', 'Es necesario ingresar al menos un correo electrónico'); 
    //  return;
    //}


    $.ajax({
      method: 'POST',
      contentType: false,
      processData: false,
      data: edit_receiver_values,
      success: function (response) {
        if (response['success']) {
          $.toast({
            heading: gettext('Success'),
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'success',
            position: 'top-right',
          });
          $('#modal-edit-receiver').modal('toggle');
          //$('#modal-edit-receiver').modal('hide');
          //receiverTable.ajax.reload();
        }
        else {
          $.toast({
            heading: 'Error',
            text: response['message'],
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
          });
        }
      }
    });
  });

  $('#formReceiver').submit(function (e) {
    e.preventDefault();
    var addRecipientData = new FormData();
    var addForm = $(this);

    addRecipientData.append('oper', 'add-receiver');
    addRecipientData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    $.each(addForm.serializeArray(), function (key, input) {
      addRecipientData.append(input.name, input.value);
    });
    addRecipientData.append(
      'emails', $('#id_emails').val()
    );
    addRecipientData.append(
      'status', $('#id_status').val()
    );
    addRecipientData.append(
      'add_use_cfdi', add_use_cfdi
    );
    $.ajax({
      method: 'POST',
      data: addRecipientData,
      contentType: false,
      processData: false,
      success: function (response) {
        if (response['success']) {
          receiverTable.ajax.reload();
          success_message('Registro exitoso');
          clearAddReceiverForm();
          $('#modal-add-receiver').modal('toggle');
        } else {
          var messages = new Array();
          $.map(response['errors'], function (errors, element) {
            return $.map(errors, function (error, idx) {
              messages.push(error);
            });
          });
          error_message(messages);
          //$('#formProdserv input:not([type=submit], [type=button], [type=hidden]), textarea').val("");
          //$('#id_prodserv, #id_key_unit').val(null).trigger('change');
        }
      }
    });
    setTimeout(
      function () {
        receiverTable.draw();
      }, 4000
    )

  });
  $(document).on("click", "#clean", function (event) {
    $("#organizacion_id, #emails, #name, #date-to-val, #date-from-val, #id_schemeID, #owner, #identifier_number").val('');
    receiverTable.ajax.reload();
  });

  /* ########################### ADDED BY jroqu3 ########################### */

  $('#id_taxpayer_id').attr('maxlength', '13');
  $('#id_taxpayer_id').attr('minlength', '12');

  $(document).on('click', '#refresh-receivers', function () {
    receiverTable.ajax.reload();
  });

  $('#use_cfdi').select2({
    ajax: {
      url: window.location.pathname,
      method: 'POST',
      width: 'resolve',
      dataType: 'json',
      delay: '250',
      data: function (params) {
        params.term = params.term.toUpperCase();
        return {
          oper: 'get-usecfdi',
          csrfmiddlewaretoken: getCookie('csrftoken'),
          usecfdi: params.term,
          select: 'filter',
        }
      },
      processResults: function (data) {
        data = data.data
        return {
          results: $.map(data, function (item, idx) {
            return {
              text: (decodeURIComponent(escape(item.desc))),
              id: item.code,
            }
          }),
        }
      },
      cache: true
    },
    language: 'es',
    inputTooShort: function (left) {
      return 'Faltan X caracteres';
    },
    placeholder: 'Uso CFDI',
    minimumInputLength: 1,
    theme: 'bootstrap',
  });

  $(document).on('click', '[data-select2-id="2"]', function () {
    if (!$('#id_taxpayer_id').val()) {
      $('#select2-id_use_cfdi-results li').html('Es necesario ingresar un RFC');
    }
  });

  $('#id_use_cfdi').select2({
    ajax: {
      url: window.location.pathname,
      method: 'POST',
      width: 'resolve',
      dataType: 'json',
      delay: '250',
      data: function (params) {
        params.term = params.term.toUpperCase();
        return {
          oper: 'get-usecfdi',
          csrfmiddlewaretoken: getCookie('csrftoken'),
          usecfdi: params.term,
          taxpayer_id: $('#id_taxpayer_id').val() ? $('#id_taxpayer_id').val() : error_message('Es necesario ingresar un RFC'), //$('#select2-id_use_cfdi-results li').html('Es necesario ingresar un RFC'),
        }
      },
      processResults: function (data) {
        data = data.data
        return {
          results: $.map(data, function (item, idx) {
            return {
              text: (decodeURIComponent(escape(item.desc))),
              id: item.code,
            }
          }),
        }
      },
      cache: true
    },
    language: 'es',
    inputTooShort: function (left) {
      return 'Faltan X caracteres';
    },
    placeholder: 'Uso CFDI',
    minimumInputLength: 1,
    theme: 'bootstrap',
  });

  $('#receiver_use_cfdi_edit').select2({
    ajax: {
      url: window.location.pathname,
      method: 'POST',
      width: 'resolve',
      dataType: 'json',
      delay: '250',
      data: function (params) {
        params.term = params.term.toUpperCase();
        return {
          oper: 'get-usecfdi',
          csrfmiddlewaretoken: getCookie('csrftoken'),
          usecfdi: params.term,
          taxpayer_id: $('#receiver_taxpayer_id_edit').val(),
        }
      },
      processResults: function (data) {
        data = data.data
        return {
          results: $.map(data, function (item, idx) {
            return {
              text: (decodeURIComponent(escape(item.desc))),
              id: item.code,
            }
          }),
        }
      },
      cache: true
    },
    language: 'es',
    inputTooShort: function (left) {
      return 'Faltan X caracteres';
    },
    placeholder: 'Uso CFDI',
    minimumInputLength: 1,
    theme: 'bootstrap',
  });
  $.fn.select2.defaults.set('theme', 'bootstrap');

  $(document).on('click', '#button-id-cancel', function (e) {
    clearAddReceiverForm();
  });

  $('#id_taxpayer_id').keyup(function (event) {
    $('#id_use_cfdi').val('').trigger('change');
  })

  $(document).on('click', '.btn-details-owner', function () {
    var data = {
      'csrfmiddlewaretoken': getCookie('csrftoken'),
      'owner': $(this).attr('owner'),
      'oper': 'get-owner-details',
    }

    $.ajax({
      'type': 'POST',
      'dataType': 'json',
      'url': window.location.pathname,
      'data': data,
      'success': function (json) {
        if (json.success) {
          values = json.values[0]
          $('#owner_taxpayer_id').val(values['taxpayer_id']);
          $('#owner_name').val(values['name']);
          $('#owner_reg_fiscal').val(values['reg_fiscal']);
          $('#owner_email').val(values['email']);
          $('#owner_status').html(values['status']);
          $('#modal-owner-details').modal('show');
        } else {
          error_message(json.message);
        }
      }
    });
  });

  /* ######################################################################## */

  //$('.emails-input').tagsinput({
  //  tagClass: 'label label-success label-important col-sm-6 col-md-6 col-lg-6'
  //});
});