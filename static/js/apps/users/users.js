
$(document).ready(function() {
    // const { type } = require("os");
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;

    $('#usuarios').addClass('active');

	aoColumns = [{
        'sWidth': '7%',
        'bSortable': false,
        },{
        'sWidth': '20%',
        'bSortable': false,
        },{
        'sWidth': '28%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
        },{
        'sWidth': '15%',
        'bSortable': false,
    }];
  
    table_users = $('#users-table').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        language: language_datatable,
        'bProcessing': true,
        'bServerSide': true,
         stateSave: true,
        'searching': false,
        "columns": aoColumns,
        "PagingType": 'full_numbers',
        "columnDefs": [
            {
                className: "priority-3 text-center user-name",
                "targets": [2],
            },{
                className: "text-center priority-3 user-type",
                "targets": [4],
            },
            {
                className: "text-center",
                "targets": "_all",
            }
        ],
        sAjaxSource: url_status,
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            if ($('#email').val() != "") {
	            aoData.push({
	                "name": "email",
	                "value": $('#email').val()
	            });
            }
            if ($('#name').val() != "") {
                aoData.push({
                    "name": "name",
                    "value": $('#name').val()
                });
            }
            if ($('#group option:selected').val() != "all") {
	            aoData.push({
	                "name": "group",
	                "value": $('#group option:selected').val()
	            });
            }
            if ($('#status option:selected').val() != "all") {
	            aoData.push({
	                "name": "status",
	                "value": $('#status option:selected').val()
	            });
            }

            if ($('#taxpayer-id').val()) {
                aoData.push({
                    'name': 'taxpayer_id',
                    'value': $('#taxpayer-id').val(),
                })
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

    $("#email, #name, #taxpayer-id").keyup(function() {
        if ($(this).val().length > 2 || $(this).val().length == 0)   {
            table_users.draw();
        } 
    });

    $("#group, #status").change(function() {
        table_users.draw();
    });

    $(document).on('click', '#clean-users',  function(event) {
        $('#taxpayer-id, #email, #name').val('');
        $('#group, #status').selectpicker('val', 'all');
        table_users.draw();
    });

    $('#refresh_users').click(function() {
        table_users.ajax.reload();
    });
    
    /* Personalización */
    $(document).on('click', '.get-in', function() {
        //console.log('GET-IN');
        var row = table_users.row( this ).data();
        if(!row){
            email =  $(this).attr('email');
        }else {
            email = row[1];
        }
        //console.log(email);
        data = {
              'csrfmiddlewaretoken': token,
              'email': email,
              'option': 'P'
        }

        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(json) {
          if (json.success) {
            $.toast({
                heading: 'Success',
                text: json.message,
                showHideTransition: 'fade',
                icon: 'success',
                position: 'top-right',
            })
            window.location.replace('/')
          } else {
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

    /* Suspender Activar */
    $(document).on('click', '.sus-act', function() {
        var row = table_users.row( this ).data();

        if(!row){
            email = $(this).attr('email');
        }else { 
           email = row[1];
        }

        data = {
            'csrfmiddlewaretoken': token,
            'email': email,
            'option': 'AS'
        }

        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(json) {
            table_users.draw();
            if (json.success) {
                $.toast({
                    heading: 'Success',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'success',
                    position: 'top-right',
                })
            } else {
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

    /* Edit user */
    $(document).on('click', '.edit', function(e){
        e.preventDefault();
        email = $(this).attr('email');
        role = $(this).attr("role");
        user_name = $(this).closest('tr').children('td.user-name').text();
        user_type = $(this).closest('tr').children('td.user-type').text();
        $('#user-name').text(user_name + ' ' + '(' + user_type + ')' );
        //$('#general-info').find('div.info').text('');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            url: '/users/options',
            data: {
                'option': 'get-info',
                'email': email,
                'csrfmiddlewaretoken': token,
            },
            success: function(response){
                if (response['success']){
                    $('#edit_user_id').val(response['info']['edit_user_id']);
                    $('#edit_username').val(response['info']['edit_username']);
                    $('#edit_email').val(response['info']['edit_email']);
                    $('#edit_firstname').val(response['info']['edit_firstname']);
                    $('#edit_lastname').val(response['info']['edit_lastname']);
                    // $('#edit_group').val(response['info']['edit_group']);
                    $('#edit_businesses').val(response['info']['edit_businesses']).change();
                    $('.selectpicker').selectpicker('refresh');
                    $('#edit_newpass').val('');
                    $('#edit_newpass2').val('');
                    $('#modal-edit-user').modal('show');
                    if (role == 'E') {
                        $('#user-group').show();
                        $('#user-businesses').show();
                    } else {
                        $('#user-group').hide();
                        $('#user-businesses').hide();
                    }
                }else{
                    $.toast({
                        heading: 'Error',
                        text: response['message'],
                        showHideTransition: 'fade',
                        icon: 'error',
                        position: 'top-right',
                    });                    
                }
            }
        })        
    });
    
    /* Update user data */
    $('.update').on('click',function(){
        user_id = $('#edit_user_id').val();
        username = $('#edit_username').val();
        email = $('#edit_email').val();
        first_name = $('#edit_firstname').val();
        last_name = $('#edit_lastname').val();
        // group = $('#edit_group').val();
        group = 'A';
        businesses = $('#edit_businesses').val();
        new_pass = $('#edit_newpass').val();
        new_pass_conf = $('#edit_newpass2').val();

        if (first_name.trim() == "" || last_name.trim() == "") {
            error_message("El nombre y apellido son requeridos.");
            return
        }

        if (new_pass != new_pass_conf){
            //$('#new_pass_conf_help').text('La confirmación de la contraseña es incorrecta');
            error_message("La confirmación de la contraseña es incorrecta.");
            return
        }

        data = {
            'csrfmiddlewaretoken': token,
            'user_id': user_id,
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'group': group,
            'businesses': businesses,
            'option': 'update-info',
        }

        if (new_pass != '') {
            data['new_password'] = new_pass
        }

        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(json) {
            table_users.draw();
            $('#modal-edit-user').modal('hide');
            if (json.success) {
                $.toast({
                    heading: 'Success',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'success',
                    position: 'top-right',
                })
            } else {
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

    /* Change password */
    $('#user-pass-new-conf').hide();
    $('#edit_newpass').keyup(function() {
        //console.log($('#new_pass').val().length);
        if ($('#edit_newpass').val().length > 7 ){
            $('#new_pass_help').hide();
            
            if ($('#edit_newpass2').val().length > 0) {
              $('#new_pass_conf_help').text('La confirmación de la contraseña es incorrecta');
            } else {
              $('#new_pass_conf_help').text('');
            }
            $('#user-pass-new-conf').show();
        } else {
            $('#edit_newpass2').val('');
            $('#user-pass-new-conf').hide();
            $('#new_pass_help').text('La nueva contraseña debe contener por lo menos 8 caractéres');
            $('#new_pass_help').show();
        }
    });

    $('#new_pass_help').hide();
    $('#edit_newpass').blur(function() {
        if ($('#edit_newpass').val().length < 8 ){
            $('#new_pass_help').text('La nueva contraseña debe contener por lo menos 8 caractéres');
            $('#new_pass_help').show();
        }
    });

    $('#new_pass_conf_help').hide();
    $('#edit_newpass2').blur(function() {
        $('#new_pass_conf_help').text('');
        if ( $('#edit_newpass').val() != $('#edit_newpass2').val() ){
            $('#new_pass_conf_help').text('La confirmación de la contraseña es incorrecta');
            $('#new_pass_conf_help').show();
        } else {
            $('#new_pass_conf_help').hide();
        }
    });

// Validate firstname | Edit
    $("#edit_firstname").blur(function() {
        if ($(this).val().trim() == "") {
            $("#edit_firstname_help").text('Éste campo es requerido.');
            $(this).parent().closest('div').addClass('has-error');
        } else {
            $("#edit_firstname_help").text('')
            $(this).parent().closest('div').removeClass('has-error');
        }
    });

    // Validate firstname | Edit
    $("#edit_lastname").blur(function() {
        if ($(this).val().trim() == "") {
            $("#edit_lastname_help").text('Éste campo es requerido.');
            $(this).parent().closest('div').addClass('has-error');
        } else {
            $("#edit_lastname_help").text('')
            $(this).parent().closest('div').removeClass('has-error');
        }
    });

    $('#add-user').on('click',function(){
        $('.selected').removeClass('selected')
        // $("#add_group").prop('selectedIndex', 10).change();
        // $("#add_businesses").prop('selectedIndex', 10).change();
    });

    /* Add user*/
    $('.add').on('click',function(){
        username = $('#add_username').val();
        first_name = $('#add_firstname').val();
        last_name = $('#add_lastname').val();
        _type = $('#add_type').val();
        taxpayer_id = $('#add_taxpayer_id').val();
        // group = $('#add_group').val();
        // businesses = $('#add_businesses').val();
        new_pass = $('#add_password').val();
        new_pass_conf = $('#add_password2').val();
        
        console.log(_type);

        if (first_name.trim() == "") {
            $("#firstname_help").text('Éste campo es requerido.');
            $("#add_firstname").parent().closest('div').addClass('has-error');
            return
        } else {
            $("#firstname_help").text('')
            $("#add_firstname").parent().closest('div').removeClass('has-error');
        }

        if (last_name.trim() == "") {
            $("#lastname_help").text('Éste campo es requerido.');
            $("#add_lastname").parent().closest('div').addClass('has-error');
            return
        } else {
            $("#lastname_help").text('')
            $("#add_lastname").parent().closest('div').removeClass('has-error');
        }
        

        if (_type == "C"  && !rfc_regex.test(taxpayer_id)) {
            $("#taxpayer_id_help").text('Estructura inválida.')
            $("#add_taxpayer_id").parent().closest('div').addClass('has-error');
            return
        } else {
            $("#taxpayer_id_help").text('')
            $("#add_taxpayer_id").parent().closest('div').removeClass('has-error');
        }

        // if (type == "E" && businesses == null) {
        //     $('#businesses_help').text('Debes selecionar al menos un negocio.');
        //     $("#add_businesses").parent().closest('div[id="user-businesses"]').addClass('has-error');
        //     return
        // } else {
        //     $('#businesses_help').text('');
        //     $("#add_businesses").parent().closest('div[id="user-businesses"]').removeClass('has-error');
        // }

        if (new_pass.trim() == "") {
            $('#pass_help').text('Éste campo es requerido.');
            $("#add_password").parent().closest('div').addClass('has-error');
            return
        } else if (new_pass.length < 7) {
            $('#pass_help').text('La contraseña debe contener al menos 8 caractéres.');
            $("#add_password").parent().closest('div').addClass('has-error');
            return
        } else {
            $('#pass_help').text('');
            $("#add_password").parent().closest('div').removeClass('has-error');
        }
        
        if (new_pass != new_pass_conf){
            $('#pass2_help').text('La confirmación de la contraseña es incorrecta.');
            $("#add_password2").parent().closest('div').addClass('has-error');
            return
        } else {
            $('#pass2_help').text('');
        }

        data = {
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            // 'group': group,
            'group': 'AD',
            'type': _type,
            'taxpayer_id': taxpayer_id,
            // 'businesses': businesses,
            'password': new_pass,
            'option': 'add-user',
        }

        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(json) {
            table_users.draw();
            
            if (json.success) {
                $('#modal-add-user').modal('hide');
                $.toast({
                    heading: 'Correcto',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'success',
                    position: 'top-right',
                });                
                table_users.draw();
            } else {
                $.toast({
                    heading: 'Error',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'error',
                    position: 'top-right',
                });
            }
            $("#add_type").prop('selectedIndex', 0).change();
            // $("#add_group").prop('selectedIndex', 0).change();
            // $("#add_businesses").prop('selectedIndex', 0).change();
        });
    });

    /* Change password */
    $('#user-pass-new-conf').hide();
    $('#edit_newpass').keyup(function() {
        if ($('#edit_newpass').val().length > 7 ){
            $('#new_pass_help').hide();
            
            if ($('#edit_newpass2').val().length > 0) {
              $('#new_pass_conf_help').text('La confirmación de la contraseña es incorrecta');
            } else {
              $('#new_pass_conf_help').text('');
            }
            $('#user-pass-new-conf').show();
        } else {
            $('#edit_newpass2').val('');
            $('#user-pass-new-conf').hide();
            $('#new_pass_help').text('La nueva contraseña debe contener por lo menos 8 caractéres');
            $('#new_pass_help').show();
        }
    });

    $('#new_pass_help').hide();
    $('#edit_newpass').blur(function() {
        if ($('#edit_newpass').val().length < 8 ){
            $('#new_pass_help').text('La nueva contraseña debe contener por lo menos 8 caractéres');
            $('#new_pass_help').show();
        }
    });

    $('#new_pass_conf_help').hide();
    $('#edit_newpass2').blur(function() {
        $('#new_pass_conf_help').text('');
        if ( $('#edit_newpass').val() != $('#edit_newpass2').val() ){
            $('#new_pass_conf_help').text('La confirmación de la contraseña es incorrecta');
            $('#new_pass_conf_help').show();
        } else {
            $('#new_pass_conf_help').hide();
        }
    });

    $('#add_type').change(function(){
        if ($(this).val() == 'C') {
            $('#add_taxpayer_id').parent().show();
            // $('#add_group').parent().parent().hide();
            // $('#add_businesses').parent().parent().hide();
        } else {
            $('#add_taxpayer_id').parent().hide();
            // $('#add_group').parent().parent().show();
            // $('#add_businesses').parent().parent().show();
        }
    });

    // Validate username | Add
    $("#add_username").blur(function() {
        username = $(this).val();
        data = {
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            'option': 'validate-email',
            'username': username
        }
        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(response) {
            if (response.success) {
                $("#username_help").text('');
                $(this).parent().closest('div').removeClass('has-error');
            } else {
                if (response.message == 'bad_email') {
                    $("#username_help").text('Ese usuario es inválido.');
                } else if (response.message == 'existing_user') {
                    $("#username_help").text('Ese usuario ya está en uso. Prueba con otro.');
                }
                $(this).parent().closest('div').addClass('has-error');
            }
        });
    });

    // Validate firstname | Add
    $("#add_firstname").blur(function() {
        if ($(this).val().trim() == "") {
            $("#firstname_help").text('Éste campo es requerido.');
            $(this).parent().closest('div').addClass('has-error');
        } else {
            $("#firstname_help").text('')
            $(this).parent().closest('div').removeClass('has-error');
        }
    });

    // Validate firstname | Add
    $("#add_lastname").blur(function() {
        if ($(this).val().trim() == "") {
            $("#lastname_help").text('Éste campo es requerido.');
            $(this).parent().closest('div').addClass('has-error');
        } else {
            $("#lastname_help").text('')
            $(this).parent().closest('div').removeClass('has-error');
        }
    });

    // Validate taxpayer id | Add
    $("#add_taxpayer_id").keyup(function() {
        limit = 13
        if ($(this).val().length > limit) {
            $(this).val($(this).val().substring(0, limit))
        }
    });
    
    $("#add_taxpayer_id").blur(function() {
        taxpayer_id = $(this).val()
        if (!rfc_regex.test(taxpayer_id)) {
            $("#taxpayer_id_help").text('Estructura inválida');
            $(this).parent().closest('div').addClass('has-error');
            return
        } else {
            $("#taxpayer_id_help").text('')
            $(this).parent().closest('div').removeClass('has-error');
        }

        data = {
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            'option': 'exists-rfc',
            'taxpayer_id': taxpayer_id
        }  

        $.ajax({
            type: 'POST',
            url: '/users/options',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(response) {
            if (response.success) {
                $("#taxpayer_id_help").text('');
                $(this).parent().closest('div').removeClass('has-error');
            } else {
                $("#taxpayer_id_help").text('RFC previamente registrado');
                $(this).parent().closest('div').addClass('has-error');
            }
        });
        //return
    });

    // Validate password | Add
    $("#add_password").blur(function() {
        if ($(this).val().length < 8) {
            $('#pass_help').text('La contraseña debe contener al menos 8 caractéres.');
            $("#add_password").parent().closest('div').addClass('has-error');
            return
        } else {
            $('#pass_help').text('');
            $("#add_password").parent().closest('div').removeClass('has-error');
        }
    });

    // Validate password confirmation
    $("#add_password2").blur(function() {
        if ($(this).val() != $("#add_password").val()) {
            $('#pass2_help').text('La confirmación de la contraseña es incorrecta.');
            $("#add_password2").parent().closest('div').addClass('has-error');
            return
        } else {
            $('#pass2_help').text('');
            $("#add_password2").parent().closest('div').removeClass('has-error');
        }
    });

    $('#modal-add-user').on('hidden.bs.modal', function (e) {
        $(this)
            .find("input")
               .val('')
               .end()
            .find("select")
               .prop('selectedIndex', 0)
               .change()
               .end()
            .find("small")
                .text('')
                .parent()
                    .closest('div')
                    .removeClass('has-error')
                .end();
    });

    $(document).on('click', '.unlock-user', function(e){
        e.preventDefault();
        user_id = $(this).attr('user');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            url: '/users/options',
            data: {
                'option': 'unlock-user',
                'user_id': user_id,
                'csrfmiddlewaretoken': token,
            },
            success: function(response){
                if (response['success']){
                    $.toast({
                        heading: 'Correcto',
                        text: response['message'],
                        showHideTransition: 'fade',
                        icon: 'success',
                        position: 'top-right',
                    });                
                    table_users.draw();
                } else {
                    $.toast({
                        heading: 'Error',
                        text: response['message'],
                        showHideTransition: 'fade',
                        icon: 'error',
                        position: 'top-right',
                    });                    
                }
            }
        })        
    });

    $(document).on('click', '.canc-del', function (e) {
        e.preventDefault();
        user_id = $(this).attr('user');
        user_username = $(this).attr('email');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            url: '/users/options',
            data: {
                'option': 'cancel-unlock',
                'user_id': user_id,
                'username': user_username,
                'csrfmiddlewaretoken': token,
            },
            success: function(response){
                if (response['success']){
                    $.toast({
                        heading: 'Correcto',
                        text: response['message'],
                        showHideTransition: 'fade',
                        icon: 'success',
                        position: 'top-right',
                    });                
                    table_users.draw();
                } else {
                    $.toast({
                        heading: 'Error',
                        text: response['message'],
                        showHideTransition: 'fade',
                        icon: 'error',
                        position: 'top-right',
                    });                    
                }
            }
        })           
     });

});