$(window).on('load', function(){
	$('#preloader').fadeOut('slow',function(){$(this).remove();});
});


/******************************************************************************************************************************
Learn More Page Scroll
*******************************************************************************************************************************/
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

/******************************************************************************************************************************
Menu
*******************************************************************************************************************************/ 
(function() {

	var bodyEl = document.body,
		//content = document.querySelector( '.content-wrap' ),
		openbtn = document.getElementById( 'open-button' ),
		closebtn = document.getElementById( 'close-button' ),
		isOpen = true;

	function init() {
		initEvents();
	}

	function initEvents() {
		openbtn.addEventListener( 'click', toggleMenu );
		if( closebtn ) {
			closebtn.addEventListener( 'click', toggleMenu );
		}

		/* close the menu element if the target it´s not the menu element or one of its descendants..
		content.addEventListener( 'click', function(ev) {
			var target = ev.target;
			if( isOpen && target !== openbtn ) {
				toggleMenu();
			}
		} );*/
		
	}

	function toggleMenu() {
		if( isOpen ) {
			classie.remove( bodyEl, 'show-menu' );
		}
		else {
			classie.add( bodyEl, 'show-menu' );
		}
		isOpen = !isOpen;
	}

	//init();

	$(document).on('click.bs.dropdown.data-api', '.nclose', function (e) {
  		e.stopPropagation();
	});

	// $(document).on('click', 'div.select-business', function(e){
	// 	var defaultToggle = $(this).children('input').prop('checked');
	// 	var business = $(this).children('input').prop('id');
	// 	if(defaultToggle){
	// 		$('li[name="select-business"]').find('input[id!="'+ business + '"]').bootstrapToggle('off');
	// 		$.ajax({
	// 			method: 'POST',
	// 			dataType: 'json',
	// 			url: '/business/activate/',
	// 			data: {
	// 				'oper': 'set-business',
	// 				'business': business,
	// 				'csrfmiddlewaretoken': getCookie('csrftoken'),
	// 			},
	// 			success: function(response){
	// 				//table_admin.ajax.reload();
	// 				location.reload();
	// 			}
	// 		});
	// 	}else{
	// 		location.reload();
	// 	}
	// })
})();

$(document).ready(function() {
$(document).on('click', '.panel-heading a.clickable', function(e){
	var $this = $(this);
	if (!$this.hasClass('panel-collapsed')){
	  $this.parents('.panel').find(this.getAttribute('pnl')).slideUp();
	  $this.addClass('panel-collapsed');
	  $this.find('span.glyphicon-chevron-up').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
	} else {
	  $this.parents('.panel').find(this.getAttribute('pnl')).slideDown();
	  $this.removeClass('panel-collapsed');
	  $this.find('span.glyphicon-chevron-down').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
	}
  });
});


var datatable_language = {
    "sProcessing": "Procesando...",
    "sLengthMenu": "Mostrar _MENU_ registros",
    "sZeroRecords": "No se encontraron resultados",
    "sEmptyTable": "Ningún dato disponible en esta tabla",
    "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
    "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
    "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
    "sInfoPostFix": "",
    "sSearch": "Buscar:",
    "sUrl": "",
    "sInfoThousands": ",",
    "sLoadingRecords": "Cargando...",
    "oPaginate": {
        "sFirst": "Primero",
        "sLast": "Último",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
    },
    "oAria": {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
    }
}

function is_valid_key(key_value){
	list = [16,17,18,19,20,33,34,35,36,37,38,39,40,144,145,225]
	return !(list.includes(key_value))
}

function error_message(message){
    $.toast({
        heading: "Error",
        text: message,
        showHideTransition: "fade",
        icon: "error",
        position: "top-right",
    });
}

function success_message(message){
    $.toast({
        heading: gettext("Success"),
        text: message,
        showHideTransition: "fade",
        icon: "success",
        position: "top-right",
    });
}

function info_message(message){
	$.toast({
		heading: gettest('Success'),
		text: message,
		showHideTransition: 'fade',
		icon: 'info',
		position: 'top-right',
	});
}

var rfc_regex = /[A-Z&Ñ]{3,4}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]/
