$(document).ready(function() {
	$('#providers_tag').addClass('active');
  $('#providers_tag').css('pointer-events', 'auto');
  var token = CSRF_TOKEN;
  var url_status = window.location.pathname;
  var rfc_regex = /[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]/

  //document.getElementById("href-providers").setAttribute("href", url_status);
  /*=============================================Table for user=====================================*/
	aoColumns = [{
    'sWidth': '10%',
    'bSortable': true,
    },{
    'sWidth': '20%',
    'bSortable': false,
    },{
    'sWidth': '15%',
    'bSortable': false,
    },{
    'sWidth': '5%',
    'bSortable': false,
    },{
    'sWidth': '5%',
    'bSortable': false,
    },{
    'sWidth': '5%',
    'bSortable': false,
    },{
    'sWidth': '5%',
    'bSortable': false,
    },{
    'sWidth': '15%',
    'bSortable': false,
    }];
  
  /*==================================Table for admin USERS===============================================*/
  table_admin = $('#providers').dataTable({
    responsive: {
      details: {
        display: $.fn.dataTable.Responsive.display.modal( {
          header: function ( row ) {
            var data = row.data();
            return 'Detalles';
          }
        }),
        renderer: function ( api, rowIdx, columns ) {
          var data = $.map( columns, function ( col, i ) {
            return '<tr>'+
              '<td>'+col.title+':'+'</td> '+
              '<td>'+col.data+'</td>'+
            '</tr>';
          } ).join('');
          return $('<table class="table"/>').append( data );
        }
      }
    },
    //"sDom": 'RHt',//Desapare en numero de elementos que desea mostrar
    //"sDom": '<"ui-toolbar ui-widget-header ui-corner-tl ui-corner-tr ui-helper-clearfix"lfr>t<"ui-toolbar ui-widget-header ui-corner-bl ui-corner-br ui-helper-clearfix"<"#add_provider">ip>',
   "sDom": 'l<"toolbar">frtip',
    language: datatable_language,
    'bProcessing': true,
    'bServerSide': true,
     stateSave: true,
    'searching': false,
    "columns": aoColumns,
    "columnDefs": [
    {
        className: "text-center",
        "targets": [0],
    },
     {
        className: "text-center",
        "targets": [1],
    },
     {
        className: "text-center",
        "targets": [2],
    },
     {
        className: "text-center",
        "targets": [3],
    },
     {
        className: "text-center",
        "targets": [4],
    },
    {
        className: "text-center",
        "targets": [5],
    },
    {
        className: "text-center",
        "targets": [6],
    },
    {
        className: "text-center",
        "targets": [7],
    },
    ],
    "PagingType": 'full_numbers',
    sAjaxSource: url_status,
    fnServerData: function(sSource, aoData, fnCallback) {
      aoData.push( { "name": "csrfmiddlewaretoken","value": token});
      if($('#taxpayer_id').val()){
        aoData.push({ "name": "taxpayer_id","value": $('#taxpayer_id').val()});
      }
      if($('#name').val()){
        aoData.push({ "name": "provider_name","value": $('#name').val()});
      }
      if($('#mail').val()){
        aoData.push({ "name": "provider_mail","value": $('#mail').val()});
      }
      aoData.push( { "name": "provider_status","value": $('#status').val()});
      aoData.push( { "name": "c69","value": $('#check69').is(':checked')});
      aoData.push( { "name": "c69b","value": $('#check69b').is(':checked')});
      aoData.push( { "name": "cc","value": $('#checkcc').is(':checked')});
      
      var params = getParams();
      if (Object.keys(params).length !== 0) {
        var cod = params['filter']
        if (cod.toUpperCase()=="SINGRUPO"){
          aoData.push( { "name": "code","value": true});
        }
        else if (cod.toUpperCase()=="CODIGOC69"){
          aoData.push( { "name": "c69","value": true});
        }
        else if (cod.toUpperCase()=="CODIGOC69-B"){
          aoData.push( { "name": "c69b","value": true});
        }
        else if (cod.toUpperCase()=="CODIGOCC"){
          aoData.push( { "name": "cc","value": true});
        }
      }
      $.ajax( {
        "dataType": 'json',
        "type": "POST",
        "url": sSource,
        "data": aoData,
        "success": function(json) {
          fnCallback(json);
        }
      });
    }
  });

  //$("div.toolbar").html('<button id="add"  data-toggle="modal" data-target="#add_provider" class="btn-success btn"><i class="fa fa-user-plus" aria-hidden="true"></i><span><b>&nbsp;Agregar</b></span></button>');           

  $("#status, #check69, #check69b, #checkcc").change(function(event){
    //alert("Change status");
    //table_admin.ajax.reload();
    table_admin.dataTable().fnDraw();
  });
  
  $("#taxpayer_id,#name,#mail").keyup(function() {
    //table_admin.ajax.reload();
    table_admin.dataTable().fnDraw();
  });
  
  $('#add_button').on('click',function(){
    person_type = "";
    var data = new FormData()
    if ($("ul#type li.active a:contains(Moral)").html()){
      person_type = "M"
    }
    if ($("ul#type li.active a:contains(Fisica)").html()){
      person_type = "F"
    }
    if (person_type){
      taxpayer_id = $.trim($('#taxpayer_id_add').val());
      email =$.trim($('#email_add').val());
      status = $.trim($('#status_add').val());
      password = $.trim($('#password_add').val());
      if (person_type=='M'){
        name = $.trim($('#name_add').val());
        if ( taxpayer_id != '' & email != '' & status != '' & name != '' & password != ''){
          data.append('name', name);

        }else{
          error_message("Son  requeridos los campos que contienen *");
          return;
        }
      
      }else if(person_type=='F'){
        names = $.trim($('#names').val());
        last_name =  $.trim($('#last_name').val());
        second_last_name = $.trim($('#second_last_name').val());
        if (taxpayer_id != '' & email != '' & status != '' & names != '' & last_name != '' & password != ''){
          data.append('names', names);
          data.append('last_name', last_name);
          data.append('second_last_name', second_last_name);
        }else{
          error_message("Son requeridos los campos que contienen *");
          return;
        }

      } else{return;}
      data.append('type', person_type);
      data.append('taxpayer_id', taxpayer_id);
      data.append('email', email);
      data.append('status',status);
      data.append('password', password);
      data.append('csrfmiddlewaretoken', token);

      $.ajax({
          type: 'POST',
          url: '/dashboard/providers/add/',
          data: data,
          cache: false,
          contentType: false,
          processData: false,
          dataType: 'json',
      }).done(function(json) {
          table_admin.dataTable().fnDraw();
          if (json.success) {
            success_message(json.message);
            $("#form_add_provider").closest('form').find("input[type=text], textarea").val("");
            $("#form_add_provider").closest('form').find("input[type=password], textarea").val("");
            $('#add_provider').modal('hide')
          } else {
              /*alert(json.message);*/
            error_message(json.message);
          }
      });

    }else {
      error_message("Error en el tipo de persona");
      return;
    }
  });

  function error_message(message){
        $.toast({
            heading: 'Error',
            text: message,
            showHideTransition: 'fade',
            icon: 'error',
            position: 'top-right',
        });
  }

  function success_message(message){
    $.toast({
        heading: 'Correcto',
        text: message,
        showHideTransition: 'fade',
        icon: 'success',
        position: 'top-right',
    });
  }
  
  $(document).on('click', '.prov', function() {
    var row = table_admin.api().row($(this).parents('tr')).data();
    if(!row){
       taxpayer_id = $(this).attr('taxpayer_id');
       try {
         var action = $(this).attr('act');
       }catch(err){
         var action = ''
       }
    }else{ 
      taxpayer_id = row[0];
      try {
         var action = $(this).attr('act');
       }catch(err){
         var action = ''
       }
    }
    data = {
      'csrfmiddlewaretoken': token,
      'taxpayer_id': taxpayer_id,
      'option': 'AS',
      'action': action
    }

    $.ajax({
        type: 'POST',
        url: '/dashboard/providers/edith/',
        data: data,
        cache: false,
        dataType: 'json',
    }).done(function(json) {
      table_admin.dataTable().fnDraw();
      if (json.success) {
        $.toast({
          heading: 'Success',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',
        })
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })
      }
    });
  });

  $(document).on('click', '.edit_prov', function() {
    var row = table_admin.api().row($(this).parents('tr')).data();

    if(!row){
       taxpayer_id = $(this).attr('taxpayer_id');
    }else { 
      taxpayer_id = row[0];
    }
    data = {
      'csrfmiddlewaretoken': token,
      'taxpayer_id': taxpayer_id,
      'option': 'C'
    }
    $('#taxpayer_id_edith').val('');
    $('#email_edith').val('');
    $('#name_edith').val('');
    $('#names_edith').val('');
    $('#last_name_edith').val('');
    $('#second_last_name_edith').val('');
    $.ajax({
        type: 'POST',
        url: '/dashboard/providers/edith/',
        data: data,
        cache: false,
        dataType: 'json',
    }).done(function(json) {
      table_admin.dataTable().fnDraw();
      if (json.success) {
        values =json.values;
        taxpayer_id = values['taxpayer_id'];
        $('#taxpayer_id_edith').val(taxpayer_id);
        $('#email_edith').val(values['user__email']);
        if (taxpayer_id.length == 12) {
          $('#e_fisica').hide();
          $('#e_moral').show();
          $('.nav-tabs a[href="#moral_edith"]').tab('show');
          $('#name_edith').val(values['first_name']);
          //$('#e_fisica').hide().removeClass('active');;
          //$('#e_moral').show().addClass('active');;

        } else {
          $('#e_moral').hide();
          $('#e_fisica').show();
          $('.nav-tabs a[href="#fisica_edith"]').tab('show');
          $('#names_edith').val(values['first_name']);
          $('#last_name_edith').val(values['last_name']);
          $('#second_last_name_edith').val(values['second_last_name']);
          //$('#e_moral').hide().removeClass('active');
          //$('#e_fisica').show().addClass('active');
        }
      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })
      }
    });
    $('#edith_provider').modal('show');
  });

  $('#edith_button').on('click',function(){

    name =  $('#name_edith').val();
    names = $('#names_edith').val();
    last_name = $('#last_name_edith').val();
    second_last_name = $('#second_last_name_edith').val();
    password = $('#password_edith').val();
    email = $('#email_edith').val();
    taxpayer_id = $('#taxpayer_id_edith').val();
    data = {
      'csrfmiddlewaretoken': token,
      'name': name,
      'names': names,
      'last_name': last_name,
      'second_last_name': second_last_name,
      'password': password,
      'email': email,
      'taxpayer_id': taxpayer_id,
      'option': 'ED'
    }

    $.ajax({
        type: 'POST',
        url: '/dashboard/providers/edith/',
        data: data,
        cache: false,
        dataType: 'json',
    }).done(function(json) {
      table_admin.dataTable().fnDraw();
      $('#edith_provider').modal('hide');
      if (json.success) {
        $.toast({
          heading: 'Success',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'success',
          position: 'top-right',
        })

      } else {
        /*alert(json.message);*/
        $.toast({
          heading: 'Error',
          text: json.message,
          showHideTransition: 'fade',
          icon: 'error',
          position: 'top-right',
        })
      }
    });
   });
  
  //$('#add_client').attr('disabled', true);
  //$('#taxpayer_id_help').addClass('hide', true);
  //$('#email_help').addClass('hide', true);

  /* Search */
  /*$("#taxpayer_id_search").keyup(function(e) {
    var code = (e.keyCode || e.which);
    $(this).val($(this).val().replace(/\s+/g, '').toUpperCase())

    var allow_keys = [8, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90];
    //console.log(code);
    //if((code >= 48 && code <= 57) || (code >= 65 && code <= 90) || code == 13 || code == 8 || code == 46) {
    if( $.inArray(code, allow_keys) != -1 ) {
      console.log(code);
      var taxpayer_id = $(this).val()
      if (taxpayer_id.length == 12 || taxpayer_id.length == 13) {
        var data = new FormData();
        data.append('taxpayer_id', taxpayer_id);
        data.append('csrfmiddlewaretoken', token);
        
        $.ajax({
            type: 'POST',
            url: '/dashboard/clients/search/',
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            dataType: 'json',
        }).done(function(response) {
            if (response.success) {
              $('#add_client').removeAttr('disabled');
              $("#name_search").val(response.taxpayer_name);
              $("#email_search").val(response.taxpayer_email);
              $('#email_search').attr('readonly', true);
              $('#taxpayer_id_help').addClass('hide', true);
              $('#email_id_help').addClass('hide', true);
              //if (! $('#name_search').hasClass('show')) {
              $('#name_search').addClass('show');
              //}
              //if (! $('#email_search').hasClass('show')) {
              $('#email_search').addClass('show');
              //}

            } else {
              if (response.already_related) {
                $('#taxpayer_id_help').removeClass('hide');
                $('#taxpayer_id_help').text('Actualmente ya estan conectados.');
                $('#email_search').attr('readonly', 'true');
                $('#email_help').addClass('hide', 'true');
                $('#add_client').attr('disabled', true);
                //if ($('#name_search').hasClass('show')) {
                $('#name_search').removeClass('show');
                //}
                //if ($('#email_search').hasClass('show')) {
                $('#email_search').removeClass('show');
                //}
              }else{
                $("#name_search").val('');
                $("#email_search").val('');
                $('#add_client').removeAttr('disabled');
                $('#taxpayer_id_help').removeClass('hide');
                $('#taxpayer_id_help').text('No registrado en el sistema.');
                $('#email_search').removeAttr('readonly');
                $('#email_help').removeClass('hide');
                $('#email_help').text('Ingrese un correo para enviar una invitación de registro.');
                //if (! $('#email_search').hasClass('show')) {
                $('#email_search').addClass('show');
                //}
                //if ($('#name_search').hasClass('show')) {
                $('#name_search').removeClass('show');
                //}
              }
            }
        });
      } else {
        console.log('IN')
        $('#taxpayer_id_help').addClass('hide', true);
        $('#email_help').addClass('hide', true);
        $('#add_client').attr('disabled', true);
        //if ($('#email_search').hasClass('show')) {
        $('#email_search').removeClass('show');
        //}
        //if ($('#name_search').hasClass('show')) {
        $('#name_search').removeClass('show');
        //}
      }
    }

  });*/
  
  // Validate taxpayer id
  $("#invite_taxpayer_id").blur(function() {
    if (!rfc_regex.test($(this).val())) {
      $("#invite_taxpayer_id_help").text('La estrucura del RFC es inválida.')
      $(this).parent().closest('div').addClass('has-error');
    } else {
      $("#invite_taxpayer_id_help").text('')
      $(this).parent().closest('div').removeClass('has-error');
    }
  });

  // Add provider
  $(document).on("click", "#register-provider", function() {
    var taxpayer_id = "";
    var email = "";
    var name = "";
    var by_email = true;
    
    var data = new FormData();
    taxpayer_id = $("#invite_taxpayer_id").val().toUpperCase();
    email = $("#invite_email").val();
    name = $("#invite_name").val();
    
    /*
    if ($('#invite_email').is('[readonly]')){
      by_email = false
    } else {
      by_email = true
    }
    */
    
    /* TODO: Check taxpayer id format */
    if (!rfc_regex.test(taxpayer_id)) {
      $("#invite_taxpayer_id_help").text('La estrucura del RFC es inválida.');
      return;
    }

    data.append('taxpayer_id', taxpayer_id);
    data.append('email', email);
    data.append('name', name);
    data.append('by_email', by_email);
    data.append('csrfmiddlewaretoken', token);

    $.ajax({
      type: 'POST',
      url: '/providers/add_provider_client/',
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      dataType: 'json',
    }).done(function(response) {
      $('#add-provider-modal').modal('hide');
      $("#invite_taxpayer_id").val('');
      $("#invite_name").val('');
      $("#invite_email").val('');
      $('#invite_taxpayer_id_help').addClass('hide', true);
      $('#providers').DataTable().ajax.reload();
      $('#invite_email_help').addClass('hide', true);
      if (response.success) {
        success_message(response.message);
      } else {
        error_message(response.message);
      }
      });
  });

  $("#refresh_providers").click(function() {
    table_admin.dataTable().fnDraw();
  });
  $(document).on('click', '#clean-filter',  function(event) {
        $("#taxpayer_id, #mail, #name").val('');
        $("#status").prop("selectedIndex",0).change();
        table_admin.dataTable().fnDraw();
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
