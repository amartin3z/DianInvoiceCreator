var DIOTColumns = [{//TIPO
    'sWidth': '20%',
    'bSortable': false,
  },{//OPERACION
    'sWidth': '20%',
    'bSortable': false,
  },{//RFC
    'sWidth': '11%',
    'bSortable': true,
  },
  {//Base 15-16
    'sWidth': '15%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },
  {//Monto15
    'sWidth': '15%',
    'bSortable': true,
    'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
  },{//Base 8
    'sWidth': '15%',
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
  },{
    'sWidth': '15%',
    'bSortable': false,
  }
];

$(document).ready(function() {

  $('[data-toggle="tooltip"]').tooltip({
    // trigger: 'click',
  });

  var DIOTDetailTable = $('#diot_detail').DataTable({
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
        "value": "get-diot-detail"
      });
      var taxpayerID = $('#taxpayer_id').val();
      if (taxpayerID !== '' && taxpayerID !== undefined) {
        aoData.push({
            "name": "taxpayer_id",
            "value": taxpayerID
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
  });
  $('#taxpayer_id').keyup(function(e){
    e.preventDefault();
    size  = $(this).val().length;
    if ((size>2 || size==0) && is_valid_key(e.which)){
      DIOTDetailTable.ajax.reload()
    }
  });

  $('#btn_clean').on('click', function(e){
    e.preventDefault();
    $("#taxpayer_id").val('');
    DIOTDetailTable.ajax.reload();
  });

  $(document).on('click', '#download_diot', function(e) {
    e.preventDefault();
    
    //dummy variable assignment :9
    var filename = downloadDIOTname;

    var xhr = new XMLHttpRequest();
    var formData = new FormData();

    formData.append('oper', 'download-diot');

    xhr.open("POST", window.location.pathname, true);
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
      }else if (this.status == 404){
        console.log('OOPS!!! WE CANT FIND THE RESOURSE YOU TRYING TO ACCESS');
      }
    }
    xhr.send(formData);
    
  });
});
