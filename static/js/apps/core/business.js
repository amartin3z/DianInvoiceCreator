// Pipelining function for DataTables. To be used to the `ajax` option of DataTables
$.fn.dataTable.pipeline = function ( opts ) {
    // Configuration options
    var conf = $.extend( {
        pages: 5,     // number of pages to cache
        url: '',      // script url
        data: null,   // function or object with parameters to send to the server
                      // matching how `ajax.data` works in DataTables
        method: 'GET' // Ajax HTTP method
    }, opts );
 
    // Private variables for storing the cache
    var cacheLower = -1;
    var cacheUpper = null;
    var cacheLastRequest = null;
    var cacheLastJson = null;
 
    return function ( request, drawCallback, settings ) {
        var ajax          = false;
        var requestStart  = request.start;
        var drawStart     = request.start;
        var requestLength = request.length;
        var requestEnd    = requestStart + requestLength;
         
        if ( settings.clearCache ) {
            // API requested that the cache be cleared
            ajax = true;
            settings.clearCache = false;
        }
        else if ( cacheLower < 0 || requestStart < cacheLower || requestEnd > cacheUpper ) {
            // outside cached data - need to make a request
            ajax = true;
        }
        else if ( JSON.stringify( request.order )   !== JSON.stringify( cacheLastRequest.order ) ||
                  JSON.stringify( request.columns ) !== JSON.stringify( cacheLastRequest.columns ) ||
                  JSON.stringify( request.search )  !== JSON.stringify( cacheLastRequest.search )
        ) {
            // properties changed (ordering, columns, searching)
            ajax = true;
        }
         
        // Store the request for checking next time around
        cacheLastRequest = $.extend( true, {}, request );
 
        if ( ajax ) {
            // Need data from the server
            if ( requestStart < cacheLower ) {
                requestStart = requestStart - (requestLength*(conf.pages-1));
 
                if ( requestStart < 0 ) {
                    requestStart = 0;
                }
            }
             
            cacheLower = requestStart;
            cacheUpper = requestStart + (requestLength * conf.pages);
 
            request.start = requestStart;
            request.length = requestLength*conf.pages;
 
            // Provide the same `data` options as DataTables.
            if ( $.isFunction ( conf.data ) ) {
                // As a function it is executed with the data object as an arg
                // for manipulation. If an object is returned, it is used as the
                // data object to submit
                var d = conf.data( request );
                if ( d ) {
                    $.extend( request, d );
                }
            }
            else if ( $.isPlainObject( conf.data ) ) {
                // As an object, the data given extends the default
                $.extend( request, conf.data );
            }
 
            settings.jqXHR = $.ajax( {
                "type":     conf.method,
                "url":      conf.url,
                "data":     request,
                "dataType": "json",
                "cache":    false,
                "success":  function ( json ) {
                    cacheLastJson = $.extend(true, {}, json);
 
                    if ( cacheLower != drawStart ) {
                        json.data.splice( 0, drawStart-cacheLower );
                    }
                    if ( requestLength >= -1 ) {
                        json.data.splice( requestLength, json.data.length );
                    }
                     
                    drawCallback( json );
                }
            } );
        }
        else {
            json = $.extend( true, {}, cacheLastJson );
            json.draw = request.draw; // Update the echo for each response
            json.data.splice( 0, requestStart-cacheLower );
            json.data.splice( requestLength, json.data.length );
 
            drawCallback(json);
        }
    }
};
 
// Register an API method that will empty the pipelined data, forcing an Ajax
// fetch on the next draw (i.e. `table.clearPipeline().draw()`)
$.fn.dataTable.Api.register( 'clearPipeline()', function () {
    return this.iterator( 'table', function ( settings ) {
        settings.clearCache = true;
    } );
} );

$(document).ready(function() {

    $('#negocios').addClass('active');
    $('#negocios').css('pointer-events', 'auto');
    
    columnsBusiness = [{
        sWidth: '20%',
        className : 'priority-1 taxpyerId text-center',
        searchable: false,
    },{
        sWidth: '30%',
        className : 'priority-3',
        searchable: false,
    },{
        sWidth: '30%',
        className : 'priority-3',
        searchable: false,
    },{
        sWidth: '20%',
        className : 'priority-1 text-center',
        searchable: false,
    }];

    columnsCSD = [{
        sWidth: '35%',
        className : 'priority-1 noCer',
        searchable: false,
    },{
        sWidth: '35%',
        className : 'priority-3',
        searchable: false,
    },{
        sWidth: '10%',
        className : 'priority-1',
        searchable: false,
    },{
        sWidth: '10%',
        className : 'priority-3',
        searchable: false,
    }];

    columnsBranch = [{
        sWidth: '20%',
        className: "priority-1 taxpyerId",
        searchable: false,
    },{
        sWidth: '20%',
        searchable: false,
    },{
        sWidth: '20%',
        searchable: false,
    },{
        sWidth: '20%',
        searchable: false,
    },{
        sWidth: '10%',
        searchable: false,
    }
    ,{
        sWidth: '10%',
        searchable: false,
    }];

    function updateBusinessTable(){
        $('#tbusiness').DataTable({
            'processing': true,
            'serverSide': true,
            'destroy': true,
            'columns': columnsBusiness,
            'language': datatable_language,
            "columnDefs": [
                    {
                        className: "text-center",
                        "targets": "_all",
                    },
                ],
            'ajax': $.fn.dataTable.pipeline({
                pages: 20,
                stateSave: true,
                method: 'POST',
                data: {
                    'oper': 'get-business',
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                }
            })
        });
    }

    updateBusinessTable();

    function updateCSDTable(id, business){
        oper = (id == '#tcsd') ? 'get-csd' : 'get-efirma';
        var dt = $(id).DataTable({
            'processing': true,
            'serverSide': true,
            'destroy': true,
            'columns': columnsCSD,
            "language": datatable_language,
            'language': datatable_language,
            'ajax': $.fn.dataTable.pipeline({
                pages: 20,
                stateSave: true,
                method: 'POST',
                data: {
                    'oper': oper,
                    'business': business,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                }
            })
        });
    }

    function updateBranchTable(business){
        state_filter = $('#state_filter').val();
        branch_filter = $('#branch_filter').val();
        zipcode_filter = $('#zipcode_filter').val();

        $('#tbranch').DataTable({
            'processing': true,
            'serverSide': true,
            'destroy': true,
            'columns': columnsBranch,
            'language': datatable_language,
            "columnDefs": [
                    {
                        className: "text-center",
                        "targets": [0,1,2,3,4,5],
                    },
                ],
            'ajax': $.fn.dataTable.pipeline({
                pages: 20,
                stateSave: true,
                method: 'POST',
                data: {
                    'oper': 'get_branch',
                    'branch_filter': branch_filter,
                    'state_filter': state_filter,
                    'zipcode_filter': zipcode_filter,
                    'csrfmiddlewaretoken': getCookie('csrftoken'),
                }
            })
        });
    }

    updateBranchTable();

    $(document).on('click', '#add-branch', function(e){
        e.preventDefault();

    });

    $("#branch_filter").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          updateBranchTable();
        }
    });

     $('#state_filter').change( function(e){
        updateBranchTable();
    });


    $("#zipcode_filter").keyup(function(e) {
        e.preventDefault();
        len = $(this).val().length
        if ((len > 2 || len == 0) && is_valid_key(e.which)) { 
          updateBranchTable();
        }
    });

    $('#modal-add-branch-btn').on('click', function(){
        bname = $('#add-bname').val();
        bstate = $('#add-bstate').val();
        bmunicipality = $('#add-bmunicipality').val();
        bneighborhood = $('#add-bneighborhood').val();
        bzipcode = $('#add-bzipcode').val();
        blocality = $('#add-blocality').val();
        bstreet = $('#add-bstreet').val();
        bnumber = $('#add-bnumber').val();

        if (bname.trim() == "") {
            $("#bname_help").text('Éste campo es requerido.');
            $("#add-bname").parent().closest('div').addClass('has-error');
            return
        } else {
            $("#bname_help").text('')
            $("#add-bname").parent().closest('div').removeClass('has-error');
        }

        if (bzipcode.trim() == "") {
            $("#bzipcode_help").text('Éste campo es requerido.');
            $("#add-bzipcode").parent().closest('div').addClass('has-error');
            return
        } else {
            $("#bzipcode_help").text('')
            $("#add-bzipcode").parent().closest('div').removeClass('has-error');
        }

        data = {    
            'name': bname,
            'municipality': bmunicipality,
            'neighborhood': bneighborhood,
            'zipcode': bzipcode,
            'locality': blocality,
            'street': bstreet,
            'number': bnumber,
            'state': bstate,
            'oper': 'add-branch',
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            }

        $.ajax({
            type: 'POST',
            cache: false,
            dataType: 'json',
            data: data,

        }).done(function(json) {
            $('#modal-add-branch').modal('hide');
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

    $(document).on('click', '.sc', function(e){
        e.preventDefault();
        taxpayerId = $(this).closest('tr').children('td.taxpyerId').text();
        $('#strong-taxpayer-csd').text(taxpayerId);
        $('#modal-csd').attr('taxpayerId', taxpayerId);
        $('#modal-csd').modal('show');
        $('#tcsd').attr('business', $(this).attr('business'));
        updateCSDTable('#tcsd', $(this).attr('business'));
    });

    $(document).on('click', '.sf', function(e){
        e.preventDefault();
        taxpayerId = $(this).closest('tr').children('td.taxpyerId').text();
        $('#strong-taxpayer-efirma').text(taxpayerId);
        $('#modal-efirma').attr('taxpayerId', taxpayerId);
        $('#modal-efirma').modal('show');
        $('#tefirma').attr('business', $(this).attr('business'));
        updateCSDTable('#tefirma', $(this).attr('business'));
    });

    $(document).on('click', '.si', function(e){
        e.preventDefault();
        business = $(this).attr('business');
        taxpayerId = $(this).closest('tr').children('td.taxpyerId').text();
        $('#strong-taxpayer-info').text(taxpayerId);
        $('#general-info').find('div.info').text('');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            data: {
                'oper': 'get-info',
                'business': business,
                'csrfmiddlewaretoken': getCookie('csrftoken'),
            },
            success: function(response){
                if (response['success']){
                    $.each(response['info'], function(id, value){
                        $('#' + id).html(value);
                    });
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
        $('#modal-info-business').modal('show');
    });

    $(document).on('click', '.bi', function(e){
        e.preventDefault();
        branch = $(this).attr('branch');
        name = $(this).closest('tr').children('td.taxpyerId').text();
        $('#strong-branch-info').text(name);
        $('#general-info_branch').find('div.info-branch').text('');
        $.ajax({
            method: 'POST',
            dataType: 'json',
            data: {
                'oper': 'get-info_branch',
                'name': name,
                'csrfmiddlewaretoken': getCookie('csrftoken'),
            },
            success: function(response){
                if (response['success']){
                    $.each(response['branch'], function(id, value){
                        $('#' + id).html(value);
                    });
                    
                    //$('#branch_name').html(response['info-branch']['info-name']);
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
        $('#modal-info-branch').modal('show');
    });

    $(document).on("click", '.ed',  function(e) {
        e.preventDefault();
        name = $(this).closest('tr').children('td.taxpyerId').text();
        $('#branch-info').text(name);
        $('#info_branch').find('div.info-branch').text('');        
        $("#edit-title").html('Editar datos para: <a id="modal-taxpayer_id" style="color: inherit; text-decoration: inherit"><b>'+ name +'</b></a>');
        $.ajax({
            method: "POST",
            dataType: "json",
            data: {
                "oper": "info-branch",
                'name': name,
                'csrfmiddlewaretoken': getCookie('csrftoken'),
            },
            success: function(response){
                if (response['success']){
                    $('#bid').val(response['info']['bid']);
                    $('#bname').val(response['info']['bname']);
                    $('#bstreet').val(response['info']['bstreet']);
                    $('#bnumber').val(response['info']['bexternalnumber']);
                    $('#bstate').val(response['info']['bstate']);
                    $('#bmunicipality').val(response['info']['bmunicipality']);
                    $('#blocality').val(response['info']['blocality']);
                    $('#bzipcode').val(response['info']['bzipcode']);
                    $('#bneighborhood').val(response['info']['bneighborhood']);
                    $('#modal-branch-edit').modal('show');
                    
                    //$('#branch_name').html(response['info-branch']['info-name']);
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
        });
        //$('#modal-branch-edit').modal('show');
    });

    /*Update branch*/
    $('#save').on('click',function(){
        bid = $('#bid').val();
        bname = $('#bname').val();
        bstate = $('#bstate').val();
        bmunicipality = $('#bmunicipality').val();
        bneighborhood = $('#bneighborhood').val();
        bzipcode = $('#bzipcode').val();
        blocality = $('#blocality').val();
        bstreet = $('#bstreet').val();
        bnumber = $('#bnumber').val();

        data = {
            'id':bid,    
            'name': bname,
            'municipality': bmunicipality,
            'neighborhood': bneighborhood,
            'zipcode': bzipcode,
            'locality': blocality,
            'street': bstreet,
            'number': bnumber,
            'state': bstate,
            'oper': 'update-branch',
            'csrfmiddlewaretoken': getCookie('csrftoken'),
            }

        $.ajax({
            type: 'POST',
            cache: false,
            dataType: 'json',
            data: data,

        }).done(function(json) {
            $('#modal-branch-edit').modal('hide');
            if (json.success) {
                $.toast({
                    heading: 'Success',
                    text: json.message,
                    showHideTransition: 'fade',
                    icon: 'success',
                    position: 'top-right',
                })
                updateBranchTable();
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


    $(document).on('click', '.ce-default, .ce-suspend, .ce-active', function(e){
        oper = null;
        if($(this).hasClass('ce-default')){
            oper = 'set-default';
        }else if($(this).hasClass('ce-active')){
            oper = 'set-active';
        }
        e.preventDefault();
        tabId = $(this).closest('table.table').attr('id');
        noCer = $(this).closest('tr').children('td.noCer').text();
        businessId = $(this).closest('table.table').attr('business');
        defaultData = new FormData();

        defaultData.append('serial', noCer);
        defaultData.append('business', businessId);
        defaultData.append('oper', oper);
        defaultData.append('csrfmiddlewaretoken', getCookie('csrftoken'));

        $.ajax({
            method: 'POST',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: defaultData,
            success: function(response){
                if (response['success']){
                    updateCSDTable('#' + tabId, businessId);
                    updateBusinessTable();
                    updateBranchTable();
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

    $(document).on('click', '.ac, .af', function(e){
        e.preventDefault();
        $('#add-cer-form').find("input, textarea").val("");
        taxpayerId = $(this).closest('div.modal').attr('taxpayerid');
        $('#strong-taxpayer').text(taxpayerId);
        $('#modal-add-csd-efirma').attr('taxpayerId', taxpayerId);
        $('#modal-add-csd-efirma').modal('show');
    });

    $('#add-cer-form').validator({
        custom:{
            'pwd': function($el){
               pwdKeyIsInvalid = null;
               pwd = $el.val();
               files = $('#input-b3').prop('files');
               if (pwd && files.length > 0){
                   keyFile = files[0];
                   var keyData = new FormData();
                   keyData.append('private_key', keyFile, keyFile.name)
                   keyData.append('pwd_key', btoa(pwd))
                   keyData.append( "csrfmiddlewaretoken", getCookie('csrftoken'))
                   keyData.append( "oper", 'validate-key')
                   $.ajax({
                       method: 'POST',
                       dataType: 'json',
                       async: false,
                       contentType: false,
                       processData: false,
                       url: 'validate/',
                       data: keyData,
                       success: function(response){
                           if (response['message'])
                               pwdKeyIsInvalid =  response['message'];
                       }
                   });
               }
                return pwdKeyIsInvalid
            },
            'cer': function($el){
               cerIsInvalid = null;
               pwd = $el.val();
               cerFiles = $('#input-b4').prop('files');
               keyFiles = $('#input-b3').prop('files');
               pwd = $('#password-key').val();
               taxpayerId = $('#modal-add-csd-efirma').attr('taxpayerId');
               if (cerFiles.length > 0 && keyFiles.length > 0 && pwd){
                   cerFile = cerFiles[0];
                   keyFile = keyFiles[0];
                   var cerData = new FormData();
                   cerData.append('private_key', keyFile, keyFile.name);
                   cerData.append('public_key', cerFile, cerFile.name);
                   cerData.append('pwd_key', btoa(pwd));
                   cerData.append( 'csrfmiddlewaretoken', getCookie('csrftoken'));
                   cerData.append( 'oper', 'validate-cer');
                   cerData.append('taxpayer_id', taxpayerId);
                   $.ajax({
                       method: 'POST',
                       dataType: 'json',
                       async: false,
                       contentType: false,
                       processData: false,
                       url: 'validate/',
                       data: cerData,
                       success: function(response){
                           if (response['message'])
                                cerIsInvalid =  response['message'];
                       }
                   });
               }
               return cerIsInvalid
            },
        }
    });

    $("#add-cer-form").submit(function(e) {
        e.preventDefault();
        isDisabled = $(this).children('button.add-cer').hasClass('disabled');
        if(isDisabled){
            var addForm = $('#add-cer-form');
            if (addForm){
                $('form').data('bs.validator').validate();
                var addFormErr = addForm.find('.has-error');
                if(addFormErr && addFormErr.length > 0){
                    $.toast({
                        heading: 'Error',
                        text: 'Verifica los certificados nuevamente, al parecer hubo un error.',
                        showHideTransition: 'fade',
                        icon: 'error',
                        position: 'top-right',
                    });
                    return false;
                }
            }
        }else{
            var addCertificateData = new FormData();
            taxpayerId = $('#modal-add-csd-efirma').attr('taxpayerId');
            var addForm = $('#add-cer-form');
            $.each(addForm.serializeArray(), function(key, input){
                addCertificateData.append(input.name, input.value);
            });
            cerFiles = $('#input-b4').prop('files');
            if (cerFiles.length > 0){
                cerFile = cerFiles[0]
                addCertificateData.append('public_key', cerFile, cerFile.name);
            }
            keyFiles = $('#input-b3').prop('files');
            if (keyFiles.length > 0){
                keyFile = keyFiles[0]
                addCertificateData.append('private_key', keyFile, keyFile.name);
            }
            addCertificateData.append('oper', 'add-certificate');
            addCertificateData.append('csrfmiddlewaretoken',  getCookie('csrftoken'));
            addCertificateData.append('taxpayer_id', taxpayerId);
            $.ajax({
                method: 'POST',
                data: addCertificateData,
                contentType: false, // You can pass false param to tell JQuery to not set any content type header.
                processData: false, //If you want to sent a DOMDocument, or other non-processed data, set to false. Otherwise will be processed and transformed into a query string.
                success: function(response){
                    if (response['success']){
                        $.toast({
                            heading: '&Eacute;xito',
                            text: 'Registro exitoso.',
                            showHideTransition: 'fade',
                            icon: 'success',
                            position: 'top-right',
                          });
                          $('#add-cer-form').find("input, textarea").val("");
                          location.reload();
                    }else{
                        $.toast({
                          heading: 'Error',
                          text: 'No es posible realizar el registro, intente más tarde.',
                          showHideTransition: 'fade',
                          icon: 'error',
                          position: 'top-right',
                        });
                        $('#add-cer-form').find("input, textarea").val("");
                        location.reload();
                    }
                }
            });
            return false;
        }
    });

    $(document).on("click", "#location_branch",  function(e) {
        e.preventDefault();
        branch_filter = $('#branch_filter').val();
        state_filter = $('#state_filter').val();
        zipcode_filter = $('#zipcode_filter').val();         
        $.ajax({
            method: "POST",
            dataType: "json",
            data: {
                "oper": "location_branch",
                'branch_filter': branch_filter,
                'state_filter': state_filter,
                'zipcode_filter': zipcode_filter,
                'csrfmiddlewaretoken': getCookie('csrftoken'),
            },
            success: function(response){
                if (response['success']){
                    data = response['data'];

                    myMap(data);
   
                }else{

                }
                
            }
        });

        $('#modal-branch-location').modal('show');        
    });

   $('#modal-add-csd-efirma').on('hidden.bs.modal', function (e) {
        $('#add-cer-form').find("input, textarea").val("");    
   });

   $('#modal-branch-edit').on('shown.bs.modal', function (e) {
        //emailTagInput.tagsinput('refresh');
    });

   $('#modal-branch-edit').on('hidden.bs.modal', function (e) {
        //emailTagInput.tagsinput('removeAll');
        $(this).find(':input').val('');
    });

   $(document).on('click', '#clean-branch',  function(event) {
        $("#branch_filter").val('');
        $("#state_filter").val('');
        $("#zipcode_filter").val('');
        updateBranchTable();
    });

   function myMap(data) {
        var map;
        var bounds = new google.maps.LatLngBounds();
        var mapOptions = {
            mapTypeId: 'roadmap'
        };

        map = new google.maps.Map(document.getElementById("googleMapBranch"), {
            zoom: 7,
            center: new google.maps.LatLng(41.503, -5.744),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        var pue, ppd, expensive, payment, payroll, transfer;
        var markers = data;
        var infoWindowContent = [];
        if (data.length>0){
            for( i = 0; i < markers.length; i++ ) {
                // Months
                var currentMonth = markers[i][22];
                var previousMonth = markers[i][23];
                var beforePreviousMonth = markers[i][24];
                // PUE
                var currentPUE = markers[i][4];
                currentPUE = parseFloat(currentPUE).toFixed(2);
                currentPUE = `$ ${Number(currentPUE).toLocaleString('en')}`;
                var previousPUE = markers[i][10];
                previousPUE = parseFloat(previousPUE).toFixed(2);
                previousPUE = `$ ${Number(previousPUE).toLocaleString('en')}`;
                var beforePreviousPUE = markers[i][16];
                beforePreviousPUE = parseFloat(beforePreviousPUE).toFixed(2);
                beforePreviousPUE = `$ ${Number(beforePreviousPUE).toLocaleString('en')}`;
                // PPD
                var currentPPD = markers[i][5];
                currentPPD = parseFloat(currentPPD).toFixed(2);
                currentPPD = `$ ${Number(currentPPD).toLocaleString('en')}`;
                var previousPPD = markers[i][11];
                previousPPD = parseFloat(previousPPD).toFixed(2);
                previousPPD = `$ ${Number(previousPPD).toLocaleString('en')}`;
                var beforePreviousPPD = markers[i][17];
                beforePreviousPPD = parseFloat(beforePreviousPPD).toFixed(2);
                beforePreviousPPD = `$ ${Number(beforePreviousPPD).toLocaleString('en')}`;
                // Egresos
                var currentEgresos = markers[i][6];
                currentEgresos = parseFloat(currentEgresos).toFixed(2);
                currentEgresos = `$ ${Number(currentEgresos).toLocaleString('en')}`;
                var previousEgresos = markers[i][12];
                previousEgresos = parseFloat(previousEgresos).toFixed(2);
                previousEgresos = `$ ${Number(previousEgresos).toLocaleString('en')}`;
                var beforePreviousEgresos = markers[i][18];
                beforePreviousEgresos = parseFloat(beforePreviousEgresos).toFixed(2);
                beforePreviousEgresos = `$ ${Number(beforePreviousEgresos).toLocaleString('en')}`;
                // Pagos
                var currentPagos = markers[i][7];
                currentPagos = parseFloat(currentPagos).toFixed(2);
                currentPagos = `$ ${Number(currentPagos).toLocaleString('en')}`;
                var previousPagos = markers[i][13];
                previousPagos = parseFloat(previousPagos).toFixed(2);
                previousPagos = `$ ${Number(previousPagos).toLocaleString('en')}`;
                var beforePreviousPagos = markers[i][19];
                beforePreviousPagos = parseFloat(beforePreviousPagos).toFixed(2);
                beforePreviousPagos = `$ ${Number(beforePreviousPagos).toLocaleString('en')}`;
                // Traslados
                var currentTraslados = markers[i][8];
                currentTraslados = parseFloat(currentTraslados).toFixed(2);
                currentTraslados = `$ ${Number(currentTraslados).toLocaleString('en')}`;
                var previousTraslados = markers[i][14];
                previousTraslados = parseFloat(previousTraslados).toFixed(2);
                previousTraslados = `$ ${Number(previousTraslados).toLocaleString('en')}`;
                var beforePreviousTraslados = markers[i][20];
                beforePreviousTraslados = parseFloat(beforePreviousTraslados).toFixed(2);
                beforePreviousTraslados = `$ ${Number(beforePreviousTraslados).toLocaleString('en')}`;
                // Nomina
                var currentNomina = markers[i][9];
                currentNomina = parseFloat(currentNomina).toFixed(2);
                currentNomina = `$ ${Number(currentNomina).toLocaleString('en')}`;
                var previousNomina = markers[i][15];
                previousNomina = parseFloat(previousNomina).toFixed(2);
                previousNomina = `$ ${Number(previousNomina).toLocaleString('en')}`;
                var beforePreviousNomina = markers[i][21];
                beforePreviousNomina = parseFloat(beforePreviousNomina).toFixed(2);
                beforePreviousNomina = `$ ${Number(beforePreviousNomina).toLocaleString('en')}`;
                infoWindowContent[i] = ['<div class="info_content" style="text-align:center;">'+
                    '<table class="egt" border="1" style="text-align:center">'+
                    '<caption style="text-align:center">Totales de los últimos 3 meses ('+ markers[i][0] +') </caption>'+
                    '<tr>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'MES' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'PUE' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'PPD' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'Egresos' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'Pagos' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'Traslados' + '</th>'+
                    '<th style="text-align:center; padding: .7rem;background-color: #cf2727; border: 1px solid #000000; color: white;" valign="middle" height="30" text-align="center">' + 'Nomina' + '</th>'+
                    '</tr>'+
                    '<tr>'+
                    '<td style="padding: .7rem;">' + currentMonth + '</td>'+
                    '<td style="padding: .7rem;">' + currentPUE + '</td>'+
                    '<td style="padding: .7rem;">' + currentPPD + '</td>'+
                    '<td style="padding: .7rem;">' + currentEgresos + '</td>'+
                    '<td style="padding: .7rem;">' + currentPagos + '</td>'+
                    '<td style="padding: .7rem;">' + currentTraslados + '</td>'+
                    '<td style="padding: .7rem;">' + currentNomina + '</td>'+
                    '</tr>'+
                    '<tr>'+
                    '<td style="padding: .7rem;">' + previousMonth + '</td>'+
                    '<td style="padding: .7rem;">' + previousPUE + '</td>'+
                    '<td style="padding: .7rem;">' + previousPPD + '</td>'+
                    '<td style="padding: .7rem;">' + previousEgresos + '</td>'+
                    '<td style="padding: .7rem;">' + previousPagos + '</td>'+
                    '<td style="padding: .7rem;">' + previousTraslados + '</td>'+
                    '<td style="padding: .7rem;">' + previousNomina + '</td>'+
                    '</tr>'+
                    '<tr>'+
                    '<td style="padding: .7rem;">' + beforePreviousMonth + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousPUE + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousPPD + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousEgresos + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousPagos + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousTraslados + '</td>'+
                    '<td style="padding: .7rem;">' + beforePreviousNomina + '</td>'+
                    '</tr>'+
                    '</table>'+
                    '</div>'];    
            }
        }
        
        var marker, i;
        //var urlIco = 'http://lacomer.com.mx/lacomer/super/images/logocm.png';
        var urlIco = `${window.location.origin}/static/img/logos/icon_marker_2.png`;
        var image = {
            url: urlIco,
            scaledSize: new google.maps.Size(53, 66),
            //size: new google.maps.Size(120, 120),
            //origin: new google.maps.Point(0, 0),
            //anchor: new google.maps.Point(0, 25)
          };

        var infoWindow = new google.maps.InfoWindow();

        // List of markers
        for( i = 0; i < markers.length; i++ ) {
            var position = new google.maps.LatLng(markers[i][1], markers[i][2]);
            bounds.extend(position);
            marker = new google.maps.Marker({
                position: position,
                map: map,
                icon: image,
                title: markers[i][0] + '\nTotal: $' + markers[i][3]
            });
            
            // Add info window to marker    
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function(){
                    infoWindow.setContent(infoWindowContent[i][0]);
                    infoWindow.open(map, marker);
                }
                                
            })(marker, i));
            // Center the map to fit all markers on the screen
            map.fitBounds(bounds);
            
        }
        // Set zoom level
        var boundsListener = google.maps.event.addListener((map), 'bounds_changed', function(event) {
            this.setZoom(6);
            google.maps.event.removeListener(boundsListener);
        });
    }

});
