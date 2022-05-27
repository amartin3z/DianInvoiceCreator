var formatNumber = {
  separator: ",",
  sepDecimal: '.',
  formatter: function (num) {
    num += '';
    var splitStr = num.split(',');
    var splitLeft = splitStr[0];
    var splitRight = splitStr.length > 1 ? this.sepDecimal + splitStr[1] : '';
    var regx = /(\d+)(\d{3})/;
    while (regx.test(splitLeft)) {
      splitLeft = splitLeft.replace(regx, '$1' + this.separator + '$2');
    }
    return this.simbol + splitLeft + splitRight;
  },
  new: function (num, simbol) {
    this.simbol = simbol || '';
    return this.formatter(num);
  }
}

var prodservColumns = [{
  'sWidth': '1%',
  'bSortable': false
}, {
  'sWidth': '13%',
  'bSortable': false,
}, {
  'sWidth': '12%',
  'bSortable': false,
}, {
  'sWidth': '12%',
  'bSortable': false,
}, {
  'sWidth': '35%',
  'bSortable': false,
}, {
  'sWidth': '15%',
  'bSortable': false,
},{
  'sWidth': '13%',
  'bSortable': false,
  'className': 'text-center'
}];

function select2Init(select2Id, catalogue, placeholder) {
  $('#' + select2Id).select2({
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
          catalogue: catalogue
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
    placeholder: placeholder,
    minimumInputLength: 1,
    theme: "bootstrap",
  });
}


$(document).ready(function () {

  $('#prodcerv').addClass('active');

  var prodservTable = $('#invoicing-prodserv').DataTable({
    "responsive": true,
    "searching": false,
    "bProcessing": true,
    "bServerSide": true,
    "stateSave": true,
    'ordering': false,
    "language": language_datatable,
    "columns": prodservColumns,
    "PagingType": "full_numbers",
    "sAjaxSource": urlProdserv,
    "columnDefs": [
      {
        className: "text-center",
        "targets": [0, 1, 2, 3, 4, 5, 6],
      },
    ],
    fnServerData: function callback(sSource, aoData, fnCallback) {
      aoData.push({
        "name": "csrfmiddlewaretoken",
        "value": getCookie('csrftoken')
      });
      aoData.push({
        "name": "oper",
        "value": "list-prodserv"
      });
      if ($("#status").val() != "A") {
        aoData.push({
          "name": "status",
          "value": $("#status").val()
        });
      }
      if ($("#product_service_filter").val()) {
        aoData.push({
          "name": "prodserv",
          "value": $("#product_service_filter").val()
        });
      }
      // if ($("#c-prodserv").val()){
      //   aoData.push({
      //       "name": "prodserv",
      //       "value": $("#c-prodserv").val()
      //   });
      // }
      if ($("#clasification_code_filter").val()) {
        aoData.push({
          "name": "clasification_code_filter",
          "value": $("#clasification_code_filter").val()
        });
      }
      if ($("#description_filter").val()) {
        aoData.push({
          "name": "description",
          "value": $("#description_filter").val()
        });
      }
      if ($("#unit_code_filter").val()) {
        aoData.push({
          "name": "unit_code",
          "value": $("#unit_code_filter").val()
        });
      }
      if ($("#date-from-val").val() && $("#date-to-val").val()) {
        aoData.push({
          "name": "date-from",
          "value": $("#date-from-val").val()
        });

        aoData.push({
          "name": "date-to",
          "value": $("#date-to-val").val()
        });
      }

      aoData.push({
        'name': 'language',
        'value': language
      });

      $.ajax({
        "dataType": "json",
        "type": "POST",
        "url": sSource,
        "data": aoData,
        "success": function (json) {
          fnCallback(json);
          for (var i = 1; i <= json['aaData'].length; i++) {
            val_monto = formatNumber.new($('#invoicing-prodserv').find('tbody').find('tr:nth-child(' + i + ')').find('td').eq(5).html(), '$ ')
            $('#invoicing-prodserv').find('tbody').find('tr:nth-child(' + i + ')').find('td').eq(5).html(val_monto);
          }
        }
      });
    }
  });

  prodservTable.on('draw.dt', function () {
    var pageInfo = prodservTable.page.info();

    prodservTable.column(0, { page: 'current' }).nodes().each(function (cell, i) {
      cell.innerHTML = i + 1 + pageInfo.start;
    });
  });

  $('#clasification_code_filter').keyup(function (e) {
    e.preventDefault();
    var pLength = $(this).val().length;
    if ((pLength > 2 || pLength == 0) && is_valid_key(e.which)) {
      prodservTable.draw();
    }
  });
  $('#product_service_filter').keyup(function (e) {
    e.preventDefault();
    var iLength = $(this).val().length;
    if ((iLength > 2 || iLength == 0) && is_valid_key(e.which)) {
      prodservTable.draw();
    }
  });
  $("#description_filter").keyup(function (e) {
    e.preventDefault();
    var dLength = $(this).val().length;
    if ((dLength > 2 || dLength == 0) && is_valid_key(e.which)) {
      prodservTable.draw();
    }
  });
  $("#unit_code_filter").keyup(function (e) {
    e.preventDefault();
    var kLength = $(this).val().length;
    if ((kLength > 1 || kLength == 0) && is_valid_key(e.which)) {
      prodservTable.draw();
    }
  });
  $("#date-from").datetimepicker({
    locale: language,
    format: "DD-MM-YYYY",
    sideBySide: true
  });
  $("#date-to").datetimepicker({
    locale: language,
    format: "DD-MM-YYYY",
    sideBySide: true
  });

  $("#date-from").on("dp.change", function (e) {
    $("#date-to").data("DateTimePicker").minDate(e.date);
    if ($("#date-from-val").val() && $("#date-to-val").val()) {
      prodservTable.ajax.reload();
    }
  });

  $("#date-to").on("dp.change", function (e) {
    $("#date-from").data("DateTimePicker").maxDate(e.date);
    if ($("#date-to-val").val() && $("#date-from-val").val()) {
      prodservTable.ajax.reload();
    }
  });

  /**
   * anp ADD NEW PRODUCT
   */
  $(document).on('click', '.anp', function (e) {
    e.preventDefault();
    // $('#prod-title').text('Add Product/Service');
    $('#prod-title-add').removeClass('hide');
    $('#prod-title-edit').addClass('hide');

    // $('#submit-id-addprodserv').text('Agregr');
    // $('#submit-id-addprodserv').attr('value', 'Agregar');
    $('.edit_prodserv').addClass('hide');
    $('.add_prodserv').removeClass('hide');
    $('#modal-prodserv').attr('edit', false);
    $('#id_identifier').attr('readonly', false);
    $('#formProdserv input:not([type=submit], [type=button], [type=hidden])').val("");
    $('#formProdserv textarea').val("");
    $('#formProdserv textinput').val("");
    $('#id_prodserv, #id_key_unit, #origin_country, #currency_id, #unit_code, #list_id').val(null).trigger('change');
    $('#item_classification_code').attr('readonly', false);
    ////////////////////////////////////////////
    $('#div_id_unit').find('label').html('Unidad<span class="asteriskField">*</span>');
    $('#id_unit').attr('required', 'required');
    ////////////////////////////////////////////
    $('#modal-prodserv').modal('show');
  });
  /**
   * canp CANCEL - ADD NEW PRODUCT
   */
  $(document).on('click', '.canp', function (e) {
    e.preventDefault();
    // $('#submit-id-addprodserv').text('Agregr');
    // $('#submit-id-addprodserv').attr('value', 'Agregar');

    $('#modal-prodserv').attr('edit', false);
    $('#id_identifier').attr('readonly', false);
    $('#modal-prodserv').modal('toggle');
    $('#formProdserv input:not([type=submit], [type=button], [type=hidden])').val("");
    $('#formProdserv textarea').val("");
    $('#id_prodserv, #id_key_unit').val(null).trigger('change');

  });

  select2Init('origin_country', 'ISO3166', 'Origin Country');
  select2Init('currency_id', 'ISO4217', 'Currency ID');
  select2Init('unit_code', 'UNECEREC20', 'Unit Code');
  select2Init('list_id', 'UNCL7143', 'List ID');
  select2Init('tax_category_code', 'UNCL5305', 'Tax Category Code');
  select2Init('standard_item_scheme', 'ICD', 'Standard Item Scheme');

  $('#formProdserv').submit(function (e) {
    e.preventDefault();

    var isEdit = $('#modal-prodserv').attr('edit');
    var action = eval(isEdit) ? 'edit' : 'add';
    var prodServData = new FormData();
    var prodServForm = $(this);
    var standar_item_scheme = $('#standard_item_scheme').val() == null ? '' : $('#standard_item_scheme').val();

    prodServData.append('oper', `${action}-prodserv`);
    prodServData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    // $.each(prodServForm.serializeArray(), function(key, input){
    //   prodServData.append(input.name, input.value);
    // });

    prodServData.append('item_name', $('#item_name').val());
    // prodServData.append('origin_country', $('#origin_country').val());
    prodServData.append('pryce_item', $('#pryce_item').val());
    prodServData.append('unit_code', $('#unit_code').val());
    prodServData.append('item_classification_code', $('#item_classification_code').val());
    prodServData.append('list_id', $('#list_id').val());
    prodServData.append('prodserv_description', $('#prodserv_description').val());
    prodServData.append('tax_category_code', $('#tax_category_code').val());
    prodServData.append('tax_percent', $('#tax_percent').val());
    prodServData.append('standard_item_identifier', $('#standard_item_identifier').val());
    prodServData.append('standard_item_scheme', standar_item_scheme);

    $.ajax({
      method: 'POST',
      data: prodServData,
      contentType: false,
      processData: false,
      success: function (response) {
        var success = response['success'];
        var send_message = success ? success_message : error_message;
        if (success) {
          // $('#formProdserv')[0].reset();
          $('#formProdserv input:not([type=submit], [type=button], [type=hidden])').val("");
          $('#origin_country,#currencyID,#unit_code,#listID,#standard_item_scheme, #tax_category_code').val(null).trigger('change');
          $('.canp').click();
          success_message(response['message']);
          prodservTable.ajax.reload();
        } else {
          var messages = new Array();
          if (response['errors']) {
            $.map(response['errors'], function (errors, element) {
              return $.map(errors, function (error, idx) {
                messages.push(error);
              });
            });
          } else {
            messages.push(response.message)
          }
          send_message(messages);
        }
      }
    });
  });

  //$('.js-example-data-ajax').select2({
  $('#id_prodserv').select2({

    ajax: {
      url: INVOICING_STUFFS_URL,
      method: 'POST',
      width: 'resolve',
      dataType: 'json',
      delay: 250,
      width: 'resolve',
      data: function (params) {
        return {
          oper: 'get-prodserv',
          csrfmiddlewaretoken: getCookie('csrftoken'),
          prodserv: params.term
        }
      },
      processResults: function (data) {
        return {
          results: $.map(data, function (item, idx) {
            return {
              text: decodeURIComponent(escape(item.des)),
              id: item.code,
            }
          }),
        }
      },
      cache: true
    },
    language: "es",
    inputTooShort: function (left) {
      console.log(left);
      return 'Faltan X caracteres';
    },
    placeholder: 'Clave Producto/Servicio (SAT)',
    minimumInputLength: 4,
    theme: "bootstrap",
  });

  $('#id_key_unit').select2({

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
          oper: 'get-keyunit',
          csrfmiddlewaretoken: getCookie('csrftoken'),
          keyunit: params.term
        }
      },
      processResults: function (data) {
        return {
          results: $.map(data, function (item, idx) {
            return {
              text: (decodeURIComponent(escape(item.des))),
              id: item.code,
            }
          }),
        }
      },
      cache: true
    },
    language: "es",
    inputTooShort: function (left) {
      console.log(left);
      return 'Faltan X caracteres';
    },
    placeholder: 'Clave Unidad (SAT)',
    minimumInputLength: 2,
    theme: "bootstrap",
  });
  $.fn.select2.defaults.set("theme", "bootstrap");

  $(document).on('click', '#clean', function (e) {
    e.preventDefault();
    $('#product_service_filter, #clasification_code_filter, #description_filter, #unit_code_filter, #date-to-val, #date-from-val').val('');
    prodservTable.draw();
  });

  $(document).on('click', '#refresh_downloads', function (e) {
    e.preventDefault();
    prodservTable.draw();
  });

  $(document).on('click', '.pe', function (e) {
    e.preventDefault();
    console.log("Click");
    var editData = new FormData();
    editData.append('product', $(this).attr('prodserv'));
    editData.append('oper', 'get-prodserv');
    editData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    $.ajax({
      method: 'POST',
      data: editData,
      contentType: false,
      processData: false,
      success: function (response) {
        var success = response['success'];
        var send_message = success ? success_message : error_message;
        if (success) {
          $('#prod-title-edit, .edit_prodserv').removeClass('hide');
          $('#prod-title-add, .add_prodserv').addClass('hide');

          // $('#submit_prod_serv').text("Edit");
          // $('#submit_prod_serv').attr('value', "{% trans 'Edit' %}");

          $('#formProdserv input:not([type=submit], [type=button], [type=hidden]), textarea').val("");
          $('#id_prodserv, #id_key_unit').val(null).trigger('change');
          $('#modal-prodserv').attr('edit', true);
          var prodinfo = response['prodservinfo'];

          // var identifier = prodinfo['identifier'];
          // $('#id_identifier').val(identifier)
          // $('#id_identifier').attr('readonly', 'readonly');

          // var unit = prodinfo['unit'];
          // $('#id_unit').val(unit);

          // var unit_price = prodinfo['unit_price'];
          // $('#id_unit_price').val(unit_price);

          // var description = prodinfo['description']; 
          // $('#id_description').val(description);

          $.each(response['info'], function (id, value) {
            $('#' + id).val(value);
          });
          /**
           * KEY UNIT SECTION (SAT)
           */
          // var keyUnitSelect = $('#id_key_unit');
          // var keyUnitData = response['key_unit'];
          // console.log(keyUnitData);
          // var optionKeyUnit = new Option((keyUnitData.full_name), keyUnitData.id, true, true);
          // console.log(optionKeyUnit);
          // keyUnitSelect.append(optionKeyUnit).trigger('change');
          // keyUnitSelect.trigger({
          //   type: 'select2:select',
          //   params: {
          //       data: keyUnitData
          //   }
          // });

          /**
           * PRODSERV SECTION (SAT)
           */
          var prodServSelect = $('#id_prodserv');
          // var prodServData = response['prodserv'];            
          // var optionProdServ = new Option((prodServData.full_name), prodServData.id, true, true);
          // prodServSelect.append(optionProdServ).trigger('change');
          // prodServSelect.trigger({
          //   type: 'select2:select',
          //   params: {
          //       data: prodServData
          //   }
          // });
          // unit_code, currency_id, list_id, origin_country
          // var currencyIdSelect = $('#currency_id');
          // var optionCurrency = new Option((response['currency_id'].full_name), response['currency_id'].id, true, true);
          // currencyIdSelect.append(optionCurrency).trigger('change');
          var unitCodeSelect = $('#unit_code');
          var optionUnitCode = new Option((response['unit_code'].full_name), response['unit_code'].id, true, true);
          unitCodeSelect.append(optionUnitCode).trigger('change');

          var listIdSelect = $('#list_id');
          var optionList = new Option((response['list_id'].full_name), response['list_id'].id, true, true);
          listIdSelect.append(optionList).trigger('change');

          // var CountrySelect = $('#origin_country');
          // var optionCountry = new Option((response['origin_country'].full_name), response['origin_country'].id, true, true);
          // CountrySelect.append(optionCountry).trigger('change');
          
          if (typeof (response['tax_category_code']) != typeof (undefined)){
            var TaxCategory = $('#tax_category_code');
            var optionTaxCategory = new Option((response['tax_category_code'].full_name), response['tax_category_code'].id, true, true);
            TaxCategory.append(optionTaxCategory).trigger('change');
          }

          if (typeof (response['standard_item_identifier']) != typeof (undefined)) {
            var StandardItemIdentifier = $('#standard_item_identifier');
            var standardCategory = new Option((response['standard_item_identifier'].full_name), response['standard_item_identifier'].id, true, true);
            StandardItemIdentifier.append(standardCategory).trigger('change');
          }

          if(typeof(response['standard_item_scheme']) != typeof(undefined)){
            var StandardItemScheme = $('#standard_item_scheme');
            var StandardScheme = new Option((response['standard_item_scheme'].full_name), response['standard_item_scheme'].id, true, true);
            StandardItemScheme.append(StandardScheme).trigger('change');
          }

          $('#item_classification_code').attr('readonly', true);
          $('#modal-prodserv').modal('show');
          //console.log(prodServ);
          //send_message(response['message']);
          //prodservTable.draw();
        } else {
          var messages = new Array();
          $.map(response['errors'], function (errors, element) {
            return $.map(errors, function (error, idx) {
              messages.push(error);
            });
          });
          send_message(messages);
        }
      }
    });
  });

});