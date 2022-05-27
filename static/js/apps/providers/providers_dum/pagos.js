$(document).ready(function() {
    $('#providers_tag').addClass('active');
    $('#proveedores_origen_pagos').addClass('active');
    $('#providers_tag').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    /*=============================================Table for user=====================================*/
    aoColumns = [{
        'sWidth': '20%',
        'bSortable': false,
        'data': 'uuid',
        'className': 'bold text-center',
    },{
        'sWidth': '15%',
        'bSortable': false,
        'data': 'rfc',
    },{
        'sWidth': '15%',
        'bSortable': false,
        'data': 'fecha',
    },{
        'sWidth': '10%',
        'bSortable': false,
        'data': 'total',
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
    },{
        'sWidth': '10%',
        'bSortable': false,
        'data': 'restante',
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
    },{
        'sWidth': '20%',
        'bSortable': false,
        'data': 'estatus',
    },{
        'sWidth': '10%',
        'bSortable': false,
        'data': 'opciones',
    }
    ];
    



function format (d) {
    var tr = '<tr>';
    $.each(d.notification_detail, function(index, details){
        tr += '<td><b># Parcialidad: </b>' + details.Nparcialidad +'</td><td><b>UUID: </b>' + details.UUID + '</td><td><b>Fecha:</b> ' +  details.Fecha + '</td><td><b>Saldo Anterior:</b> ' +  details.SaldoAnterior +  '</td><td><b>Importe Pagado:</b> ' +  details.ImportePagado +'</td><td><b>Importe Pagado Insoluto:</b> ' +  details.ImportePagadoInsoluto +'</td><td><b>Estatus:</b> '+ details.Status +'</td></tr>'
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
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6],
            },
        ],
        'PagingType': 'full_numbers',
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
      //table_admin.ajax.reload();
    });
    
    $("#filter_taxpayer_id").keyup(function(e){
      e.preventDefault();
      size = $('#filter_taxpayer_id').val().length;
      if ((size>2 || size==0) && is_valid_key(e.which)){
        table_admin.ajax.reload(); //Using when is Datatable
      }
      //table_admin.ajax.reload();
    });
    $("#origen_pagos").change(function(event){
      table_admin.ajax.reload();
  
    });

    //$(document).on('click', '#clean',  function(event) {
    //    $("#filter_uuid").val('');
    //    $("#filter_taxpayer_id").val('');
    //    $('#to').data('DateTimePicker').clear();
    //    $('#from').data('DateTimePicker').clear();
    //    $("#origen_pagos").prop("selectedIndex",0).change();
    //    //$('#from_val').val('');
    //    //$('#to_val').val('');
    //    table_admin.ajax.reload();
    //});

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

        $('#to').datetimepicker({
            useCurrent: false //Important! See issue #1075
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
        $(document).on('click', '#clean',  function(event) {
            $("#filter_uuid").val('');
            $("#filter_taxpayer_id").val('');
            //$('#to').data('DateTimePicker').clear();
            //$('#from').data('DateTimePicker').clear();
            $("#origen_pagos").prop("selectedIndex",0).change();
            $('#from_val').val('');
            $('#to_val').val('');
            table_admin.ajax.reload();
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
  

});
