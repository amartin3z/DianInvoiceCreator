var DIOTColumns = [
  {//Año
  'sWidth': '10%',
  'bSortable': false,
  },{//Periodo
    'sWidth': '10%',
    'bSortable': false,
  },{//Proveedores
    'sWidth': '20%',
    'bSortable': true,
  },{//Base 15-16
    'sWidth': '11%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Monto 15
    'sWidth': '10%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Base 8
    'sWidth': '10%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Monto 8
    'sWidth': '15%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Retenido
    'sWidth': '15%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Bonificacion
    'sWidth': '15%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Acciones
    'sWidth': '15%',
    'bSortable': false,
  }
];

$(document).ready(function() {

    $('[data-toggle="tooltip"]').tooltip({
      // trigger: 'click',
    });

    var DIOTTable = $('#diot_global').DataTable({
      "responsive": true,
      "searching": false,
      "bProcessing": true,
      "bServerSide": true,
      "language": datatable_language,
      "columns": DIOTColumns,
      "PagingType": "full_numbers",
      fnServerData: function callback(sSource, aoData, fnCallback){

        var ordering = null;
        aoData.map(function(element, idx){
          if (element.name === "order"){
            element.value.map(function(el){
              ordering = `${el.column}-${el.dir}`;
              return null;
            });
          }
        });
        aoData.push({
          "name": 'ordering',
          value: ordering
        });

        aoData.push({
          "name": "csrfmiddlewaretoken",
          "value": getCookie('csrftoken')
        });
        aoData.push({
          "name": "oper",
          "value": "get-diot"
        });
        var monthDIOT = $('#monthDIOT').find("option:selected").val();
        console.log(monthDIOT);
        if (monthDIOT !== '' && monthDIOT !== undefined){
          aoData.push({
            "name": "month",
            "value": monthDIOT,
          });
        }
        var yearDIOT = $('#yearDIOT').find("option:selected").val();
        console.log(yearDIOT);
        if (yearDIOT !== '' && yearDIOT !== undefined){
          aoData.push({
            "name": "year",
            "value": yearDIOT,
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
        $('[data-toggle="tooltip"]').tooltip();
      }
    });

    $('#monthDIOT').on('change', function(e){
      let month = $(this).find("option:selected").text();
      month = month === 'Todos' ? '' : month;
      $('#diot-container-title-month').text(month);
      DIOTTable.ajax.reload();
    });
    $('#yearDIOT').on('change', function(e){
      let year = $(this).find("option:selected").text();
      year = year === 'Todos' ? currentYear : year;
      $('#diot-container-title-year').text(year);
      DIOTTable.ajax.reload();
    });

    $('#btn_clean').on('click', function(e){
      e.preventDefault();
      $("#monthDIOT").val('default');
      $("#monthDIOT").selectpicker("refresh");
      $("#yearDIOT").val('default');
      $("#yearDIOT").selectpicker("refresh");
      $('#diot-container-title-year').text(currentYear);
      $('#diot-container-title-month').text('');
      DIOTTable.ajax.reload();
    });

    $(document).on('click', '.getdiot', function(e) {
      e.preventDefault();

      var oper = 'download-diot';
      var diotID = $(this).data('diot');
      var filename = $(this).data('name');
      var downloadURL = $(this).data('url');
      

      var xhr = new XMLHttpRequest();
      var formData = new FormData();

      formData.append('diotID', diotID);
      formData.append('oper', oper);

      xhr.open("POST", downloadURL, true);
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

      xhr.onload = function(e) {
        if (this.status == 201){
          var blob = this.response;
          if (window.navigator.msSaveOrOpenBlob){
            window.navigator.msSaveBlob(blob, filename);
          }else{
            var downloadLink = window.document.createElement('a');
            var contentTypeHeader = xhr.getResponseHeader("Content-Type");
            var blob = new Blob([blob], {type: contentTypeHeader});
            downloadLink.href = window.URL.createObjectURL(blob);
            downloadLink.download = filename;
            $(downloadLink)[0].click();
            $(downloadLink).remove();
          }
        }else if (this.status == 403){
          console.log('YOU DONT HAVE PERMISSIONS TO DOWNLOAD THIS FILE');
        }
      }
      xhr.send(formData);
      
    });
});
