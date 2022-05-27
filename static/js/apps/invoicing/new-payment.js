var idDocto_increment = 0;
const rfcCtaOrd = document.getElementById("id_pago_rfcCtaOrd");

rfcCtaOrd.addEventListener("input", function (event) {
    if (rfcCtaOrd.validity.patternMismatch) {
      rfcCtaOrd.setCustomValidity("El rfc ingresado debe ser tipo Moral o genérico extranjero.");
    } else {
      rfcCtaOrd.setCustomValidity("");
    }
  });

const rfcCtaBen = document.getElementById("id_pago_rfcCtaBen");

rfcCtaBen.addEventListener("input", function (event) {
    if (rfcCtaBen.validity.patternMismatch) {
      rfcCtaBen.setCustomValidity("El rfc ingresado debe ser tipo Moral.");
    } else {
      rfcCtaBen.setCustomValidity("");
    }
  });

const ctaOrd = document.getElementById("id_pago_ctaOrd");

ctaOrd.addEventListener("input", function (event) {
    if (ctaOrd.validity.patternMismatch) {
      ctaOrd.setCustomValidity("Revisa el patrón permitido para tu Forma de Pago en el catálogo FormaDePagoP.");
    } else {
      ctaOrd.setCustomValidity("");
    }
  });

const ctaBen = document.getElementById("id_pago_ctaBen");

ctaBen.addEventListener("input", function (event) {
    if (ctaBen.validity.patternMismatch) {
      ctaBen.setCustomValidity("Revisa el patrón permitido para tu Forma de Pago en el catálogo FormaDePagoP.");
    } else {
      ctaBen.setCustomValidity("");
    }
  });

function JSONify(){
	invoice = {
		'TipoDeComprobante': $('#id_type_invoice').val(),
		'LugarExpedicion': $('#id_expedition_place').val(),
		'Serie': $('#id_serial').val(),
		'Folio': $('#id_folio').val(),
		'Moneda': 'XXX',
		'Total': '0',
		'SubTotal': '0',
	}
	
	invoice['Receptor'] = {
		'Rfc': $('#id_rtaxpayer').val(),
		'UsoCFDI': $('#id_use_cfdi').val(),
		'ResidenciaFiscal': $('#id_fiscal_address').val(),
		'NumRegIdTrib': $('#id_rit').val(),
	}

	invoice['CfdiRelacionados'] = {
		'TipoRelacion': $('#id_relation_type').val(),
		'CfdiRelacionado': $('input[id^="id_uuid_related_"]').map(function(idxi, uuidRelated){
			var uuidRelatedNode = null;
			if ($(uuidRelated).val()){
				uuidRelatedNode = {
					'UUID': $(uuidRelated).val()
				}
			}
			return uuidRelatedNode
		}).get()
	}

	var monedap = $('#id_pago_select').val();
	var tipocambiop = $('#id_pago_current').val();
	if (monedap == 'MXN'){
		tipocambiop = '';
	}

	var date_payment_obj = $('#id_pago_date').data('DateTimePicker').date();
	var fechaPagoFormateado = date_payment_obj.format('MM/DD/YYYY');

	invoice['Complemento'] = {
		'Pagos': {
		'Version': '1.0',
		'Pago': {
			'FechaPago': fechaPagoFormateado,
			'FormaDePagoP': $('#id_pago_way').val(),
			'MonedaP': monedap,
			'TipoCambioP': tipocambiop,
			'Monto': $('#id_pago_mount').val(),
			'NumOperacion': $('#id_pago_numoper').val(),
			'RfcEmisorCtaOrd': $('#id_pago_rfcCtaOrd').val(),
			'NomBancoOrdExt': $('#id_pago_nomBanOrd').val(),
			'CtaOrdenante': $('#id_pago_ctaOrd').val(),
			'RfcEmisorCtaBen': $('#id_pago_rfcCtaBen').val(),
			'CtaBeneficiario': $('#id_pago_ctaBen').val(),
			'TipoCadPago': $('#id_pago_tipocadena').val(),
			'CertPago': $('#id_pago_cert').val(),
			'CadPago': $('#id_pago_cadena').val(),
			'SelloPago': $('#id_pago_sello').val(),
			'DoctoRelacionado': $('div[id^="docto_"]').map(function(idxdr, docto){
				idDocto = parseInt($(docto).prop('id').match(/\d+/), 10);
				
				idDocRela = $('#docto_idDoc_' + idDocto).val();
				serieDr = $('#docto_serie_' + idDocto).val();
				folioDr = $('#docto_folio_' + idDocto).val();
				monedaDr = $('#docto_monedaDr_' + idDocto).val();
				tipoCambioDr = $('#docto_tipoCambioDr_' + idDocto).val();
				metodoPagoDr = $('#docto_metodoPagoDr_' + idDocto).val();
				numParcialidad = $('#docto_numParcialidad_' + idDocto).val();
				impSalAnt = $('#docto_impSalAnt_' + idDocto).val();
				impPagado = $('#docto_impPagado_' + idDocto).val();
				impSaldoInsoluto = $('#docto_impSaldoInsoluto_' + idDocto).val();

				return {
					'IdDocumento': idDocRela,
					'Serie': serieDr,
					'Folio': folioDr,
					'MonedaDR': monedaDr,
					'TipoCambioDR': tipoCambioDr,
					'MetodoDePagoDR': metodoPagoDr,
					'NumParcialidad': numParcialidad,
					'ImpSaldoAnt': impSalAnt,
					'ImpPagado': impPagado,
					'ImpSaldoInsoluto': impSaldoInsoluto,
				}
			}).get()
		}}
	}

	return JSON.stringify(invoice)
}

function Notes(){
	var internal_notes = $('#notes').val();
	return internal_notes;
}

function resetFormInvoice() {
	generalTax = {
		"Retenciones": {},
		"Traslados": {},
	}
	totalInvoice = 0.0;
	discountInvoice = 0.0;
	totalRetInvoice = 0.0;
	subtotalInvoice = 0.0;
	totalTrasInvoice = 0.0;
	$('#cfdi-invoice').trigger("reset");
	$('#receptor_name').text('');
	$('small[id^="subtitle_"]').text('');
	$('div[id^="div_concepto_"]').not('#div_concepto_0').remove();
	$('div[id^="impuesto_"]').remove();
	$('#id_serial').val(null).trigger('change');
	$('#header-total').text('$ 0.00');
	$('#total-invoice').text('$ 0.00');
	$('#totalret-invoice').text('$ 0.00');
	$('#totaltras-invoice').text('$ 0.00');
	$('#discount-invoice').text('$ 0.00');
	$('#subtotal-invoice').text('$ 0.00');
	$('#success-uuid').text('');
	$('#success-total').text('');
	$('#success-rfc').text('');
	$('#success-rrfc').text('');
	$('#id_pago_select').val(null).trigger('change');
	$('div[id^="div_docto_"]').not('#div_docto_0').remove();
	$('#docto_monedaDr_0').val(null).trigger('change');
}

function monedaDr_funtion(element, destroy=false, idDr=0){
	if ($(element).hasClass("select2-hidden-accessible")) {
    	$(element).select2("destroy");
    	if (destroy){
    		return null;
    	}
	}

	$(element).select2({
		ajax:{
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function(params){
				return { 
					oper: 'get-currency',
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
							tipoCambio: item.tipo_cambio
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
			var monedapago = $('#id_pago_select').val();
			var tipoCambio = data.tipoCambio;
			if(data.text === 'MXN - Peso Mexicano' && monedapago != 'MXN'){
				//$('#docto_tipoCambioDr_' + idDr).attr('readonly', 'readonly');
				//tipoCambio = '1'
				//$('#docto_tipoCambioDr_' + idDr).val(tipoCambio);
			}else if(data.text != 'MXN - Peso Mexicano' && monedapago === 'MXN'){
				var tipoCambioP = data.tipoCambio
				tipoCambio = 1 / tipoCambioP;
				tipoCambio = tipoCambio.toFixed(6);
				$('#docto_tipoCambioDr_' + idDr).removeAttr('readonly');
				$('#docto_tipoCambioDr_' + idDr).val(tipoCambio);

			}else if(data.id === monedapago){
				$('#docto_tipoCambioDr_' + idDr).val('');
				$('#docto_tipoCambioDr_' + idDr).attr('readonly', 'readonly');

			}else{
				$('#docto_tipoCambioDr_' + idDr).val('');
				$('#docto_tipoCambioDr_' + idDr).removeAttr('readonly');
			}
			return data.text;
		},
		placeholder: 'Moneda',
		minimumInputLength: 3,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});

	//var saldoAnterior = $('#docto_impSalAnt_' + idDr).val();
	//var saldoPagado = $('#docto_impPagado_' + idDr).val();	
	//var saldoInsoluto = parseInt(saldoAnterior - saldoPagado);
	//$('#docto_impSaldoInsoluto_' + idDr).text(saldoInsoluto);
}


function initClearRTaxpayerID(){
	$('#id_rtaxpayer').on('select2:clear', function(e){
		$('#receptor_name').text('');
	});
}

var UUID_PATTERN = /^[a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12}$/;
function validateForm(btn){
	var isValid = true;
	var emptyUUIDRelated = false;
	var badUUIDRelated = false;
	if ($('#id_rtaxpayer').val() === '' || $('#id_rtaxpayer').val() === null || $('#id_rtaxpayer').val() === undefined){
		$('#div_id_rtaxpayer').addClass('has-error');
		error_message('Debes ingresar el RFC del receptor');
		isValid = false;
	}

	if ( !$('#div_uuid_relacionados').hasClass('hidden')){
		$('input[id^="id_uuid_related_"]').each(function(idx, element){
			var tmpUUID = $(element).val();
			if(tmpUUID === null || tmpUUID === undefined || tmpUUID === ""){
				emptyUUIDRelated = true;
				isValid = false;
				$(element).parents('div[id^="div_uuidrelacionado_"]').addClass('has-error');
			}else if(!tmpUUID.match(UUID_PATTERN)){
				badUUIDRelated = true;
				isValid = false;
				$(element).parents('div[id^="div_uuidrelacionado_"]').addClass('has-error');
			}
		});
	}
	if ($('#id_expedition_place').val() == null || $('#id_expedition_place').val() == ""){
		error_message('Ingresa un código postal.');
		isValid = false;
	}
	if(emptyUUIDRelated){
		error_message('El UUID relacionado no puede estar vacio.');
	}
	if(badUUIDRelated){
		error_message('El UUID esta mal formado.');
	}
	return isValid;
}

function initPayment(){
	$("#id_pago_date").datetimepicker({
		locale: "es",
		format: "DD MMMM YYYY",
		sideBySide: true
	});
	$('#id_pago_date').data("DateTimePicker").maxDate(new Date());
	
	$(document).on('click', '.add-docto', function(e){
		var docto = $('#seccion_doctos div[id^="div_docto_"]:last');
		var oldIdDocto = parseInt(docto.prop('id').match(/\d+/g), 10);
		var idDocto = oldIdDocto + 1;
		monedaDr_funtion($('#docto_monedaDr_' + oldIdDocto), true);
		var newWrapDocto = docto.clone(false, false).prop('id', 'div_docto_' + idDocto);
		
		newWrapDocto.find('#titledocto_' + oldIdDocto).prop('id', 'titledocto_' + idDocto);
		newWrapDocto.find('#titledocto_' + idDocto).attr('data-target', '#docto_' + idDocto);
		
		newWrapDocto.find('#docto_' + oldIdDocto).prop('id', 'docto_' + idDocto);
		var newDocto = newWrapDocto.find('#docto_' + idDocto);

		newWrapDocto.find('#subtitledocto_' + oldIdDocto).prop('id', 'subtitledocto_' + idDocto);
		newWrapDocto.find('#subtitledocto_' + idDocto).text('');

		$(newDocto).find(':input', 'label').each(function(){
			self = $(this);
			console.log(self.attr('name') + '_' + idDocto);
			name = self.attr('name') + '_' + idDocto;
			self.prop('id', name);
			self.closest('div.form-group').find('label.control-label').prop('for', name);
		});
		
		docto.after(newWrapDocto);

		monedaDr_funtion($('#docto_monedaDr_' + idDocto), false, idDocto);
		monedaDr_funtion($('#docto_monedaDr_' + oldIdDocto), false, oldIdDocto);
	});
	
	$(document).on('click', '.remove-docto', function(e){
		var docto = $(this).closest('div[id^="div_docto_"]');
		$(docto).find('small[id^="subtitle_"]').text('');
		if ($('div[id^="div_docto_"]').length > 1){
			docto.remove();
			oldIdDocto = $('div[id^="div_docto_"]').length
		}
	});

	monedaDr_funtion($('#docto_monedaDr_0'));

	$('#id_pago_tipocadena').prop("disabled", true);
	$('#id_pago_cert').prop("disabled", true);
	$('#id_pago_cadena').prop("disabled", true);
	$('#id_pago_sello').prop("disabled", true);
	$('#id_pago_ctaOrd').prop("disabled", true);
	$('#id_pago_rfcCtaBen').prop("disabled", true);
	$('#id_pago_ctaBen').prop("disabled", true);
	$('#id_pago_way').change(function(){ 
		var formapagop = $(this).val();
		if (formapagop == '03'){
			$('#id_pago_tipocadena').prop("disabled", false);
			$('#id_pago_cert').prop("disabled", false);
			$('#id_pago_cadena').prop("disabled", false);
			$('#id_pago_sello').prop("disabled", false);
		}else{
			$('#id_pago_tipocadena').prop("disabled", true);
			$('#id_pago_cert').prop("disabled", true);
			$('#id_pago_cadena').prop("disabled", true);
			$('#id_pago_sello').prop("disabled", true);
		}

		if(formapagop == '02' || formapagop == '03' || formapagop == '04' || formapagop == '05' || formapagop == '28' || formapagop == '29'){
			$('#id_pago_rfcCtaBen').prop("disabled", false);
			$('#id_pago_ctaBen').prop("disabled", false);
			$('#id_pago_ctaOrd').prop("disabled", false);
		}else{
			$('#id_pago_rfcCtaBen').prop("disabled", true);
			$('#id_pago_ctaBen').prop("disabled", true);
			$('#id_pago_ctaOrd').prop("disabled", true);
			if(formapagop == '06'){
				$('#id_pago_ctaOrd').prop("disabled", false);
			}else{
				$('#id_pago_ctaOrd').prop("disabled", true);
			}
		}
	});

	$('#id_pago_select').select2({
		ajax:{
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function(params){
				return { 
					oper: 'get-currency',
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
							tipoCambio: item.tipo_cambio,
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
			var docto = $('#seccion_doctos div[id^="div_docto_"]:last');
			var oldIdDocto = parseInt(docto.prop('id').match(/\d+/g), 10); 
			var tipoCambio = data.tipoCambio;
			if(data.text === 'MXN - Peso Mexicano'){
				$('#id_pago_current').attr('readonly', 'readonly');
				tipoCambio = ''
			}else{
				$('#id_pago_current').removeAttr('readonly');
				//tipoCambio = tipoCambio.toFixed(2);
			}

			for (x=0; x<=oldIdDocto; x++){
				var monedadr = $('#docto_monedaDr_' + x).val();
				if (data.id === monedadr){
					$('#docto_tipoCambioDr_' + x).val('');
                	$('#docto_tipoCambioDr_' + x).attr('readonly', 'readonly');
				}else if(data.id !== 'MXN' && monedadr == 'MXN'){
					$('#docto_tipoCambioDr_' + x).removeAttr('readonly');
				}
			}

			//tipoCambio = tipoCambio.toFixed(2);
			$('#id_pago_current').val(tipoCambio);
			// $(data.element).attr('data-custom-attribute', data.customValue);
			return data.text;
		},
		placeholder: 'Moneda',
		minimumInputLength: 3,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});
}


$(document).ready(function(e){
	// inicializar pagos
	initPayment();
});
