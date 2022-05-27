$(document).ready(function() {
    $('#support').addClass('active');
    $('#support').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;

    aoColumns = [{
        'sWidth': '5%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '30%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '12%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
        },{
        'sWidth': '10%',
        'bSortable': false,
    }];
    var table_tickets = $('#table-tickets').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        "language": language_datatable,
        "bProcessing": true,
        "bServerSide": true,
        "stateSave": true,
        "searching": false,
        "columns": aoColumns,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            { className: "text-center", "targets": [0,1,3,4,5,6,7],},
            { className: "txt-title", "targets": [2] },
        ],
        fnServerData: function(sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": token
            });
            if ($('#ticket_id').val()){
                aoData.push({
                    "name": "ticket_id",
                    "value": $('#ticket_id').val()
                });
            }
            if ($('#tickets_subject').val()){
                aoData.push({
                    "name": "ticket_subject",
                    "value": $('#tickets_subject').val()
                });
            }
            if ($('#ticket_status').val() != 'T'){
                aoData.push({
                    "name": "ticket_status",
                    "value": $('#ticket_status').val()
                });
            }
            if ($('#ticket_category').val() != 'T'){
                aoData.push({
                    "name": "ticket_category",
                    "value": $('#ticket_category').val()
                });
            }
            if ($('#ticket_priority').val() != 'T'){
                aoData.push({
                    "name": "ticket_priority",
                    "value": $('#ticket_priority').val()
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
            $('[data-toggle="popover"]').popover();
        }
    });

   /* ============================ FILTRADO LISTADO DE TICKETS ============================ */
    $("#ticket_id").keyup(function(e) {
       e.preventDefault();
       len = $(this).val().length
       if ((len > 0 || len == 0) && is_valid_key(e.which)) { 
         table_tickets.ajax.reload()
       }
    });
    $("#tickets_subject").keyup(function(e) {
       e.preventDefault();
       len = $(this).val().length
       if ((len > 3 || len == 0) && is_valid_key(e.which)) { 
         table_tickets.ajax.reload()
       }
    });
    $('#ticket_status, #ticket_category , #ticket_priority').change( function(e){
           table_tickets.ajax.reload()
    });
   /* ===================================================================================== */

    $(document).on("click", "#add_ticket, #add_new_ticket",  function(e) {
        e.preventDefault();
        var adata = new FormData()
        adata.append('csrfmiddlewaretoken', token);
        adata.append('option', 'get_queues');
        $.ajax({
            type: 'POST',
            url: TICKETS_OPTIONS,
            data: adata,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false
        }).done(function(json) {
            if (json.success == true) {
                $("#ticket_queue").empty();
                $.each(json.message,function(key, queue_dic) {
                    $("#ticket_queue").append('<option value='+queue_dic.code+'>'+queue_dic.des+'</option>').selectpicker('refresh');
                });
                $('#modal-add-ticket').modal('show');
            } else {
                error_message(json.message)
            }
        });
    });

    $(document).on("click", "#close_ticket, #close-ticket",  function(e) {
        clear_modal();
    });

    validate_inputs()

    $(document).on("click", "#show_ticket",  function(e) {
        var id = $(this).attr("data-id")
        $("#ticket-id").text("#"+id)
        var subject = $(this).attr("data-sub")
        $("#ticket-subject").text(subject)

        var adata = new FormData()
        adata.append('csrfmiddlewaretoken', token);
        adata.append('option', 'followup_ticket');
        adata.append('data-id', id);
        $.ajax({
            type: 'POST',
            url: TICKETS_OPTIONS,
            data: adata,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false
        }).done(function(json) {
            if (json.success == true) {
                $(".timeline").empty();
                json.message.forEach(element => $(".timeline").append(element));
                $('#modal-followup-ticket').modal('show');
            } else {
                error_message(json.message)
            }
        });
    });

    $(document).on("click", "#update_ticket",  function(e) {
        var id = $(this).attr("data-id")
        $("#ticket-up-id").text("#"+id)
        var subject = $(this).attr("data-sub")
        $("#ticket-up-subject").val(subject)
        $("#ticket-up-desc, #ticket_file2").val("")
        $(".update_ticket").attr("data-up-id",id)
        $('#modal-update-ticket').modal('show');
    });

    $(document).on("click", ".update_ticket",  function(e) {
        var data = new FormData();
        data.append('data-id', $(this).attr("data-up-id"));
        var description = $("#ticket-up-desc").val()
        data.append('description', description);
        if (description == "" || description == null){
            $('#ticket-up-desc-help').text('Campo requerido');
            $('#ticket-up-desc-help').addClass('text-danger');
            $("#ticket-up-desc-help").parent().closest('div').addClass('has-error');
            return;
        }
        if ($('#ticket_file2')[0].files.length >0){
            var file = $('#ticket_file2')[0].files[0]
            data.append('file', file);
        }
        data.append('csrfmiddlewaretoken', token);
        data.append('option', 'update_ticket');
        $.ajax({
              type: 'POST',
              url: TICKETS_OPTIONS,
              data: data,
              dataType: 'json',
              cache: false,
              contentType: false,
              processData: false
          }).done(function(json) {
            if (json.success) {
                success_message(json.message)
                $('#modal-update-ticket').modal('hide');
                table_tickets.ajax.reload()
            } else {
                error_message(json.message)
            }
        });
    });


    $(document).on("click", ".save_ticket",  function(e) {
        var data = new FormData();
        var subject = $("#ticket_subject").val()
        data.append('subject', subject);
        if (subject == "" || subject == null){
            $('#ticket_subject_help').text('Campo requerido');
            $('#ticket_subject_help').addClass('text-danger');
            $("#ticket_subject_help").parent().closest('div').addClass('has-error');
            return;
        }
        var description = $("#ticket_desc").val()
        data.append('description', description);
        if (description == "" || description == null){
            $('#ticket_desc_help').text('Campo requerido');
            $('#ticket_desc_help').addClass('text-danger');
            $("#ticket_desc_help").parent().closest('div').addClass('has-error');
            return;
        }
        var queue = $("#ticket_queue").val()
        data.append('queue', queue);
        if (queue == "" || queue == null){
            $('#ticket_queue_help').text('Campo requerido');
            $('#ticket_queue_help').addClass('text-danger');
            $("#ticket_queue_help").parent().closest('div').addClass('has-error');
            return;
        }
        var priorty = $("#ticket_priorty").val()
        data.append('priorty', priorty);
        if (priorty == "" || priorty == null){
            $('#ticket_priorty_help').text('Campo requerido');
            $('#ticket_priorty_help').addClass('text-danger');
            $("#ticket_priorty_help").parent().closest('div').addClass('has-error');
            return;
        }
        if ($('#ticket_file')[0].files.length >0){
            var file = $('#ticket_file')[0].files[0]
            data.append('file', file);
        }
        data.append('csrfmiddlewaretoken', token);
        data.append('option', 'add_ticket');
        $.ajax({
              type: 'POST',
              url: TICKETS_OPTIONS,
              data: data,
              dataType: 'json',
              cache: false,
              contentType: false,
              processData: false
          }).done(function(json) {
            if (json.success) {
                clear_modal();
                success_message(json.message)
                $('#modal-add-ticket').modal('hide');
                table_tickets.ajax.reload()
            } else {
                error_message(json.message)
            }
        });
    });

    $(document).on("click", "#solved_ticket",  function(e) {
        var id = $(this).attr("data-id")
        $("#ticket-solved-id").text("#"+id)
        var subject = $(this).attr("data-sub")
        $("#ticket-solved-subject").val(subject)
        $("#ticket-solved-desc, #ticket_file2").val("")
        $(".solved_ticket").attr("data-solved-id",id)
        $('#modal-solved-ticket').modal('show');
    });

    $(document).on("click", ".solved_ticket",  function(e) {
        var data = new FormData();
        data.append('data-id', $(this).attr("data-solved-id"));
        var description = $("#ticket-solved-desc").val()
        data.append('description', description);
        if (description == "" || description == null){
            $('#ticket-solved-desc-help').text('Campo requerido');
            $('#ticket-solved-desc-help').addClass('text-danger');
            $("#ticket-solved-desc-help").parent().closest('div').addClass('has-error');
            return;
        }
        data.append('csrfmiddlewaretoken', token);
        data.append('option', 'solved_ticket');
        $.ajax({
              type: 'POST',
              url: TICKETS_OPTIONS,
              data: data,
              dataType: 'json',
              cache: false,
              contentType: false,
              processData: false
          }).done(function(json) {
            if (json.success) {
                success_message(json.message)
                $('#modal-solved-ticket').modal('hide');
                table_tickets.ajax.reload()
            } else {
                error_message(json.message)
            }
        });
    });


    $(document).on("click", "#clean",  function(e) {
        clear_filters();
        table_tickets.ajax.reload();
    });


    $(function() {
        bs_input_file();
        bs_input_file2();
    });

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

});

function bs_input_file() {
    $(".input-file").before(
        function() {
            if ( ! $(this).prev().hasClass('input-ghost') ) {
                var element = $("<input type='file' class='input-ghost' id='ticket_file' style='visibility:hidden; height:0'>");
                element.attr("name",$(this).attr("name"));
                element.change(function(){
                    element.next(element).find('input').val((element.val()).split('\\').pop());
                });
                $(this).find("button.btn-choose").click(function(){
                    element.click();
                });
                $(this).find("button.btn-reset").click(function(){
                    element.val(null);
                    $(this).parents(".input-file").find('input').val('');
                });
                $(this).find('input').css("cursor","pointer");
                $(this).find('input').mousedown(function() {
                    $(this).parents('.input-file').prev().click();
                    return false;
                });
                return element;
            }
        }
    );
}

function bs_input_file2() {
    $(".input-file2").before(
        function() {
            if ( ! $(this).prev().hasClass('input-ghost') ) {
                var element = $("<input type='file' class='input-ghost' id='ticket_file2' style='visibility:hidden; height:0'>");
                element.attr("name",$(this).attr("name"));
                element.change(function(){
                    element.next(element).find('input').val((element.val()).split('\\').pop());
                });
                $(this).find("button.btn-choose").click(function(){
                    element.click();
                });
                $(this).find("button.btn-reset2").click(function(){
                    element.val(null);
                    $(this).parents(".input-file2").find('input').val('');
                });
                $(this).find('input').css("cursor","pointer");
                $(this).find('input').mousedown(function() {
                    $(this).parents('.input-file2').prev().click();
                    return false;
                });
                return element;
            }
        }
    );
}


function clear_modal(){
    $("#ticket_subject").val("")
    $("#ticket_desc").val("")
    $("#ticket_file, #ticket_file1").val("")
    $("#ticket_priorty").prop("selectedIndex",2).change();
    $("#ticket_subject_help, #ticket_desc_help, #ticket_priorty_help, #ticket_priorty_help").text('') 
}

function clear_filters(){
    $("#ticket_id, #tickets_subject").val("")
    $("#ticket_status, #ticket_category, #ticket_priority").prop("selectedIndex",0).change();
}


function validate_inputs(){
    $("#ticket_subject").blur(function() {
        $('#ticket_subject_help').text('');
        $("#ticket_subject_help").parent().closest('div').removeClass('has-error');
    });
    $("#ticket_desc").blur(function() {
        $('#ticket_desc_help').text('');
        $("#ticket_desc_help").parent().closest('div').removeClass('has-error');
    });
    $("#ticket_priorty").blur(function() {
        $('#ticket_priorty_help').text('');
        $("#ticket_priorty_help").parent().closest('div').removeClass('has-error');
    });
    $("#ticket_queue").blur(function() {
        $('#ticket_queue_help').text('');
        $("#ticket_queue_help").parent().closest('div').removeClass('has-error');
    });
    $("#ticket-up-desc").blur(function() {
        $('#ticket-up-desc-help').text('');
        $("#ticket-up-desc-help").parent().closest('div').removeClass('has-error');
    });
}
