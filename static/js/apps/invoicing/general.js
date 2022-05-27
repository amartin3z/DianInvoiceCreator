var totalInvoice = 0.0;
var discountInvoice = 0.0;
var totalRetInvoice = 0.0;
var subtotalInvoice = 0.0;
var totalTrasInvoice = 0.0;

var generalTax = {
	"Retenciones": {},
	"Traslados": {},
}

function initTaxpayerID(){
	var inputTaxpayerid = $('#id_rtaxpayer');

	$(inputTaxpayerid).select2({
		ajax:{
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function(params){
				return { 
					oper: 'get-receiver',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					taxpayer_id: params.term
				}
			},
			processResults: function(data){
				return {
					results: $.map(data, function(item, idx){
						return {
							text: `${item.tax_idenfier_number} - ${item.company_name}`,
							id: item.tax_idenfier_number,
							UsoCFDI: item.organization_id,
							name: item.company_name,
							country: item.country,
						}
					}),
				}
			},
			cache: true
		},
		language: "es",
		inputTooShort: function (left) {
			return 'Faltan X caracteres';
		},
		templateSelection: function (data, container) {
            // Add custom attributes to the <option> tag for the selected option
            //if (IS_PAYMENT !== 'pagos'){
            //    $('#id_use_cfdi').val(data.UsoCFDI).trigger('change');
            //}
            $('#id_fiscal_address').val(data.country).trigger('change');
            $('#id_id_company').val(data.UsoCFDI);
            $('#receptor_name').text(data.name);
			$('#div_id_rtaxpayer').removeClass('has-error');
			// $(data.element).attr('data-custom-attribute', data.customValue);
			return data.id;
		},
		placeholder: 'Receptor',
		minimumInputLength: 1,
		allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
    });
    
	$('#id_rtaxpayer').on('change blur', function(event){
		var rtapxyaer_id = $(this).val();
		if (rtapxyaer_id === 'XEXX010101000'){
			$('#id_fiscal_address').removeAttr('disabled');
            $('#id_rit').removeAttr('disabled');
            if ($('#id_fiscal_address').hasClass("select2-hidden-accessible")) {
                $('#id_fiscal_address').select2('destroy');
            }
			$('#id_fiscal_address').select2({
				ajax:{
					url: INVOICING_STUFFS_URL,
					method: 'POST',
					width: 'resolve',
					dataType: 'json',
					data: function(params){
						return { 
							oper: 'get-country',
							csrfmiddlewaretoken: getCookie('csrftoken'),
							clave: params.term
						}
					},
					processResults: function(data){
						return {
							results: $.map(data, function(item, idx){
								return {
									text: `${item.clave} - ${item.descripcion}`,
									id: item.clave,
									rit: item.rit,
								}
							}),
						}
					},
					cache: true
				},
				language: "es",
				inputTooShort: function (left) {
					return 'Faltan X caracteres';
				},
				// templateSelection: function (data, container) {
				// 	// Add custom attributes to the <option> tag for the selected option
				// 	console.log(data);
				// 	// $(data.element).attr('data-custom-attribute', data.customValue);
				// 	return data.text;
				// },
				placeholder: 'Residencia Fiscal (SAT)',
				minimumInputLength: 3,
				allowClear: true,
				width: 'resolve',
				theme: "bootstrap"
			});
		}else{
			// $('#id_fiscal_address').select2('destroy');
			$('#receptor_name').text('');
			//$('#id_fiscal_address').attr('disabled', 'disabled');
			$('#id_rit').attr('disabled', 'disabled');
			//$('#id_fiscal_address').val(null).trigger('change');
			$('#id_rit').val('');
		}
	});
}

function initExpeditionPlace(){
    $('#id_expedition_place').select2({
		ajax:{
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function(params){
				return { 
					oper: 'get-cp',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					clave: params.term
				}
			},
			processResults: function(data){
				return {
					results: $.map(data, function(item, idx){
						return {
							text: `${item.clave} - ${item.estado}`,
							id: item.clave,
						}
					}),
				}
			},
			cache: true
		},
		templateSelection: function (data, container) {
			// Add custom attributes to the <option> tag for the selected option
			$('#div_id_expedition_place').removeClass('has-error');
			return data.text;
		},
		language: "es",
		inputTooShort: function (left) {
			return 'Faltan X caracteres';
		},
		placeholder: 'Lugar de Expedición',
		minimumInputLength: 4,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});
}

function initSerial(){
    $('#id_serial').select2({
		ajax:{
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function(params){
				return { 
					oper: 'get-serial',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					serial: params.term
				}
			},
			processResults: function(data){
				return {
					results: $.map(data, function(item, idx){
						return {
							text: `Serie: ${item.serial} Folio: ${item.folio}`,
							id: item.serial,
							folio: item.folio,
						}
					}),
				}
			},
			cache: true
		},
		language: "es",
		inputTooShort: function (left) {
			return 'Faltan X caracteres';
		},
		templateSelection: function (data, container) {
			// Add custom attributes to the <option> tag for the selected option
			var folio = data.folio;
			if(folio !== null || folio !== undefined){
				$('#id_folio').val(folio);
			}
			return data.id;
		},
		placeholder: 'Serie',
		minimumInputLength: 1,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});
}

function initFakeClick(){
	$('#generate-invoice').on('click', function(e){
		$('#generate-invoice-real').click();
	})
}

function initDownloadfiles(){
    $(document).on('click', '.download-file', function(e){
		e.preventDefault();
		var type = $(this).data('type');
		var invoice = $('#modal-invoice-success').data('invoice');
		
		var currenDate = new Date();
		var xhr = new XMLHttpRequest();
		var formData = new FormData();
		formData.append('invoice', invoice);

		//filename = currenDate.getFullYear().toString() + '_'+ (currenDate.getMonth() + 1).toString() + '.zip';

		xhr.open("POST", DOWNLOAD_ZIP_URL, true);
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		
		xhr.onload = function(e){
			if (this.status === 201){
				var blob = this.response;
				var filename = xhr.getResponseHeader('Download-Filename');
				console.log(blob);
				if(window.navigator.msSaveOrOpenBlob) {
					window.navigator.msSaveBlob(blob, filename);
				}else{
					var downloadLink = window.document.createElement('a');
					var contentTypeHeader = xhr.getResponseHeader("Content-Type");
					var blob = new Blob([blob], { type: contentTypeHeader });
					downloadLink.href = window.URL.createObjectURL(blob);
					downloadLink.download = filename;
					$(downloadLink)[0].click();
					$(downloadLink).remove();
				}	
			}
			// else if (this.status === 403){
			// 	console.log(this.response);
			// }
		}
		xhr.responseType = "arraybuffer"; // TO ZIP CONTENT IS NECESSARY TO ADD THIS PARAMTER
		xhr.send(formData);
	});
}

function initCloseModalOnError(){
    // $('#modal-invoice-success #modal-invoice-error').on('hidden.bs.modal', function () {
	// 	resetFormInvoice()
	// });
}

function initUUIDRelated(){
    $('#id_relation_type').select2({
		width: '100%',
		theme: "bootstrap"
	});
	$('#button_add_related').on('click', function(e){
		e.preventDefault();
		// console.log('click');
		isVisible = $('#div_uuid_relacionados').hasClass('hidden');
		if(!isVisible){
			$('#div_uuid_relacionados').addClass('hidden');
			$(this).children().remove();
			$(this).html('<i class="fa fa-plus"></i>');
			$(this).removeClass('btn-danger');
			$(this).addClass('btn-success');
			$('#div_uuid_relacionados').find('input').empty();
			$('#div_uuidsrelacionado').find('input').empty();
			$('#div_uuidsrelacionado').children('div[id^="div_uuidrelacionado_"]').not('div#div_uuidrelacionado_0').remove();
			$('#div_uuidrelacionado_0').attr('required', 'required');
		}else{
			$('#div_uuid_relacionados').removeClass('hidden');
			$(this).children().remove();
			$(this).html('<i class="fa fa-eraser"></i>');
			$(this).removeClass('btn-success');
			$(this).addClass('btn-danger');
			$('#div_uuidrelacionado_0').removeAttr('required');
		}
	});

	$(document).on('click', '.add-uuid', function(e){
		var uuid_relacionado = $('#div_uuidsrelacionado div[id^="div_uuidrelacionado_"]:last');
		var oldIdUUID = parseInt(uuid_relacionado.prop('id').match(/\d+/g), 10);
		var idUUID = oldIdUUID + 1;
		var newWrapUUID = uuid_relacionado.clone(false, false).prop('id', 'div_uuidrelacionado_' + idUUID);
		
		newWrapUUID.find(':input').empty();
		$(newWrapUUID).find(':input', 'label').each(function(){
			self = $(this);
		 	// console.log(self.attr('name') + '_' + idUUID);
		 	name = self.attr('name') + '_' + idUUID;
			self.val('');
			self.prop('id', name);
		});
		$(newWrapUUID).children('label.control-label').remove();
		$(newWrapUUID).find('.add-uuid').children().remove()
		$(newWrapUUID).find('.add-uuid').removeClass('btn-success');
		$(newWrapUUID).find('.add-uuid').addClass('btn-danger');
		$(newWrapUUID).find('.add-uuid').html('<i class="fa fa-eraser"></i>');
		$(newWrapUUID).find('.add-uuid').addClass('remove-uuid');
		$(newWrapUUID).find('.add-uuid').removeClass('add-uuid')
		uuid_relacionado.after(newWrapUUID);
	});


	$(document).on('click', '.remove-uuid', function(e){
		var uuid_related = $(this).closest('div[id^="div_uuidrelacionado_"]');
		if ($(this).closest('div#div_uuidsrelacionado').children('div[id^="div_uuidrelacionado_"]').length > 1){
			uuid_related.remove();
		}
	});
}


function stampInvoice(invoiceJSON, notes, btn){
	$.ajax({
		async: true,
		dataType: 'json',
		method: 'POST',
		data: {
			'invoice': invoiceJSON,
			'notes': notes,
			'csrfmiddlewaretoken': getCookie('csrftoken'),
			'oper': 'add-invoice',
		},
		success: function(response, textStatus, jqXHR){
			var send_message = response['success'] ? success_message : error_message;
			var message = 'message' in response ? response['message'] : 'Hubo un error, intente más tarde.';
			if (response['success']){
				$('#modal-invoice-success').attr('data-invoice', response['invoice']);
				$('#modal-invoice-success').modal('show');
				$('#invoice-uuid').text(response['UUID']);
				resetFormInvoice();
				$('#success-uuid').text(response.data.UUID);
				$('#success-total').text(`$ ${response.data.total.toLocaleString('es-MX')}`);
				$('#success-rfc').text(response.data.rfc);
				$('#success-rrfc').text(response.data.rrfc);
				$('#invoice-dashboard').attr('href', `${INVOICING_LIST_URL}`);
				btn.button('reset');
			}else{
				$('#modal-invoice-error').attr('data-invoice', response['invoice']);
				$('#modal-invoice-error').modal('show');
				$('#invoice-error-title').text(message);
				$('#invoice-error-message').html(response.error);
				totalInvoice = 0.0;
				discountInvoice = 0.0;
				totalRetInvoice = 0.0;
				subtotalInvoice = 0.0;
                totalTrasInvoice = 0.0;
                if (IS_PAYMENT !== 'pagos'){
                    calculateTotals();
                }
				btn.button('reset');
				
			}
		}
	});
}

$(document).ready(function(e){
    //Inicializar elemento lugar expedición
    initExpeditionPlace();
    //Inicializar elemento serial
    initSerial();
    //inicializar RFC
    initTaxpayerID();
    //Inicializar el boton superior de sumbit
    initFakeClick();
    //inicializar descarga
    initDownloadfiles();
    //initCloseModalOnError();
    //inicializar uuid relacionado
    initUUIDRelated();

    $('#cfdi-invoice').submit(function(event){
        event.preventDefault();

       var btn = $('#generate-invoice');
       btn.button('loading');
       isValid = validateForm();
       if(isValid){
           var invoiceJSON = JSONify();
           var notes = Notes();
           stampInvoice(invoiceJSON, notes, btn);
       }
       else{
        btn.button('reset');
       }
       return false;
    });
});