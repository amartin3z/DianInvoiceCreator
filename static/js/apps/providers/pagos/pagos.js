$(document).ready(function() {
    $('#providers_tag').addClass('active');
    $('#providers_tag').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    /*=============================================Table for user=====================================*/
    aoColumns = [{
        'bSortable': false,
        'data': 'status',
    },{
        'bSortable': false,
        'data': 'uuid',
    },{
        'bSortable': false,
        'data': 'rfc',
    },{
        'bSortable': true,
        'data': 'fecha',
    },{
        'bSortable': true,
        'data': 'total',
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
    },{
        'bSortable': true,
        'data': 'restante',
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
    },{
        'bSortable': false,
        'data': 'estatus',
    },{
        'bSortable': false,
        'data': 'opciones',
    }
    ];
    



function format (d) {
    var tr = '<tr>';
    $.each(d.notification_detail, function(index, details){
        tr += '<td><b># Parcialidad: </b>' + details.Nparcialidad +'</td><td><b>UUID: </b>' + details.UUID + '</td><td><b>Fecha:</b> ' +  details.Fecha + '</td><td><b>Fecha E:</b> ' +  details.Fecha_E + '</td><td><b>Saldo Anterior:</b> ' +  details.SaldoAnterior +  '</td><td><b>Importe Pagado:</b> ' +  details.ImportePagado +'</td><td><b>Importe Pagado Insoluto:</b> ' +  details.ImportePagadoInsoluto +'</td><td><b>Estatus:</b> '+ details.Status +'</td><td>'+details.Archivos+'</td></tr>'
    })
    tr += '</tr>';
    table = '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            tr
        '</tr>'+
    '</table>';
    return table;
}

/*==================================Table for admin USERS===============================================*/

    table_admin = $('#pagos_list').DataTable({
        responsive: {
          details: {
            display: $.fn.dataTable.Responsive.display.modal( {
              header: function ( row ) {
                var data = row.data();
                return 'Detalles';
              }
            }),
          }
        },
        'language': datatable_language,
        "autoWidth": true,
        'bProcessing': true,
        'bServerSide': true,
        'stateSave': true,
        'searching': false,
        'columns': aoColumns,
        'PagingType': 'full_numbers',
        "columnDefs": [
        {
            className: "text-center",
            "targets": [0],
        },
         {
            className: "text-center",
            "targets": [1],
        },
         {
            className: "text-center",
            "targets": [2],
        },
         {
            className: "text-center",
            "targets": [3],
        },
         {
            className: "text-center",
            "targets": [4],
        },
        {
            className: "text-center",
            "targets": [5],
        },
        {
            className: "text-center",
            "targets": [6],
        },
        {
            className: "text-center",
            "targets": [7],
        },
        ],
        'sAjaxSource': url_status,
        'fnServerData': function(sSource, aoData, fnCallback) {
            aoData.push( { "name": "csrfmiddlewaretoken","value": token});
            if ($('#filter_uuid').val()){
                aoData.push({
                    'name': 'uuid',
                    'value': $('#filter_uuid').val(),
                });
            }

            if ($('#filter_taxpayer_id').val()){
                aoData.push({
                    'name': 'taxpayer_id',
                    'value': $('#filter_taxpayer_id').val(),
                });
            }

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
                    "name": "origen_pagos",
                    "value": $('#origen_pagos').val()
                });
                aoData.push({
                    "name": "surplus",
                    "value": $('#excedente').is(':checked')
                });

                aoData.push({
                  "name": "incon",
                  "value": $('#inconsistente').is(':checked')
              });
  

            $.ajax({
                "dataType": 'json',
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    fnCallback(json);
                }
            });
        },
    });
    //table_admin.api().column(2).visible(false);

    $("#filter_uuid").keyup(function(e){
      e.preventDefault();
      size = $('#filter_uuid').val().length;
      if ((size>2 || size==0) && is_valid_key(e.which)){
        table_admin.ajax.reload(); //Using when is Datatable
      }
    });
    
    $("#filter_taxpayer_id").keyup(function(e){
      e.preventDefault();
      size = $('#filter_taxpayer_id').val().length;
      if ((size>2 || size==0) && is_valid_key(e.which)){
        table_admin.ajax.reload(); //Using when is Datatable
      }
    });
    $("#origen_pagos, #excedente, #inconsistente").change(function(event){
      table_admin.ajax.reload();
  
    });

    $(document).on('click', '#clean',  function(event) {
        $("#filter_uuid").val('');
        $("#filter_taxpayer_id").val('');
        $('#to').data('DateTimePicker').clear();
        $('#from').data('DateTimePicker').clear();
        $("#origen_pagos").prop("selectedIndex",0).change();
        //$('#from_val').val('');
        //$('#to_val').val('');
        table_admin.ajax.reload();
    });

    $(function() {
        $('#from').datetimepicker({
            locale: 'es',
            format: "DD MMMM YYYY",
            sideBySide: true

        });
        $('#to').datetimepicker({
            locale: 'es',
            format: "DD MMMM YYYY",
            sideBySide: true
        });


        $("#from").on("dp.change", function(e) {
            $('#to').data("DateTimePicker").minDate(e.date);
            if ($('#to_val').val() != "") {
                table_admin.ajax.reload();
            }

        });

        $("#to").on("dp.change", function(e) {
            $('#from').data("DateTimePicker").maxDate(e.date);
            if ($('#from_val').val() != "") {
                //table.ajax.reload();
                table_admin.ajax.reload();
            }
        });
    });

    $('.dtr-modal-content').on('click', '.shd', function(){
      var shd = $(this);
      var tr = $(this).closest('tr');
      var row = table_admin.row(tr);
      if ( row.child.isShown() ){
        //This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
        shd.text('Ver detalles');
        shd.removeClass('btn-danger');
        shd.addClass('btn-default');
      }else{
        row.child( format(row.data()) ).show();
        tr.addClass('shown');
        shd.text('Ocultar detalles');
        shd.addClass('btn-danger');
        shd.removeClass('btn-default');
      }  
    })
    $('#pagos_list tbody').on('click', '.shd', function(){
      var shd = $(this);
      var tr = $(this).closest('tr');
      var row = table_admin.row(tr);
      if ( row.child.isShown() ){
        //This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
        shd.text('Ver detalles');
        shd.removeClass('btn-danger');
        shd.addClass('btn-default');
      }else{
        row.child( format(row.data()) ).show();
        tr.addClass('shown');
        shd.text('Ocultar detalles');
        shd.addClass('btn-danger');
        shd.removeClass('btn-default');
      }
    });
  
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

});
