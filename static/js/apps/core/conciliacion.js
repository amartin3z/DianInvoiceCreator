$(document).ready(function() {
    var url_status = window.location.pathname;
    columnsInvoices = [{
        sWidth: '20%',
        className : 'priority-1 text-center',
        bSortable: false,
        },{
        sWidth: '20%',
        className : 'priority-1 text-center',
        bSortable: false,
        },{
        sWidth: '20%',
        className : 'priority-3 text-center',
        bSortable: false,
        },{
        sWidth: '20%',
        className : 'priority-3 text-center',
        bSortable: false,
        },{
        sWidth: '20%',
        className : 'priority-1 text-center',
        bSortable: false,
    }];
    var conciliacion_table = $('#table_conciliation').DataTable({
         responsive: true,
         "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'columns': columnsInvoices,
        'language': datatable_language,
        'stateSave': true,
        'searching': false,
        sAjaxSource: url_status,
        'fnServerData': function(sSource, aoData, fnCallback){
            aoData.push({
                'name': 'csrfmiddlewaretoken',
                'value': getCookie('csrftoken')
            });
            if ($("#tipo").val() != "E"){
                aoData.push({
                    "name": "tipo",
                    "value": 'R'
                });
            }else{
                aoData.push({
                    "name": "tipo",
                    "value": 'E'
                });
            }
            if ($('#d-dp-from-val').val()) {
                aoData.push({
                    "name": "date_from",
                    "value": $('#d-dp-from-val').val()
                });
            }
            if ($('#d-dp-to-val').val()){
                aoData.push({
                    "name": "date_to",
                    "value": $('#d-dp-to-val').val()
                });
            }
            
            if ($('#uuid').val()){
                aoData.push({
                    "name": "uuid",
                    "value": $('#uuid').val()
                });
            }
            aoData.push( { "name": "ambos","value": $('#ambos').is(':checked')});
            aoData.push( { "name": "sat","value": $('#sat').is(':checked')});
            aoData.push( { "name": "negocio","value": $('#negocio').is(':checked')});
            
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

    $("#tipo").change(function(e) {
        conciliacion_table.ajax.reload();

    });
   $("#d-dp-from").on("dp.change", function(e) {
        if ($('#d-dp-from-val').val() != "") {
            conciliacion_table.ajax.reload();
        }
    });
    $("#d-dp-to").on("dp.change", function(e) {
        if ($('#d-dp-to-val').val() != "") {
            conciliacion_table.ajax.reload();
        }
    });
    /* end draw*/
    /* init datepicker*/
    $('#d-dp-from').datetimepicker({
        locale: 'es',
        format: "DD MMMM YYYY",
        sideBySide: false
    });

    $('#d-dp-to').datetimepicker({
        locale: 'es',
        format: "DD MMMM YYYY",
        sideBySide: false
    });
    $("#ambos, #sat, #negocio").change(function(event){
        conciliacion_table.ajax.reload();
    });
    $("#uuid").on('keyup', function(e) {
         conciliacion_table.ajax.reload();
    });
    $('#clean-filter').on('click', function(){
        $('#uuid, #d-dp-to-val, #d-dp-from-val').val('');
        $("#tipo").prop("selectedIndex",0).change();
        $(".toggle-off").click();
        conciliacion_table.ajax.reload();
    });
    function getParams(){
        var search = location.search;
        var params = {}
        if (search){
            var queries = search.split('&');
            queries.map(query => {
                query = query.replace('?', '');
                values = query.split('=');
                params[values[0]] = values[1];
            });
        }
        return params;
      }

});
