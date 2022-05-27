var datatable_language = {
  "sProcessing": "Procesando...",
  "sLengthMenu": "Mostrar _MENU_ registros",
  "sZeroRecords": "No se encontraron resultados",
  "sEmptyTable": "Ningún dato disponible en esta tabla",
  "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
  "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
  "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
  "sInfoPostFix": "",
  "sSearch": "Buscar:",
  "sUrl": "",
  "sInfoThousands": ",",
  "sLoadingRecords": "Cargando...",
  "oPaginate": {
      "sFirst": "Primero",
      "sLast": "Último",
      "sNext": "Siguiente",
      "sPrevious": "Anterior"
  },
  "oAria": {
      "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
      "sSortDescending": ": Activar para ordenar la columna de manera descendente"
  }
}
var urlInvoices = window.location.pathname;
var invoicingColumns = [{
    'sWidth': '10%',
    'bSortable': false,
  },{
    'sWidth': '10%',
    'bSortable': false,
  },{
    'sWidth': '20%',
    'bSortable': false,
  },{
    'sWidth': '25%',
    'bSortable': false,
  }, {
    'sWidth': '5%',
    'bSortable': false,
  }, {
    'sWidth': '15%',
    'bSortable': false,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{
    'sWidth': '15%',
    'bSortable': false,
  },{
    'sWidth': '10%',
    'bSortable': false,
  }];
  
  $(document).ready(function(){
  
      var invoicingTable = $('#invoicing-invoice').DataTable({
        "responsive": true,
        "searching": false,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "language": datatable_language,
        "columns": invoicingColumns,
        "columnDefs": [
        {
            className: "text-center",
            "targets": "_all",
        },],
        "PagingType": "full_numbers",
        "sAjaxSource": urlInvoices,
        fnServerData: function callback(sSource, aoData, fnCallback){
          aoData.push({
            "name": "csrfmiddlewaretoken",
            "value": getCookie('csrftoken')
          });
          aoData.push({
            "name": "oper",
            "value": "list-invoices"
          });
          if ($('#uuid').val().length >= 10){
            aoData.push({
              "name": "uuid",
              "value": $('#uuid').val()
            });
          }
          if ($("#taxpayer_id").val()) {
            aoData.push({
                "name": "taxpayer_id",
                "value": $("#taxpayer_id").val()
            });
          }
          if ($('#type_invoice').val()) {
            aoData.push({
              'name': 'type_invoice',
              'value': $('#type_invoice').val(),
            });
          }
          /*if ($("#rtaxpayer_id").val()){
            aoData.push({
                "name": "rtaxpayer_id",
                "value": $("#rtaxpayer_id").val()
            });
          }*/
          if ($("#emission_date").val() && $('#date-to-val').val()){
            aoData.push({
                "name": "date-from",
                "value": $("#emission_date").val()
            });
            aoData.push({
                "name": "date-to",
                "value": $("#date-to-val").val()
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
          $('[data-toggle="popover"]').popover({
            placement: 'left'
          });

        }
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
        $('#date-to').data("DateTimePicker").minDate(e.date);
        if ($('#date-to-val').val() && $('#emission_date').val()){
          invoicingTable.draw();
        }
      });
      $("#date-to").on("dp.change", function (e) {
        $('#date-from').data("DateTimePicker").maxDate(e.date);
        if ($('#date-to-val').val() && $('#emission_date').val()){
          invoicingTable.draw();
        }
      });
  
      $('#uuid,#rtaxpayer_id, #taxpayer_id').keyup(function(e){
        if ($(this).val().length >= 3 || ($(this).val() && e.keyCode === 8 || e.keyCode === 46)){
          e.preventDefault();
          invoicingTable.draw();
        }
      });

      $('#type_invoice').change(function(e) {
        invoicingTable.draw();
      });

      $(document).on("click", "#clean",  function(event) {
          $('#uuid, #taxpayer_id, #rtaxpayer_id, #emission_date, #date-to-val').val("");
          invoicingTable.ajax.reload();
      });

      $('#download_report').change(function(event) {
        $("#download_report").attr("disabled", true);
        report_type = $("#download_report").val()
        if (["csv", "xlsx"].indexOf(report_type) == -1) {
            $("#download_report").attr("disabled", false);
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
        

        if ($("#uuid").val()) {
            data.push({
                "name": "uuid",
                "value": $("#uuid").val()
            });                 
        }
        
        if ($("#taxpayer_id").val()) {
            data.push({
                "name": "taxpayer_id",
                "value": $("#taxpayer_id").val()
            });
        }

        /*if ($("#rtaxpayer_id").val()){
            data.push({
                "name": "rtaxpayer_id",
                "value": $("#rtaxpayer_id").val()
            });
        }*/
        //if ($("#date-to-val").val()){
        //  data.push({
        //      "name": "date-to-val",
        //      "value": $("#date-to-val").val()
        //  });
        //}
        if ($("#emission_date").val()){
          data.push({
              "name": "emission_date",
              "value": $("#emission_date").val()
          });
        
        }      

        data.push({
            "name": "get_report_sat",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/business/generatereport_sat/',
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

  
  });