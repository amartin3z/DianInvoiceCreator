var token = csrftoken;
var idioma = lenaguaje;
var url_page_series = window.location.pathname;

$(document).ready(function(){
  var columns_CSD = [{
    sWidth: '25%',
    'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '25%',
      'className': 'text-center',
      bSortable: false,
    }];
  var dt_serie = $('#dt_serie').DataTable({
    "sDom": 'l<"toolbar">frtip',
    'responsive': true,
    'bProcessing': true,
    'bServerSide': true,
    "language": language_datatable,
    'columns': columns_CSD,
    'columnDefs': [
      {
        "targets": [0,1,2,3],
      },
    ],
    'responsive': {
      details: {
        display: $.fn.dataTable.Responsive.display.modal({
          header: function(row) {
            var data = row.data();
            return 'Detalles '+'de'+' '+data[1];
          }
        }),
        renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
          tableClass: 'table'
        })
      }
    },
    // 'language': idioma,
    'stateSave': true,
    'searching': false,
    sAjaxSource: url_page_series,
    'fnServerData': function(sSource, aoData, fnCallback){
      aoData.push({
        'name': 'csrfmiddlewaretoken',
        'value': token,
      });
      aoData.push({
        'name': 'option',
        'value': 'dt_series',
      });
      $.ajax({
        'dataType': 'json',
        'type': 'POST',
        'url': sSource,
        'data': aoData, 
        'success': function(json){
          fnCallback(json.object);
        }
      });
    },
  });
});