$(document).ready(function(){
	$('#reportes').addClass('active');
    $('#reportes').css('pointer-events', 'auto');
    var token = CSRF_TOKEN;
    var url_status = window.location.pathname;
    $('.select2-container--bootstrap').css('width', '100%')

    $("#date-from").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });
    $("#date-to").datetimepicker({
        locale: "es",
        format: "DD MMMM YYYY",
        sideBySide: true
    });

    columns_revision = [{
        sWidth: '9%',
        'className': 'bold text-center',
        bSortable: false,
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '5%',
        bSortable: false,
        },{
        sWidth: '9%',
        bSortable: false,
        },{
        sWidth: '10%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '10%',
        bSortable: false,
        'render': $.fn.dataTable.render.number(',', '.', 2, '$ '),
        },{
        sWidth: '20%',
        bSortable: false,
        },{
        sWidth: '10%',
        bSortable: false,
    }];

    $("#date-from").on("dp.change", function(e) {
        if ($('#date-from-val').val() != "") {
            $('#date-to').data("DateTimePicker").minDate(e.date);
            revision_table.draw();
        }
    });
    $("#date-to").on("dp.change", function(e) {
        if ($('#date-to-val').val() != "") {
            $('#date-from').data("DateTimePicker").maxDate(e.date);
            revision_table.draw();
        }
    });
    
    
    var revision_table = $('#tbilling_revision').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        'bProcessing': true,
        'bServerSide': true,
        'PagingType': 'full_numbers',
        'columns': columns_revision,
        //"columnDefs": [
        //    {
        //        className: "text-center",
        //        "targets": [0,1,2,3],
        //    },
        //],
        'language': datatable_language,
        'stateSave': true,
        'searching': false,
        sAjaxSource: url_status,
        fnServerData: function(sSource, aoData, fnCallback){
            aoData.push({
                'name': 'csrfmiddlewaretoken',
                'value': getCookie('csrftoken')
            });
            if ($("#id_prodserv").val() != null) {
                aoData.push({
                    "name": "cve_prod",
                    "value": $("#id_prodserv").val()
                });
            }
            if ($("#filter_descripcion").val() != null ) {
                aoData.push({
                    "name": "description",
                    "value": $("#filter_descripcion").val()
                });
            }
            if ($("#filter_proveedor").val() != null) {
                aoData.push({
                    "name": "taxpayer",
                    "value": $("#filter_proveedor").val()
                });
            }
            var date_from_obj = $('#date-from').data('DateTimePicker').date();
            var date_to_obj = $('#date-to').data('DateTimePicker').date();
            if (date_from_obj !== null && date_to_obj !== null) {
                var date_from_str = date_from_obj.format('YYYY-MM-DD');
                var date_to_str = date_to_obj.format('YYYY-MM-DD');
                aoData.push({
                    "name": "date_from",
                    "value": date_from_str
                });

                aoData.push({
                    "name": "date_to",
                    "value": date_to_str
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
        drawCallback: function(settings){
            $('[data-toggle="popover-package-invoices"]').popover({
              placement: 'top'
            });
            $('.add-tax').on('click', function(e){
                e.preventDefault();
                var taxpayer = $(this).attr('taxpayer_id');
                $('#filter_proveedor').val(taxpayer);
                revision_table.draw();
            });
        },

    });
    //$('#id_prodserv, #filter_descripcion, #filter_proveedor').on('change', function(e){
    $('#id_prodserv, #filter_descripcion').on('change', function(e){
      e.preventDefault();
      revision_table.draw()
    });
    //$('#filter_descripcion, #filter_proveedor').keyup(function(e){
    $('#filter_descripcion').keyup(function(e){
        e.preventDefault();
      if($("#filter_proveedor").val().length > 4 || $("#filter_descripcion").val().length > 4){
        revision_table.draw()
      }
      });
    $(document).on('click', '#clean-filter',  function(event) {
        $("#date-from-val").val('');
        $("#date-to-val").val('');
        $("#filter_proveedor").val('');
        $("#filter_descripcion").val('');
        $("#id_prodserv").children().remove();
        revision_table.draw()
    });
    $('#download_concept_report').on('click', function(e){
      e.preventDefault();
      $("#download_concept_report").attr("disabled", true);
      data = [{
        'name': 'csrfmiddlewaretoken',
        'value': getCookie('csrftoken')
      }];
    if ($("#id_prodserv").val() != null) {
        data.push({
            "name": "cve_prod",
            "value": $("#id_prodserv").val()
        });
    }
    if ($("#filter_descripcion").val() != null ) {
        data.push({
            "name": "description",
            "value": $("#filter_descripcion").val()
        });
    }
    if ($("#filter_proveedor").val() != null) {
        data.push({
            "name": "taxpayer",
            "value": $("#filter_proveedor").val()
        });
    }
      var date_from_obj = $('#date-from').data('DateTimePicker').date();
      var date_to_obj = $('#date-to').data('DateTimePicker').date();
      if (date_from_obj !== null && date_to_obj !== null) {
          var date_from_str = date_from_obj.format('YYYY-MM-DD');
          var date_to_str = date_to_obj.format('YYYY-MM-DD');
          data.push({
              "name": "date_from",
              "value": date_from_str
          });

          data.push({
              "name": "date_to",
              "value": date_to_str
          });
      }

      $.ajax( {
          "dataType": "json",
          "type": "POST",
          "url": '/billing/revision/report/',
          "data": data,
          "success": function(json) {
            if (json.success) {
                $("#download_concept_report").attr("disabled", false);
                window.open(json.url);
              } else {
                /*alert(json.message);*/
                $("#download_concept_report").attr("disabled", false);
                $.toast({
                  heading: 'Error',
                  text: json.message,
                  showHideTransition: 'fade',
                  icon: 'error',
                  position: 'top-right',
                })
              
          }
        }
    });

    });

    var optionsTaxpayerID = {
		url: function(){
			return window.location.pathname;
		},
		getValue: function(element){
			return element.taxpayer_id;
		},
		template:{
			type: "description",
			fields: {
				description: "name",
			}
		},
		list: {
			onChooseEvent: function(){
                revision_table.draw();
			}
		},
		ajaxSettings: {
			dataType: 'json',
			method: 'POST',
			data: {
				'csrfmiddlewaretoken': getCookie('csrftoken'),
				'oper': 'get-taxpayer-revision',
				'dataType': "json"
			}
		},
		preparePostData: function(data){
			var taxpayerID = $('#filter_proveedor').val();
			data.taxpayer = taxpayerID;
			return data;
		},
		requestDelay: 200
	};
	$('#filter_proveedor').easyAutocomplete(optionsTaxpayerID);


});
