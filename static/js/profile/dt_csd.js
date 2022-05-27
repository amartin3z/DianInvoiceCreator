var token = csrftoken;
var idioma = lenaguaje;
var url_page_csd = window.location.pathname;

$(document).ready(function(){
  console.log(language_datatable);
  var columns_CSD = [{
    sWidth: '10%',
    'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '18%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '18%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '18%',
      'className': 'text-center',
      bSortable: false,
    },{
      sWidth: '18%',
      'className': 'text-center',
      bSortable: false,
    }];
  var dt_csd = $('#dt_csd').DataTable({
    "sDom": 'l<"toolbar">frtip',
    'responsive': true,
    "language": language_datatable,
    'bProcessing': true,
    'bServerSide': true,
    'columns': columns_CSD,
    'columnDefs': [
      {
        "targets": [0,1,2,3,4],
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
    sAjaxSource: url_page_email,
    'fnServerData': function(sSource, aoData, fnCallback){
      aoData.push({
        'name': 'csrfmiddlewaretoken',
        'value': token,
      });
      aoData.push({
        'name': 'option',
        'value': 'dt_csd',
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