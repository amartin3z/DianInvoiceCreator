$(document).ready(function() {
    $('#reportes').addClass('active');
    $('#reportes').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    //var month = month;
    //var year = year;
    var url_status = window.location.pathname;

    columns_billing_branch = [{
        sWidth: '15%',
        'className': 'bold text-center',
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
        },{
        sWidth: '5%',
        bSortable: false,
    }];


    var billing_branch_table = $('#tbillingbranch').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'columns': columns_billing_branch,
        "columnDefs": [
            {
                className: "text-center",
                "targets": [0,1,2,3,4,5,6,7,8,9,10,11,12,13],
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

            if($('#name_branch').val() != ''){
                aoData.push({
                    'name': 'name_branch',
                    'value': $('#name_branch').val()
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
            $('[data-toggle="popover"]').popover();
        }
    });

    /* draw tables*/    
    $('#refresh_invoices').click(function() {
        billing_branch_table.ajax.reload();
    });

    $('#clean-filter').on('click', function(){
        $("#select_status_branch").prop("selectedIndex",0).change();
        $("#name_branch").val('');
        billing_branch_table.ajax.reload();
    });
    
    $('#select_status_branch').change( function(e){
        billing_branch_table.ajax.reload()
    });

    $("#name_branch").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 4 || len == 0) && is_valid_key(e.which)) { 
          billing_branch_table.ajax.reload()
        }
    });

    $(document).on("click", ".loctaion_branch",  function(e) {
        e.preventDefault();

        var latitude = $(this).attr('latitude');
        var longitude = $(this).attr('longitude');
        var sucursal = $(this).attr('sucursal');
        
        myMap(latitude, longitude);

        $('#strong-taxpayer-csd').text(sucursal);
        $('#modal-branch').modal('show');        
    });


    $('#download_report_branch').change(function(event) {
        $("#download_report_branch").attr("disabled", true);
        report_type = $("#download_report_branch").val()
        if (["csv", "xlsx"].indexOf(report_type) == -1) {
            $("#download_report_branch").attr("disabled", false);
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

        if ($("#select_status_branch").val() != "T") {
            data.push({
                "name": "status",
                "value": $("#select_status_branch").val()
            });                 
        }else{
            data.push({
                "name": "status",
                "value": 'V'
            });
        }
        
        if ($("#name_branch").val() !="") {
            data.push({
                "name": "name_branch",
                "value": $("#name_branch").val()
            });
        }
       

        data.push({
            "name": "get_report_branch",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_billing_branch/',
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
            $("#download_report_branch").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
            $(document.body).css({"cursor" : "default"});
        });
        
        $('#download_report_branch').val("select").change();
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

    function myMap(lat, lng) {

      var mapProp= {
        center:new google.maps.LatLng(lat,lng),
        zoom:18,
      };
      var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    }

});

