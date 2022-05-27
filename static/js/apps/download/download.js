$(document).ready(function() {

    /*============= Downloads =============*/
    $("#date-from-d").datetimepicker({
        locale: "es",
        format: 'DD/MM/YYYY HH:mm:ss',
        useCurrent:false,
        sideBySide: true
    });
    $("#date-to-d").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    /*============= Searches =============*/
    $("#date-from-s").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    $("#date-to-s").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    /*============= Packages =============*/
    $("#date-from-p").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    $("#date-to-p").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    
    //var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    $('#descarga_sat').addClass('active');    

    aoColumns = [{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '19%',
        'bSortable': false,
        },{
        'sWidth': '8%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
        },{
        'sWidth': '8%',
        'bSortable': false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
        },{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '5%',
        'bSortable': false,
        }];

    aoColumns_searches = [{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '15%',
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
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
    }];

    aoColumns_packages = [{
        'sWidth': '8%',
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
        'sWidth': '6%',
        'bSortable': false,
        },{
        'sWidth': '7%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '7%',
        'bSortable': false,
        },{
          'sWidth': '7%',
          'bSortable': false,
        }

    ];

    aoColumns_dpackages = [
        {
            'sWidth': '15%',
            'bSortable': false,
        },{
            'sWidth': '24%',
            'bSortable': false,
        },{
            'sWidth': '22%',
            'bSortable': false,
        },{
            'sWidth': '22%',
            'bSortable': false,
        },{
            'sWidth': '17%',
            'bSortable': false,
        }
    ];

    var table_searches = $('#sat-searches').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        language: datatable_language,
        "bProcessing": true,
        "bServerSide": true,
         stateSave: true,
        "searching": false,
        "columns": aoColumns_searches,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": "_all",
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": getCookie('csrftoken')
            });
            aoData.push({
                "name": "oper",
                "value": "list-searches"
            });
            if ($("#search-id").val()) {
                aoData.push({
                    "name": "search_id",
                    "value": $("#search-id").val()
                });
            }
            if ($("#status-search").val() != "A") {
                aoData.push({
                    "name": "status",
                    "value": $("#status-search").val()
                });
            }
            if ($("#type-search").val() != "A") {
                aoData.push({
                    "name": "type",
                    "value": $("#type-search").val()
                });
            }
            if ($("#type-data").val() != "A") {
                aoData.push({
                    "name": "type_data",
                    "value": $("#type-data").val()
                });
            }
            var date_from_obj = $('#date-from-s').data('DateTimePicker').date();
            var date_to_obj = $('#date-to-s').data('DateTimePicker').date();
            if (date_from_obj !== null && date_to_obj !== null) {
                var date_from_str = date_from_obj.format('YYYY-MM-DD');
                var date_to_str = date_to_obj.format('YYYY-MM-DD');
                aoData.push({
                    "name": "date_from",
                    "value": date_from_str
                });

                aoData.push({
                    "name": "date_to",
                    "value": date_to_str
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
        drawCallback: function(settings){
            $('[data-toggle="popover"]').popover({
              placement: 'top'
            });
        },
    });

    var table_packages = $('#sat-packages').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        language: datatable_language,
        "bProcessing": true,
        "bServerSide": true,
         stateSave: true,
        "searching": false,
        "columns": aoColumns_packages,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": "_all",
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": getCookie('csrftoken')
            });
            aoData.push({
                "name": "oper",
                "value": "list-packages"
            });
            if ($("#status-package").val() != "A") {
                aoData.push({
                    "name": "status",
                    "value": $("#status-package").val()
                });
            }
            if ($("#package-id").val()) {
                aoData.push({
                    "name": "package_id",
                    "value": $("#package-id").val()
                });
            }
            if ($("#type-search-p").val() != "A") {
                aoData.push({
                    "name": "type_search",
                    "value": $("#type-search-p").val()
                });
            }
            if ($("#type-package").val() != "A") {
                aoData.push({
                    "name": "type",
                    "value": $("#type-package").val()
                });
            }
            var date_from_obj = $('#date-from-p').data('DateTimePicker').date();
            var date_to_obj = $('#date-to-p').data('DateTimePicker').date();
            if (date_from_obj !== null && date_to_obj !== null) {
                var date_from_str = date_from_obj.format('YYYY-MM-DD');
                var date_to_str = date_to_obj.format('YYYY-MM-DD');
                aoData.push({
                    "name": "date_from",
                    "value": date_from_str
                });
                aoData.push({
                    "name": "date_to",
                    "value": date_to_str
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
        drawCallback: function(settings){
            $('[data-toggle="popover-package-invoices"]').popover({
              placement: 'top'
            });
        },
    });
    
    var table_downloads = $('#sat-downloads').DataTable({
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
            lenColumns = table_downloads.columns().header().length;
            for (col=0; col<lenColumns; col++){
                var datatableCol = table_downloads.column(col);
                if(default_columns.indexOf(col) > -1){
                    if(!datatableCol.visible())
                        datatableCol.visible(true)
                    $("#multi-select").dropdown('set selected', col + "");
                }else{
                    if(datatableCol.visible())
                        datatableCol.visible(false)
                }
            }
          },
        "sDom": 'l<"toolbar">frtip',
        "language": datatable_language,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-left",
                "targets": [5],
            },
            {
                className: "text-right",
                "targets": [7, 8],
            },
            {
                className: "text-center",
                "targets": [0,1,2,3,4,6,7,9,10,11,12, -1],
            },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": getCookie('csrftoken')
            });
            aoData.push({
            "name": "oper",
                "value": 'list-downloads'
            });
            aoData.push({
                "name": "sent_received",
                "value": $("#sent_received").val()
            });
            if ($("#status").val() != "A") {
                aoData.push({
                    "name": "status",
                    "value": $("#status").val()
                });
            }
            aoData.push({
                "name": "type",
                "value": $("#type").val()
            });
            if ($("#uuid").val()) {
                aoData.push({
                    "name": "uuid",
                    "value": $("#uuid").val()
                });
            }
            if ($("#taxpayer_id").val()){
                aoData.push({
                    "name": "taxpayer_id",
                    "value": $("#taxpayer_id").val()
                });
            }
            if ($("#date-from-d-val").val() && $("#date-to-d-val").val()){
                aoData.push({
                    "name": "date_from",
                    "value": $("#date-from-d-val").val()
                });
                aoData.push({
                    "name": "date_to",
                    "value": $("#date-to-d-val").val()
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

    $('#download_report').change(function(event) {
        $("#download_report").attr("disabled", true);
        report_type = $("#download_report").val()
        if (["csv"].indexOf(report_type) == -1) {
            $("#download_report").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        
        data = [{
            "name": "csrfmiddlewaretoken",
            "value": getCookie('csrftoken')
        }];
        
        data.push({
            "name": "oper",
            "value": "list-downloads"
        });
        
        data.push({
            "name": "sent_received",
            "value": $('#sent_received').val()
        });
        if ($("#taxpayer_id").val()){
            data.push({
                "name": "taxpayer_id",
                "value": $('#taxpayer_id').val()
            });
        }
        if ($("#type").val() != "A") {
            data.push({
                "name": "type",
                "value": $("#type").val()
            });
        }
        if ($("#status").val() != "A") {
            data.push({
                "name": "status",
                "value": $("#status").val()
            });
        }
        var date_from_obj = $('#date-from-d').data('DateTimePicker').date();
        var date_to_obj = $('#date-to-d').data('DateTimePicker').date();
        if (date_from_obj !== null && date_to_obj !== null) {
            var date_from_str = date_from_obj.format('YYYY-MM-DD');
            var date_to_str = date_to_obj.format('YYYY-MM-DD');
            data.push({
                "name": "date_from",
                "value": date_from_str
            });
            data.push({
                "name": "date_to",
                "value": date_to_str
            });
        }
        if ($('#uuid').val()) {
            data.push({
                "name": "uuid",
                "value": $('#uuid').val()
            });
        }

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/download/generatereport/',
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
            $("#download_report").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
            $(document.body).css({"cursor" : "default"});
        });
        
        $('#download_report').val("select").change();
      });

    $("#taxpayer_id").keyup(function(e) {
        len = $(this).val().length
        if ((0==len || len>12) && is_valid_key(e.which)) { // You can use "e.keyCode" for other browsers
            table_downloads.draw();
        }
    });
    $("#uuid").keyup(function(e) {
        len = $(this).val().length
        if ((0==len || len>35) && is_valid_key(e.which)) { // You can use "e.keyCode" for other browsers
            table_downloads.draw();
        }
    });
    $("#sent_received").change(function(e) {
        if ($(this).val() == 'received') {
            $("#label_issuing_receiver").text("Emisor");
        } else {
            $("#label_issuing_receiver").text("Receptor");
        }
        table_downloads.draw();
    });
    $("#status").change(function(e) {
        table_downloads.draw();
    });
    $("#type").change(function(e) {
        table_downloads.draw();
    });
    $("#date-from-d").on("dp.change", function(e) {
        if ($('#date-from-d-val').val() != "") {
            $('#date-to-d').data("DateTimePicker").minDate(e.date);
            table_downloads.draw();
        }
    });
    $("#date-to-d").on("dp.change", function(e) {
        if ($('#date-to-d-val').val() != "") {
            $('#date-from-d').data("DateTimePicker").maxDate(e.date);
            table_downloads.draw();
        }
    });
    
    $("#status-search").change(function(e) {
        table_searches.draw();
    });
    $("#search-id").keyup(function(e) {
        len = $(this).val().length
        if ((0==len || len>35) && is_valid_key(e.which)) { // You can use "e.keyCode" for other browsers
            table_searches.draw();
        }
    });
    $("#type-search").change(function(e) {
        table_searches.draw();
    });
    $("#type-data").change(function(e) {
        table_searches.draw();
    });
    $("#date-from-s").on("dp.change", function(e) {
        if ($('#date-from-s-val').val() != "") {
            $('#date-to-s').data("DateTimePicker").minDate(e.date);
            table_searches.draw();
        }
    });
    $("#date-to-s").on("dp.change", function(e) {
        if ($('#date-to-s-val').val() != "") {
            $('#date-from-s').data("DateTimePicker").maxDate(e.date);
            table_searches.draw();
        }
    });

    $("#status-package").change(function(e) {
        table_packages.draw();
    });
    $("#package-id").keyup(function(e) {
        len = $(this).val().length
        if ((0==len || len>35) && is_valid_key(e.which)) { // You can use "e.keyCode" for other browsers
            table_packages.draw();
        }
    });
    $("#type-search-p").change(function(e) {
        table_packages.draw();
    });
    $("#type-package").change(function(e) {
        table_packages.draw();
    });
    $("#date-from-p").on("dp.change", function(e) {
        if ($("#date-from-p-val").val() != "") {
            $('#date-to-p').data("DateTimePicker").minDate(e.date);
            table_packages.draw();
        }
    });
    $("#date-to-p").on("dp.change", function(e) {
        if ($("#date-to-p-val").val() != "") {
            $('#date-from-p').data("DateTimePicker").maxDate(e.date);
            table_packages.draw();
        }
    });
    
    $(document).on("click", "#clean-search",  function(event) {
        $('#date-from-s').data('DateTimePicker').date(null)
        $('#date-to-s').data('DateTimePicker').date(null)
        $("#status-search, #type-search, #type-data").prop("selectedIndex",0).change();
        $('#searches-filters input').val("");
        table_searches.ajax.reload();
    });

    $(document).on("click", "#clean-package",  function(event) {
        $('#date-from-p').data('DateTimePicker').date(null)
        $('#date-to-p').data('DateTimePicker').date(null)
        $("#status-package, #type-search-p, #type-package").prop("selectedIndex",0).change();
        $('#packages-filters input').val("");
        table_packages.ajax.reload();
    });

    $(document).on("click", "#clean-d",  function(event) {
        $("#sent_received, #status, #type").prop("selectedIndex",0).change();
        $('#download-filters input').val("");
        table_downloads.ajax.reload();
    });
   
    $("#refresh_downloads").click(function() {
        table_downloads.ajax.reload();
    });
    
    $("#refresh_searches").click(function() {
        table_searches.ajax.reload();
    });
    
    $("#refresh_packages").click(function() {
        table_packages.ajax.reload();
    });

    $('#multi-select').dropdown();
    $('.ui.multiple.dropdown').dropdown({
        onAdd: function (value, text, $selected) {
            var column = table_downloads.column($selected.attr('data-value'));
            visible = column.visible();
            if (visible)
                return
            column.visible(!visible);
        },
        onRemove: function (value, text, $selected) {
          var column = table_downloads.column($selected.attr('data-value'));
          visible = column.visible();
          if(!visible)
            return
          column.visible(!visible);
        }
      });

    $(document).on('click', '.run-utility', function(e){
        var oper = $(this).data('oper');
        var packageID = $(this).data('package');
        var utilityRequest  = new FormData();
        utilityRequest.append('oper', oper);
        utilityRequest.append('package_id', packageID);
        utilityRequest.append('package_id', packageID);
        utilityRequest.append('csrfmiddlewaretoken', getCookie('csrftoken'));
        $.ajax({
            type: 'POST',
            url: '/download/utilities/',
            async: true,
            data: utilityRequest,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function(response){
                var send_message = response['success'] ? success_message : error_message;
                var message = 'message' in response ? response['message'] : 'Hubo un error, intente más tarde.';
                send_message(message);
                table_packages.ajax.reload();
            }
        });
    })
});
