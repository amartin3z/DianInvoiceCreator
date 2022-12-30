$(document).ready(function () {
    token = CSRF_TOKEN
    url_status = window.location.pathname;
    var role = role
    var taxpayer_id;
    var code = $('#scheme_val_hidden').attr('code');
    var name = $('#scheme_val_hidden').attr('name');

    if(code != "" || code != null && name != "" || name != null){
        var scheme_id = $('#list_id_wizard');
        var optionScheme = new Option((code+'-'+name), code, true, true);
        scheme_id.append(optionScheme).trigger('change');
    }

    $(document).on("click", ".btnrs",  function(e) {
       var data = new FormData();
      if ($('#taxpayer_id_file')[0] != null){
        var taxpayer_id_file = $('#taxpayer_id_file')[0].files[0]
        data.append('taxpayer_id_file', taxpayer_id_file);
        if (taxpayer_id_file == null){
            $('#taxpayer_id_file-help').text('Campo requerido');
            $('#taxpayer_id_file-help').addClass('text-danger');
            $("#taxpayer_id_file-help").parent().closest('div').addClass('has-error');
            return;
        }
      }

      if ($('#com_dom_file')[0] != null){
          var com_dom_file = $('#com_dom_file')[0].files[0]
          data.append('com_dom_file', com_dom_file);
          if (com_dom_file == null){
              $('#com_dom_file-help').text('Campo requerido');
              $('#com_dom_file-help').addClass('text-danger');
              $("#com_dom_file-help").parent().closest('div').addClass('has-error');
              return;
          }
      }
      if ($('#acta_file')[0] != null){
        var acta_file = $('#acta_file')[0].files[0]
        data.append('acta_file', acta_file);
        if (acta_file == null){
          $('#acta_file-help').text('Campo requerido');
          $('#acta_file-help').addClass('text-danger');
          $("#acta_file-help").parent().closest('div').addClass('has-error');
          return;
        }
      }

      data.append('csrfmiddlewaretoken', token);
      data.append('oper', 'retry');
      data.append('role', 'role');
      data.append('data-id', $(this).attr("data-id"));
      $.ajax({
            type: 'POST',
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false
        }).done(function(json) {
          if (json.success) {
              success_message("Registro Exitoso")
            //   for (var i = 0; i < json.billing.length; i++) {
            //     send_notification(json.title_new, json.message_new, json.billing[i], 'BILLING', json.taxpayer_id_billing)
            //   }
            //   send_notification(json.title_new_user, json.message_new_user, json.user_id)
              sleep(3000);
              location.reload();
          } else {
              error_message(json.message)
          }
      });


    });

    $(document).on('change', ':file', function() {
      var input = $(this),
          numFiles = input.get(0).files ? input.get(0).files.length : 1,
          label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });

    // We can watch for our custom `fileselect` event like this
    $(document).ready( function() {
        $(':file').on('fileselect', function(event, numFiles, label) {

            var input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;

            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }

        });
    });
    //Initialize tooltips
    $('.nav-tabs > li a[title]').tooltip();
    
    //Wizard
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {

        var $target = $(e.target);
    
        if ($target.parent().hasClass('disabled')) {
            return false;
        }
    });

    $('#input-b3').val('');
    $('#input-b4').val('');

    /*$('#manifest_contract').text("");*/
    $(".next-step").click(function (e) {

        var btn_name = $(this).attr('name');
        if(btn_name == "step_one"){
            validate_account()
        }
        if(btn_name == "step_two"){
            $('#checkbox-manifest').removeAttr('checked');
            /*!==*/
            if(typeof $('#show_contract_hidden').val() !== "undefined"){
              success_tab($("#tab_two"));
              next_tab($("#tab_two"));
              var $active = $('.wizard .nav-tabs li.active');
              $active.next().removeClass('disabled');
              nextTab($active);
            }
            if(typeof $('#show_contract_hidden').val() === "undefined"){
                validate_fiel_nxt_step();
                console.log('Entro aqui');
            }
        }
        if(btn_name == "step_three"){
            validate_agreement()
        }
    });
    $(".prev-step").click(function (e) {
        back_tab($(this))
        var $active = $('.wizard .nav-tabs li.active');
        prevTab($active);


    });
   validate_inputs();


   $('#add-cer-form').validator({
    custom:{
        'pwd': function($el){
           pwdKeyIsInvalid = null;
           pwd = $el.val();
           if (!pwd){
               pwd='';
           }
           files = $('#input-b3').prop('files');
           if (pwd){
               keyFile = files[0];
               var keyData = new FormData();
               if (keyFile) {
                keyData.append('private_key', keyFile, keyFile.name)
               }
               keyData.append('pwd_key', btoa(pwd))
               keyData.append( "csrfmiddlewaretoken", getCookie('csrftoken'))
               keyData.append( "oper", 'validate-key-fiel')
               keyData.append('taxpayer_id', $('#taxpayer_id').val());
               $.ajax({
                   method: 'POST',
                   dataType: 'json',
                   async: false,
                   contentType: false,
                   processData: false,
                   url: WIZARD_URL,
                   data: keyData,
                   success: function(response){
                    if (response['message'])
                        pwdKeyIsInvalid = response['message'];

                   },
               });
           }
            return pwdKeyIsInvalid
        },
        'cer': function($el){
           cerIsInvalid = null;
           pwd = $el.val();
           keyFiles = $('#input-b3').prop('files');
           pwd = $('#password-key').val();
           if (keyFiles.length <= 0){
            cerIsInvalid = 'Su archivo .key no debe estar vacio';
            return cerIsInvalid;
           }

           if (cerFiles.length > 0){
               cerFile = cerFiles[0];
               keyFile = keyFiles[0];
               var cerData = new FormData();
               cerData.append('private_key', keyFile, keyFile.name);
               cerData.append('public_key', cerFile, cerFile.name);
               cerData.append('pwd_key', btoa(pwd));
               cerData.append( 'csrfmiddlewaretoken', getCookie('csrftoken'));
               cerData.append( 'oper', 'validate-cer-fiel');
               cerData.append('taxpayer_id', $('#taxpayer_id').val());
               $.ajax({
                   method: 'POST',
                   dataType: 'json',
                   async: false,
                   contentType: false,
                   processData: false,
                   url: WIZARD_URL,
                   data: cerData,
                   success: function(response){
                    if (response['message'])
                        cerIsInvalid = response['message'];
                   },
               });
           }
           return cerIsInvalid
        },
        'key': function($el){
            pwdKeyIsInvalid = null;
            pwd = $('#password-key').val();
            files = $('#input-b3').prop('files');
            cerFiles = $('#input-b4').prop('files');
            if (cerFiles.length <= 0){
              cerIsInvalid = 'Su archivo .cer no debe estar vacio.';
              return cerIsInvalid;
             }
            if (files.length > 0){
                keyFile = files[0];
                var keyData = new FormData();
                keyData.append('private_key', keyFile, keyFile.name)
                keyData.append('pwd_key', btoa(pwd))
                keyData.append( "csrfmiddlewaretoken", getCookie('csrftoken'))
                keyData.append( "oper", 'validate-key-fiel')
                keyData.append('taxpayer_id', $('#taxpayer_id').val());
                $.ajax({
                    method: 'POST',
                    dataType: 'json',
                    async: false,
                    contentType: false,
                    processData: false,
                    url: WIZARD_URL,
                    data: keyData,
                    success: function(response){
                     if (response['message'])
                         pwdKeyIsInvalid = response['message'];
                    },
                });
            }
             return pwdKeyIsInvalid
         },}
    });

});

$('#download_contracts').click(function(e){
  e.preventDefault();
  window.location = '/business/download_manifest_files/';
});

/*$('#show_contract').click(function(e){
  e.preventDefault();
  window.open($(this).val(), '_blank');
});*/

function nextTab(elem) {
    $(elem).next().find('a[data-toggle="tab"]').click();
}
function prevTab(elem) {
    $(elem).prev().find('a[data-toggle="tab"]').click();
}

function validate_account(){
    // NAME IS NOT REQUIRED
    // var name = $("#name").val()
    // if (name == "" || name == null){
    //     $('#name-help').text('Campo requerido');
    //     $('#name-help').addClass('text-danger');
    //     $("#name-help").parent().closest('div').addClass('has-error');
    //     return;
    // }
    // EMAIL IS NOT REQUIRED
    // var email = $("#email").val()
    // if (email == "" || email == null){
    //     $('#email-help').text('Campo requerido');
    //     $('#email-help').addClass('text-danger');
    //     $("#email-help").parent().closest('div').addClass('has-error');
    //     return;
    // }
    var name = $('#name').val();
    var taxpayer_id_regex = /[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]/;

    // var taxpayer_id = $("#taxpayer_id").val();
    var scheme_id = $('#list_id_wizard').val();
    if (scheme_id == "" || scheme_id == null){
        $('#taxpayer_id-help').text('Campo requerido.');
        $('#taxpayer_id-help').addClass('text-danger');
        $("#taxpayer_id-help").parent().closest('div').addClass('has-error');
        return;
    }
    // if (taxpayer_id.match(taxpayer_id_regex) === null){
    //     $('#taxpayer_id-help').text('RFC inválido.');
    //     $('#taxpayer_id-help').addClass('text-danger');
    //     $("#taxpayer_id-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    // var SchemeID = $("#schemeID").val();
    // if (SchemeID == "" || SchemeID === null){
    //     $('#schemeID-help').text('Campo requerido');
    //     $('#schemeID-help').addClass('text-danger');
    //     $("#schemeID-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    var organization_id = $("#organization_id").val();
    if (organization_id == "" || organization_id === null){
        $('#organization_id-help').text('Campo requerido');
        $('#organization_id-help').addClass('text-danger');
        $("#organization_id-help").parent().closest('div').addClass('has-error');
        return;
    }

    // if (organization_id.match(taxpayer_id_regex) === null){
    //     $('#organization_id-help').text('RFC inválido.');
    //     $('#organization_id-help').addClass('text-danger');
    //     $("#organization_id-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    var org_id_party = $("#org_id_party").val();
    if (org_id_party == "" || org_id_party === null){
        $('#org_id_party-help').text('Campo requerido');
        $('#org_id_party-help').addClass('text-danger');
        $("#org_id_party-help").parent().closest('div').addClass('has-error');
        return;
    }

    // var seller_elect_address = $("#s_e_a").val();
    // if (seller_elect_address == "" || seller_elect_address === null){
    //     $('#s_e_a-help').text('Campo requerido');
    //     $('#s_e_a-help').addClass('text-danger');
    //     $("#s_e_a-help").parent().closest('div').addClass('has-error');
    //     return;
    // }
    
    // var cp = $("#zip_code").val();
    // if (cp == "" || cp === null){
    //     $('#cp-help').text('Campo requerido');
    //     $('#cp-help').addClass('text-danger');
    //     $("#cp-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    // var tax_regime = $("#tax_regime").val()
    // if (tax_regime == "" || tax_regime == null){
    //     $('#tax_regime-help').text('Campo requerido');
    //     $('#tax_regime-help').addClass('text-danger');
    //     $("#tax_regime-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    var contry = $("#country").val()
    if (contry == "" || contry == null){
        $('#country-help').text('Campo requerido');
        $('#country-help').addClass('text-danger');
        $("#country-help").parent().closest('div').addClass('has-error');
        return;
    }
    
    // var CountrySubentity = $("#CountrySubentity").val()
    // if (CountrySubentity == "" || CountrySubentity == null){
    //     $('#CountrySubentity-help').text('Campo requerido');
    //     $('#CountrySubentity-help').addClass('text-danger');
    //     $("#CountrySubentity-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    var city = $("#City_Name").val()
    if (city == "" || city == null){
        $('#City_Name-help').text('Campo requerido');
        $('#City_Name-help').addClass('text-danger');
        $("#City_Name-help").parent().closest('div').addClass('has-error');
        return;
    }

    var stree = $("#Street_Name").val()
    if (stree == "" || stree == null){
        $('#Street_Name-help').text('Campo requerido');
        $('#Street_Name-help').addClass('text-danger');
        $("#Street_Name-help").parent().closest('div').addClass('has-error');
        return;
    }

    // var legal_company_id = $('#Legal_Company_Id').val();
    // if(legal_company_id == "" || legal_company_id == null){
    //     $('#Legal_Company_Id-help').text('Campo requerido');
    //     $('#Legal_Company_Id-help').addClass('text-danger');
    //     $("#Legal_Company_Id-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    // var ext_numb = $("#external_number").val()
    // if (ext_numb == "" || ext_numb == null){
    //     $('#external_number-help').text('Campo requerido');
    //     $('#external_number-help').addClass('text-danger');
    //     $("#external_number-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    // var inter_numb = $("#internal_number").val()
    // if (inter_numb == "" || inter_numb == null){
    //     $('#internal_number-help').text('Campo requerido');
    //     $('#internal_number-help').addClass('text-danger');
    //     $("#internal_number-help").parent().closest('div').addClass('has-error');
    //     return;
    // }

    
    // var stree_additional = $("#Additional_StreetName").val()
    // if (stree_additional == "" || stree_additional == null){
        // $('#Additional_StreetName-help').text('Campo requerido');
        // $('#Additional_StreetName-help').addClass('text-danger');
        // $("#Additional_StreetName-help").parent().closest('div').addClass('has-error');
        // return;
    // }

    
    // var address_line = $("#address_line").val()
    // if (address_line == "" || address_line == null){
        // $('#address_line-help').text('Campo requerido');
        // $('#address_line-help').addClass('text-danger');
        // $("#address_line-help").parent().closest('div').addClass('has-error');
        // return;
    // }

    var data = new FormData();
    data.append('csrfmiddlewaretoken', token);
    data.append('oper', 'add_bussines');
    data.append('name', name);
    // data.append('taxpayer_id', taxpayer_id);
    data.append('contry', contry);
    // data.append('CountrySubentity', CountrySubentity);
    data.append('city', city);
    data.append('stree', stree);
    // data.append('cp', cp);
    // data.append('schemeid', SchemeID);
    data.append('schemeID', scheme_id);
    data.append('org_id', organization_id);
    data.append('org_id_party', org_id_party)
    // data.append('legal_org_id', legal_company_id)
    // data.append('sl_elect_add', seller_elect_address);
    // data.append('exter_numb', ext_numb);
    // data.append('inter_numb', inter_numb);

    // data.append('stree_additional', stree_additional);
    // data.append('address_line', address_line);
    // data.append('tax_regime', tax_regime);

    $.ajax({
          type: 'POST',
          data: data,
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false
      }).done(function(json) {
        if (json.success) {
            success_tab($("#tab_one"))
            next_tab($("#tab_one"))
            var $active = $('.wizard .nav-tabs li.active');
            $active.next().removeClass('disabled');
            nextTab($active);
        } else {
            error_message(json.message)
        }
    });

}

$('#taxpayer_id').on('change', function(){
  $('#add-cer-form')[0].reset();
});

$('#sign-manifest').attr('disabled', true).css({'color':'black'});
/*validate_csd();*/
$('#password-key, input[type="file"]').on('change', function(){
    validate_fiel();
    $('#checkbox-manifest').removeAttr('checked');
});

function validate_fiel(){
  var addForm = $('#add-cer-form');
  $('#add-cer-form').data('bs.validator').validate();
  var addFormErr = addForm.find('.has-error');
  keyFiles = $('#input-b3').prop('files');
  cerFiles = $('#input-b4').prop('files');
  pwd = $('#password-key').val();

  if(addFormErr && addFormErr.length > 0 ){
      $('#sign-manifest').attr('disabled', true).css({'color':'black'});
      return
  }else{
      if (keyFiles.length > 0 && cerFiles.length > 0 && pwd !== ''){
          $('#sign-manifest').attr('disabled', false).css({'color':'white'});
      }
      else{
        $('#sign-manifest').attr('disabled', true).css({'color':'black'});
      }
    }
}

function validate_fiel_nxt_step(){
    // var state = $("#state").val()
    // if (state == "" || state == null){
    //     $('#state-help').text('Campo requerido');
    //     $('#state-help').addClass('text-danger');
    //     $("#state-help").parent().closest('div').addClass('has-error');
    //     return;
    // }
    var addForm = $('#add-cer-form');
    $('#add-cer-form').data('bs.validator').validate();
    var addFormErr = addForm.find('.has-error');
    keyFiles = $('#input-b3').prop('files');
    cerFiles = $('#input-b4').prop('files');
    pwd = $('#password-key').val();

    if(addFormErr && addFormErr.length > 0){
        console.log('Entro en el return');
        return
    }else{
        if (keyFiles.length > 0 && cerFiles.length > 0 && pwd !== ''){
            $('#sign-manifest').attr('disabled', false).css({'color':'white'});
            $('#password-key, input[type="file"]').on('change', function(){
                $('#sign-manifest').attr('disabled', true).css({'color':'black'});
                /*$('#checkbox-manifest').removeAttr('checked')*/
            });
        }else{
          $('#sign-manifest').attr('disabled', true).css({'color':'black'});
        }

        if (keyFiles.length <= 0 && cerFiles.length <= 0 && pwd == ''){
            success_tab($("#tab_two"));
            next_tab($("#tab_two"));
            var $active = $('.wizard .nav-tabs li.active');
            $active.next().removeClass('disabled');
            nextTab($active);
            $('#sign-manifest').attr('disabled', true).css({'color':'black'});
        }
    }

}

var checked = false;
$('#checkbox-manifest').click(function(){
  if($(this).is(':checked')){
    checked = true;
  }
  else{
    checked = false;
  }
});


$('#sign-manifest').on('click', function(e){
  e.preventDefault();
  console.log('sdfjaks');
  console.log( $('#taxpayer_id').val());
  var data_fiel = new FormData();
  var key_fiel = $('#input-b3').prop('files');
  var cer_fiel = $('#input-b4').prop('files');
  data_fiel.append('private_key_fiel', key_fiel[0], key_fiel.name)
  data_fiel.append('pwd_key', btoa($('#password-key').val()))
  data_fiel.append('fiel_cer', cer_fiel[0], cer_fiel.name);
  data_fiel.append( "csrfmiddlewaretoken", getCookie('csrftoken'))
  data_fiel.append( "oper", 'sign-manifest')
  data_fiel.append('taxpayer_id', $('#taxpayer_id').val());
  data_fiel.append('name', $('#name').val());
  data_fiel.append('checked', checked);

  $.ajax({
   method: 'POST',
   dataType: 'json',
   async: true,
   contentType: false,
   processData: false,
   url: WIZARD_URL,
   success: function(response){
    if(response['success']){
      setInterval(function(){ window.location = window.location}, 6000);
      $.toast({
            heading: "Exito",
            text: response['message'],
            showHideTransition: "fade",
            icon: "success",
            position: "top-right",
        });
    }
    else{
    }
   },
   data: data_fiel,}).done(function(json) {
        if (json.success) {
          $('#message_alert').removeClass('alert-danger');
            $('#message_alert').addClass('alert-info');
            $('#message_alert').html('<strong>¡Atención!</strong> Por favor, aseg&uacute;rese de que los archivos .cer y .key corresponden a la FIEL, la Firma Electr&oacute;nica (FIEL) sera utilizada para la firma del manifiesto, puede saltar este paso, ya que es opcional, usted puede realizar la firma del manifiesto cuando lo requiera!');
        } else {
            error_message(json.message)
            $('#message_alert').removeClass('alert-info');
            $('#message_alert').addClass('alert-danger');
            $('#message_alert').html('<strong>¡Atención!</strong> Para realizar la firma del manifiesto, es necesario que acepte el contrato');
        }
    }). success;
});

function validate_agreement(){
    var contract = $("#checkbox-contract").is(':checked');
    if (!contract){
        $('#checkbox-contract-help').text('Campo requerido. Acepta el contrato de servicios');
        $('#checkbox-contract-help').addClass('text-danger');
        $("#checkbox-contract-help").parent().closest('div').addClass('has-error');
    }
    var privacy = $("#checkbox-privacy").is(':checked');
    if (!privacy){
        $('#checkbox-privacy-help').text('Campo requerido. Acepta el Aviso de Prisvacidad');
        $('#checkbox-privacy-help').addClass('text-danger');
        $("#checkbox-privacy-help").parent().closest('div').addClass('has-error');
    }
    if (!privacy || !contract ){
        return;
    }
    var data = new FormData();
    data.append('csrfmiddlewaretoken', token);
    data.append('oper', 'sign_agreement');
    $.ajax({
          type: 'POST',
          data: data,
          dataType: 'json',
          cache: false,
          contentType: false,
          processData: false
      }).done(function(json) {
        if (json.success) {
            success_tab($("#tab_three"))
            next_tab($("#tab_three"))
            var $active = $('.wizard .nav-tabs li.active');
            $active.next().removeClass('disabled');
            nextTab($active);
            //type_user = json.typeuser
            // for (var i = 0; i < json.billing.length; i++) {
            //     send_notification(json.title_new, json.message_new, json.billing[i], typeuser, json.taxpayer_id_billing)
            // }
            // send_notification(json.title_new_user, json.message_new_user, json.user_id)
        } else {
            error_message(json.message)
        }
    }).fail(function(e) {
      console.log(e)
      //alert(e);
    });
}

function validate_inputs(){
    $("#name").blur(function() {
        $('#name-help').text('');
        $("#name-help").parent().closest('div').removeClass('has-error');
    });
    // $("#taxpayer_id").blur(function() {
    //     $('#taxpayer_id-help').text('');
    //     $("#taxpayer_id-help").parent().closest('div').removeClass('has-error');
    // });
    $("#checkbox-privacy").click( function(){
       if( $(this).is(':checked') ){
            $('#checkbox-privacy-help').text('');
            $("#checkbox-privacy-help").parent().closest('div').removeClass('has-error');
       }
    });
    $("#checkbox-contract").click( function(){
       if( $(this).is(':checked') ){
            $('#checkbox-contract-help').text('');
            $("#checkbox-contract-help").parent().closest('div').removeClass('has-error');
       }
    });
}

function success_tab(elem){
    var tab = elem
    tab.css("background-color","green");
    tab.children().css("color","#fff");
    tab.children().remove();
    tab.html(`<i style="color:#fff;" class="glyphicon glyphicon-ok"></i>`);
    //tab.children().removeAttr('class');
}

function back_tab(elem){
    var name = elem.attr("name")
    if (name == "step_two"){
        var tab = $("#tab_two")
        tab.css("background-color","#fff")
        tab.children().css("color","#2d2d2d")
        var tab = $("#tab_one")
        tab.css("background-color","#448aff")
        tab.children().css("color","#fff")
        tab.children().removeAttr('class');
        tab.children().attr("class","fa fa-user")
    }else if(name == "step_three"){
        var tab = $("#tab_three")
        tab.css("background-color","#fff")
        tab.children().css("color","#2d2d2d")
        var tab = $("#tab_two")
        tab.css("background-color","#448aff")
        tab.children().css("color","#fff")
        tab.children().removeAttr('class');
        tab.children().attr("class","glyphicon glyphicon-edit")
    }
}
function next_tab(elem){
    var name = elem.attr("id")
    if (name == "tab_one"){
        var tab = $("#tab_two")
        tab.css("background-color","rgb(68, 138, 255)")
    }
    if (name == "tab_two"){
        var tab = $("#tab_three")
        tab.css("background-color","rgb(68, 138, 255)")
    }
    if (name == "tab_three"){
        var tab = $("#tab_end")
        tab.css("background-color","green")
        $('li[name="tabs"]').addClass("disabled")
    }
    tab.children().css("color","#fff")

}

/* ============================ FUNCION MENSAJES DE ERROR ============================ */
    function error_message(message){
            $.toast({
                heading: "Error",
                text: message,
                showHideTransition: "fade",
                icon: "error",
                position: "top-right",
            });
    }

    /* ============================ FUNCION MENSAJES EXITOSOS ============================ */
    function success_message(message){
        $.toast({
            heading: "Correcto",
            text: message,
            showHideTransition: "fade",
            icon: "success",
            position: "top-right",
        });
    }

    function sleep(milliseconds) {
     var start = new Date().getTime();
     for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds) {
       break;
      }
     }
    }

    