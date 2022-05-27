$(document).ready(function() {
    $('#cancelacion').addClass('active');
    $('#cancelacion').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
   
    aoColumns_emisor = [{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        'sWidth': '8%',
        'bSortable': false,
    }];

    aoColumns_receiver_p = [{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
    }];

    aoColumns_receiver_f = [{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '25%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
    }];

    aoColumns_history = [{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '30%',
        'bSortable': false,
    }];
    
    

    var table_emisor = $('#cancellation-emisor-table').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        "language": datatable_language,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns_emisor,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7,8,9],
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            aoData.push({
                "name": "oper",
                "value": 'list-cancel-emisor'
            });
            if ($('#uuid').val()){
                aoData.push({
                    "name": "uuid",
                    "value": $('#uuid').val()
                });
            }
            if ($("#date-from-e-res").val() && $("#date-to-e-res").val()){
                aoData.push({
                    "name": "date_from",
                    "value": $('#date-from-e-res').val()
                });
                aoData.push({
                    "name": "date_to",
                    "value": $('#date-to-e-res').val()
                });
            }
            if ($('#estado_sat').val() != 'A'){
                aoData.push({
                    "name": "estado_sat",
                    "value": $('#estado_sat').val()
                });
            }
            if ($('#estatus_cancelacion').val() != 'A'){
                aoData.push({
                    "name": "estatus_cancelacion",
                    "value": $('#estatus_cancelacion').val()
                });
            }
            if ($('#taxpayer_id_e').val()){
                aoData.push({
                    "name": "taxpayer_id",
                    "value": $('#taxpayer_id_e').val()
                });
            }
            if ($('#rtaxpayer_id_e').val()){
                aoData.push({
                    "name": "rtaxpayer_id",
                    "value": $('#rtaxpayer_id_e').val()
                });
            }
            if ($('#invoice_type').val() != 'A'){
                aoData.push({
                    "name": "invoice_type",
                    "value": $('#invoice_type').val()
                });
            }
            $.ajax( {
                "dataType": "json",
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    fnCallback(json);
            }
          });
        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover();
        }
    });


    var table_receiver_pending = $('#cancellation-receiver-table-p').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        "language": datatable_language,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns_receiver_p,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7],
            },
            { responsivePriority: 1, targets: 6 },
            { responsivePriority: 2, targets: 7 },
            { responsivePriority: 3, targets: 2 }
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            aoData.push({
                "name": "oper",
                "value": 'list-cancel-receiver-pending'
            });
            if ($('#uuid_p').val()){
                aoData.push({
                    "name": "uuid",
                    "value": $('#uuid_p').val()
                });
            }
            if ($("#date-from-pending-res").val() && $("#date-to-pending-res").val()){
                aoData.push({
                    "name": "date_from",
                    "value": $('#date-from-pending-res').val()
                });
                aoData.push({
                    "name": "date_to",
                    "value": $('#date-to-pending-res').val()
                });
            }
            if($('#taxpayer_p').val()){
                aoData.push({
                    "name": "taxpayer_id",
                    "value": $('#taxpayer_p').val()
                });
            }
            if ($('#invoice_type').val() != 'A'){
                aoData.push({
                    "name": "invoice_type",
                    "value": $('#invoice_type').val()
                });
            }

            $.ajax( {
                "dataType": "json",
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    fnCallback(json);
            }
          });
        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover();
        }
    });


    var table_receiver_finished = $('#cancellation-receiver-table-f').DataTable({
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
        "sDom": 'l<"toolbar">frtip',
        "language": datatable_language,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns_receiver_f,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5],
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            aoData.push({
                "name": "oper",
                "value": 'list-cancel-receiver-finished'
            });

            if ($('#uuid_finished').val()){
                aoData.push({
                    "name": "uuid",
                    "value": $('#uuid_finished').val()
                });
            }
            if ($("#date-from-d-res").val() && $("#date-to-d-res").val()){
                aoData.push({
                    "name": "date_from",
                    "value": $('#date-from-d-res').val()
                });
                aoData.push({
                    "name": "date_to",
                    "value": $('#date-to-d-res').val()
                });
            }
            if ($('#answer').val() != "B"){
               aoData.push({
                    "name": "answer",
                    "value": $('#answer').val()
                });
            }
            if ($('#estado_sat_finished').val() != "A"){
                aoData.push({
                    "name": "estado_sat",
                    "value": $('#estado_sat_finished').val()
                });
            }

            $.ajax( {
                "dataType": "json",
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    fnCallback(json);
            }
          });
        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover();
        }
    });


    function updateHistoryTable(uuid){
        $('#thistory').DataTable({
            responsive : true,
            'processing': true,
            'serverSide': true,
            'destroy': true,
            'columns': aoColumns_history,
            "language": datatable_language,
            "searching": false,
            "columnDefs": [
                {
                    className: "text-center",
                    "targets": [0,1,2,3,4],
                },
                { responsivePriority: 1, targets: 0 },
                { responsivePriority: 2, targets: 2 },
                { responsivePriority: 3, targets: 3 }
            ],
            'ajax': ({
                //pages: 20,
                stateSave: true,
                method: 'POST',
                url: '/cancel/history/',
                data: {
                    'uuid': uuid,
                    'csrfmiddlewaretoken': token,
                }
            })
        });
    }

    /* ============================ FILTRADO LISTA DE CANCELACIONES ============================ */
    $("#uuid").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_emisor.ajax.reload()
        }
    });
    $("#taxpayer_id_e").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_emisor.ajax.reload()
        }
    });
    $("#rtaxpayer_id_e").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_emisor.ajax.reload()
        }
    });
    $('#estado_sat').change( function(e){
        table_emisor.ajax.reload()
    });
    $('#estatus_cancelacion').change( function(e){
        table_emisor.ajax.reload()
    });
    $(function () {
        $("#date-from-e, #date-to-e").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY",
            sideBySide: true
        });
        $("#date-from-e").on("dp.change", function(e) {
             $('#date-to-e').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-e-res").val() != '' && $("#date-from-e-res").val() != '') {
             table_emisor.ajax.reload()
           }
        });
        $("#date-to-e").on("dp.change", function(e) {
             $('#date-from-e').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-e-res").val() != '' && $("#date-to-e-res").val() != '') {
             table_emisor.ajax.reload()
           }
        });
    });

    $('#invoice_type').change( function(e){
        table_emisor.ajax.reload()
    });

    /* ============================ FILTRADO HISTORIAL DE SOLICITUDES ============================ */
    $("#uuid_finished").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_receiver_finished.ajax.reload()
        }
    });
    $(function () {
        $("#date-from-d, #date-to-d").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY",
            sideBySide: true
        });

        $("#date-from-d").on("dp.change", function(e) {
             $('#date-to-d').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-d-res").val() != '' && $("#date-from-d-res").val() != '') {
             table_receiver_finished.ajax.reload()
           }
        });
        $("#date-to-d").on("dp.change", function(e) {
             $('#date-from-d').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-d-res").val() != '' && $("#date-to-d-res").val() != '') {
             table_receiver_finished.ajax.reload()
           }
        });
    });

    $('#answer').change(function(e) {
        table_receiver_finished.ajax.reload()
    });
    $('#estado_sat_finished').change( function(e){
        table_receiver_finished.ajax.reload()
    });

    /* ============================ FILTRADO SOLICITUDES PENDIENTES ============================ */
    $("#uuid_p").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_receiver_pending.ajax.reload()
        }
    });
    $(function () {
        $("#date-from-pending, #date-to-pending").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY",
            sideBySide: true
        });
        $("#date-from-pending").on("dp.change", function(e) {
             $('#date-to-pending').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-pending-pending-res").val() != '' && $("#date-from-pending-pending-res").val() != '') {
             table_receiver_pending.ajax.reload()
           }
        });
        $("#date-to-pending").on("dp.change", function(e) {
             $('#date-from-pending').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-pending-res").val() != '' && $("#date-to-pending-pending-res").val() != '') {
             table_receiver_pending.ajax.reload()
           }
        });
    });
    $("#taxpayer_p").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_receiver_pending.ajax.reload()
        }
    });
    $('#invoice_type').change( function(e){
        table_receiver_pending.ajax.reload()
    });


    /* ============================ FUNCION MENSAJES DE ERROR ============================ */
    function error_message(message){
            $.toast({
                heading: "Error",
                text: message,
                showHideTransition: "fade",
                icon: "error",
                position: "top-right",
            });
    }

    /* ============================ FUNCION MENSAJES EXITOSOS ============================ */
    function success_message(message){
        $.toast({
            heading: "Correcto",
            text: message,
            showHideTransition: "fade",
            icon: "success",
            position: "top-right",
        });
    }

    $(document).on("click", "#clean-d-emisor",  function(event) {
        $("#uuid").val("");
        $("#date-from-e-res").val("");
        $("#date-to-e-res").val("");
        $("#estado_sat").prop("selectedIndex",0).change();
        $("#estatus_cancelacion").prop("selectedIndex",0).change();
        $("#taxpayer_id_e").val("");
        $("#rtaxpayer_id_e").val("");
        $("#invoice_type").prop("selectedIndex",0).change();
        table_emisor.ajax.reload();
    });

    $(document).on("click", "#clean-d-receiver-pending",  function(event) {
        $("#uuid_p").val("");
        $("#taxpayer_p").val("");
        $("#date-to-pending-res").val("");
        $("#date-from-pending-res").val("");
        $("#invoice_type").prop("selectedIndex",0).change();
        table_receiver_pending.ajax.reload();
    });

    $(document).on("click", "#clean-d-receiver-finished",  function(event) {
        $("#uuid_finished").val("");
        $("#date-from-d-res").val("");
        $("#date-to-d-res").val("");
        $("#answer").prop("selectedIndex",0).change();
        $("#estado_sat_finished").prop("selectedIndex",0).change();
        table_receiver_finished.ajax.reload();
    });


    $("#refresh_emisor").click(function() {
        table_emisor.ajax.reload();
    });
    
    $("#refresh_receiver-pending").click(function() {
        table_receiver_pending.ajax.reload();
    });

    $("#refresh_receiver-finished").click(function() {
        table_receiver_finished.ajax.reload();
    });

    /*============= btn for accept/recject request cancel =============*/
    $(document).on("click", ".accept_reject",  function(event) {
        templete = '<div style="width: 25px; height: 25px; margin: 0 auto;" class="loader" id="loader"></div>';
        var answer = '';
        var td = $(this).parents("tr").find("td");
        var answer = td.find('input:checked').attr('value');
        if (answer == 'A' || answer == 'R'){
            var btn = td.find('.accept_reject');
            var uuid = btn.attr('uuid');
            btn.hide();
            $(this).parents("tr").find("td:eq(7)").append(templete);
            var loader = $(this).parents("tr").find("td:eq(7)").find('div')
            var adata = new FormData()
            adata.append('csrfmiddlewaretoken', token);
            adata.append('answer', answer);
            adata.append('uuid', uuid);
            $.ajax({
                type: 'POST',
                url: '/cancel/answer/',
                data: adata,
                dataType: 'json',
                cache: false,
                contentType: false,
                processData: false
            }).done(function(json) {
                if (json.success == true) {
                    success_message(json.message)
                    table_receiver_pending.ajax.reload(); 
                } else {
                    error_message(json.message)
                    loader.remove();
                    btn.show();
                }
            });
        }else{
            message = "Selecciona una respuesta";
            error_message(message); 
        }
    });

    /*============= btn history accept/recject request cancel =============*/
    $(document).on("click", ".ch",  function(e) {
        e.preventDefault();
        var data = table_receiver_finished.row($('#cancellation-receiver-table-f tbody').parents('tr')).data();
        if(!data){
          var uuid = $(this).attr('uuid');
        }else{
          var uuid = data[1];
        }
        
        $('#strong-taxpayer-csd').text(uuid);
        $('#modal-history').modal('show');
        updateHistoryTable(uuid);        
    });

    /*================== btn consult get_sat_status =====================*/
    $(document).on("click", ".get_sat_status",  function(e) {
        e.preventDefault();
        if($(this).attr('total') == ''){
            templete = '<div style="width: 34px; height: 34px; margin: 0 auto;" class="loader" id="loader"></div>';
            var uuid = $(this).closest('tr').children('td:eq(1)').text();
            var btn = $(this).closest('tr').children('td:eq(5)').find('button');
            btn.hide();
            $(this).parents("tr").find("td:eq(5)").append(templete);
            var loader = $(this).parents("tr").find("td:eq(5)").find('div')
            var adata = new FormData()
            adata.append('csrfmiddlewaretoken', token);
            adata.append('option', 'receiver');
            adata.append('uuid', uuid);

        }
        else{
            templete = '<div style="width: 34px; height: 34px; margin: 0 auto;" class="loader" id="loader"></div>';
            var taxpayer_id = $(this).closest('tr').children('td:eq(5)').text();
            var rtaxpayer_id = $(this).closest('tr').children('td:eq(6)').text();
            var uuid = $(this).closest('tr').children('td:eq(1)').text();
            var total = $(this).closest('tr').children('td:eq(9)').find('button').attr('total');
            var btn = $(this).closest('tr').children('td:eq(9)').find('button');
            btn.hide();
            $(this).closest('tr').children('td:eq(9)').append(templete);
            var loader = $(this).closest('tr').children('td:eq(9)').find('div')
            var adata = new FormData()
            adata.append('csrfmiddlewaretoken', token);
            adata.append('option', 'emisor');
            adata.append('taxpayer_id', taxpayer_id);
            adata.append('rtaxpayer_id', rtaxpayer_id);
            adata.append('uuid', uuid);
            adata.append('total', total);
        }
        $.ajax({
            type: 'POST',
            url : '/cancel/consult_status/',
            data : adata,
            dataType : 'json',
            cache : false,
            contentType: false,
            processData: false
        }).done(function(json) {
            if (json.success == true) {
                success_message(json.message)
                table_emisor.ajax.reload();
                loader.remove();
                btn.show(); 
                table_receiver_finished.ajax.reload()
            } else {
                loader.remove();
                btn.show();
                error_message(json.message)
            }
        });
    });



   /*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
   /*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
   aoColumns_provider = [{
       'sWidth': '10%',
       'bSortable': false,
       },{
       'sWidth': '20%',
       'bSortable': false,
       },{
       'sWidth': '10%',
       'bSortable': false,
       },{
       'sWidth': '8%',
       'bSortable': false,
       },{
       'sWidth': '8%',
       'bSortable': false,
       },{
       'sWidth': '10%',
       'bSortable': false,
       },{
       'sWidth': '8%',
       'bSortable': false,
       },{
       'sWidth': '8%',
       'bSortable': false,
       'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
   }];


   var table_provider = $('#cancellation-provider-table').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        "language": datatable_language,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns_provider,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7],
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            aoData.push({
                "name": "oper",
                "value": 'list-cancel-provider'
            });
            if ($('#p_uuid').val()){
                aoData.push({
                    "name": "uuid",
                    "value": $('#p_uuid').val()
                });
            }
            if ($("#date-from-pro-res").val() && $("#date-to-pro-res").val()){
                aoData.push({
                    "name": "date_from",
                    "value": $('#date-from-pro-res').val()
                });
                aoData.push({
                    "name": "date_to",
                    "value": $('#date-to-pro-res').val()
                });
            }
            if ($('#p_estado_sat').val() != 'A'){
                aoData.push({
                    "name": "estado_sat",
                    "value": $('#p_estado_sat').val()
                });
            }
            if ($('#p_estatus_cancelacion').val() != 'A'){
                aoData.push({
                    "name": "estatus_cancelacion",
                    "value": $('#p_estatus_cancelacion').val()
                });
            }
            if ($('#p_taxpayer_id_e').val()){
                aoData.push({
                    "name": "taxpayer_id",
                    "value": $('#p_taxpayer_id_e').val()
                });
            }
            if ($('#p_rtaxpayer_id_e').val()){
                aoData.push({
                    "name": "rtaxpayer_id",
                    "value": $('#p_rtaxpayer_id_e').val()
                });
            }
            if ($('#p_invoice_type').val() != 'A'){
                aoData.push({
                    "name": "invoice_type",
                    "value": $('#p_invoice_type').val()
                });
            }
            $.ajax( {
                "dataType": "json",
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    fnCallback(json);
            }
          });
        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover();
        }
    });



       $("#p_uuid").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_provider.ajax.reload()
        }
    });
    $("#p_taxpayer_id_e").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_provider.ajax.reload()
        }
    });
    $("#p_rtaxpayer_id_e").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          table_provider.ajax.reload()
        }
    });
    $('#p_estado_sat').change( function(e){
        table_provider.ajax.reload()
    });
    $('#p_estatus_cancelacion').change( function(e){
        table_provider.ajax.reload()
    });
    $(function () {
        $("#date-from-pro, #date-to-pro").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY",
            sideBySide: true
        });
        $("#date-from-pro").on("dp.change", function(e) {
             $('#date-to-pro').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-pro-res").val() != '' && $("#date-from-pro-res").val() != '') {
             table_provider.ajax.reload()
           }
        });
        $("#date-to-pro").on("dp.change", function(e) {
             $('#date-from-pro').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-pro-res").val() != '' && $("#date-to-pro-res").val() != '') {
             table_provider.ajax.reload()
           }
        });
    });
    $('#p_invoice_type').change( function(e){
        table_provider.ajax.reload()
    });


        $(document).on("click", "#p_clean-d-provider",  function(event) {
        $("#p_uuid").val("");
        $("#date-from-pro-res").val("");
        $("#date-to-pro-res").val("");
        $("#p_estado_sat").prop("selectedIndex",0).change();
        $("#p_estatus_cancelacion").prop("selectedIndex",0).change();
        $("#p_taxpayer_id_e").val("");
        $("#p_rtaxpayer_id_e").val("");
        $("#p_invoice_type").prop("selectedIndex",0).change();
        table_provider.ajax.reload();
    });
    /*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
     /*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

});

