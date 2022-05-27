$(document).ready(function() {
  $('#multi-select').dropdown();
  var token = CSRF_TOKEN;
  var url_status = window.location.pathname;
  //document.getElementById("href-providers").setAttribute("href", url_status);
  $('#providers_tag').addClass('active');
  $('#providers_tag').css('pointer-events', 'auto');
  /*=============================================Table for user=====================================*/
  aoColumns = [{
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': true,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
    //'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,
    //'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,
    //'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,
    //'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,
  }, {
    'sWidth': '1%',
    'bSortable': false,//Total
    //'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Subtotal
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//IVA
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Retencion IVA
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Retencion ISR
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Impuestos T
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Impuestos R
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Descuentos
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//Estatus p
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//fecha p
    'render': $.fn.dataTable.render.number(',', '.', 2, '$')
  }, {
    'sWidth': '1%',
    'bSortable': false,//opciones
  }];

  $('li[id="comprobantes"]').addClass('active');

  /*==================================Table for admin USERS===============================================*/
  $(document).on( 'preInit.dt', function (e, settings) {
    
} );


  table_admin = $('#invoices_list').DataTable({

    responsive: {
      details: {
        display: $.fn.dataTable.Responsive.display.modal({
          header: function(row) {
            var data = row.data();
            return 'Detalles';
          }
        }),
        renderer: function(api, rowIdx, columns) {
          var data = $.map(columns, function(col, i) {
            return '<tr>' +
              '<td>' + col.title + ':' + '</td> ' +
              '<td>' + col.data + '</td>' +
              '</tr>';
          }).join('');
          return $('<table class="table"/>').append(data);
        }
      }
    },
    "initComplete": function(settings, json) {
      table_admin.columns([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]).visible(false);
      $('.ui.multiple.dropdown').dropdown('clear');
      for (x = 0; x < 26; x++) {
        try {
          
          //var column = table_admin.column(x);
          if (show_columns.indexOf(x) >= 0) {
            /*if(column.visible()==false){*/
            // column.visible(true)

            //}
            $("#multi-select").dropdown('set selected', x+"");
          } 
        } catch (error) {
          console.log(error);
        }

      }
    },
    // "drawCallback": function( settings ) {
    //   alert( 'DataTables has redrawn the table' );
    //},
    //'dom': '<"toolbar">frtip',
    language: datatable_language,
    'bProcessing': true,
    'bServerSide': true,
    stateSave: true,
    'searching': false,
    "columns": aoColumns,
    "PagingType": 'full_numbers',
    sAjaxSource: url_status,
    fnServerData: function(sSource, aoData, fnCallback) {
      aoData.push({
        "name": "csrfmiddlewaretoken",
        "value": token
      });
      aoData.push({
        "name": "issuer_taxpayer_id",
        "value": $('#filter_taxpayer_id').val()
      });
      if ($('#from_val').val() && $('#to_val').val()) {
        aoData.push({
          "name": "to",
          "value": $('#to_val').val()
        });
        aoData.push({
          "name": "from",
          "value": $('#from_val').val()
        });
      }
      
      aoData.push({
        "name": "metodo_pago",
        "value": $('#metodo_pago').val()
      });

      aoData.push({
        "name": "status",
        "value": $('#status_input').val()
      });
      aoData.push({
      "name": "version",
      "value": $('#version').val()
    });
      aoData.push({
        "name": "type",
        "value": $('#type').val()
      });
      if ($('#filter_uuid').val()) {
        aoData.push({
          "name": "uuid_value",
          "value": $('#filter_uuid').val()
        });
      }
      var search = location.search;
      if (search){
          var queries = search.split('&');
          queries.map(query => {
              query = query.replace('?', '');
              values = query.split('=');
              aoData.push({
                  "name": values[0],
                  "value": values[1],
              });
          });
      }
      $.ajax({
        "dataType": 'json',
        "type": "POST",
        "url": sSource,
        "data": aoData,
        "success": function(json) {
          $('#transladados').val(json.trans);
          $('#retenidos').val(json.ret);
          $('#descuentos').val(json.des);
          $('#subtotal_field').val(json.sub);
          $('#total_field').val(json.tot);
          fnCallback(json);

        }
      });
    }
  });

$('.ui.multiple.dropdown').dropdown({
  onAdd: function (value, text, $selected) {
    var column = table_admin.column($selected.attr('data-value'));
        data = []
    visible = column.visible();
    //id = $(this).attr('id');
    id = $selected.attr('data-value');
    if (visible){
      return;
    }
    data.push({
      "name": "csrfmiddlewaretoken",
      "value": token
    });
    data.push({
      "name": "atributes",
      "value": '{"' + id + '":' + (+!visible) + '}'
    });

    $.ajax({
      type: 'POST',
      url: '/providers/preferences/',
      data: data,
      dataType: 'json',
    }).done(function(json) {
      if (json.success) {

        if (visible) {

        } else {

        }
        column.visible(!column.visible());
      } else {
        return;

      }
    });
  },
  onRemove: function (value, text, $selected) {
    var column = table_admin.column($selected.attr('data-value'));
        data = []
    visible = column.visible();
    
    //id = $(this).attr('id');
    id = $selected.attr('data-value');
    if (!visible){
      return;
    }
    data.push({
      "name": "csrfmiddlewaretoken",
      "value": token
    });
    data.push({
      "name": "atributes",
      "value": '{"' + id + '":' + (+!visible) + '}'
    });

    $.ajax({
      type: 'POST',
      url: '/providers/preferences/',
      data: data,
      dataType: 'json',
    }).done(function(json) {
      if (json.success) {
        column.visible(!column.visible());
      } else {
        return;

      }
    });
  }
});

    //$('a.toggle-vis').on('click', function(e) {
  $('a.toggle-vis' ).on('click', function(e) {
    e.preventDefault();

    // Get the column API object
    var column = table_admin.column($(this).attr('data-column'));
    var column = table_admin.column($(this).attr('data-value'));
    //alert($(this).attr('data-column'));
    data = []
    visible = column.visible();
    id = $(this).attr('id');
    data.push({
      "name": "csrfmiddlewaretoken",
      "value": token
    });
    data.push({
      "name": "atributes",
      "value": '{"' + id + '":' + (+!visible) + '}'
    });
    //data.push({"name": 'unique', "value": true});

    $.ajax({
      type: 'POST',
      url: '/dashboard/account/preferences/',
      data: data,
      dataType: 'json',
    }).done(function(json) {
      if (json.success) {

        if (visible) {
          $('#' + id + ' i').removeClass("fa-check-square-o").addClass("fa-square-o");
          $('#' + id).removeClass("raised_presed").addClass("raised");
        } else {
          $('#' + id + ' i').removeClass("fa-square-o").addClass("fa-check-square-o");
          $('#' + id).removeClass("raised").addClass("raised_presed");
        }
        column.visible(!column.visible());
      } else {
        return;

      }
    });

    // Toggle the visibility

  });
  //$("div.toolbar").html('<select><option value="volvo">Volvo</select>');

  /*================================== FILTROS ===============================================*/
  // @Filtro por uuid
  $('#filter_uuid').keyup(function(e) {
    e.preventDefault();
    size = $('#filter_uuid').val().length;
    if ((size>2 || size==0) && is_valid_key(e.which)){
      table_admin.ajax.reload(); //Using when is Datatable
    }
  });

  $("#filter_taxpayer_id").keyup(function(e) {
    e.preventDefault();
    size = $('#filter_taxpayer_id').val().length;
    if ((size>2 || size==0) && is_valid_key(e.which)){
      table_admin.ajax.reload(); //Using when is Datatable
    }
  });

  $("#status_input, #version, #metodo_pago").change(function(event) {
    //table_admin.dataTable().fnDraw(); //Using when is datatable
    table_admin.ajax.reload() //Using when is Datatable
  });
  $("#type").change(function(event) {
    //table_admin.dataTable().fnDraw(); //Using when is datatable
    table_admin.ajax.reload() //Using when is Datatable
  });

  $(function() {
    $('#assign').datetimepicker({
      locale: 'es'
    });
    $('#from').datetimepicker({
      locale: 'es',
      format: "DD MMMM YYYY",
      sideBySide: true
    });

    $('#to').datetimepicker({
      locale: 'es',
      format: "DD MMMM YYYY",
      sideBySide: true //Important! See issue #1075
    });

    $("#from").on("dp.change", function(e) {
      $('#to').data("DateTimePicker").minDate(e.date);
      if ($('#to_val').val() != "") {
        //table_admin.dataTable().fnDraw(); //Using when is datatable
        table_admin.ajax.reload() //Using when is Datatable
      }

    });

    $("#to").on("dp.change", function(e) {
      $('#from').data("DateTimePicker").maxDate(e.date);
      if ($('#from_val').val() != "") {
        //table_admin.dataTable().fnDraw(); //Using when is datatable
        table_admin.ajax.reload() //Using when is Datatable
      }
    });
  });

  $(document).on('click', '.hi', function() {
    var oData = [];
    var data = table_admin.row($('#invoices_list tbody').parents('tr')).data();
    if (!data) {
      var uuid = $(this).attr('uuid');
    } else {
      var uuid = data[0];
    }
    oData.push({
      "name": "csrfmiddlewaretoken",
      "value": token
    });
    oData.push({
      "name": "uuid",
      "value": uuid
    });
    $.ajax({
      'dataType': 'html',
      'type': 'POST',
      'url': '/providers/invoices/history/',
      'data': oData,
      'statusCode': {
        404: function() {
          $.toast({
            heading: 'Error',
            text: 'UUID no encontrado',
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',

          })
        }
      }
    }).done(function(result) {
      $('#history-container').html(result);
      $('#gridSystemModalHistory').bsModal({
        show: true
      });
    });
  });

  $(document).on('click', '.af', function() {
    //var data = table_admin.api().row($('#invoices_list tbody').parents('tr')).data();
    var data = table_admin.row($('#invoices_list tbody').parents('tr')).data();
    if (!data) {
      var uuid = $(this).attr('uuid');

    } else {
      var uuid = data[0];
    }
    $('#uuid_modal').text('');
    $('#gridSystemModal').bsModal('show');
    $('#uuid_modal').text(uuid);
    //alert(data[1])
    //alert( data[1] +"'s salary is: "+ data[ 4 ] );
  });
  $(document).on('click', '.sp', function() {
    //var data = table_admin.api().row($('#invoices_list tbody').parents('tr')).data();
    var data = table_admin.row($('#invoices_list tbody').parents('tr')).data();
    if (!data) {
      var uuid = $(this).attr('uuid');
    } else {
      var uuid = data[0];
    }
    $('#uuid_modal_upload').text('');
    $('#uploadfile').bsModal('show');
    $('#uuid_modal_upload').text(uuid);
    //alert(data[1])
    //alert( data[1] +"'s salary is: "+ data[ 4 ] );
  });

  $('#gridSystemModal, #uploadfile').on('hidden.bs.modal', function() {
    $('#uuid_modal').text('');
    $('#date').val('');
    $('#file').val('');
    $('#uuid_modal_upload').text('');

    // do something…
    //alert('close');
  });
  $('#asign_date').click(function() {
    data = {
      'csrfmiddlewaretoken': token,
      'uuid': $('#uuid_modal').text(),
      'details': $('#details_date').val(),
      'date': $('#date').val()
    }

    $.ajax({
      type: 'POST',
      url: '/providers/invoices/assign/',
      data: data,
      dataType: 'json',
    }).done(function(json) {
      if (json.success) {
        $('#uuid_modal').text('');
        $('#date').val('')
        $('#gridSystemModal').bsModal('hide')
        //table_admin.dataTable().fnDraw(); //Using when is datatable
        table_admin.ajax.reload() //Using when is Datatable
        $.toast({
          heading: 'Success',
          text: 'asignacion realizada con exito',
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',

        })
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })

      }
    });
  });

  $('#file').fileinput({
    language: 'es',
    allowedFileExtensions : ['png', 'jpg'],
    //maxFileSize: 1000,
    maxFileCount: 1,
    showCaption: true,
    multiple: false,
 
    uploadUrl:'/providers/invoices/uploadpay/',
    uploadExtraData: {'csrfmiddlewaretoken': CSRF_TOKEN, },
}).on('fileuploaded', function(e, data){
  var success = data.response['success'];
  var message = data.response['message'];
  if (success){

        $.toast({
          heading: 'Exitoso',
          text: message,
          showHideTransition: 'fade',
          icon: 'success',
          //position: 'top-right',
          position: 'top-right',
          //showDuration: 100,
          newestOnTop: true,
          //hideAfter: true,
          progressBar:false,
        });
    $('#uuid_modal_upload').text('');
    $('#file').val('');
    $('#uploadfile').bsModal('hide');
    //table_admin.dataTable().fnDraw(); //Using when is datatable
    table_admin.ajax.reload() //Using when is Datatable
  }else{
    //message.forEach(function(error){
      $.toast({
        heading: 'Algo salio mal',
        text: message,
        showHideTransition: 'fade',
        icon: 'error',
        //position: 'top-right',
        position: 'top-right',
        //showDuration: 100,
        newestOnTop: true,
        //hideAfter: true,
        progressBar: false,
      });
    //});
  }  
   $('#file').fileinput('clear');
   $('#file').fileinput('reset');
   $('#file').fileinput('refresh').fileinput('enable');
   $('#file').fileinput('refresh').fileinput('enable');
   
});
$('#file').on('filebatchpreupload', function(event, data, index) {
  data.form = {'uuid': $('#uuid_modal_upload').text(), 'details': $('#details_file_pay').val()  };
  data.extra.uuid = $('#uuid_modal_upload').text();
  data.extra.details = $('#details_file_pay').val();
});



  $('#invoices_list tbody').on('click', '.cp', function() {
    var data = table_admin.row($(this).parents('tr')).data();
    var uuid = data[3]
    data = {
      'csrfmiddlewaretoken': token,
      'uuid': uuid,
      'option': 'C'
    }
    $.ajax({
      type: 'POST',
      url: '/providers/invoices/paymentok/',
      data: data,
      cache: false,
      dataType: 'json',
    }).done(function(json) {
      //table_admin.dataTable().fnDraw(); //Using when is datatable
      table_admin.ajax.reload() //Using when is Datatable
      if (json.success) {
        $.toast({
          heading: 'Success',
          text: 'Pago confirmado',
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',

        })
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })

      }
    });
  });
  $('#invoices_list tbody').on('click', '.rp', function() {
    var data = table_admin.row($(this).parents('tr')).data();
    var uuid = data[3]
    data = {
      'csrfmiddlewaretoken': token,
      'uuid': uuid,
      'option': 'R'
    }
    $.ajax({
      type: 'POST',
      url: '/providers/invoices/paymentok/',
      data: data,
      cache: false,
      dataType: 'json',
    }).done(function(json) {
      //table_admin.dataTable().fnDraw(); //Using when is datatable
      table_admin.ajax.reload() //Using when is Datatable
      if (json.success) {
        $.toast({
          heading: 'Success',
          text: 'Pago Rechazado',
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',

        })
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })

      }
    });
  });

  $(document).on('click', '.can', function() {
    var data = table_admin.row($('#invoices_list tbody').parents('tr')).data();
    if (!data) {
      var uuid = $(this).attr('uuid');
    } else {
      var uuid = data[0];
    }
    $('#uuid_detalles').val(uuid);
    $('#detalles').bsModal('show');
  });

  $('#download_report').change(function(event) {
    $("#download_report").attr("disabled", true);

    item_selected= $("#download_report").val()
    if(item_selected == 'C'){
      url =  '/providers/invoices/download_report_pagos/';
    }else if(item_selected == 'P'){
      url =  '/providers/invoices/download_report_csv/';

    }else {
     return;
    }
    $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
    $("#icon_download").addClass("fa-spinner fa-spin text-primary");
    $(document.body).css({'cursor' : 'wait'});
    data = [{
      "name": "csrfmiddlewaretoken",
      "value": token
    }];
    data.push({
        "name": "issuer_taxpayer_id",
        "value": $('#filter_taxpayer_id').val()
      });
    data.push({
        "name": "receiver_taxpayer_id",
        "value": $('#filter_taxpayer_id_r').val()
      });
    if ($('#from_val').val() && $('#to_val').val()) {
      data.push({
        "name": "to",
        "value": $('#to_val').val()
      });
      data.push({
        "name": "from",
        "value": $('#from_val').val()
      });
    }
    data.push({
      "name": "status",
      "value": $('#status_input').val()
    });
    data.push({
      "name": "version",
      "value": $('#version').val()
    });
    if ($('#filter_uuid').val()) {
      data.push({
        "name": "uuid_value",
        "value": $('#filter_uuid').val()
      });
    }
    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      cache: false,
      dataType: 'json',
    }).done(function(json) {

      $("#download_report").attr("disabled", false);
      $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
      $('#download_report').val("T").change()
      $(document.body).css({'cursor' : 'context-menu'});
      //alert('Done')
      //table_admin.dataTable().fnDraw();
      if (json.success) {
        $("#download_report").attr("disabled", false);
        window.open(json.url);
      } else {
        /*alert(json.message);*/
        $("#download_report").attr("disabled", false);
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })

      }
    }).fail(function(jqXHR, status, errorThrown) {
      $(document.body).css({'cursor' : 'context-menu'});
      $('#download_report').val("T").change()
      $("#download_report").attr("disabled", false);
      //$("#download_report").val('T');
      //$("#download_report").change();
      $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
      $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
      $(document.body).css({'cursor' : 'default'});
      //alert(jqXHR);
      //alert(status);
      //alert(errorThrown);
    });

  });


  $('#button_reject').click(function(event) {
    event.preventDefault();
    uuid = $('#uuid_detalles').val();
    details = $('#message-text').val();
    var adata = {
      'csrfmiddlewaretoken': token,
      'uuid': uuid,
      'details': details
    }
    $.ajax({
      type: 'POST',
      url: '/providers/invoices/reject/',
      data: adata,
      cache: false,
      dataType: 'json',
    }).done(function(json) {
      if (json.success) {
        //table_admin.dataTable().fnDraw(); //Using when is datatable
        table_admin.ajax.reload() //Using when is Datatable
        $.toast({
          heading: 'Success',
          text: 'Comprobante Rechazado',
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',

        });
        $('#detalles').bsModal('hide');
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })

      }
    });
  });

  $(document).on("click", "#btn_clean",  function(event) {
    $('#filter_uuid').val("")
    $('#filter_taxpayer_id').val("")
    $('#filter_taxpayer_id_r').val("")
    $('#to_val').val("")
    $('#from_val').val("")
    $('#metodo_pago').prop("selectedIndex",0).change();
    $('#status_input').prop("selectedIndex",0).change();
    $('#version').prop("selectedIndex",2).change();
    $('#type').prop("selectedIndex",0).change();
    table_admin.ajax.reload()
  });

  /*$(document).on('click', '.panel-heading a.clickable', function(e){
    var $this = $(this);
    if (!$this.hasClass('panel-collapsed')){
      $this.parents('.panel').find(this.getAttribute('pnl')).slideUp();
      $this.addClass('panel-collapsed');
      $this.find('span.glyphicon-chevron-up').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
    } else {
      $this.parents('.panel').find(this.getAttribute('pnl')).slideDown();
      $this.removeClass('panel-collapsed');
      $this.find('span.glyphicon-chevron-down').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
    }
  });*/

  $(document).on('click', '.upd', function(event){
    event.preventDefault();
    var $btn = $(this);
    $btn.button('loading');
    var invoice = $btn.data('invoice');
    $.ajax({
      'type': 'POST',
      'dataType': 'json',
      'async': true,
      'url': '/providers/invoices/update/status/sat/',
      'data':{
        'invoice': invoice,
        'csrfmiddlewaretoken':token,
      },
    }).done(function(response, textStatus, jqXHR){
      var send_message = response['success'] ? success_message : error_message;
      var message =  response['message']!='' ? response['message'] : 'Hubo un error, intente más tarde.';
      
      if (response['status']=='C'){
        
        info_message(message);
        setTimeout(
            function(){
              //table_admin.draw();
              table_admin.ajax.reload();
            }, 4000 
          );

      }
      else{
        send_message(message);
      }
      $btn.button('reset');
    });
  });


  $(document).on("click", ".btn-details", function(event){
      var uuid = $(this).attr("data-whatever");
      var type = $(this).attr("data-invoicetype");
      $("#modal-show_details-title").html('FACTURA: <a id="uuid" style="color: inherit; text-decoration: inherit"><b>' + uuid +'</b></a>');
      get_info_invoice(uuid, "get_info_invoice", "R");
      update_table_concepts(uuid, "get_info_concepts", "R");
  });

      function get_info_invoice(uuid, oper, type){
        var data = new FormData();
        token = getCookie('csrftoken');
        data.append("csrfmiddlewaretoken", token);
        data.append("uuid", uuid);
        data.append("oper", oper);
        data.append("type", type);
        $.ajax({
            type: 'POST',
            url : '/stamping/get_info_invoice/',
            data : data,
            dataType : 'json',
            cache : false,
            contentType: false,
            processData: false
        }).done(function(json) {
            if (json.success) {
                $('#invoice_name').text(json.issuing.name)
                $('#invoice_taxpayer_id').text(json.issuing.taxpayer_id)
                $('#invoice_address').text(json.issuing.address)
                //$('#invoice_phone').text(json.issuing.phone)
                //$('#invoice_email').text(json.issuing.email)
                $('#invoice_rname').text(json.receiver.rname)
                $('#invoice_rtaxpayer_id').text(json.receiver.rtaxpayer_id)
                $('#invoice-id').text("Folio: "+json.invoice.serial+"-"+json.invoice.folio)
                $("#invoice_type").html("<label>Tipo de Comprobante: </label> "+ json.invoice.type);
                $("#invoice_status").html("<label>Estatus SAT: </label> "+ json.invoice.status);
                $('#invoice_date').text("Fecha de Emisión : "+json.invoice.date)
                $('#invoice_subtotal').html("$ "+json.totals.sub_total)
                $('#invoice_total_tra').html("$ "+json.totals.total_tra)
                $('#invoice_total_ret').html("$ "+json.totals.total_ret)
                $('#invoice_discounts').html("$ "+json.totals.discounts)
                $('#invoice_total').html("$ "+json.totals.total)
                //table_emisor.ajax.reload();
                //table_receiver_finished.ajax.reload()
            } else {
                error_message(json.message)
            }
        });
    }

    aoColumns_concepts = [{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '25%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
    }];

    function update_table_concepts(uuid, oper, type){
        token = getCookie('csrftoken');
        $('#table_concepts').DataTable({
            responsive : true,
            'processing': true,
            'serverSide': true,
            'destroy': true,
            'columns': aoColumns_concepts,
            "language": datatable_language,
            "searching": false,
            //"scrollY": 200,
            //"scrollX": true,
            //"scrollCollapse": true,
            "paging": false,
            'ajax': ({
                //pages: 20,
                stateSave: true,
                method: 'POST',
                url: '/stamping/get_info_invoice/',
                data: {
                    'uuid': uuid,
                    'csrfmiddlewaretoken': token,
                    'oper': oper,
                    'type': type,
                }
            })
        });
    }


});
