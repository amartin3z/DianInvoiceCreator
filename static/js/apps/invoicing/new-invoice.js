function initNoIdentification(_ID = 0, destroy = false, new_element = true) {
	// seccion para declarar variables.
	//var quantityAvoid = 0;
	var unitPriceAvoid = 0;
	//var inputIdentifier =  _ID !== 0 ? concept.find('#identifier_' + _ID) : concept;
	var inputIdentifier = $('#identifier_' + _ID);
	if ($(inputIdentifier).hasClass("select2-hidden-accessible")) {
		$(inputIdentifier).select2("destroy");
		if (destroy) {
			return null;
		}
	}
	if (new_element) {
		$(inputIdentifier).empty();
	}
	$(inputIdentifier).select2({
		ajax: {
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function (params) {
				return {
					oper: 'get-business-identifier',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					identifier: params.term
				}
			},
			processResults: function (data) {
				return {
					results: $.map(data, function (item, idx) {
						return {
							text: `${item.iden} (${item.code}) - ${item.des}`,
							descripcion: item.des,
							price: item.price,
							id: item.iden,
							su: item.su,
							code: item.code,
						}
					}),
				}
			},
			// cache: true
		},
		language: "es",
		inputTooShort: function (left) {
			return 'Faltan X caracteres';
		},
		templateSelection: function (data, container) {

			var satCode = data.code;
			var satUnit = data.su;
			var unitPrice = data.price;
			var identifier = data.iden;
			var description = data.descripcion;
			if (satCode !== undefined) {
				$('#prodservice_' + _ID).val(satCode).trigger('change');
			}
			if (satUnit !== undefined) {
				$('#key_unit_' + _ID).val(satUnit).trigger('change');
			}
			if (unitPrice !== undefined) {
				$('#unit_price_' + _ID + ', #amount_' + _ID).val(unitPrice).trigger('change');
				calculateTotals();
			}


			if (description !== undefined) {
				$('#subtitle_' + _ID).text(description);
			}
			//$('input[id^="tasaocuota_' + counter + '_"]').trigger('change');

			return data.id;
		},
		placeholder: 'Producto / Servicio',
		minimumInputLength: 1,
		width: 'resolve',
		theme: "bootstrap"
	});
	if (new_element) {

		$('#quantity_' + _ID).on('change blur', function (e) {
			//if (unitPriceAvoid !== $(this).val())
			calculateAmounts(_ID);
			//quantityAvoid = $(this).val();
		});
		//$('#unit_price_' + _ID).on('change keyup', function(e){
		$('#unit_price_' + _ID).on('change blur', function (e) {
			e.preventDefault();
			//if (unitPriceAvoid !== $(this).val())
			calculateAmounts(_ID);
			//unitPriceAvoid = $(this).val();
		});

		$('#discount_' + _ID).on('change', function (e) {
			// if (unitPriceAvoid !== $(this).val())
			var discountAmount = parseFloat($(this).val());
			var _amount = $('#amount_' + _ID).val();
			_discountDecimals = parseFloat(discountAmount).countDecimals();
			_amountDecimals = parseFloat(_amount).countDecimals();
			if (_discountDecimals > _amountDecimals) {
				$(this).val(discountAmount.toFixed(_amountDecimals));
			}
			if (discountAmount > _amount) {
				$(this).val(_amount).trigger('change');
				error_message(gettext('Discount cannot be greater than the amount.'));
			}

			calculateAmounts(_ID);
			//quantityAvoid = $(this).val();
		});
		$('ul#dropdown_' + _ID).on('click', function (event) {
			event.stopPropagation();
		});
	}

}

function calculateTotals() {

	amounts = $("input[id^='amount_']").map(function () { return this.value }).get();
	discounts = $("input[id^='discount_']").map(function () { return this.value }).get();
	//totalTras = $("input[id^='discount_']").map(function(){ return this.value}).get();
	taxes = { 'tax': {} }
	$('div[id^="impuesto_"]').map(function () {
		id = $(this).prop('id').match(/\d+_\d+$/);
		type = $('#tipo_' + id).val();
		if (!(type in taxes['tax']))
			taxes['tax'][type] = [];
		taxes['tax'][type].push($('#iimporte_' + id).val());
		console.log($('#iimporte_' + id).val());
	});
	$.ajax({
		url: INVOICING_CALCULATING_AMOUNTS_URL,
		async: true,
		dataType: 'json',
		method: 'POST',
		data: {
			'taxes': taxes,
			'amounts': amounts,
			'discounts': discounts,
			'currency': $('#id_select').val(),
			'csrfmiddlewaretoken': getCookie('csrftoken'),
			'oper': 'get-subtotal',
		},
		success: function (data, textStatus, jqXHR) {

			totalRetInvoice = data.ret;
			totalTrasInvoice = data.tras;
			subtotalInvoice = data.subtotal;
			discountInvoice = data.discount;
			subtotal_taxes = data.subtotal_taxes_trunc;

			$('#totalret-invoice').text(`$ ${data.ret_display.toLocaleString('es-MX')}`);
			//$('#totaltras-invoice').text(`$ ${data.tras_display.toLocaleString('es-MX')}`);
			$('#totaltras-invoice').text(`$ ${subtotal_taxes.toLocaleString('es-MX')}`);
			$('#subtotal-invoice').text(`$ ${data.subtotal_display.toLocaleString('es-MX')}`);
			$('#discount-invoice').text(`$ ${data.discount_display.toLocaleString('es-MX')}`);

			$.ajax({
				url: INVOICING_CALCULATING_AMOUNTS_URL,
				async: false,
				dataType: 'json',
				method: 'POST',
				data: {
					'amounts': subtotalInvoice,
					'discounts': discountInvoice,
					'totalRet': totalRetInvoice,
					'totalTras': subtotal_taxes,
					'currency': $('#id_select').val(),
					'csrfmiddlewaretoken': getCookie('csrftoken'),
					'oper': 'get-total',
				},
				success: function (data, textStatus, jqXHR) {
					// totalInvoice = data.total;
					$('#total-letter').text(data.total_letter);
					$('#total-invoice,#header-total').text(`$ ${data.total.toLocaleString('es-MX')}`);
					totalInvoice = data.total;
				}
			});
		}
	});

}

function calculateAmounts(counter) {
	$.ajax({
		url: INVOICING_STUFFS_URL,
		async: true,
		dataType: 'json',
		method: 'POST',
		data: {
			'quantity': $('#quantity_' + counter).val(),
			'identifier': $('#identifier_' + counter).val(),
			'prodserv': $('#prodserv_' + counter).val(),
			'csrfmiddlewaretoken': getCookie('csrftoken'),
			'oper': 'get-amount',
		},
		success: function (data, textStatus, jqXHR) {
			$('#amount_' + counter).val(data.amount);
			$(`input[id^='tasaocuota_${counter}_']`).each(function (idx, element) {
				calculateIVAConcept(element);
			});
			calculateTotals();
		}
	});
}

function addTaxElement(element) {
	taxElement = $(element).closest('div[id^="concepto_"]').find('div[id^="impuestos_"]');
	serial = parseInt(taxElement.prop('id').match(/\d+/g), 10);
	serialTAXElement = $(taxElement).find('div[id^="impuesto_' + serial + '_"]:last');
	id = serialTAXElement.prop('id');
	serialTAX = serialTAXElement.length >= 1 ? parseInt(id.match(/\d+$/g), 10) + 1 : 0;
	ivaElement = $.parseHTML(TAX_TEMPLATE);
	$(ivaElement).prop('id', 'impuesto_' + serial + '_' + serialTAX);
	$(ivaElement).find('#tasaocuota_0_0').prop('id', 'tasaocuota_' + serial + '_' + serialTAX);
	$(ivaElement).find('#iimpuesto_0_0').prop('id', 'iimpuesto_' + serial + '_' + serialTAX);
	$(ivaElement).find('#factor_0_0').prop('id', 'factor_' + serial + '_' + serialTAX);
	$(ivaElement).find('#tipo_0_0').prop('id', 'tipo_' + serial + '_' + serialTAX);
	$(ivaElement).find('#iimporte_0_0').prop('id', 'iimporte_' + serial + '_' + serialTAX);
	$(ivaElement).find('#rimpuesto_0_0').prop('id', 'rimpuesto_' + serial + '_' + serialTAX);
	$(taxElement).append(ivaElement);

	let elementoFactor = $('#factor_' + serial + '_' + serialTAX);
	let elementoTasaOCuota = $('#tasaocuota_' + serial + '_' + serialTAX);
	let elementoTipo = $('#tipo_' + serial + '_' + serialTAX);
	let elementoImpuesto = $('#iimpuesto_' + serial + '_' + serialTAX);
	let elementoImporte = $('#iimporte_' + serial + '_' + serialTAX);

	/*elementoImpuesto.on('change', function(e){
		let vImpuesto = $(this).val();
		if (vImpuesto !== '003'){
			if (elementoFactor.val() !== 'Tasa'){
				elementoFactor.val('Tasa').trigger('change');
			}
			if(vImpuesto === '001'){
				if (elementoTipo.val() !== 'Retencion'){
					elementoTipo.val('Retencion').trigger('change');
				}
			}
		}
	});*/

	elementoFactor.on('change', function (e) {
		let vFactor = $(this).val();
		elementoTasaOCuota.removeAttr('disabled', 'disabled');
		if (vFactor == 'Exento') {

			elementoTasaOCuota.attr('disabled', 'disabled');
			if (elementoTipo.val() == 'Retencion') {
				selfFactor.val('Tasa').trigger('change');
			}
		} else if (vFactor === 'Cuota') {
			if (elementoImpuesto.val() != '003') {
				elementoImpuesto.val('003').trigger('change');
			}
		}
	});
	elementoTipo.on('change', function (e) {
		let selfTipo = $(this);
		let vTipo = selfTipo.val();
		if (vTipo == 'Retencion') {
			elementoImporte.val('0.000000');
			elementoFactor.val('Tasa').trigger('change');
		} else {
			if (elementoImpuesto.val() == '001') {
				elementoImpuesto.val('002').trigger('change');
			}
		}
		calculateIVAConcept(elementoTasaOCuota)
	});

	$('.taxinvoice').select2({
		ajax: {
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			delay: 250,
			width: 'resolve',
			data: function (params) {
				params.term = params.term.toUpperCase();
				return {
					oper: 'get-peppol-catalogue',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					peppolkey: params.term,
					catalogue: 'UNCL5305'
				}
			},
			processResults: function (data) {
				return {
					results: $.map(data, function (item, idx) {
						return {
							text: item.text,
							id: item.id,
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
		placeholder: 'TaxCategory ID',
		minimumInputLength: 1,
		theme: "bootstrap",
	});
	calculateTotals();
	calculateIVAConcept(elementoTasaOCuota);
}

function deleteTax(element) {
	taxElement = $(element).closest('div[id^="impuesto_"]');
	$(taxElement).find(':input').each(function () {
		$(this).off('change');
	});
	taxElement.remove();
	calculateTotals();
}

function JSONify() {
	var moneda = $('#id_select').val();
	var tipocambio = $('#id_currency').val();
	var internal_notes = $('#notes').val();
	//if (moneda == 'MXN'){
	//	tipocambio = '1';
	//}

	/*invoice = {
		'TipoDeComprobante': $('#id_type_invoice').val(),
		'MetodoPago': $('#id_payment_method').val(),
		'FormaPago': $('#id_payment_way').val(),
		'LugarExpedicion': $('#id_expedition_place').val(),
		'Serie': $('#id_serial').val(),
		'Folio': $('#id_folio').val(),
		'Moneda': moneda,
		'TipoCambio': tipocambio,
		'CondicionesDePago': $('#payment_conditions').val(),
		'Total': totalInvoice,
		'SubTotal': subtotalInvoice,
		'Descuento': discountInvoice,
	}*/



	var id_invoice = $("#id_id_invoice").val()
	var type_invoice = $("#id_type_invoice").val()
	var currency = $("#id_select").val()
	var accounting_cost_invoice = $("#id_accounting_cost_invoice").val()
	var buyer_reference_invoice = $("#buyer_reference_invoice").val()
	var date = new Date();
	var paymentMeans = $('#payment_name_select').select2('data')[0];
	// var issue_date = formatDate(date);
	// var due_date = formatDate(date);

	var invoice = {}

	invoice['invoice'] = {
		// "CustomizationID": "urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0",
		"CustomizationID": "1.0",
		"UBLVersionID": "1.2",
		// "ProfileID": "urn:fdc:peppol.eu:2017:poacc:billing:01:1.0",
		"ID": id_invoice,
		"PaymentMeans": {
            "PaymentMeansCode":{
                "value": paymentMeans.id,
                "name": paymentMeans.name
			}
		},
		"Note": $('#notes').val(),
		// "IssueDate": issue_date,
		// "DueDate": due_date,
		"InvoiceTypeCode": type_invoice,
		"DocumentCurrencyCode": currency,
		"AccountingCost": accounting_cost_invoice,
		"BuyerReference": buyer_reference_invoice,

	}

	invoice['asp'] = {
		'taxpayer_id': $('#business_taxpayer_id').text(),
	}

	invoice['acp'] = {
		'taxpayer_id': $('#id_rtaxpayer').val(),
		'customer_country': $('#id_fiscal_address').val()
	}

	invoice['payment_terms'] = {
		// 'note': $('#payment_conditions').val()
		'note': ''
	}

	invoice['taxes'] = {
		'TaxAmount': subtotal_taxes
	}

	invoice['items'] = get_items();

	invoice['taxes'] = {
		'total_invoice': totalInvoice,
		'total_taxes': subtotal_taxes,
		'currency': $("#id_select").val(),
		'TaxSubtotal': get_taxes(totalInvoice)
	}
	invoice['legal_monetary_total'] = {
		'total': totalInvoice,
		'SubTotal': subtotalInvoice,
		'total_taxes': subtotal_taxes,
		'currency': $("#id_select").val(),
		'discountInvoice': discountInvoice
	}

	/*invoice['Conceptos'] = $('div[id^="concepto_"]').map(function(idxc, concept){
		
		idComplement = parseInt($(concept).prop('id').match(/\d+/), 10);
		
		taxes = {};
		
		cantidad = $('#quantity_' + idComplement).val();
		descuento = $('#discount_' + idComplement).val();
		if (descuento == 0.0){
			descuento = '';
		}
		claveUnidad = $('#key_unit_' + idComplement).val();
		claveProdServ = $('#prodservice_' + idComplement).val();
		noIdentificacion = $('#identifier_' + idComplement).val();
		importe = $('#amount_' + idComplement).val();

		//mpuestosD['Traslados'] = $('#impuestos_' + idComplemento + ' div[id^="impuesto_' + idComplemento +'_"] select[value="Traslado"]').map(function(idxi, impuesto){
		//	impuestoJSON = {}
		//	idImpuesto = parseInt($(impuesto).prop('id').match(/\d+$/g));
		//	impuestoSerial = '_' + idComplemento + '_' + idImpuesto;
		//	tasaocuota = $('#tasaocuota'+ impuestoSerial).val();
		//	iimpuesto = $('#iimpuesto'+ impuestoSerial).val();
		//	factor = $('#factor'+ impuestoSerial).val();
		//	tipo = $('#tipo'+ impuestoSerial).val();
		//	iimporte = $('#iimporte'+ impuestoSerial).val();
		//	impuestoJSON = {
		//		'TasaOCuota': tasaocuota,
		//		'Impuesto': iimpuesto,
		//		'Factor': factor,
		//		'Importe': iimporte
		//	}
		//	return  impuestoJSON
		//}).get();
		taxes['Traslados'] = $('#impuestos_' + idComplement + ' div[id^="impuesto_' + idComplement +'_"] select[id^="tipo_"] option[value="Traslado"]:selected').closest('div[id^="impuesto_' + idComplement +'_"]').map(function(idxi, tax){
			idTax = parseInt($(tax).prop('id').match(/\d+$/g));
			serialTax = `_${idComplement}_${idTax}`;

			tipoFactor = $('#factor'+ serialTax).val();
			iImporte = $('#iimporte'+ serialTax).val();
			iImpuesto = $('#iimpuesto'+ serialTax).val();
			tasaOCuota = $('#tasaocuota'+ serialTax).val().padEnd(8, '0');

			if (iImporte == '0' || iImporte == null || iImporte == undefined){
				iImporte = '0.000000';
			}

			if (tipoFactor === 'Exento'){
				tasaOCuota = '0.000000';
			}
			
			// taxKey = `${iImpuesto}-${tipoFactor}-${tasaOCuota}`
			// if (!(taxKey in generalTax['Traslados']))
			// 	generalTax['Traslados'][taxKey] = 0
			// generalTax['Traslados'][taxKey] += parseFloat(iImporte)

			return {
				'Base': importe,
				'Importe': iImporte,
				'Impuesto': iImpuesto,
				'TipoFactor': tipoFactor,
				'TasaOCuota': tasaOCuota
			}
		}).get();

		taxes['Retenciones'] = $('#impuestos_' + idComplement + ' div[id^="impuesto_' + idComplement +'_"] select[id^="tipo_"] option[value="Retencion"]:selected').closest('div[id^="impuesto_' + idComplement +'_"]').map(function(idxi, tax){
			idTax = parseInt($(tax).prop('id').match(/\d+$/g));
			serialTax = `_${idComplement}_${idTax}`;

			tipoFactor = $('#factor'+ serialTax).val();
			iImporte = $('#iimporte'+ serialTax).val();
			iImpuesto = $('#iimpuesto'+ serialTax).val();
			tasaOCuota = $('#tasaocuota'+ serialTax).val();

			if (iImporte == '0'){
				iImporte = '0.000000';
			}
			if(tipoFactor == 'Exento'){
				iImporte = 0.0;
			}

			// if (!(tipoFactor in generalTax['Retenciones']))
			// 	generalTax['Retenciones'][iImpuesto] = 0
			// generalTax['Retenciones'][iImpuesto] += parseFloat(iImporte)
			

			return {
				'Base': importe,
				'Importe': iImporte,
				'Impuesto': iImpuesto,
				'TasaOCuota': tasaOCuota,
				'TipoFactor': tipoFactor,
			}
		}).get();

		return {
			'Cantidad': cantidad,
			'Descuento': descuento,
			'ClaveUnidad': claveUnidad,
			'Impuestos': taxes,
			'ClaveProdServ': claveProdServ,
			'NoIdentificacion': noIdentificacion,
			'Importe': importe
		}
	}).get();*/

	/*invoice['Receptor'] = {
		'Rfc': $('#id_rtaxpayer').val(),
		'UsoCFDI': $('#id_use_cfdi').val(),
		'ResidenciaFiscal': $('#id_fiscal_address').val(),
		'NumRegIdTrib': $('#id_rit').val(),
	}*/

	/*invoice['CfdiRelacionados'] = {
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
	}*/

	//invoice['NotasInternas'] = internal_notes;
	// invoice['Impuestos'] = generalTax;

	return JSON.stringify(invoice)
}

function Notes() {
	var internal_notes = $('#notes').val();
	return internal_notes;
}

function calculateIVAConcept(feeorfeeElement) {

	feeorFeeVal = $(feeorfeeElement).val()
	//if(feeorFeeVal.length > 8){
	//	$(feeorfeeElement).val(feeorFeeVal.slice(0,8));
	//}else if(feeorFeeVal != null || feeorFeeVal != ''){
	//	if(feeorFeeVal != 0){
	//		$(feeorfeeElement).val(feeorFeeVal.padEnd(8, '0'));
	//	}else{
	//		$(feeorfeeElement).val('0.000000');
	//	}
	//	
	//}

	amount = $('#amount_' + parseInt($(feeorfeeElement).prop('id').match(/\d+/), 10)).val();

	serial = $(feeorfeeElement).prop('id').match(/\d+_\d+$/g).toString();

	tipo = $('#tipo_' + serial).val();
	factor = $('#factor_' + serial).val();
	tasaocuota = $(feeorfeeElement).val();
	impuesto = $('#iimpuesto_' + serial).val();
	discounts = $("#discount_" + parseFloat(serial).toString()).val();

	$.ajax({
		url: INVOICING_STUFFS_URL,
		async: false,
		dataType: 'json',
		method: 'POST',
		data: {
			'amount': amount,
			'feeorfee': tasaocuota,
			'tax': impuesto,
			'factor': factor,
			'tipo': tipo,
			'discount': discounts,
			'csrfmiddlewaretoken': getCookie('csrftoken'),
			'oper': 'get-tax',
		},
		success: function (data, textStatus, jqXHR) {
			console.log(data.total_tax);
			console.log("Total Tax");
			$('#iimporte_' + serial).val(data.total_tax);
			calculateTotals();
		}
	});
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
	$('#id_serial').empty();
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
	$('#total-letter').text('');
	$('#id_rtaxpayer').empty();
	$('#id_rtaxpayer').val(null).trigger('change');
	$('#identifier_0').empty();
	$('#identifier_0').val(null).trigger('change');
}

function initaddConcept() {
	$(document).on('click', '.add-concept', function (e) {
		var concept = $('#seccion_conceptos div[id^="div_concepto_"]:last');
		var oldIdConcept = parseInt(concept.prop('id').match(/\d+/g), 10);
		initNoIdentification(oldIdConcept, true, false);
		var idConcept = oldIdConcept + 1;
		var newWrapConcept = concept.clone(false, false).prop('id', 'div_concepto_' + idConcept);
		initNoIdentification(oldIdConcept, false, false);

		// newConcept.find('div.hr-select strong').prop('id', 'concepto_' + idConcept);
		// newConcept.find('div[id^="concepto-titulo_"]').prop('id', 'concepto-titulo_' + idConcept);
		// newConcept.find('button[data-target^="#concepto_"]').prop('data-target', '#concepto_' + idConcept)
		// newConcept.find('div[id^="concepto_"]').prop('id', 'concepto_' + idConcept);
		// newConcept.find('small[id^="subtitle_"]').prop('id', 'subtitle_' + idConcept);
		// newConcept.find('small[id^="subtitle_"]').text('');
		// newConcept.find('div[id^="impuestos_"]').empty();
		// newConcept.find('div[id^="impuestos_"]').prop('id', 'impuestos_' + idConcept);

		newWrapConcept.find('#title_' + oldIdConcept).prop('id', 'title_' + idConcept);
		newWrapConcept.find('#title_' + idConcept).attr('data-target', '#concepto_' + idConcept);

		newWrapConcept.find('#concepto_' + oldIdConcept).prop('id', 'concepto_' + idConcept);
		var newConcept = newWrapConcept.find('#concepto_' + idConcept);

		newWrapConcept.find('#subtitle_' + oldIdConcept).prop('id', 'subtitle_' + idConcept);
		newWrapConcept.find('#subtitle_' + idConcept).text('');

		newConcept.find('#impuestos_' + oldIdConcept).prop('id', 'impuestos_' + idConcept);
		newConcept.find('#impuestos_' + idConcept).empty();
		$(newConcept).find(':input', 'label').each(function () {
			self = $(this);
			// console.log(self.attr('name') + '_' + idConcept);
			name = self.attr('name') + '_' + idConcept;
			if (self.attr('name') == 'quantity') {
				self.val('1.0');
			} else if (self.attr('name') == 'unit_price') {
				self.val('1.0');
			} else if (self.attr('name') == 'amount') {
				self.val('0.0');
			} else if (self.attr('name') == 'discount') {
				self.val('0.0');
			} else {
				self.val('');
			}
			self.prop('id', name);
			self.closest('div.form-group').find('label.control-label').prop('for', name);
		});
		// $(newConcept).find('ul.dropdown-menu').each(function(){
		// 	self = $(this);
		// 	name = self.attr('name') + '_' + idConcept;
		// 	self.prop('id', name);
		// });

		concept.after(newWrapConcept);
		// getProdServ(newConcept, idConcept);
		initNoIdentification(idConcept, false, true);
		calculateAmounts(idConcept);
	});
}

function initRemoveConcept() {
	$(document).on('click', '.remove-concept', function (e) {
		var concept = $(this).closest('div[id^="div_concepto_"]');
		$(concept).find('small[id^="subtitle_"]').text('');
		if ($('div[id^="div_concepto_"]').length > 1) {
			concept.remove();
		} else {
			concept.find(':input').each(function () {
				self = $(this);
				if (self.attr('name') == 'quantity') {
					self.val('1.0');
				} else if (self.attr('name') == 'unit_price') {
					self.val('1.0');
				} else if (self.attr('name') == 'amount') {
					self.val('0.0');
				} else if (self.attr('name') == 'discount') {
					self.val('0.0');
				} else {
					self.val('');
				}
			});
			concept.find('select').empty();
			concept.find('select').val(null).trigger('change');
		}
		calculateAmounts(parseInt(concept.prop('id').match(/\d+/g), 10));
	});
}

function initComprobante() {
	$('#id_payment_method').select2({
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_select').select2({
		ajax: {
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			data: function (params) {
				return {
					oper: 'get-currency',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					clave: params.term
				}
			},
			processResults: function (data) {
				return {
					results: $.map(data, function (item, idx) {
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
			var tipoCambio = data.tipoCambio;
			if (data.text === 'MXN - Peso Mexicano') {
				$('#id_currency').attr('readonly', 'readonly');
				tipoCambio = '1.0'
			} else {
				$('#id_currency').removeAttr('readonly');
			}

			$('#id_currency').val(tipoCambio);
			// $(data.element).attr('data-custom-attribute', data.customValue);
			return data.text;
		},
		placeholder: 'Moneda',
		minimumInputLength: 3,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#payment_name_select').select2({
		ajax: {
			url: INVOICING_STUFFS_URL,
			method: 'POST',
			width: 'resolve',
			dataType: 'json',
			delay: 250,
			data: function (params) {
				return {
					oper: 'get-payment-name',
					csrfmiddlewaretoken: getCookie('csrftoken'),
					code: params.term
				}
			},
			processResults: function (data) {
				return {
					results: $.map(data, function (item, idx) {
						return {
							text: `${item.code} - ${item.name}`,
							id: item.code,
							name: item.name,
						}
					}),
				}
			},
			cache: true
		},
		language: "es",
		inputTooShort: function (left) {
			return gettext('Enter X more characters.');
		},
		placeholder: gettext("Payment Name"),
		minimumInputLength: 1,
		// allowClear: true,
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_payment_way').select2({
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_use_cfdi').select2({
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_type_invoice').select2({
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_fiscal_address').select2({
		width: 'resolve',
		theme: "bootstrap"
	});
	$('#id_type_invoice').on('change', function (e) {
		if ($(this).val() == 'P') {
			$("#modal-invoice-payment").modal('show');
		}
	});
	$('#id_select').on('change', function (e) {
		if ($(this).val() == 'MXN') {
			$('#id_currency').val('1.0');
			$('#id_currency').attr('readonly', 'readonly');
		} else {
			$('#id_currency').removeAttr('readonly');
			// $('#id_select').select2('destroy');
		}
	});
	$('#modal-invoice-payment').on('hide.bs.modal', function (e) {
		$('#id_type_invoice').val('I').trigger('change');
	})
}

function initClearRTaxpayerID() {
	$('#id_rtaxpayer').on('select2:clear', function (e) {
		$('#id_use_cfdi').val(null).trigger('change');
		$('#receptor_name').text('');
	});
}

function formatDate(date) {
	var d = new Date(date),
		month = '' + (d.getMonth() + 1),
		day = '' + d.getDate(),
		year = d.getFullYear();

	if (month.length < 2)
		month = '0' + month;
	if (day.length < 2)
		day = '0' + day;

	return [year, month, day].join('-');
}

var UUID_PATTERN = /^[a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12}$/;
function validateForm(btn) {
	var isValid = true;
	var emptyProdServ = false;
	var emptyPais = false;
	var emptyUUIDRelated = false;
	var badUUIDRelated = false;
	if ($('#id_rtaxpayer').val() === '' || $('#id_rtaxpayer').val() === null || $('#id_rtaxpayer').val() === undefined) {
		$('#div_id_rtaxpayer').addClass('has-error');
		// error_message(gettext('You must enter the RFC of the receiver'));
		isValid = false;
	}
	if($('#payment_name_select').val() === null){
		isValid = false;
		$('#div_id_payment_name').addClass('has-error');
		// error_message('Debes seleccionar la forma de pago');
	}
	if($("#id_fiscal_address").val() === null){
		isValid = false;
		$('#div_id_fiscal_address').addClass('has-error');
		// error_message('Debes seleccionar el pais');
	}
	$('select[id^="identifier_"]').each(function (idx, element) {
		if ($(element).val() === null || $(element).val() == '') {
			emptyProdServ = true;
			$(element).parents('#div_id_identifier').addClass('has-error');
			isValid = false;
		}
	});

	if (!$('#div_uuid_relacionados').hasClass('hidden')) {
		$('input[id^="id_uuid_related_"]').each(function (idx, element) {
			var tmpUUID = $(element).val();
			if (tmpUUID === null || tmpUUID === undefined || tmpUUID === "") {
				emptyUUIDRelated = true;
				isValid = false;
				$(element).parents('div[id^="div_uuidrelacionado_"]').addClass('has-error');
			} else if (!tmpUUID.match(UUID_PATTERN)) {
				badUUIDRelated = true;
				isValid = false;
				$(element).parents('div[id^="div_uuidrelacionado_"]').addClass('has-error');
			}
		});
	}
	//if ($('#id_expedition_place').val() == null || $('#id_expedition_place').val() == ""){
	//	$('#div_id_expedition_place').addClass('has-error');
	//	error_message('Ingresa un código postal.');
	//	isValid = false;
	//}
	// if (emptyProdServ) {
	// 	error_message(gettext('You must enter a product or service.'));
	// }
	if (emptyUUIDRelated) {
		error_message(gettext('Related UUID cannot be empty.'));
	}
	if (badUUIDRelated) {
		error_message(gettext('The UUID is poorly formed.'));
	}
	if (emptyPais){
		error_message(gettext('You must enter a country.'));
	}
	if(isValid === false){
		error_message(gettext('Highlighted fields cannot be empty'));
	}
	return isValid;
}

function get_taxes(total) {
	var taxes = []
	$('div[id^="impuesto_"]').each(function (index, element) {
		cont = $(element).attr('id');
		ext_index = cont.split('_');
		id_concept = ext_index[1];
		id_tax = ext_index[2];
		var tax_percent = $("#tasaocuota_" + id_concept + "_" + id_tax).val()
		var tax_id = $("#iimpuesto_" + id_concept + "_" + id_tax).val()
		var tax_value = $("#iimporte_" + id_concept + "_" + id_tax).val()
		taxes.push(
			{
				"value": tax_value,
				"ID": tax_id,
				"Percent": tax_percent,
			}
		)

	})
	return taxes
}

function get_taxes(total) {
	var taxes = []
	$('div[id^="impuesto_"]').each(function (index, element) {
		cont = $(element).attr('id');
		ext_index = cont.split('_');
		id_concept = ext_index[1];
		id_tax = ext_index[2];
		var tax_percent = $("#tasaocuota_" + id_concept + "_" + id_tax).val()
		var tax_id = $("#iimpuesto_" + id_concept + "_" + id_tax).val()
		var tax_value = $("#iimporte_" + id_concept + "_" + id_tax).val()
		taxes.push(
			{
				"value": tax_value,
				"ID": tax_id,
				"Percent": tax_percent,
			}
		)

	})
	return taxes
}

function get_items() {
	var items = []
	var currency = $("#id_select").val()
	var country = $("#id_fiscal_address").val()
	var payment_name = $('#payment_name_select').val();
	var accounting_cost_invoice = $("#id_accounting_cost_invoice").val()
	$('div[id^="concepto_"]').each(function (index, element) {
		console.log(element);
		cont = $(element).attr('id');
		ext_index = cont.split('_');
		id_concept = ext_index[1];
		$("#discount_" + id_concept).attr("required", false);
		var identifier = $("#identifier_" + id_concept).val()
		var quantity = $("#quantity_" + id_concept).val()
		var discount = $("#discount_" + id_concept).val()
		var amount = $("#amount_" + id_concept).val()
		var tax_type = typeof($(`#iimpuesto_${id_concept}_0`).select2('data')) != typeof(undefined) ? $(`#iimpuesto_${id_concept}_0`).select2('data')[0].id : '';
		var tax_percent = $(`#tasaocuota_${id_concept}_0`).val() ? $(`#tasaocuota_${id_concept}_0`).val() : 0;
		items.push(
			{
				"currency": currency,
				"item_id": identifier,
				"quantity": quantity,
				"discount": discount,
				"amount": amount,
				"accounting_cost": accounting_cost_invoice,
				"country": country,
				'payment_name': payment_name,
				// "tax_percent": $(`#tasaocuota_${id_concept}_0`).val(),
				// "tax_type": $(`#iimpuesto_${id_concept}_0`).select2('data')[0].id,
				"tax_percent": tax_percent,
				"tax_type": tax_type
			}
		)
	})
	$('#div_id_discount, .amounts numberinput .form-control').keypress(function (e) { 
		if(e.which == 13) {
			return false;
		}
	});
	$('#div_id_discount .amounts').attr("required", false);
	return items
}

function get_uuid() {
	$.ajax({
		url: INVOICING_STUFFS_URL,
		async: true,
		dataType: 'json',
		method: 'POST',
		data: {
			'csrfmiddlewaretoken': getCookie('csrftoken'),
			'oper': 'get-uuid',
		},
		success: function (data, textStatus, jqXHR) {
			var uuid = data[0].uuid;
			console.log(uuid);
			$("#id_id_invoice").val(uuid)
		}
	});
}

$(document).ready(function (e) {
	//Eventos para agregar conceptos
	initaddConcept();
	//Eventos para borrar conceptos
	initRemoveConcept();
	//Eventos para traer el producto
	initNoIdentification(0, false, true);
	//Inicializacion de todos los elementos de  comprobante
	initComprobante();
	// Eventos para limpiar el Rfc receptor
	initClearRTaxpayerID();
	// Eventos para asignar el UUID
	get_uuid()

	// Evita que se timbre la factura antes de validar el descuento de cada concepto
	$(document).on('keypress', '.amounts.numberinput',function (e) { 
		if(e.which == 13) {
			return false;
		}
	});
	$('.amounts.numberinput').attr("required", false);
	$('#modal-add-certificate').modal('show');

});