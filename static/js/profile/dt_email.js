var token = csrftoken;
var idioma = lenaguaje;
var url_page_email = window.location.pathname;

$(document).ready(function(){
  var columns_email = [{
    sWidth: '50%',
    'className': 'text-center',
      // bSortable: false,
    },{
      sWidth: '50%',
      'className': 'text-center',
      // bSortable: false,
    }];
  var dt_email = $('#dt_email').DataTable({
    "sDom": 'lfrti',
    'responsive': true,
    'bProcessing': true,
    'bServerSide': true,
    "language": language_datatable,
    'columns': columns_email,
    'columnDefs': [
      {
        // "targets": [0,1],
        "bSortable": false, "targets":[ 0, 1 ] 
      }
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
    "info": false,
    "lengthChange": false,
    'stateSave': true,
    'searching': false,
    sAjaxSource: url_page_email,
    'fnServerData': function(sSource, aoData, fnCallback){
      aoData.push({
        'name': 'csrfmiddlewaretoken',
        'value': token,
      });
      aoData.push({
        'name': 'option',
        'value': 'dt_email',
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