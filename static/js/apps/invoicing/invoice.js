var invoicingColumns = [{
  'sWidth': '1%',
  'bSortable': false,
},{
  'sWidth': '20%',
  'bSortable': false,
},{
  'sWidth': '15%',
  'bSortable': false,
},{
  'sWidth': '20%',
  'bSortable': false,
},{
  'sWidth': '20%',
  'bSortable': false,
},
// {
//   'sWidth': '5%',
//   'bSortable': false,
// },
{
  'sWidth': '11%',
  'bSortable': false,
  'render': $.fn.dataTable.render.number(',', '.', 2, '$ ')
},{
  'sWidth': '10%',
  'bSortable': false,
},
// {
//   'sWidth': '10%',
//   'bSortable': false,
// },
{
  'sWidth': '15%',
  'bSortable': false,
}];

if (role != 'A') {
  invoicingColumns.splice(1, 1)
}

function clear_email_modal() {
  $('#emails_destiny').tagsinput('removeAll');
  $('#pdf_check, #xml_check').removeAttr('checked');
}

function validate_email(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}

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

$(document).ready(function(){

    $('#emision').addClass('active');

    var invoicingTable = $('#invoicing-invoice').DataTable({
      "responsive": true,
      "searching": false,
      "bProcessing": true,
      "bServerSide": true,
      "stateSave": true,
      'ordering': false,
      "language": language_datatable,
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
        }else{
          var params = getParams()
          if (params.uuid !== undefined && params.uuid){
            aoData.push({
              "name": "uuid",
              "value": params.uuid
            });
          }
        }
        if ($("#type").val() != "A") {
          aoData.push({
              "name": "type",
              "value": $("#type").val()
          });
        }
        if ($("#status").val() != "A") {
          aoData.push({
              "name": "status",
              "value": $("#status").val()
          });
        }
        if ($("#receiver").val()){
          aoData.push({
              "name": "receiver",
              "value": $("#receiver").val()
          });
        }
        if ($("#owner").val()){
          aoData.push({
              "name": "owner",
              "value": $("#owner").val()
          });
        }
        if ($("#date-from-val").val() && $("#date-to-val").val()){
          aoData.push({
              "name": "date_from",
              "value": $("#date-from-val").val()
          });
          aoData.push({
              "name": "date_to",
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
        /*
        $(document).on('click', '.rts', function(){
          console.log('HOLA inside');
          $(this).button('loading');
        });
        $('.rts').click(function(){
          console.log('Hola2');
        });
        $('.rts').on('click',function(){
          var $this = $(this);
          $this.button('loading')
          var invoice = $this.data("invoice");
          $.ajax({
            'type': 'POST',
            'dataType': 'json',
            'data':{
              'invoice': invoice,
              'oper': 'restamp-invoice',
              'csrfmiddlewaretoken': getCookie('csrftoken'),
            }
          }).done(function(response, textStatus, jqXHR){
            if (response['success']){
              success_message('Solicitud exitosa');
            }else{
              error_message('Hubo un error, intente más tarde');
            }
          });
          $this.button('reset');
          setTimeout(function(){invoicingTable.draw()}, 3000 );
        });*/
      }
    });

    $("#date-from").datetimepicker({
      locale: language,
      format: "DD-MM-YYYY",
      sideBySide: true
    });
    $("#date-to").datetimepicker({
      locale: language,
      format: "DD-MM-YYYY",
      sideBySide: true
    });

    $("#date-from").on("dp.change", function (e) {
      $('#date-to').data("DateTimePicker").minDate(e.date);
      if ($('#date-from-val').val() && $('#date-to-val').val()){
        invoicingTable.draw();
      }
    });
    $("#date-to").on("dp.change", function (e) {
      $('#date-from').data("DateTimePicker").minDate(e.date);
      if ($('#date-to-val').val() && $('#date-from-val').val()){
        invoicingTable.draw();
      }
    });

    $('#uuid,#receiver,#owner').keyup(function(e){
      if ($(this).val().length >= 3 || ($(this).val() && e.keyCode === 8 || e.keyCode === 46)){
        e.preventDefault();
        invoicingTable.draw();
      } else if ($(this).val().length == 0) {
        e.preventDefault();
        invoicingTable.draw();
      }
    });

    $("#type").change(function(e) {
      invoicingTable.draw();
    });
    $("#status").change(function(e) {
      invoicingTable.draw();
    });
    $(document).on("click", "#clean",  function(event) {
        $("#type, #status").prop("selectedIndex",0).change();
        $('#uuid,  #receiver, #date-from-val, #date-to-val').val("");
        invoicingTable.ajax.reload();
    });

    invoicingTable.on('draw.dt', function(){
      var pageInfo = invoicingTable.page.info();

      invoicingTable.column(0, {page: 'current'}).nodes().each(function(cell, i){
        cell.innerHTML = i+1+pageInfo.start;
      });
    });

    /*$(document).on("click", "#clean-d",  function(event) {

    });*/
    
    $(document).on('click', '.rts', function(event){
      event.preventDefault();
      var $btn = $(this);
      $btn.button('loading');

      var invoice = $btn.data("invoice");
      $.ajax({
        'type': 'POST',
        'dataType': 'json',
        'async': false,
        'data':{
          'invoice': invoice,
          'oper': 'restamp-invoice',
          'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
        //'success': function(response){
        //  var send_message = response['success'] ? success_message : error_message;
        //  var message = 'message' in response ? response['message'] : 'Hubo un error, intente más tarde.';
        //  send_message(message);
        //}
      }).done(function(response, textStatus, jqXHR){
        var send_message = response['success'] ? success_message : error_message;
        var message = 'message' in response ? response['message'] : gettext('There was an error, try again later.');
        send_message(message);
      });
      
      setTimeout(
        function(){
          invoicingTable.draw();
        }, 4000 
      );
      //$btn.button('reset');
    });

    $(document).on('click', '.rci', function(event){
      event.preventDefault();
      var btn = $(this);
      btn.button('loading');
      var invoice = btn.data("invoice");
      var notes = $(document.getElementById(invoice)).val();
      $.ajax({
        'type': 'POST',
        'dataType': 'json',
        'async': false,
        'data':{
          'invoice': invoice,
          'oper': 'cancel-invoice',
          'notes': notes,
          'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
      }).done(function(response, textStatus, jqXHR){
        var send_message = response['success'] ? success_message : error_message;
        var message = 'message' in response ? response['message'] : gettext('There was an error, try again later.');
        send_message(message);
      });
      
      setTimeout(
        function(){
          invoicingTable.draw();
        }, 4000 
      );
      //$btn.button('reset');
    });

    $(document).on('click', '.usi', function(event){
      event.preventDefault();
      var btn = $(this);
      btn.button('loading');
      var invoice = btn.data('invoice');
      $.ajax({
        'type': 'POST',
        'dataType': 'json',
        'async': true,
        'data':{
          'invoice': invoice,
          'oper': 'update-status',
          'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
      }).done(function(response, textStatus, jqXHR){
        var send_message = response['success'] ? success_message : error_message;
        var message = 'message' in response ? response['message'] : gettext('There was an error, try again later.');
        send_message(message);
      });

      setTimeout(
        function(){
          invoicingTable.draw();
        }, 4000 
      );

    })

    $(document).on('click', '.sci', function(event){
      event.preventDefault();
      var btn = $(this);
      btn.button('loading');
      var invoice = btn.data('invoice');
      $.ajax({
        'type': 'POST',
        'dataType': 'json',
        'async': false,
        'data':{
          'invoice': invoice,
          'oper': 'stop-cancellation',
          'csrfmiddlewaretoken': getCookie('csrftoken'),
        },
      }).done(function(response, textStatus, jqXHR){
        var send_message = response['success'] ? success_message : error_message;
        var message = 'message' in response ? response['message'] : gettext('There was an error, try again later.');
        send_message(message);
      });

      setTimeout(
        function(){
          invoicingTable.draw();
        }, 4000 
      );

    });

    $(document).on('click', '#refresh_downloads', function() {
      invoicingTable.draw();
    });

    $(document).on('click', '.btn-email-confirm', function() {
      $('.uuid').html('<label>UUID:&nbsp;&nbsp;' + $(this).attr('uuid') + '</label>')
      $('.btn-send-invoice-email').attr('uuid', $(this).attr('uuid'));
      $('.bootstrap-tagsinput input').addClass('form-control');
      $('#modal-send-email').modal('show');
    });

    $(document).on('click', '.btn-close-email', function() {
      clear_email_modal();  
      $('#modal-send-email').modal('hide');
    })

    $(document).on('click', '#xml_check, #pdf_check', function() {
      if ($(this).attr('checked')) {
        $(this).removeAttr('checked');
      } else {
        $(this).attr('checked', 'true');
      }
    })

    $(document).on('click', '.btn-send-invoice-email', function() {

      if (!$('#xml_check').attr('checked')) {
        if(!$('#pdf_check').attr('checked')) {
          error_message(gettext('You must select a format'));
          return
        }
      }
      if (!$('#emails_destiny').tagsinput('items').length) {
        $('.bootstrap-tagsinput input').attr('placeholder', gettext('Please enter a recipient'))
        setTimeout(function(){
          $('.bootstrap-tagsinput input').attr('placeholder', gettext('Comma separated emails (,)'))
        }, 2000);
        return
      }

      var data = {
        'csrfmiddlewaretoken': getCookie('csrftoken'),
        'invoice': $(this).attr('uuid'),
        'oper': 'send-invoice-email',
        'emails': $('#emails_destiny').val(),
        'xml_check': $('#xml_check').attr('checked'),
        'pdf_check': $('#pdf_check').attr('checked'),
      }

      $.ajax({
        'type': 'POST', 
        'dataType': 'json',
        'async': false,
        'data': data,
        'url': window.location.pathname,
        'success': function(json) {
          if (json.success) {
            success_message(json.message);
          } else {
            error_message(json.message);
          }
          clear_email_modal();
          $('#modal-send-email').modal('hide');
        }
      });
    });
});