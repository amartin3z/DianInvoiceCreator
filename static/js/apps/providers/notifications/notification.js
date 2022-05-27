//var table_admin = null;
$(document).ready(function() {

    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    /*=============================================Table for user=====================================*/
    aoColumns = [{
        'bSortable': false,
        'data': 'notification',
    },{
        'bSortable': false,
        'data': 'uploaded_by',
    },{
        'bSortable': false,
        'data': 'datendetail',
    }
    ];

    $('li[id="providers_tag"]').addClass('active');


/* Formatting function for row details - modify as you need */
function format (d) {
    // `d` is the original data object for the row
    var tr = '<tr>';
    $.each(d.notification_detail, function(index, details){
        tr += '<td>Nombre: ' +'</td><td>' + details.Nombre + '</td><td>Estado: ' +  details.Estado + '</td><td>Error: ' +  details.Error + '</td></tr>'
    })
    tr += '</tr>';
    return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">'+
        '<tr>'+
            tr
        '</tr>'+
    '</table>';
}

/*==================================Table for admin USERS===============================================*/

    table_admin = $('#upload_list').dataTable({
        responsive: {
          details: {
            display: $.fn.dataTable.Responsive.display.modal( {
              header: function ( row ) {
                var data = row.data();
                return 'Detalles';
              }
            }),
            renderer: function ( api, rowIdx, columns ) {
              $('.shd');
              var tr = $('.shd').closest('tr');
              var row = table_admin.api().row(tr);
              var data2 = row.data();
              var tr_d = '';
              $.each(data2, function(name, content){
                var tr_data = '<tr>';
                if (typeof(content) == 'string'){
                  tr_data += '<td>' + name + '</td><td>' + content + '<td></tr>';
                }else{
                  $.each(content, function(name, value){
                    tr_data += '<td>Nombre: ' +'</td><td>' + value.Nombre + '</td><td>Subio: ' +'</td><td>Estado: ' +  value.Estado + '</td></tr>'
                  })
                }
                tr_d += tr_data;
              });
              return $('<table class="table"/>').append( tr_d );
            }
          }
        },
        'language': datatable_language,
        "autoWidth": true,
        'bProcessing': true,
        'bServerSide': true,
        'stateSave': true,
        'searching': false,
        'columns': aoColumns,
        'PagingType': 'full_numbers',
        'sAjaxSource': url_status,
        'fnServerData': function(sSource, aoData, fnCallback) {
            aoData.push( { "name": "csrfmiddlewaretoken","value": token});
            if ($('#filter_uuid').val()){
                aoData.push({
                    'name': 'uuid',
                    'value': $('#filter_uuid').val(),
                });
            }

            if ($('#filter_user').val()){
                aoData.push({
                    'name': 'user',
                    'value': $('#filter_user').val(),
                });
            }

            if ($('#from_val').val() && $('#to_val').val()) {
                aoData.push({
                    "name": "to",
                    "value": $('#to_val').val()
                });
                aoData.push({
                    "name": "from",
                    "value": $('#from_val').val()
                });
            }

            aoData.push({
                "name": "status",
                "value": $('#status').val()
            });

            $.ajax({
                "dataType": 'json',
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function(json) {
                    /*var users = json['users']
                    $.each(users, function (i, user) {
                      $('#filter_user').append($('<option>', {value: user, text: user}));
                    });
                    */

                    fnCallback(json);
                }
            });
        },
    });
    //table_admin.api().column(2).visible(false);

    var filter_uuid = $("#filter_uuid").keyup(function(event){
      table_admin.dataTable().fnDraw();
    });
    
    var filter_user = $("#filter_user").change(function(event){
      table_admin.dataTable().fnDraw();
    });

    var filter_status = $("#status").change(function(event) {
        table_admin.dataTable().fnDraw();
    });

    $(document).on('click', '#clean',  function(event) {
        $("#filter_uuid").val('');
        $("#filter_user").val('');
        $("#status").val('');
        $('#from').data('DateTimePicker').clear();
        $('#to').data('DateTimePicker').clear();
        table_admin.dataTable().fnDraw();
    });

    $(function() {
        $('#from').datetimepicker({
          locale: 'es'
        });
        $('#to').datetimepicker({
          locale: 'es'
        });

        $('#to').datetimepicker({
            useCurrent: false //Important! See issue #1075
        });

        $("#from").on("dp.change", function(e) {
            $('#to').data("DateTimePicker").minDate(e.date);
            if ($('#to_val').val() != "") {
                table_admin.dataTable().fnDraw();
            }

        });

        $("#to").on("dp.change", function(e) {
            $('#from').data("DateTimePicker").maxDate(e.date);
            if ($('#from_val').val() != "") {
                //table.ajax.reload();
                table_admin.dataTable().fnDraw();
            }
        });
    });

    $('.dtr-modal-content').on('click', '.shd', function(){
      var shd = $(this);
      var tr = $(this).closest('tr');
      var row = table_admin.api().row(tr);
      if ( row.child.isShown() ){
        //This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
        shd.text('Ver detalles');
        shd.removeClass('btn-danger');
        shd.addClass('btn-default');
      }else{
        row.child( format(row.data()) ).show();
        tr.addClass('shown');
        shd.text('Ocultar detalles');
        shd.addClass('btn-danger');
        shd.removeClass('btn-default');
      }  
    })
    $('#upload_list tbody').on('click', '.shd', function(){
      var shd = $(this);
      var tr = $(this).closest('tr');
      var row = table_admin.api().row(tr);
      if ( row.child.isShown() ){
        //This row is already open - close it
        row.child.hide();
        tr.removeClass('shown');
        shd.text('Ver detalles');
        shd.removeClass('btn-danger');
        shd.addClass('btn-default');
      }else{
        row.child( format(row.data()) ).show();
        tr.addClass('shown');
        shd.text('Ocultar detalles');
        shd.addClass('btn-danger');
        shd.removeClass('btn-default');
      }
    });
  

  /*
    Hide|Show panel
  */

});
