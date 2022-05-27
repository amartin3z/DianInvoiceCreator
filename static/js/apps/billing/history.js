$(document).ready(function() {
    $('#reportes').addClass('active');
    $('#reportes').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;

    columns_billing_history = [{
        sWidth: '10%',
        'className': 'bold text-center',
        bSortable: false,
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '10%',
        bSortable: false,
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5.5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '6%',
        bSortable: false,
        },{
        sWidth: '6%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '6%',
        bSortable: false,
        },{
        sWidth: '7%',
        bSortable: true,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
    }];


    var billing_history_table = $('#tbillinhistory').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'columns': columns_billing_history,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
            },
        ],
        'language': datatable_language,
        'stateSave': true,
        'searching': false,
        sAjaxSource: url_status,
        'fnServerData': function(sSource, aoData, fnCallback){
            aoData.push({
                'name': 'csrfmiddlewaretoken',
                'value': getCookie('csrftoken')
            });

            if ($('#select_status_branch').val()){
                aoData.push({
                    "name": "status",
                    "value": $('#select_status_branch').val()
                });
            }

            if($('#taxpayer_history').val() != ''){
                aoData.push({
                    'name': 'taxpayer_history',
                    'value': $('#taxpayer_history').val()
                })
            }

            $.ajax({
                'dataType': 'json',
                'type': 'POST',
                "url": sSource,
                'data': aoData,
                'success': function(json){
                    fnCallback(json);
                }
            });

        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover({html:true});
        }
    });

    /* draw tables*/    
    $('#refresh_invoices').click(function() {
        billing_history_table.ajax.reload();
    });

    $('#clean-filter').on('click', function(){
        $("#select_status_branch").prop("selectedIndex",0).change();
        $("#taxpayer_history").val('');
        billing_history_table.ajax.reload();
    });
    
    $('#select_status_branch').change( function(e){
        billing_history_table.ajax.reload()
    });

    $("#taxpayer_history").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 3 || len == 0) && is_valid_key(e.which)) { 
          billing_history_table.ajax.reload()
        }
    });

   /* $(function () {
        $("#date-from, #date-to").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY HH:mm:ss",
            sideBySide: true
        });

        $("#date-from").on("dp.change", function(e) {
             $('#date-to').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-val").val() != '' && $("#date-from-val").val() != '') {
             billing_history_table.ajax.reload()
           }
        });
        $("#date-to").on("dp.change", function(e) {
             $('#date-from').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-val").val() != '' && $("#date-to-val").val() != '') {
             billing_history_table.ajax.reload()
           }
        });
    });*/
    
/*===============================HISTORY RECEIPT==============================00*/


    var datatablebilling_history = $("#tbilling_history").DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7,8,9,10,11,12],
            },
        ],
        'language': datatable_language,
        'stateSave': true,
        'searching': false,
        sAjaxSource: url_status,
        aoColumns: [
          {sWidth: "8%",
            'className': 'bold text-center',
            bSortable: false,
          },{
            sWidth: "5%",
            bSortable: false,
            'className': 'text-center',
          },{
            sWidth: "5%",
            bSortable: false,
             'className': 'bold text-center',
          },{
            sWidth: "5%",
            bSortable: false,
          },
          {sWidth: "8%",
            bSortable: true,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: "10%",
            bSortable: true,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: "10%",
            bSortable: true,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: "10%",
            bSortable: true,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: "10%",
            bSortable: true,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          }],

        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": getCookie('csrftoken')
            });
            if ($("#status").val() != "V"){
                aoData.push({
                    "name": "oper",
                    "value": 'C'
                });
            }else{
                aoData.push({
                    "name": "oper",
                    "value": 'V'
                });
            }
            if($('#taxpayer_id').val()){
                aoData.push({  
                    "name": "taxpayer_id",
                    "value": $('#taxpayer_id').val()
                })
            }

            $.ajax( {
              "dataType": 'json',
              "type": "POST",
              "url": sSource,
              "data": aoData,
              "success": function(json) {
                fnCallback(json);
              }
            });
        },
        'drawCallback': function(settings){
            $('[data-toggle="popover"]').popover({html:true});
        }

    
    });
    
    $("#status").change(function(e) {
        datatablebilling_history.draw();
    });

    $("#taxpayer_id").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          datatablebilling_history.ajax.reload()
        }
    });

    $('#refresh_invoices').click(function() {
        datatablebilling_history.ajax.reload();
    });

    $('#clean-filter').on('click', function(){
        $("#status").prop('selectedIndex',0).change();
        $("#taxpayer_id").val('');
        datatablebilling_history.ajax.reload();
    });

    $('#clean-filter').click(function() {
        datatablebilling_history.ajax.reload();
    });
    /*$('#date-from').keyup(function(e) {
        e.preventDefault();
        var value = $('#date-from').val();
            datatablebilling_history.dataTable().fnDraw();
    });
    $(function () {
        $("#date-from, #date-to").datetimepicker({
            locale: "es",
            format: "DD MMMM YYYY HH:mm:ss",
            sideBySide: true
        });

        $("#date-from").on("dp.change", function(e) {
             $('#date-to').data("DateTimePicker").minDate(e.date);
           if ($("#date-to-val").val() != '' && $("#date-from-val").val() != '') {
             datatablebilling_history.ajax.reload()
           }
        });
        $("#date-to").on("dp.change", function(e) {
             $('#date-from').data("DateTimePicker").maxDate(e.date);
           if ($("#date-from-val").val() != '' && $("#date-to-val").val() != '') {
             datatablebilling_history.ajax.reload()
           }
        });
    });*/

    $('#download_report_receipt').change(function(event) {
        $("#download_report_receipt").attr("disabled", true);
        report_type = $("#download_report_receipt").val()
        if (["csv", "xlsx"].indexOf(report_type) == -1) {
            $("#download_report_receipt").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        token = getCookie('csrftoken');
        data = [{
            "name": "csrfmiddlewaretoken",
            "value": token
        }];
        
        data.push({
            "name": "oper",
            "value": "list-downloads"
        });
        
        data.push({
            "name": "month",
            "value": month
        });

        data.push({
            "name": "year",
            "value": year
        });

        if ($("#status").val() != "V"){
            data.push({
                "name": "oper",
                "value": 'C'
            });
        }else{
            data.push({
                "name": "oper",
                "value": 'V'
            });
        }
        if($('#taxpayer_id').val()){
            data.push({  
                "name": "taxpayer_id",
                "value": $('#taxpayer_id').val()
            })
        }       

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_history_receipt/',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(response) {
            $("#download_report").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $(document.body).css({"cursor" : "default"});
            if (response.success) {
                window.open(response.url);
            } else {
                error_message(response.message)
            }
        }).fail(function(jqXHR, status, errorThrown) {
            $("#download_report_receipt").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
            $(document.body).css({"cursor" : "default"});
        });
        
        $('#download_report_receipt').val("select").change();
    });


    $('#download_report_emision').change(function(event) {
        $("#download_report_emision").attr("disabled", true);
        report_type = $("#download_report_emision").val()
        if (["csv", "xlsx"].indexOf(report_type) == -1) {
            $("#download_report_emision").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        token = getCookie('csrftoken');
        data = [{
            "name": "csrfmiddlewaretoken",
            "value": token
        }];
        
        data.push({
            "name": "oper",
            "value": "list-downloads"
        });
        
        data.push({
            "name": "month",
            "value": month
        });

        data.push({
            "name": "year",
            "value": year
        });
        
        if ($("#select_status_branch").val() != "V"){
            data.push({
                "name": "oper",
                "value": 'C'
            });
        }else{
            data.push({
                "name": "oper",
                "value": 'V'
            });
        }
        if($('#taxpayer_history').val()){
            data.push({  
                "name": "taxpayer_id",
                "value": $('#taxpayer_history').val()
            })
        }       

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_history_emision/',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(response) {
            $("#download_report").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $(document.body).css({"cursor" : "default"});
            if (response.success) {
                window.open(response.url);
            } else {
                error_message(response.message)
            }
        }).fail(function(jqXHR, status, errorThrown) {
            $("#download_report_emision").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
            $(document.body).css({"cursor" : "default"});
        });
        
        $('#download_report_emision').val("select").change();
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


});

