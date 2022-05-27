$(function() {
    $("input[type='password'][data-eye]").each(function(i) {
        var $this = $(this);

        $this.wrap($("<div/>", {
            style: 'position:relative'
        }));
        $this.css({
            paddingRight: 60
        });
        $this.after($("<div/>", {
            html: 'Ver',
            class: 'btn btn-primary btn-sm',
            id: 'passeye-toggle-'+i,
            style: 'position:absolute;right:10px;top:50%;transform:translate(0,-50%);-webkit-transform:translate(0,-50%);-o-transform:translate(0,-50%);padding: 2px 7px;font-size:12px;cursor:pointer;'
        }));
        $this.after($("<input/>", {
            type: 'hidden',
            id: 'passeye-' + i
        }));
        $this.on("keyup paste", function() {
            $("#passeye-"+i).val($(this).val());
        });

        $("#passeye-toggle-"+i).on("click", function() {
            if($this.hasClass("show")) {
                $("#passeye-toggle-"+i).text('Ver');
                $this.attr('type', 'password');
                $this.removeClass("show");
                $(this).removeClass("btn-outline-primary");
            }else{
                $("#passeye-toggle-"+i).text('Ocultar');
                $("#passeye-toggle-"+i).css('color', '#FFFFFF');
                $this.attr('type', 'text');
                $this.val($("#passeye-"+i).val());              
                $this.addClass("show");
                $(this).addClass("btn-outline-primary");
            }
        });

        if (localStorage.chkbx && localStorage.chkbx != '') {
            $('#remember_me').attr('checked', 'checked');
            $('#email').val(localStorage.usrname);
            $('#password').val(localStorage.pass);
        } else {
            $('#remember_me').removeAttr('checked');
            $('#username').val('');
            $('#password').val('');
        }

        $('#remember_me').click(function() {
            if ($('#remember_me').is(':checked')) {
                // save username and password
                localStorage.usrname = $('#email').val();
                localStorage.pass = $('#password').val();
                localStorage.chkbx = $('#remember_me').val();
            } else {
                localStorage.usrname = '';
                localStorage.pass = '';
                localStorage.chkbx = '';
            }
        });
    });
});


$(document).ready(function() {
    var win = location.search.substr(1);
    var activate = '¡Éxito! Tu cuenta ha sido activada ahora puede iniciar sesión.'
    if (win.indexOf('activate') != -1) {
      $("#div_activate").text(activate);
    } else {
      $("#div_strong").css("display", "none");
    }
    $("#login_form").submit(function(event) {
            event.preventDefault(); 
            data = new FormData($('#login_form')[0]);

            $.ajax({
                  type: 'POST',
                  url: LOGIN_URL,
                  data: data,
                  dataType: 'json',
                  cache: false,
                  contentType: false,
                  processData: false
              }).done(function(json) {
                 if (json.success) {
                    //window.location.replace(json.url);
                    window.location.reload();
                    /**
                     * ¿Usar windows.location.reload()
                     * o Usar windows.location.replace()?
                     */
                 }
                 else{
                    /*alert(json.message);*/
                    $.toast({
                        heading: 'Error',
                        text: json.message,
                        showHideTransition: 'fade',
                        icon: 'error',
                        position: 'top-right',
                    })
     
                 }
              }).fail(function(jqXHR,status, errorThrown) {
                  //console.log(errorThrown);
                  //console.log(jqXHR.responseText);
                  //console.log(jqXHR.status);
                  //showSuccessMessage('');
                  alert(status);
              });
        });

    $('.set-language').on('click', function(event){
        event.preventDefault();
        var languageCode = $(this).data('code');
        var setLanguageForm = new FormData();
        setLanguageForm.append('language', languageCode);
        setLanguageForm.append("csrfmiddlewaretoken", $("[name=csrfmiddlewaretoken]").val());
        $.ajax({
            type: 'POST',
            url: SET_LANGUAGE,
            data: setLanguageForm,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false
        }).done(function(response) {
           window.location.reload();
        }).fail(function(jqXHR,status, errorThrown) {
            console.log(status);
        });
        
    });
 });
