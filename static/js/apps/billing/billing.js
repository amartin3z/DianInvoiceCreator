$(document).ready(function() {
    $('#reportes').addClass('active');
    $('#reportes').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    columns_billing = [{
        sWidth: '6.5%',
        'className': 'bold text-center',
        bSortable: false,
        },{
        sWidth: '9%',
        bSortable: false,
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5.5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '6%',
        bSortable: false,
        },{
        sWidth: '6%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '8%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '6%',
        bSortable: false,
        },{
        sWidth: '7%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '5%',
        bSortable: false,
    }];
    
    var billing_table = $('#tbilling').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'columns': columns_billing,
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
            
            if ($('#select_status').val()){
                aoData.push({
                    "name": "status",
                    "value": $('#select_status').val()
                });
            }

            if ($('#select_year').val() != 'T'){
                aoData.push({
                    "name": "year",
                    "value": $('#select_year').val()
                });
            }
            if ($('#select_month').val() != 'T'){
                aoData.push({
                    "name": "month",
                    "value": $('#select_month').val()
                });
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
            $('[data-toggle="popover"]').popover();
        }
    });

    /* draw tables*/    
    $('#refresh_invoices').click(function() {
        billing_table.ajax.reload();
    });

    $('#clean-filter').on('click', function(){
        $("#select_year, #select_month, #select_status").prop("selectedIndex",0).change();
        billing_table.ajax.reload();
    });

    $('#select_year, #select_month, #select_status').change( function(e){
        billing_table.ajax.reload()
    });

/*================================BILLING RECEIPT==================================*/
    var datatablebilling_receipt = $("#tbilling_receipt").DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'language': datatable_language,
        'stateSave': true,
        'searching': false,
        sAjaxSource: url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7,8,9,10,11,12],
            },
        ],
        aoColumns: [
          {sWidth: '5%',
            'className': 'bold text-center',
            bSortable: false,
          },
          {sWidth: '5%',
            bSortable: false,
          },
          { sWidth: '5%',
            bSortable: false,
          },
          {sWidth: '10%',
            bSortable: false,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: '8%',
            bSortable: false,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: '10%',
            bSortable: false,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: '10%',
            bSortable: false,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
          },
          {sWidth: '10%',
            bSortable: false,
            'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
          },
          {sWidth: "5%",
            bSortable: false,
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
            if ($("#month").val() != "A") {
                aoData.push({
                    "name": "month",
                    "value": $("#month").val()
                });                 
            }
            
            if ($("#year").val() !="T") {
                aoData.push({
                    "name": "year",
                    "value": $("#year").val()
                });
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
            $('[data-toggle="popover"]').popover();
        }

    });

    $("#status").change(function(e) {
        datatablebilling_receipt.draw();
    });
    $("#month").change(function(e) {
        datatablebilling_receipt.draw();
    });
    
    $("#year").change(function(e) {
        datatablebilling_receipt.draw();
    });

    $(document).on('click', '#clean-filter',  function(event) {
        $("#status").prop('selectedIndex',0).change();
        $("#month").prop('selectedIndex',0).change();
        $('#year').prop('selectedIndex',0).change();
        datatablebilling_receipt.ajax.reload();
    });

    $('#clean-filter').click(function() {
        datatablebilling_receipt.ajax.reload();
    });

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
        

        if ($("#month").val() != "A") {
            data.push({
                "name": "month",
                "value": $("#month").val()
            });                 
        }
        
        if ($("#year").val() !="T") {
            data.push({
                "name": "year",
                "value": $("#year").val()
            });
        }

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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_billing_receipt/',
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
        

        if ($("#select_month").val() != "T") {
            data.push({
                "name": "month",
                "value": $("#select_month").val()
            });                 
        }
        
        if ($("#select_year").val() !="T") {
            data.push({
                "name": "year",
                "value": $("#select_year").val()
            });
        }

        if ($("#select_status").val() != "V"){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_billing_emision/',
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

