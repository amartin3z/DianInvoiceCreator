errors = {
  # Validation errors cancellation cfd
  "201" : {
    "event":201,
    "message":u"UUID Cancelado exitosamente"
  },
  "202" : {
    "event":202,
    "message":u"UUID Previamente cancelado"
  },
  "203" : {
    "event":203,
    "message":u"UUID No corresponde el RFC del emisor y de quien solicita la cancelación"
  },
  "205" : {
    "event":205,
    "message":u"UUID No existe"
  },
  "206" : {
    "event":206,
    "message":u"Lista de UUIDs vacia"
  },
  "207" : {
    "event":207,
    "message":u"La lista enviada contiene UUIDS con formato invalido"
  },

  # Validation errors canceling and signing CFD
  "300":{"event":300,
    "message":u"El usuario o contraseña son inválidos"
  },
  "301" : {
    "event":301,
    "message":u"XML mal formado"
  },
  "302" : {
    "event":302,
    "message":u"Sello mal formado o inválido"
  },
  "303" : {
    "event":303,
    "message":u"Sello no corresponde a emisor"
  },
  "304" : {
    "event":304,
    "message":u"Certificado revocado o caduco"
  },
  "305" : {
    "event":305,
    "message":u"La fecha de emisión no esta dentro de la vigencia del CSD del Emisor"
  },
  "306" : {
    "event":306,
    "message":u"EL certificado no es de tipo CSD"
  },
  "307" : {
    "event":307,
    "message":u"El CFDI contiene un timbre previo"
  },
  "308" : {
    "event":308,
    "message":u"Certificado no expedido por el SAT"
  },

  "401" : {
    "event":401,
    "message":u"Fecha y hora de generación fuera de rango"
  },
  "402" : {
    "event":402,
    "message":u"RFC del emisor no se encuentra en el régimen de contribuyentes"
  },
  "403" : {
    "event":403,
    "message":u"La fecha de emisión no es posterior al 01 de enero 2012"
  },

  #primary sector taxpayer validation.
  "404" : {
    "event":404,
    "message":u"RFC del emisor no es del Sector Primario"
  },
  "405" : {
    "event":405,
    "message":u"RFC emisor no existe"
  },
  # Query service errors
  "601" : {
    "event":601,
    "message":u"La información para buscar el comprobante no es válida."
  },
  "602" : {
    "event":602,
    "message":u"Comprobante que se desea descargar no existe"
  },
  "603" : {
    "event":603,
    "message":u"El CFDI no contiene un timbre previo"
  },
  "604" : {
    "event" : 604,
    "message" : u"Hubo un error al crear el XML, contacte a soporte"
  },


  # Typing of errors
  "501" : {
    "event":501,
    "message":u"Autenticación no válida"
  },
  "502" : {
    "event":502,
    "message":u"Comprobante no encontrado en la ruta especificada. Ruta proporcionada"
  },
  "503" : {
    "event":503,
    "message":u"Metadatos no válidos. Hash: <Hash>, RFC Emisor: <RFC Emisor>, No.Certificado: <Numero Certificado>, UUID: <UUID, Fecha Timbrado:{Fecha Timbrado}"
  },
  "504" : {
    "event":504,
    "message":u"La estructura del comprobante recibido no es válida"
  },
  "505" : {
    "event":505,
    "message":u"Metadatos no correspondientes al CFDI"
  },
  "506" : {
    "event":506,
    "message":u"El Timbre proporcionado ya existe UUID: <UUID>"
  },
  "507" : {
    "event":507,
    "message":u"Comprobante recibido fue previamente cancelado"
  },
  "508" : {
    "event":508,
    "message":u"El Pac que envía es diferente al PAC que certificó"
  },
  "509" : {
    "event":509,
    "message":u"El CFDI no cuenta con los datos mínimos"
  },
  "510" : {
    "event":510,
    "message":u"Sello de certificación inválido"
  },
  "511" : {
    "event":511,
    "message":u"Sello del comprobante inválido"
  },
  "512" : {
    "event":512,
    "message":u"TFD no válido"
  },
  "513" : {
    "event":513,
    "message":u"Versión del estándar no vigente"
  },
  "514" : {
    "event":514,
    "message":u"Comprobante con envío extemporáneo por vigencia de versión"
  },
  "701" : {
    "event":701,
    "message":u"The Reseller User is Suspended and can't create Invoices"
  },
  "702" : {
    "event":702,
    "message":u"RFC Emisor no registrado en la cuenta"
  },
  "703" : {
    "event":703,
    "message":u"Usuario Suspendido"
  },
  "704" : {
    "event":704,
    "message":u"Error con la contraseña de la llave Privada"
  },
  "705" : {
    "event":705,
    "message":u"XML Estructura inválida"
  },
  "706" : {
    "event":706,
    "message":u"Socio de Negocios Inválido"
  },
  "707" : {
    "event":707,
    "message":u"Timbre Existente"
  },
  "709" : {
    "event":709,
    "message":u"SelloSat no pudo ser creado"
  },
  "710" : {
    "event":710,
    "message":u"Las cantidades no concuerdan"
  },
  "711" : {
    "event":711,
    "message":u"Error con el certificado"
  },
  "712" : {
    "event":712,
    "message":u"El atributo noCertificado no corresponde al certificado"
  },
  "713" : {
    "event":713,
    "message":u"RFC Emisor no corresponde a la cuenta"
  },
  "714" : {
    "event":714,
    "message":u"Límite mensual alcanzado"
  },
  "715" : {
    "event" : 715,
    "message" : u"Error al crear XML de consulta Sector Primario"
  },
  "716" : {
    "event" : 716,
    "message" : u"Firma Inválida - Consulta Sector Primario"
  },
  "717" : {
    "event": 717,
    "message" : u"Error al generar la firma del XML",
  },
  "718" : {
    "event": 718,
    "message" : u"Timbres agotados, por favor, contacte a su proveedor.",
  },
  "719" : {
    "event": 719,
    "message" : u"RFC del Emisor no corresponde al noCertificado",
  },
  "720" : {
    "event": 720,
    "message" : u"RFC del Emisor no tiene Certificado Activo",
  },
  "721" : {
    "event": 721,
    "message" : u"RFC emisor del comprobante no corresponde al de la cuenta.",
  },
  #Errors to beat wsdl
  "722" : {
    "event": 722,
    "message" : u"Json no valido",
  },
  "723" : {
    "event": 723,
    "message" : u"Error en la generacion del sello",
  },
  "724" : {
    "event": 724,
    "message" : u"CSV formato no valido",
  },
  "725" : {
    "event": 725,
    "message" : u"Error en la generacion del reporte",
  },
  "726": {
    "event": 726,
    "message": u"Prefijo no permitido, por favor verifique la documentación."
  },
  "727": {
    "event": 727,
    "message": u"El archivo enviado no es base64 o no se pudieron obtener los bytes."
  },
  "728": {
    "event": 728,
    "message": u"El archivo enviado no corresponde a un archivo zip o gzip."
  },
  "729": {
    "event": 729,
    "message": u"El archivo zip no contiene un solo archivo."
  },
  "730": {
    "event": 730,
    "message": u"Id de proceso no encontrado."
  },
  "731": {
    "event": 731,
    "message": u"El id de proceso se encuentra en ejecución."
  },
  "732": {
    "event": 732,
    "message": u"El id de proceso excedió el tiempo límite de ejecución (TIMEOUT)."
  },
  "733": {
    "event": 733,
    "message": u"Hubo un error con el id de proceso (FAILURE)."
  },
  "734": {
    "event": 734,
    "message": u"El parametro ctype debe ser zip o gzip."
  },
  "735": {
    "event": 735,
    "message": u"Error no controlado."
  },
  "736": {
    "event": 736,
    "message": u"Folio Duplicado."
  },
  # Validaciones Extra
  'ex140' : {
    "event": 'ex140',
    "message" : u"Atributo metodoDePago no pertenece al catálogo vigente.",
  },

  # Complemento INE
  'INE180' : {
    "event": 'INE180',
    "message" : u"Atributo TipoProceso: con valor {Ordinario}, debe existir el atributo ine:TipoComite",
  },
  'INE181' : {
    "event": 'INE181',
    "message" : u"Atributo TipoProceso con valor {Precampaña} o el valor {Campaña}, debe existir al menos un elemento Entidad:Ambito",
  },
  'INE182' : {
    "event": 'INE182',
    "message" : u"Atributo TipoProceso con valor {Precampaña} o el valor {Campaña}, no debe existir ine:TipoComite",
  },
  'INE183' : {
    "event": 'INE183',
    "message" : u"Atributo TipoProceso con valor {Precampaña} o el valor {Campaña}, no debe existir ine:IdContabilidad",
  },
  'INE184' : {
    "event": 'INE184',
    "message" : u"Atributo TipoComite con valor {Ejecutivo Nacional}, no debe existir ningún elemento ine:Entidad",
  },
  'INE185' : {
    "event": 'INE185',
    "message" : u"Atributo TipoComite con valor {Ejecutivo Estatal}, no debe existir ine:IdContabilidad",
  },
  'INE186' : {
    "event": 'INE186',
    "message" : u"Atributo TipoComite con valor {Ejecutivo Estatal}, debe existir al menos un elemento ine:Entidad y en ningún caso debe existir ine:Entidad:Ambito",
  },
  'INE187' : {
    "event": 'INE187',
    "message" : u"Elemento Entidad, no se debe repetir la combinación de ine:Entidad:ClaveEntidad con ine:Entidad:Ambito",
  },
  'INE188' : {
    "event": 'INE188',
    "message" : u"No se pueden seleccionar las claves  NAC, CR1, CR2, CR3, CR4 y CR5 por que el Ambito es Local.",
  },
  'INE999' : {
    "event": 'INE999',
    "message" : u"Error no clasificado.",
  },

  # Complemento ComercioExterior
  'cce140' : {
    "event": 'cce140',
    "message" : u"El valor del atributo cfdi:Comprobante:version debe ser 3.2.",
  },
  'cce141' : {
    "event": 'cce141',
    "message" : u"cfdi:Comprobante:subTotal, Debe ser igual a la suma de los atributos [importe] por cada [Concepto] ubicado en el nodo cfdi:Comprobante:Conceptos",
  },
  'cce142' : {
    "event": 'cce142',
    "message" : u"cfdi:Comprobante:Moneda, Es requerido para este complemento.",
  },
  'cce143' : {
    "event": 'cce143',
    "message" : u"cfdi:Comprobante:Moneda, Debe contener un valor del catálogo c_Moneda",
  },
  'cce144' : {
    "event": 'cce144',
    "message" : u"cfdi:Comprobante:TipoCambio, Es requerido para este complemento",
  },
  'cce145' : {
    "event": 'cce145',
    "message" : u"cfdi:Comprobante:TipoCambio, Debe cumplir con el patrón [0-9]{1,14}(.([0-9]{1,6}))?",
  },
  'cce146' : {
    "event": 'cce146',
    "message" : u"El valor del atributo cfdi:Comprobante:tipoDeComprobante debe ser {ingreso} cuando el valor del atributo cce:ComercioExterior:TipoOperacion sea {A} ó {2}.",
  },
  'cce147' : {
    "event": 'cce147',
    "message" : u"cfdi:Comprobante:total, Debe ser igual a la suma del cfdi:Comprobante:subTotal, menos el cfdi:Comprobante:Descuento, más los impuestos trasladados (cfdi:Comprobante:Impuestos:totalImpuestosTrasladados), menos los impuestos retenidos (cfdi:Comprobante:Impuestos:totalImpuestosRetenidos)",
  },
  'cce148' : {
    "event": 'cce148',
    "message" : u"El atributo [pais] de los nodos DomicilioFiscal y/o ExpedidoEn debe contener la clave {MEX}.",
  },
  'cce149' : {
    "event": 'cce149',
    "message" : u"El atributo [estado] de los nodos DomicilioFiscal y/o ExpedidoEn debe contener una clave del catálogo c_Estado donde la columna c_Pais tenga el valor {MEX}.",
  },
  'cce150' : {
    "event": 'cce150',
    "message" : u"El atributo [municipio] de los nodos DomicilioFiscal y/o ExpedidoEn debe contener una clave del catálogo c_Municipio donde la columna c_Estado sea igual a la clave registrada en el atributo [estado].",
  },
  'cce151' : {
    "event": 'cce151',
    "message" : u"El atributo [localidad] de los nodos DomicilioFiscal y/o ExpedidoEn debe contener una clave del catálogo c_Localidad donde la columna c_Estado sea igual a la clave registrada en el atributo [estado].",
  },
  'cce152' : {
    "event": 'cce152',
    "message" : u"cfdi:Comprobante:Emisor:DomicilioFiscal|ExpedidoEn, El atributo [colonia] debe contener una clave del catálogo de c_Colonia, donde la columna c_CP debe debe ser igual a la clave registrada en el atributo [codigoPostal]. Si el atributo no tiene una clave numérica de cuatro posiciones, no se valida el contenido.",
  },
  'cce153' : {
    "event": 'cce153',
    "message" : u"El atributo [codigoPostal] de los nodos DomicilioFiscal y/o ExpedidoEn debe contener una clave del catálogo c_CP, donde la columna clave c_Estado sea igual a la clave registrada en el atributo [estado], la columna clave c_Municipio",
  },
  'cce154' : {
    "event": 'cce154',
    "message" : u"cfdi:Comprobante:Receptor:rfc, Debe tener el valor {XEXX010101000} ",
  },
  'cce155' : {
    "event": 'cce155',
    "message" : u"El atributo cfdi:Comprobante:Receptor:nombre es requerido.",
  },
  'cce156' : {
    "event": 'cce156',
    "message" : u"El nodo cfdi:Comprobante:Receptor:Domicilio es requerido.",
  },
  'cce157' : {
    "event": 'cce157',
    "message" : u"cfdi:Comprobante:Receptor:Domicilio:pais, La clave en el atributo [pais] debe existir en el catálogo c_pais y debe ser diferente de {MEX}.",
  },
  'cce158' : {
    "event": 'cce158',
    "message" : u"El atributo [estado] del nodo cfdi:Comprobante:Receptor:Domicilio debe contener una clave del catálogo c_Estado donde la columna c_Pais sea igual al valor registrado en el atributo [pais], siempre y cuando el valor del atributo [pais]",
  },
  'cce159' : {
    "event": 'cce159',
    "message" : u"El atributo [codigoPostal] del nodo cfdi:Comprobante:Receptor:Domicilio debe cumplir con el patrón especificado en el catálogo c_Pais para el país indicado en el atributo [pais].",
  },
  'cce160' : {
    "event": 'cce160',
    "message" : u"El atributo [codigoPostal] del nodo cfdi:Comprobante:Receptor:Domicilio es requerido.",
  },
  'cce161' : {
    "event": 'cce161',
    "message" : u"Si la clave registrada es {A} en el atributo cce:ComercioExterior:TipoOperacion, no deben existir los atributos [ClaveDePedimento], [CertificadoOrigen], [NumCertificadoOrigen], [NumExportadorConfiable], [Incoterm], [Subdivision],",
  },
  'cce162' : {
    "event": 'cce162',
    "message" : u"Si la clave registrada es {1} ó {2} en el atributo cce:ComercioExterior:TipoOperacion, deben existir los atributos [ClaveDePedimento], [CertificadoOrigen], [Incoterm], [Subdivision], [TipoCambioUSD] y [TotalUSD], así como el nodo",
  },
  'cce163' : {
    "event": 'cce163',
    "message" : u"Si el valor del atributo cce:ComercioExterior:CertificadoOrigen es cero, no debe registrarse el atributo [NumCertificadoOrigen].",
  },
  'cce164' : {
    "event": 'cce164',
    "message" : u"El atributo cce:ComercioExterior:TotalUSD no coincide con la suma de los valores del atributo [ValorDolares] de las mercancías. ",
  },
  'cce165' : {
    "event": 'cce165',
    "message" : u"El atributo cce:ComercioExterior:TotalUSD no tiene dos decimales.",
  },
  'cce166' : {
    "event": 'cce166',
    "message" : u"El atributo cce:ComercioExterior:Emisor:Curp no debe existir cuando la longitud del valor del atributo [rfc] del nodo cfdi:Comprobante:Emisor es de longitud 12. ",
  },
  'cce167' : {
    "event": 'cce167',
    "message" : u"El valor del atributo cce:ComercioExterior:Receptor:NumRegIdTrib no es válido.",
  },
  'cce168' : {
    "event": 'cce168',
    "message" : u"Debe existir al menos uno de los atributos [NumRegIdTrib] o [Rfc] en el nodo cce:ComercioExterior:Destinartario.",
  },
  'cce169' : {
    "event": 'cce169',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:NumRegIdTrib no es válido.",
  },
  'cce170' : {
    "event": 'cce170',
    "message" : u"El atributo cce:ComercioExterior:Destinatario:Rfc no debe ser rfc genérico {XAXX010101000} ni {XEXX010101000}.",
  },
  'cce171' : {
    "event": 'cce171',
    "message" : u"El atributo cce:ComercioExterior:Destinatario:Domicilio:Colonia es de captura libre si la clave de país es diferente de {MEX}.",
  },
  'cce172' : {
    "event": 'cce172',
    "message" : u"El atributo cce:ComercioExterior:Destinatario:Domicilio:Colonia no tiene uno de los valores permitidos.",
  },
  'cce173' : {
    "event": 'cce173',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:Colonia no se debe validar si no contiene una cadena numérica de cuatro posiciones. ",
  },
  'cce174' : {
    "event": 'cce174',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:Localidad debe contener una clave del catálogo de localidades (c_Localidad), donde la columna c_estado sea igual a la clave registrada en el atributo [Estado] cuando la",
  },
  'cce175' : {
    "event": 'cce175',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:Municipio debe contener una clave del catálogo de municipios (c_Municipio), donde la columna c_estado sea igual a la clave registrada en el atributo [Estado].",
  },
  'cce176' : {
    "event": 'cce176',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:Estado debe contener una clave del catálogo de estados c_Estado, donde la columna c_País sea igual a la clave de país registrada en el atributo [Pais] cuando la clave es",
  },
  'cce177' : {
    "event": 'cce177',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:CodigoPostal debe cumplir con el patrón especificado en el catálogo de países publicado en el portal del SAT para cuando la clave de país sea distinta de {MEX}. ",
  },
  'cce178' : {
    "event": 'cce178',
    "message" : u"El valor del atributo cce:ComercioExterior:Destinatario:Domicilio:CodigoPostal cuando la clave de país es {MEX} debe existir en el catálogo de códigos postales, donde la columna c_Estado sea igual a la clave registrada en el atributo",
  },
  'cce179' : {
    "event": 'cce179',
    "message" : u"Todos los conceptos registrados en el elemento cfdi:Comprobante:Conceptos deben tener registrado el atributo cfdi:Comprobante:Conceptos:Concepto:noIdentificacion.",
  },
  'cce180' : {
    "event": 'cce180',
    "message" : u"El valor del atributo cfdi:Comprobante:Conceptos:Concepto:noIdentificacion no se debe repetir en todos los conceptos registrados en el elemento cfdi:Comprobante:Conceptos.",
  },
  'cce181' : {
    "event": 'cce181',
    "message" : u"Por cada concepto registrado en el elemento cfdi:Comprobante:Conceptos, debe existir una mercancía en el complemento cce:ComercioExterior, donde el atributo cce:ComercioExterior:Mercancias:Mercancia:NoIdentificacion sea igual",
  },
  'cce182' : {
    "event": 'cce182',
    "message" : u"Si no existe el atributo  cce:ComercioExterior:Mercancias:Mercancia:CantidadAduana entonces el valor del atributo cfdi:Comprobante:Conceptos:Concepto:cantidad debe tener como valor mínimo incluyente {0.001} y debe cumplir con",
  },
  'cce183' : {
    "event": 'cce183',
    "message" : u"Si no existe el atributo  cce:ComercioExterior:Mercancias:Mercancia:CantidadAduana entonces el valor del atributo cfdi:Comprobante:Conceptos:Concepto:unidad debe tener un valor del catálogo c_UnidadMedidaAduana.",
  },
  'cce184' : {
    "event": 'cce184',
    "message" : u"Si no existe el atributo  cce:ComercioExterior:Mercancias:Mercancia:CantidadAduana entonces el valor del atributo cfdi:Comprobante:Conceptos:Concepto:valorUnitario debe tener como valor mínimo incluyente {0.0001}, debe cumplir",
  },
  'cce185' : {
    "event": 'cce185',
    "message" : u"El valor del atributo cfdi:Comprobante:Conceptos:Concepto:importe de cada concepto registrado, debe ser igual al valor del atributo cfdi:Comprobante:Conceptos:Concepto:cantidad multiplicado por el valor del atributo",
  },
  'cce186' : {
    "event": 'cce186',
    "message" : u"No debe existir el atributo cce:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria cuando el atributo cce:ComercioExterior:Mercancias:Mercancia:UnidadAduana o el atributo cfdi:Comprobante:Conceptos:Concepto:unidad",
  },
  'cce187' : {
    "event": 'cce187',
    "message" : u"El valor del atributo cfdi:Comprobante:descuento debe ser mayor o igual  a la suma del atributo cce:ComercioExterior:Mercancias:Mercancia:ValorDolares de todos los elementos Mercancia que tengan la fracción arancelaria",
  },
  'cce188' : {
    "event": 'cce188',
    "message" : u"Si se registra alguno de los atributos CantidadAduana, UnidadAduana o ValorUnitarioAduana, entonces deben existir los tres.",
  },
  'cce189' : {
    "event": 'cce189',
    "message" : u"Existe uno o más elementos cce:ComercioExterior:Mercancias:Mercancia que no tienen los atributos CantidadAduana, UnidadAduana y ValorUnitarioAduana.",
  },
  'cce190' : {
    "event": 'cce190',
    "message" : u"El valor del atributo cce:ComercioExterior:Mercancias:Mercancia:ValorUnitarioAduana debe ser mayor que cero cuando el valor del atributo cce:ComercioExterior:Mercancias:Mercancia:UnidadAduana es distinto de {99} que corresponde a los servicios.",
  },
  'cce191' : {
    "event": 'cce191',
    "message" : u"El valor del atributo ComercioExterior:Mercancias:Mercancia:ValorDolares no cumple con los valores permitidos. ",
  },
  # Complemento Nomina 1.2
  'nom101': {
    'event': 'nom101',
    'message': u'El atributo fecha no cumple con el patrón requerido. (20[1-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]).'
  },
  'nom102': {
    'event': 'nom102',
    'message': u'El atributo metodoDePago debe tener el valor "NA".'
  },
  'nom103': {
    'event': 'nom103',
    'message': u'El atributo noCertificado no cumple con el patrón requerido. ([0-9]{20})'
  },
  'nom104': {
    'event': 'nom104',
    'message': u'El atributo Moneda debe tener el valor MXN.'
  },
  'nom105': {
    'event': 'nom105',
    'message': u'El atributo TipoCambio no tiene el valor = "1". (Se debe registrar el Valor "1" sin decimales.)'
  },
  'nom106': {
    'event': 'nom106',
    'message': u'El valor del atributo subTotal no coincide con la suma de Nomina12:TotalPercepciones más Nomina12:TotalOtrosPagos.'
  },
  'nom107': {
    'event': 'nom107',
    'message': u'El valor de descuento no es igual a Nomina12:TotalDeducciones.'
  },
  'nom108': {
    'event': 'nom108',
    'message': u'El atributo total no cumple con el patrón requerido. ([0-9]{1,18}(.[0-9]{1,2})?)'
  },
  'nom109': {
    'event': 'nom109',
    'message': u'El valor del atributo total no coincide con la suma Nomina12:TotalPercepciones más Nomina12:TotalOtrosPagos menos Nomina12:TotalDeducciones.'
  },
  'nom110': {
    'event': 'nom110',
    'message': u'El atributo tipoDeComprobante no tiene el valor = “egreso”.'
  },
  'nom111': {
    'event': 'nom111',
    'message': u'El valor del atributo LugarExpedicion no cumple con un valor del catálogo c_CodigoPostal.'
  },
  'nom112': {
    'event': 'nom112',
    'message': u'Los atributos motivoDescuento, NumCtaPago, condicionesDePago, SerieFolioFiscalOrig, FechaFolioFiscalOrig, MontoFolioFiscalOrig: no deben existir.'
  },
  'nom113': {
    'event': 'nom113',
    'message': u'El atributo Nomina12:Emisor:Curp. no aplica para persona moral.'
  },
  'nom114': {
    'event': 'nom114',
    'message': u'El atributo Nomina12:Emisor:Curp. Debe aplicar para persona física.'
  },
  'nom115': {
    'event': 'nom115',
    'message': u'El nodo Subcontratacion se debe registrar.'
  },
  'nom116': {
    'event': 'nom116',
    'message': u'Los elementos cfdi:Comprobante.Emisor.DomicilioFiscal y ExpedidoEn: no deben existir.'
  },
  'nom117': {
    'event': 'nom117',
    'message': u'Solo debe existir un solo nodo RegimenFiscal.'
  },
  'nom118': {
    'event': 'nom118',
    'message': u'El valor del atributo Regimen no cumple con un valor del catálogo c_RegimenFiscal.'
  },
  'nom119': {
    'event': 'nom119',
    'message': 'El atributo Regimen no cumple con un valor de acuerdo al tipo de persona moral.'
  },
  'nom120': {
    'event': 'nom120',
    'message': 'El atributo Regimen no cumple con un valor de acuerdo al tipo de persona fisica.'
  },
  'nom121': {
    'event': 'nom121',
    'message': u'El atributo cfdi:Comprobante.Receptor.rfc debe ser persona fisica (13 caracteres).'
  },
  'nom122': {
    'event': 'nom122',
    'message': u'El atributo cfdi:Comprobante.Receptor.rfc no es válido segun la lista de RFC inscritos no cancelados en el SAT (l_RFC).'
  },
  'nom123': {
    'event': 'nom123',
    'message': u'El nodo Receptor:Domicilio no debe existir.'
  },
  'nom124': {
    'event': 'nom124',
    'message': u'El nodo concepto solo debe existir uno, sin elementos hijo.'
  },
  'nom125': {
    'event': 'nom125',
    'message': u'El atributo Concepto:noIdentificacion no debe existir.'
  },
  'nom126': {
    'event': 'nom126',
    'message': u'El atributo cfdi:Comprobante.Conceptos.Concepto.cantidad no tiene el valor =  “1”.'
  },
  'nom127': {
    'event': 'nom127',
    'message': u'El atributo cfdi:Comprobante.Conceptos.Concepto.unidad no tiene el valor =  “ACT”.'
  },
  'nom128': {
    'event': 'nom128',
    'message': u'El atributo cfdi:Comprobante.Conceptos.Concepto.descripcion, no tiene el valor “Pago de nómina”.'
  },
  'nom129': {
    'event': 'nom129',
    'message': u'El valor del atributo.cfdi:Comprobante.Conceptos.Concepto.valorUnitario no coincide con la suma TotalPercepciones más TotalOtrosPagos.'
  },
  'nom130': {
    'event': 'nom130',
    'message': u'El valor del atributo.cfdi:Comprobante.Conceptos.Concepto.Importe no coincide con la suma TotalPercepciones más TotalOtrosPagos.'
  },
  'nom131': {
    'event': 'nom131',
    'message': u'El nodo cfdi:Comprobante.Impuestos no cumple la estructura.'
  },
  'nom132': {
    'event': 'nom132',
    'message': u'El atributo Moneda no tiene el valor =  “MXN”.'
  },
  'nom133': {
    'event': 'nom133',
    'message': u'El atributo FormaPago no tiene el valor =  99.'
  },
  'nom134': {
    'event': 'nom134',
    'message': u'El atributo TipoDeComprobante no tiene el valor =  N.'
  },
  'nom135': {
    'event': 'nom135',
    'message': u'El atributo Nomina12:Emisor:Curp, no aplica para persona moral.'
  },
  'nom136': {
    'event': 'nom136',
    'message': u'El atributo Nomina12:Emisor:Curp, debe aplicar para persona fisica.'
  },
  'nom137': {
    'event': 'nom137',
    'message': u'El atributo Comprobante.Receptor.rfc, debe ser de longitud 13.'
  },
  'nom138': {
    'event': 'nom138',
    'message': u'El atributo Comprobante.Receptor.rfc, no está en la lista de RFC inscritos no cancelados en el SAT (l_RFC).'
  },
  'nom139': {
    'event': 'nom139',
    'message': u'El nodo Comprobante.Conceptos.Concepto, Solo puede registrarse un nodo concepto, sin elementos hijo.'
  },
  'nom140': {
    'event': 'nom140',
    'message': u'El atributo Comprobante.Conceptos.Concepto,ClaveProdServ no tiene el valor =  “84111505”.'
  },
  'nom141': {
    'event': 'nom141',
    'message': u'El atributo Comprobante.Conceptos.Concepto.NoIdentificacion, no debe existir.'
  },
  'nom142': {
    'event': 'nom142',
    'message': u'El atributo Comprobante.Conceptos.Concepto,Cantidad no tiene el valor =  “1”.'
  },
  'nom143': {
    'event': 'nom143',
    'message': u'El atributo Comprobante.Conceptos.Concepto,ClaveUnidad no tiene el valor =  “ACT”.'
  },
  'nom144': {
    'event': 'nom144',
    'message': u'El atributo Comprobante.Conceptos.Concepto,Unidad, no debe existir.'
  },
  'nom145': {
    'event': 'nom145',
    'message': u'El atributo Comprobante.Conceptos.Concepto,Descripcion no tiene el valor =  “Pago de nómina”.'
  },
  'nom146': {
    'event': 'nom146',
    'message': u'El valor del atributo Comprobante.Conceptos.Concepto,ValorUnitario no coincide con la suma TotalPercepciones más TotalOtrosPagos.'
  },
  'nom147': {
    'event': 'nom147',
    'message': u'El valor del atributo Comprobante.Conceptos.Concepto,Importe no coincide con la suma TotalPercepciones más TotalOtrosPagos.'
  },
  'nom148': {
    'event': 'nom148',
    'message': u'El valor del atributo Comprobante.Conceptos.Concepto,Descuento no es igual a el valor del campo Nomina12:TotalDeducciones.'
  },
  'nom149': {
    'event': 'nom149',
    'message': u'El nodo Comprobante.Impuestos, no debe existir.'
  },
  'nom150': {
    'event': 'nom150',
    'message': u'El nodo Nomina no se puede utilizar dentro del elemento ComplementoConcepto. '
  },
  'nom151': {
    'event': 'nom151',
    'message': u'El nodo Nomina no tiene TotalPercepciones y/o TotalOtrosPagos.'
  },
  'nom152': {
    'event': 'nom152',
    'message': u'El valor del atributo Nomina.TipoNomina no cumple con un valor del catálogo c_TipoNomina.'
  },
  'nom153': {
    'event': 'nom153',
    'message': u'El valor del atributo tipo de periodicidad es 99.'
  },
  'nom154': {
    'event': 'nom154',
    'message': u'El valor del atributo tipo de periodicidad no es 99.'
  },
  'nom155': {
    'event': 'nom155',
    'message': u'El valor del atributo FechaInicialPago no es menor o igual al valor del atributo FechaFinalPago.'
  },
  'nom156': {
    'event': 'nom156',
    'message': u'El atributo Nomina.TotalPercepciones, no debe existir.'
  },
  'nom157': {
    'event': 'nom157',
    'message': u'El valor del atributo Nomina.TotalPercepciones no coincide con la suma TotalSueldos más TotalSeparacionIndemnizacion más TotalJubilacionPensionRetiro del  nodo Percepciones.'
  },
  'nom158': {
    'event': 'nom158',
    'message': u'El atributo Nomina.TotalDeducciones, no debe existir.'
  },
  'nom159': {
    'event': 'nom159',
    'message': u'El valor del atributo Nomina.TotalDeducciones no coincide con la suma de los atributos TotalOtrasDeducciones más TotalImpuestosRetenidos del elemento Deducciones.'
  },
  'nom160': {
    'event': 'nom160',
    'message': u'El valor del atributo Nomina.TotalOtrosPagos no está registrado o  no coincide con la suma de los atributos Importe de los nodos nomina12:OtrosPagos:OtroPago.'
  },
  'nom161': {
    'event': 'nom161',
    'message': u'El atributo Nomina.Emisor.RfcPatronOrigen no está inscrito en el SAT (l_RFC).'
  },
  'nom162': {
    'event': 'nom162',
    'message': u'El atributo Nomina.Emisor.RegistroPatronal se debe registrar.'
  },
  'nom163': {
    'event': 'nom163',
    'message': u'El atributo Nomina.Emisor.RegistroPatronal  no se debe registrar.'
  },
  'nom164': {
    'event': 'nom164',
    'message': u'Los atributos nomina12:Receptor: NumSeguridadSocial,  nomina12:Receptor:FechaInicioRelLaboral, nomina12:Receptor:Antigüedad,  nomina12:Receptor:RiesgoPuesto y nomina12:Receptor:SalarioDiarioIntegrado. deben existir.'
  },
  'nom164.A': {
    'event': 'nom164',
    'message': u'Los atributos nomina12:Receptor: NumSeguridadSocial,  nomina12:Receptor:FechaInicioRelLaboral, nomina12:Receptor:Antigüedad,  nomina12:Receptor:RiesgoPuesto y nomina12:Receptor:SalarioDiarioIntegrado. NO deben existir.'
  },
  'nom165': {
    'event': 'nom165',
    'message': u'El nodo Nomina.Emisor.EntidadSNCF debe existir.'
  },
  'nom166': {
    'event': 'nom166',
    'message': u'El nodo Nomina.Emisor.EntidadSNCF no debe existir.'
  },
  'nom167': {
    'event': 'nom167',
    'message': u'El valor del atributo Nomina.Emisor.EntidadSNCF.OrigenRecurso no cumple con un valor del catálogo c_OrigenRecurso.'
  },
  'nom168': {
    'event': 'nom168',
    'message': u'El atributo Nomina.Emisor.EntidadSNCF.MontoRecursoPropio debe existir.'
  },
  'nom169': {
    'event': 'nom169',
    'message': u'El atributo Nomina.Emisor.EntidadSNCF.MontoRecursoPropio no debe existir.'
  },
  'nom170': {
    'event': 'nom170',
    'message': u'El valor del atributo Nomina.Emisor.EntidadSNCF.MontoRecursoPropio no es menor a la suma de los valores de los atributos TotalPercepciones y TotalOtrosPagos. '
  },
  'nom171': {
    'event': 'nom171',
    'message': u'El valor del atributo Nomina.Receptor.TipoContrato no cumple con un valor del catálogo c_TipoContrato.'
  },
  'nom172': {
    'event': 'nom172',
    'message': u'El valor del atributo Nomina.Receptor.TipoJornada no cumple con un valor del catálogo c_TipoJornada.'
  },
  'nom173': {
    'event': 'nom173',
    'message': u'El valor del atributo Nomina.Receptor.FechaInicioRelLaboral no es menor o igual al atributo a FechaFinalPago.'
  },
  'nom174': {
    'event': 'nom174',
    'message': u'El valor numérico del atributo Nomina.Receptor.Antigüedad no es menor o igual al cociente de (la suma del número de días transcurridos entre la FechaInicioRelLaboral y la FechaFinalPago más uno) dividido entre siete.'
  },
  'nom175': {
    'event': 'nom175',
    'message': u'El valor del atributo Nomina.Receptor.Antigüedad. no cumple con el número de años, meses y días transcurridos entre la FechaInicioRelLaboral y la FechaFinalPago.'
  },
  'nom176': {
    'event': 'nom176',
    'message': u'El valor del atributo Nomina.Receptor.TipoRegimen no cumple con un valor del catálogo c_TipoRegimen.'
  },
  'nom177': {
    'event': 'nom177',
    'message': u'El atributo Nomina.Receptor.TipoRegimen no es 02, 03 ó 04.'
  },
  'nom178': {
    'event': 'nom178',
    'message': u'El atributo Nomina.Receptor.TipoRegimen no está entre 05 a 99.'
  },
  'nom179': {
    'event': 'nom179',
    'message': u'El valor del atributo Nomina.Receptor.RiesgoPuesto no cumple con un valor del catálogo c_RiesgoPuesto.'
  },
  'nom180': {
    'event': 'nom180',
    'message': u'El valor del atributo Nomina.Receptor.PeriodicidadPago no cumple con un valor del catálogo c_PeriodicidadPago.'
  },
  'nom181': {
    'event': 'nom181',
    'message': u'El valor del atributo Nomina.Receptor.Banco no cumple con un valor del catálogo c_Banco.'
  },
  'nom182': {
    'event': 'nom182',
    'message': u'El atributo CuentaBancaria no cumple con la longitud de 10, 11, 16 ó 18 posiciones.'
  },
  'nom183': {
    'event': 'nom183',
    'message': u'El atributo Banco no debe existir.'
  },
  'nom184': {
    'event': 'nom184',
    'message': u'El dígito de control del atributo CLABE no es correcto.'
  },
  'nom185': {
    'event': 'nom185',
    'message': u'El atributo Banco debe existir.'
  },
  'nom186': {
    'event': 'nom186',
    'message': u'El valor del atributo ClaveEntFed no cumple con un valor del catálogo c_Estado.'
  },
  'nom187': {
    'event': 'nom187',
    'message': u'El valor del atributo Nomina.Receptor.SubContratacion.RfcLabora no está en la lista de RFC (l_RFC).'
  },
  'nom188': {
    'event': 'nom188',
    'message': u'La suma de los valores registrados en el atributo Nomina.Receptor.SubContratacion.PorcentajeTiempo no es igual a 100.'
  },
  'nom189': {
    'event': 'nom189',
    'message': u'La suma de los valores de los atributos TotalSueldos más TotalSeparacionIndemnizacion más TotalJubilacionPensionRetiro no es igual a la suma de los valores de los atributos TotalGravado más TotalExento.'
  },
  'nom190': {
    'event': 'nom190',
    'message': u'El valor del atributo Nomina.Percepciones.TotalSueldos , no es igual a la suma de los atributos ImporteGravado e ImporteExento donde la clave expresada en el atributo TipoPercepcion es distinta de 022 Prima por Antigüedad, 023 Pagos por separación, 025 Indemnizaciones, 039 Jubilaciones, pensiones o haberes de retiro en una exhibición y 044 Jubilaciones, pensiones o haberes de retiro en parcialidades.'
  },
  'nom191': {
    'event': 'nom191',
    'message': u'El valor del atributo Nomina.Percepciones.TotalSeparacionIndemnizacion, no es igual a la suma de los atributos ImporteGravado e ImporteExento donde la clave en el atributo TipoPercepcion es igual a 022 Prima por Antigüedad, 023 Pagos por separación ó 025 Indemnizaciones.'
  },
  'nom192': {
    'event': 'nom192',
    'message': u'El valor del atributo Nomina.Percepciones.TotalJubilacionPensionRetiro, no es igual a la suma de los atributos ImporteGravado e importeExento donde la clave expresada en el atributo TipoPercepcion es igual a 039(Jubilaciones, pensiones o haberes de retiro en una exhibición)  ó 044 (Jubilaciones, pensiones o haberes de retiro en parcialidades).'
  },
  'nom193': {
    'event': 'nom193',
    'message': u'El valor del atributo Nomina.Percepciones.TotalGravado, no es igual a la suma de los atributos ImporteGravado de los nodos Percepcion.'
  },
  'nom194': {
    'event': 'nom194',
    'message': u'El valor del atributo Nomina.Percepciones.TotalExento, debe ser igual a la suma de los atributos ImporteExento de los nodos Percepcion.'
  },
  'nom195': {
    'event': 'nom195',
    'message': u'La suma de los importes de los atributos ImporteGravado e ImporteExento no es mayor que cero.'
  },
  'nom196': {
    'event': 'nom196',
    'message': u'El valor del atributo Nomina.Percepciones.Percepcion.TipoPercepcion no cumple con un valor del catálogo c_TipoPercepcion.'
  },
  'nom197': {
    'event': 'nom197',
    'message': u'TotalSueldos, debe existir. Ya que la clave expresada en TipoPercepcion es distinta de 022, 023, 025, 039 y 044.'
  },
  'nom198': {
    'event': 'nom198',
    'message': u'TotalSeparacionIndemnizacion y el elemento SeparacionIndemnizacion, debe existir. Ya que la clave expresada en TipoPercepcion es 022 ó 023 ó 025.'
  },
  'nom199': {
    'event': 'nom199',
    'message': u'TotalJubilacionPensionRetiro y el elemento JubilacionPensionRetiro debe existir,  ya que la clave expresada en el atributo TipoPercepcion es 039 ó 044,'
  },
  'nom200': {
    'event': 'nom200',
    'message': u'TotalUnaExhibicion debe existir y no deben existir TotalParcialidad, MontoDiario. Ya que la clave expresada en el atributo TipoPercepcion es 039.'
  },
  'nom201': {
    'event': 'nom201',
    'message': u'TotalUnaExhibicion no debe existir y deben existir TotalParcialidad, MontoDiario. Ya que la clave expresada en el atributo TipoPercepcion es 044.'
  },
  'nom202': {
    'event': 'nom202',
    'message': u'El elemento AccionesOTitulos debe existir. Ya que la clave expresada en el atributo TipoPercepcion es 045.'
  },
  'nom203': {
    'event': 'nom203',
    'message': u'El elemento AccionesOTitulos no debe existir. Ya que la clave expresada en el atributo TipoPercepcion no es 045.'
  },
  'nom204': {
    'event': 'nom204',
    'message': u'El elemento HorasExtra, debe existir. Ya que la clave expresada en el atributo TipoPercepcion es 019.'
  },
  'nom205': {
    'event': 'nom205',
    'message': u'El elemento HorasExtra, no debe existir. Ya que la clave expresada en el atributo TipoPercepcion no es 019.'
  },
  'nom206': {
    'event': 'nom206',
    'message': u'El nodo Incapacidades debe existir, Ya que la clave expresada en el atributo TipoPercepcion es 014.'
  },
  'nom207': {
    'event': 'nom207',
    'message': u'La suma de los campos ImporteMonetario no es igual a la suma de los valores ImporteGravado e ImporteExento de la percepción, Ya que la clave expresada en el atributo TipoPercepcion es 014.'
  },
  'nom208': {
    'event': 'nom208',
    'message': u'El valor del atributo Nomina.Percepciones.Percepcon.HorasExtra.TipoHoras no cumple con un valor del catálogo c_TipoHoras.'
  },
  'nom209': {
    'event': 'nom209',
    'message': u'Los atributos MontoDiario y TotalParcialidad no deben existir, ya que existe valor en TotalUnaExhibicion.'
  },
  'nom210': {
    'event': 'nom210',
    'message': u'El atributo MontoDiario debe existir y el atributo TotalUnaExhibicion no debe existir, ya que Nomina.Percepciones.JubilacionPensionRetiro.TotalParcialidad tiene valor.'
  },
  'nom211': {
    'event': 'nom211',
    'message': u'El valor en el atributo Nomina.Deducciones.TotalImpuestosRetenidos no es igual a la suma de los atributos Importe de las deducciones que tienen expresada la clave 002 en el atributo TipoDeduccion.'
  },
  'nom212': {
    'event': 'nom212',
    'message': u'Nomina.Deducciones.TotalImpuestosRetenidos no debe existir, ya que no existen deducciones con clave 002 en el atributo TipoDeduccion.'
  },
  'nom213': {
    'event': 'nom213',
    'message': u'El valor del atributo Nomina.Deducciones.Deduccion.TipoDeduccion no cumple con un valor del catálogo c_TipoDeduccion.'
  },
  'nom214': {
    'event': 'nom214',
    'message': u'Debe existir el elemento Incapacidades, ya que la clave expresada en Nomina.Deducciones.Deduccion.TipoDeduccion es 006.'
  },
  'nom215': {
    'event': 'nom215',
    'message': u'El atributo Deduccion:Importe no es igual a la suma de los nodos Incapacidad:ImporteMonetario. Ya que la clave expresada en Nomina.Deducciones.Deduccion.TipoDeduccion es 006'
  },
  'nom216': {
    'event': 'nom216',
    'message': u'Nomina.Deducciones.Deduccion.Importe no es mayor que cero.'
  },
  'nom217': {
    'event': 'nom217',
    'message': u'El valor del atributo Nomina.OtrosPagos.OtroPago.TipoOtroPago no cumple con un valor del catálogo c_TipoOtroPago.'
  },
  'nom218': {
    'event': 'nom218',
    'message': u'El nodo CompensacionSaldosAFavor debe existir, ya que el valor de Nomina.OtrosPagos.OtroPago.TipoOtroPago es 004.'
  },
  'nom219': {
    'event': 'nom219',
    'message': u'El nodo SubsidioAlEmpleo. debe existir, ya que el valor de Nomina.OtrosPagos.OtroPago.TipoOtroPago es 002.'
  },
  'nom219.A': {
    'event': 'nom219',
    'message': u'El valor de Nomina.OtrosPagos.OtroPago.TipoOtroPago es 002, 007 u 008, el nodo SubsidioAlEmpleo debe existir es 002.'
  },
  'nom220': {
    'event': 'nom220',
    'message': u'El Importe del elemento Nomina.OtrosPagos.OtroPago no es mayor que cero.'
  },
  'nom221': {
    'event': 'nom221',
    'message': u'El valor del atributo SubsidioCausado no puede ser mayor que 407.02 ya que el valor de NumDiasPagados es menor o igual a 31.'
  },
  'nom222': {
    'event': 'nom222',
    'message': u'Nomina.OtrosPagos.OtroPago.CompensacionSaldosAFavor.SaldoAFavor no es mayor o igual que el valor del atributo CompensacionSaldosAFavor:RemanenteSalFav.'
  },
  'nom223': {
    'event': 'nom223',
    'message': u'Nomina.OtrosPagos.OtroPago.CompensacionSaldosAFavor.Año no es igual al año inmediato anterior o al año en curso. Favor de considerar el valor del atributo FechaPago.'
  },
  'nom224': {
    'event': 'nom224',
    'message': u'El valor del atributo Incapacidades.Incapacidad.TipoIncapacidad no cumple con un valor del catálogo c_TIpoIncapacidad.'
  },
  'nom225': {
    'event': 'nom225',
    'message': u'Error no clasificado.'
  },
  'nom900': {
    'event': 'nom900',
    'message': u'Puede existir más de un complemento de Nómina en un comprobante y deben tener contenido diferente.'
  },
  'nom901': {
    'event': 'nom901',
    'message': u'El valor del atributo FechaFinalPago debe ser menor o igual al tributo FechaInicialPago.'
  },
  'nom226': {
    'event': 'nom226',
    'message': u'TipoRegimen es igual a 02, por lo tanto, el valor del atributo OtroPago.TipoOtroPago debe ser 002 y no deben existir los valores 007 y 008 en el atributo OtroPago.TipoOtroPago.'
  },
  'nom227': {
    'event': 'nom227',
    'message': u'En el atributo TipoOtroPago no deben registrarse las claves 002, 007 o 008 ya que en el atributo TipoRegimen no existe la clave 02.'
  },
  'nom228.A': {
    'event': 'nom228',
    'message': u'El Importe del elemento OtroPago no es menor o igual que el valor del atributo SubsidioCausado.'
  },
  'nom228': {
    'event': 'nom228',
    'message': u'El Importe del elemento OtroPago no es menor o igual que el valor del atributo SubsidioCausado.'
  },
  'nom229': {
    'event': 'nom229',
    'message': u'El valor del atributo SubsidioCausado no puede ser mayor que, el resultado de multiplicar el factor 13.39 por el valor del atributo NumDiasPagados.'
  },
  # Reglas de validación para CFDI que incluyan el complemento de Comercio Exterior 1.1
  "CCE101": {
    "event": "CCE101",
    "message": u"El atributo cfdi:Comprobante:version no tiene un valor válido"
  },
  # Reglas de validación para CFDI versión 3.2 que incluyan el complemento de Comercio Exterior 1.1
  "CCE102": {
    "event": "CCE102",
    "message": u"El atributo cfdi:Comprobante:fecha no cumple con el formato requerido."
  },
  "CCE103": {
    "event": "CCE103",
    "message": u"El atributo cfdi:Comprobante:subTotal no coincide con la suma de los atributos importe de los nodos Concepto."
  },
  "CCE104": {
    "event": "CCE104",
    "message": u"El atributo cfdi:Comprobante:Moneda se debe registrar"
  },
  "CCE105": {
    "event": "CCE105",
    "message": u"El atributo cfdi:Comprobante:Moneda no contiene un valor del catálogo catCFDI:c_Moneda. "
  },
  "CCE106": {
    "event": "CCE106",
    "message": u"El atributo TipoCambio no tiene el valor '1' y la moneda indicada es MXN."
  },
  "CCE107": {
    "event": "CCE107",
    "message": u"El atributo cfdi:Comprobante:TipoCambio se debe registrar cuando el atributo cfdi:Comprobante:Moneda tiene un valor distinto de MXN y XXX. "
  },
  "CCE108": {
    "event": "CCE108",
    "message": u"El atributo cfdi:Comprobante:TipoCambio no se debe registrar cuando el atributo cfdi:Comprobante:Moneda tiene el valor XXX."
  },
  "CCE109": {
    "event": "CCE109",
    "message": u"El atributo cfdi:Comprobante:TipoCambio no cumple con el patrón requerido."
  },
  "CCE110": {
    "event": "CCE110",
    "message": u"El atributo cfdi:Comprobante:tipoDeComprobante no cumple con alguno de los valores permitidos."
  },
  "CCE111": {
    "event": "CCE111",
    "message": u"El atributo MotivoTraslado debe registrarse cuando cfdi:Comprobante:tipoDeComprobante tiene el valor 'traslado'."
  },
  "CCE112": {
    "event": "CCE112",
    "message": u"El nodo Propietario se debe registrar cuando cfdi:Comprobante:tipoDeComprobante tiene el valor 'traslado' y MotivoTraslado tiene la clave '05'."
  },
  "CCE113": {
    "event": "CCE113",
    "message": u"El atributo MotivoTraslado no debe existir cuando cfdi:Comprobante:tipoDeComprobante es distinto de 'traslado'."
  },
  "CCE114": {
    "event": "CCE114",
    "message": u"El nodo Propietario no debe existir cuando cfdi:Comprobante:tipoDeComprobante es distinto de 'traslado' y MotivoTraslado tiene una clave distinta de '05'."
  },
  "CCE115": {
    "event": "CCE115",
    "message": u"El atributo cfdi:Comprobante:total no coincide con la suma del cdi:Comprobante:subTotal, menos el cfdi:Comprobante:descuento, más cfdi:Comprobante:Impuestos:totalImpuestosTrasladados menos cfdi:Comprobante:Impuestos:totalImpuestosRetenidos. "
  },
  "CCE116": {
    "event": "CCE116",
    "message": u"El atributo cfdi:Comprobante:LugarExpedicion no cumple con alguno de los valores permitidos."
  },
  "CCE117": {
    "event": "CCE117",
    "message": u"El atributo cfdi:Comprobante:Emisor:nombre se debe registrar. "
  },
  "CCE118": {
    "event": "CCE118",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:pais debe tener el valor 'MEX'. "
  },
  "CCE119": {
    "event": "CCE119",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:pais debe tener el valor 'MEX'. "
  },
  "CCE120": {
    "event": "CCE120",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:estado debe contener una clave del catálogo catCFDI:c_Estado donde la columna c_Pais tenga el valor 'MEX'. "
  },
  "CCE121": {
    "event": "CCE121",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:estado debe contener una clave del catálogo catCFDI:c_Estado donde la columna c_Pais tenga el valor 'MEX'. "
  },
  "CCE122": {
    "event": "CCE122",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:municipio debe contener una clave del catálogo de catCFDI:c_Municipio donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el nodo es generado. "
  },
  "CCE123": {
    "event": "CCE123",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:municipio debe contener una clave del catálogo de catCFDI:c_Municipio donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el nodo es generado. "
  },
  "CCE124": {
    "event": "CCE124",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:localidad debe contener una clave del catálogo de catCFDI:c_Localidad, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el nodo es generado. "
  },
  "CCE125": {
    "event": "CCE125",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:localidad debe contener una clave del catálogo de catCFDI:c_Localidad, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el nodo es generado. "
  },
  "CCE126": {
    "event": "CCE126",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:colonia debe contener una clave del catálogo de catCFDI:c_Colonia, donde la columna c_CodigoPostal debe ser igual a la clave registrada en el atributo codigoPostal si el nodo es generado. "
  },
  "CCE127": {
    "event": "CCE127",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:colonia debe contener una clave del catálogo de catCFDI:c_Colonia, donde la columna c_CodigoPostal debe ser igual a la clave registrada en el atributo codigoPostal si el nodo es generado. "
  },
  "CCE128": {
    "event": "CCE128",
    "message": u"El atributo cfdi:Comprobante:Emisor:DomicilioFiscal:codigoPostal debe contener una clave del catálogo de catCFDI:c_CodigoPostal, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado, la columna clave de c_Municipio debe ser igual a la clave registrada en el atributo municipio, y si existe el atributo de localidad, la columna clave de c_Localidad debe ser igual a la clave registrada en el atributo localidad si el nodo es generado. "
  },
  "CCE129": {
    "event": "CCE129",
    "message": u"El atributo cfdi:Comprobante:Emisor:ExpedidoEn:codigoPostal debe contener una clave del catálogo de catCFDI:c_CodigoPostal, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado, la columna clave de c_Municipio debe ser igual a la clave registrada en el atributo municipio, y si existe el atributo de localidad, la columna clave de c_Localidad debe ser igual a la clave registrada en el atributo localidad si el nodo es generado. "
  },
  "CCE130": {
    "event": "CCE130",
    "message": u"El nodo Comprobante.Emisor.RegimenFiscal debe tener solo un elemento hijo Regimen. "
  },
  "CCE131": {
    "event": "CCE131",
    "message": u"El atributo cfdi:Comprobante:Emisor:RegistroFiscal:Regimen no cumple con alguno de los valores permitidos para el tipo de persona del emisor. "
  },
  "CCE132": {
    "event": "CCE132",
    "message": u"El atributo cfdi:Comprobante:Receptor:rfc no tiene el valor 'XEXX010101000' y el tipoDeComprobante tiene un valor distinto de 'traslado' y MotivoTraslado un valor distinto de '02'."
  },
  "CCE133": {
    "event": "CCE133",
    "message": u"El atributo cfdi:Comprobante:Receptor:rfc debe tener un RFC válido dentro de la lista de RFC's o el valor 'XEXX010101000' cuando el tipoDeComprobante es 'traslado' y MotivoTraslado es '02'."
  },
  "CCE134": {
    "event": "CCE134",
    "message": u"El atributo cfdi:Comprobante:Receptor:nombre se debe registrar. "
  },
  "CCE135": {
    "event": "CCE135",
    "message": u"El nodo cfdi:Comprobante:Receptor:Domicilio se debe registrar. "
  },
  "CCE136": {
    "event": "CCE136",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:estado debe contener una clave del catálogo catCFDI:c_Estado donde la columna c_Pais tenga el valor 'MEX' si el atributo pais tiene el valor 'MEX', el tipoDeComprobante es 'traslado' y MotivoTraslado tiene el valor '02'."
  },
  "CCE137": {
    "event": "CCE137",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:municipio debe contener una clave del catálogo de catCFDI:c_Municipio donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el atributo pais tiene el valor 'MEX', el tipoDeComprobante es 'traslado' y MotivoTraslado tiene el valor '02'."
  },
  "CCE138": {
    "event": "CCE138",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:localidad debe contener una clave del catálogo de catCFDI:c_Localidad, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado si el atributo pais tiene el valor 'MEX', el tipoDeComprobante es 'traslado' y MotivoTraslado tiene el valor '02'."
  },
  "CCE139": {
    "event": "CCE139",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:colonia debe contener una clave del catálogo de catCFDI:c_Colonia, donde la columna c_CodigoPostal debe ser igual a la clave registrada en el atributo codigoPostal si el atributo pais tiene el valor 'MEX', el tipoDeComprobante es 'traslado' y MotivoTraslado tiene el valor '02'."
  },
  "CCE140": {
    "event": "CCE140",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:codigoPostal debe contener una clave del catálogo de catCFDI:c_CodigoPostal, donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo estado, la columna clave de c_Municipio debe ser igual a la clave registrada en el atributo municipio, y si existe el atributo de localidad, la columna clave de c_Localidad debe ser igual a la clave registrada en el atributo localidad si el atributo pais tiene el valor 'MEX', el tipoDeComprobante es 'traslado' y MotivoTraslado tiene el valor '02'."
  },
  "CCE141": {
    "event": "CCE141",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:pais debe ser distinto de 'MEX' y existir en el catálogo catCFDI:c_Pais si tipoDeComprobante es distinto de 'traslado' o MotivoTraslado es distinto de '02'."
  },
  "CCE142": {
    "event": "CCE142",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:pais debe contener una clave del catálogo catCFDI:c_Estado donde la columna c_Pais sea igual a la clave del pais registrada en el atributo pais del mismo nodo."
  },
  "CCE143": {
    "event": "CCE143",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:codigoPostal se debe registrar cuando tipoDeComprobante es distinto de 'traslado' o MotivoTraslado es distinto de '02' y el pais es distinto de 'MEX'."
  },
  "CCE144": {
    "event": "CCE144",
    "message": u"El atributo cfdi:Comprobante:Receptor:Domicilio:codigoPostal debe cumplir con el patrón especificado en el catálogo catCFDI:c_Pais cuando tipoDeComprobante es distinto de 'traslado' o MotivoTraslado es distinto de '02' y el pais es distinto de 'MEX'."
  },
  # Reglas de validación para CFDI's versión 3.3 que incluyan el complemento de Comercio Exterior 1.1
  "CCE145": {
    "event": "CCE145",
    "message": u"El atributo cfdi:Comprobante:TipoDeComprobante no cumple con alguno de los valores permitidos para este complemento."
  },
  "CCE146": {
    "event": "CCE146",
    "message": u"El atributo MotivoTraslado se debe registrar cuando el atributo cfdi:Comprobante:TipoDeComprobante tiene el valor 'T'."
  },
  "CCE147": {
    "event": "CCE147",
    "message": u"El nodo Propietario se debe registrar cuando el atributo cfdi:Comprobante:TipoDeComprobante tiene el valor 'T' y MotivoTraslado tiene la clave '05'."
  },
  "CCE148": {
    "event": "CCE148",
    "message": u"El nodo Propietario no se debe registrar cuando el atributo cfdi:Comprobante:TipoDeComprobante tiene un valor distinto de 'T' y MotivoTraslado tiene una clave distinta de '05'."
  },
  "CCE149": {
    "event": "CCE149",
    "message": u"El atributo cfdi:Comprobante:Emisor:nombre se debe registrar. "
  },
  "CCE150": {
    "event": "CCE150",
    "message": u"El atributo cfd:Comprobante:Receptor:Rfc no tiene el valor 'XEXX010101000' y el TipoDeComprobante tiene un valor distinto de 'T' y MotivoTraslado un valor distinto de '02'."
  },
  "CCE151": {
    "event": "CCE151",
    "message": u"El atributo cfdi:Comprobante:Receptor:Rfc debe tener un RFC válido dentro de la lista de RFC's o el valor 'XEXX010101000' cuando el TipoDeComprobante es 'T' y MotivoTraslado es '02'."
  },
  "CCE152": {
    "event": "CCE152",
    "message": u"El atributo cfdi:Comprobante:Receptor:nombre se debe registrar. "
  },
  # Reglas de validación para el complemento de Comercio Exterior 1.1
  "CCE153": {
    "event": "CCE153",
    "message": u"El nodo cce11:ComercioExterior no puede registrarse mas de una vez. "
  },
  "CCE154": {
    "event": "CCE154",
    "message": u"El nodo cce11:ComercioExterior debe registrarse como un nodo hijo del nodo Complemento en el CFDI. "
  },
  "CCE155": {
    "event": "CCE155",
    "message": u"El nodo cce11:ComercioExterior solo puede coexistir con los complementos Timbre Fiscal Digital, otros derechos e impuestos, leyendas fiscales, recepción de pago, CFDI registro fiscal."
  },
  "CCE156": {
    "event": "CCE156",
    "message": u"El atributo cfdi:FolioFiscalOrig se debe registrar si el valor de cce11:ComercioExterior:MotivoTraslado es '01'."
  },
  "CCE157": {
    "event": "CCE157",
    "message": u"El atributo cfdi:CfdiRelacionados:CfdiRelacionado:UUID se debe registrar si el valor de cce11:ComercioExterior:MotivoTraslado es '01' con el tipo de relación '05'."
  },
  "CCE158": {
    "event": "CCE158",
    "message": u"El atributo XXXXX no debe existir si el valor de cce11:ComercioExterior:TipoOperacion es 'A'. "
  },
  "CCE159": {
    "event": "CCE159",
    "message": u"El atributo XXXX debe registrarse si la clave de cce11:ComercioExterior:TipoOperacion registrada es '1' ó '2'."
  },
  "CCE160": {
    "event": "CCE160",
    "message": u"El atributo cce11:ComercioExterior:NumCertificadoOrigen no se debe registrar si el valor de cce11:ComercioExterior:CertificadoOrigen es '0'."
  },
  "CCE161": {
    "event": "CCE161",
    "message": u"El atributo cce11:ComercioExterior:NumExportadorConfiable no se debe registrar si la clave de país del receptor o del destinatario no corresponde a un país del catálogo catCFDI:c_Pais donde la columna Agrupación tenga el valor Unión Europea."
  },
  "CCE162": {
    "event": "CCE162",
    "message": u"El atributo cce11:ComercioExterior:TotalUSD no coincide con la suma de ValorDolares de las mercancías."
  },
  "CCE163": {
    "event": "CCE163",
    "message": u"El atributo cce11:ComercioExterior:TotalUSD debe registrarse con dos decimales."
  },
  "CCE164": {
    "event": "CCE164",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Curp no se debe registrar si el atributo Rfc del nodo cfdi:Comprobante:Emisor es de longitud 12."
  },
  "CCE165": {
    "event": "CCE165",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Curp se debe registrar si el atributo Rfc del nodo cfdi:Comprobante:Emisor es de longitud 13."
  },
  "CCE166": {
    "event": "CCE166",
    "message": u"El nodo cce11:ComercioExterior:Emisor:Domicilio no debe registrarse si la versión de CFDI es 3.2. "
  },
  "CCE167": {
    "event": "CCE167",
    "message": u"El nodo cce11:ComercioExterior:Emisor:Domicilio debe registrarse si la versión de CFDI es 3.3. "
  },
  "CCE168": {
    "event": "CCE168",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:Pais debe tener la clave 'MEX'."
  },
  "CCE169": {
    "event": "CCE169",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:Estado debe contener una clave del catálogo de catCFDI:c_Estado donde la columna c_Pais tiene el valor 'MEX'."
  },
  "CCE170": {
    "event": "CCE170",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:Municipio debe contener una clave del catálogo de catCFDI:c_Municipio donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo Estado."
  },
  "CCE171": {
    "event": "CCE171",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:Localidad debe contener una clave del catálogo de catCFDI:c_Localidad donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo Estado."
  },
  "CCE172": {
    "event": "CCE172",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:Colonia debe contener una clave del catálogo de catCFDI:c_Colonia donde la columna c_CodigoPostal debe ser igual a la clave registrada en el atributo CodigoPostal."
  },
  "CCE173": {
    "event": "CCE173",
    "message": u"El atributo cce11:ComercioExterior:Emisor:Domicilio:CodigoPostal debe contener una clave del catálogo catCFDI:c_CodigoPostal donde la columna clave de c_Estado debe ser igual a la clave registrada en el atributo Estado, la columna clave de c_Municipio debe ser igual a la clave registrada en el atributo Municipio y si existe el atributo de Localidad, la columna clave de c_Localidad debe ser igual a la clave registrada en el atributo Localidad."
  },
  "CCE174": {
    "event": "CCE174",
    "message": u"El atributo cce11:ComercioExterior:Propietario:NumRegIdTrib no tiene un valor que exista en el registro del país indicado en el atributo cce1:Propietario:ResidenciaFiscal."
  },
  "CCE175": {
    "event": "CCE175",
    "message": u"El atributo cce11:ComercioExterior:Propietario:NumRegIdTrib no cumple con el patrón publicado en la columna 'Formato de registro de identidad tributaria' del país indicado en el atributo cce1:Propietario:ResidenciaFiscal."
  },
  "CCE176": {
    "event": "CCE176",
    "message": u"El atributo cce11:ComercioExterior:Receptor:NumRegIdTrib no debe registrarse si la versión de CFDI es 3.3. "
  },
  "CCE177": {
    "event": "CCE177",
    "message": u"El atributo cce11:ComercioExterior:Receptor:NumRegIdTrib debe registrarse si la versión de CFDI es 3.2. "
  },
  "CCE178": {
    "event": "CCE178",
    "message": u"El atributo cce11:ComercioExterior:Receptor:NumRegIdTrib no tiene un valor que exista en el registro del país indicado en el atributo cfdi:Comprobante:Receptor:Domicilio:pais."
  },
  "CCE179": {
    "event": "CCE179",
    "message": u"El atributo cce11:ComercioExterior:Receptor:NumRegIdTrib no cumple con el patrón publicado en la columna 'Formato de registro de identidad tributaria' del país indicado en el atributo cfdi:Comprobante:Receptor:Domicilio:pais."
  },
  "CCE180": {
    "event": "CCE180",
    "message": u"El nodo cce11:ComercioExterior:Receptor:Domicilio no debe registrarse si la versión de CFDI es 3.2. "
  },
  "CCE181": {
    "event": "CCE181",
    "message": u"El nodo cce11:ComercioExterior:Receptor:Domicilio debe registrarse si la versión de CFDI es 3.3. "
  },
  "CCE182": {
    "event": "CCE182",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:Colonia debe tener un valor del catálogo de colonia donde la columna código postal sea igual a la clave registrada en el atributo CodigoPostal cuando la clave de país es 'MEX', contiene una cadena num\u00e9rica de cuatro posiciones y la versión de CFDI es 3.3."
  },
  "CCE183": {
    "event": "CCE183",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:Localidad debe tener un valor del catálogo de localidades (catCFDI:c_Localidad) donde la columna c_Estado sea igual a la clave registrada en el atributo Estado cuando la clave de país es 'MEX' y la versión de CFDI es 3.3. "
  },
  "CCE184": {
    "event": "CCE184",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:Municipio debe tener un valor del catálogo de municipios (catCFDI:c_Municipio) donde la columna c_Estado sea igual a la clave registrada en el atributo Estado cuando la clave de país es 'MEX' y la versión de CFDI es 3.3. "
  },
  "CCE185": {
    "event": "CCE185",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:Estado debe tener un valor del catálogo de estados catCFDI:c_Estado donde la columna c_Pais sea igual a la clave de país registrada en el atributo Pais y la versión de CFDI es 3.3."
  },
  "CCE186": {
    "event": "CCE186",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:CodigoPostal debe cumplir con el patrón especificado para el país cuando es distinta de 'MEX' y la versión de CFDI es 3.3. "
  },
  "CCE187": {
    "event": "CCE187",
    "message": u"El atributo cce11:ComercioExterior:Receptor:Domicilio:CodigoPostal debe tener un valor del catálogo de códigos postales catCFDI:c_CodigoPostal donde la columna c_Estado sea igual a la clave registrada en el atributo Estado, la columna c_Municipio sea igual a la clave registrada en el atributo Municipio y la columna c_Localidad sea igual a la clave registrada en el atributo Localidad en caso de que se haya registrado cuando la clave de país es 'MEX' y la versión de CFDI es 3.3. "
  },
  "CCE188": {
    "event": "CCE188",
    "message": u"El campo tipoDeComprobante tiene el valor 'traslado' por lo tanto sólo podrás registrar un Destinatario."
  },
  "CCE189": {
    "event": "CCE189",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:NumRegIdTrib no tiene un valor que exista en el registro del país indicado en el atributo cce11:ComercioExterior:Destinatario:Domicilio:Pais."
  },
  "CCE190": {
    "event": "CCE190",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:NumRegIdTrib no cumple con el patrón publicado en la columna 'Formato de registro de identidad tributaria' del país indicado en el atributo cce11:ComercioExterior:Destinatario:Domicilio:Pais."
  },
  "CCE191": {
    "event": "CCE191",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:Colonia debe tener un valor del catálogo de colonias donde la columna código postal sea igual a la clave registrada en el atributo CodigoPostal cuando la clave de país es 'MEX' y contiene una cadena num\u00e9rica de cuatro posiciones."
  },
  "CCE192": {
    "event": "CCE192",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:Localidad debe tener un valor del catálogo de localidades (catCFDI:c_Localidad) donde la columna c_Estado sea igual a la clave registrada en el atributo Estado cuando la clave de país es 'MEX'. "
  },
  "CCE193": {
    "event": "CCE193",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:Municipio debe tener un valor del catálogo de municipios (catCFDI:c_Municipio) donde la columna c_Estado sea igual a la clave registrada en el atributo Estado cuando la clave de país es 'MEX'."
  },
  "CCE194": {
    "event": "CCE194",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:Estado debe tener un valor del catálogo de estados catCFDI:c_Estado donde la columna c_Pais sea igual a la clave de país registrada en el atributo Pais cuando la clave de país existe en la columna c_Pais del catálogo catCFDI:c_Estado y es diferente de 'ZZZ'."
  },
  "CCE195": {
    "event": "CCE195",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:CodigoPostal debe cumplir con el patrón especificado para el país cuando es distinta de 'MEX'. "
  },
  "CCE196": {
    "event": "CCE196",
    "message": u"El atributo cce11:ComercioExterior:Destinatario:Domicilio:CodigoPostal debe tener un valor del catálogo de códigos postales catCFDI:c_CodigoPostal donde la columna c_Estado sea igual a la clave registrada en el atributo Estado, la columna c_Municipio sea igual a la clave registrada en el atributo Municipio y la columna c_Localidad sea igual a la clave registrada en el atributo Localidad en caso de que se haya registrado cuando la clave de país es 'MEX'."
  },
  "CCE197": {
    "event": "CCE197",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:NoIdentificacion se debe registrar en cada concepto. "
  },
  "CCE198": {
    "event": "CCE198",
    "message": u"Debe existir al menos un cfdi:Comprobante:Conceptos:Concepto:NoIdentificacion relacionado con cce11:ComercioExterior:Mercancias:Mercancia:NoIdentificacion."
  },
  "CCE199": {
    "event": "CCE199",
    "message": u"Debe existir al menos un concepto en el nodo cfdi:Comprobante:Conceptos por cada mercancía registrada en el elemento cce1:ComercioExterior:Mercancias donde el atributo cce11:ComercioExterior:Mercancias:Mercancia:NoIdentificacion sea igual al atributo cfdi:Comprobante:Conceptos:Concepto:NoIdentificacion."
  },
  "CCE200": {
    "event": "CCE200",
    "message": u"No se deben repetir elementos Mercancia donde el NoIdentificacion y la FraccionArancelaria sean iguales en el elemento cce11:ComercioExterior:Mercancias."
  },
  "CCE201": {
    "event": "CCE201",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:Cantidad no cumple con alguno de los valores permitidos cuando no se registra el atributo cce11:ComercioExterior:Mercancias:Mercancia:CantidadAduana."
  },
  "CCE202": {
    "event": "CCE202",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:Unidad no cumple con alguno de los valores permitidos cuando no se registra el atributo cce11:ComercioExterior:Mercancias:Mercancia:CantidadAduana."
  },
  "CCE203": {
    "event": "CCE203",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:ValorUnitario no cumple con alguno de los valores permitidos cuando no se registra el atributo cce11:ComercioExterior:Mercancias:Mercancia:CantidadAduana."
  },
  "CCE204": {
    "event": "CCE204",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:importe debe ser mayor o igual que el límite inferior y menor o igual que el límite superior calculado."
  },
  "CCE205": {
    "event": "CCE205",
    "message": u"La suma de los campos cce11:ComercioExterior:Mercancias:Mercancia:ValorDolares distintos de '0' y '1' de todas las mercancías que tengan el mismo NoIdentificacion y \u00e9ste sea igual al NoIdentificacion del concepto debe ser mayor o igual al valor mínimo y menor o igual al valor máximo calculado."
  },
  "CCE206": {
    "event": "CCE206",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria debe registrarse cuando el atributo cce11:ComercioExterior:Mercancias:Mercancia:UnidadAduana o el atributo cfdi:Comprobante:Conceptos:Concepto:Unidad tienen un valor distinto de '99'."
  },
  "CCE207": {
    "event": "CCE207",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria no debe registrarse cuando el atributo cce11:ComercioExterior:Mercancias:Mercancia:UnidadAduana o el atributo cfdi:Comprobante:Conceptos:Concepto:Unidad tienen el valor '99'."
  },
  "CCE208": {
    "event": "CCE208",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria debe tener un valor vigente del catálogo catCFDI:c_FraccionArancelaria."
  },
  "CCE209": {
    "event": "CCE209",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:Mercancia:UnidadAduana debe tener el valor especificado en el catálogo catCFDI:c_FraccionArancelaria columna 'UMT' cuando el atributo cce11:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria está registrado."
  },
  "CCE210": {
    "event": "CCE210",
    "message": u"El atributo cfdi:Comprobante:Conceptos:Concepto:Unidad del concepto relacionado a la mercncía debe tener el valor especificado en el catálogo catCFDI:c_FraccionArancelaria columna 'UMT' cuando el atributo cce11:ComercioExterior:Mercancias:Mercancia:FraccionArancelaria está registrado."
  },
  "CCE211": {
    "event": "CCE211",
    "message": u"El atributo cfdi:Comprobante:descuento debe ser mayor o igual que la suma de los atributos cce11:ComercioExterior:Mercancias:Mercancia:ValorDolares de todas las mercancías que tengan la fracción arancelaria '98010001' convertida a la moneda del comprobante si la versión del CFDI es 3.2. "
  },
  "CCE212": {
    "event": "CCE212",
    "message": u"La suma de los valores de cfdi:Comprobante:Conceptos:Concepto:Descuento donde el NoIdentificacion es el mismo que el de la mercancía convertida a la moneda del comprobante debe ser mayor o igual que la suma de los valores de cce11:ComercioExterior:Mercancias:Mercancia:ValorDolares de todas las mercancías que tengan la fracción arancelaria '98010001' y el NoIdentificacion sea igual al NoIdentificacion del concepto si la versión del CFDI es 3.3. "
  },
  "CCE213": {
    "event": "CCE213",
    "message": u"Los atributos CantidadAduana, UnidadAduana y ValorUnitarioAduana deben existir en los registros involucrados si se ha registrado alguno de ellos, si existe más de un concepto con el mismo NoIdentificacion o si existe más de una mercancía con el mismo NoIdentificacion."
  },
  "CCE214": {
    "event": "CCE214",
    "message": u"Los atributos CantidadAduana, UnidadAduana y ValorUnitarioAduana deben registrarse en todos los elementos mercancía del comprobante, siempre que uno de ellos los tenga registrados."
  },
  "CCE215": {
    "event": "CCE215",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:Mercancia:ValorUnitarioAduana debe ser mayor que '0' cuando  cce11:ComercioExterior:Mercancias:Mercancia:UnidadAduana es distinto de '99'."
  },
  "CCE216": {
    "event": "CCE216",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:ValorDolares de cada mercancía registrada debe ser mayor o igual que el límite inferior y menor o igual que el límtie superior o uno, cuando la normatividad lo permita y exista el atributo cce11:ComercioExterior:Mercancias:Mercancia:CantidadAduana."
  },
  "CCE217": {
    "event": "CCE217",
    "message": u"El atributo cce11:ComercioExterior:Mercancias:ValorDolares de cada mercancía registrada debe ser igual al producto del valor del atributo cfdi:Comprobante:Conceptos:Concepto:Importe por el valor del atributo cfdi:Comprobante:TipoCambio y dividido entre el valor del atributo cce11:ComercioExterior:TipoDeCambioUSD donde el atributo cfdi:Comprobante:Conceptos:NoIdentificacion es igual al atributo cce11:ComercioExterior:Mercancias:Mercancia:NoIdentificacion, '0' cuando el atributo cce11:ComercioExterior:Mercancias:Mercancia:UnidadAduana o el atributo cfdi:Comprobante:Conceptos:Concepto:Unidad tienen el valor '99', o '1', cuando la normatividad lo permita y no debe existir el atributo cce11:ComercioExterior:Mercancias:Mercancia:CantidadAduana. "
  },
  "CCE218": {
    "event": "CCE218",
    "message": u"Error no clasificado"
  },
  "CCE999": {
    "event": "CCE999",
    "message": u"El prefijo y namespace usados para comercio exterior son incorrectos o no están localizados a nivel cfdi:Comprobante."
  },

  # Reglas de validacion para CFDI 3.3
  "CFDI33101": {
    "event": "CFDI33101",
    "message": u"El campo Fecha no cumple con el patrón requerido."
  },
  "CFDI33102": {
    "event": "CFDI33102",
    "message": u"El resultado de la digestión debe ser igual al resultado de la desencripción del sello."
  },
  "CFDI33103": {
    "event": "CFDI33103",
    "message": u"Si existe el complemento para recepción de pagos este campo no debe existir"
  },
  "CFDI33104": {
    "event": "CFDI33104",
    "message": u"El campo FormaPago no contiene un valor del catálogo c_FormaPago. "
  },
  "CFDI33105": {
    "event": "CFDI33105",
    "message": u"EL certificado no cumple con alguno de los valores permitidos"
  },
  "CFDI33106": {
    "event": "CFDI33106",
    "message": u"El valor de este campo SubTotal excede la cantidad de decimales que soporta la moneda."
  },
  "CFDI33107": {
    "event": "CFDI33107",
    "message": u"El TipoDeComprobante es I,E o N, el importe registrado en el campo no es igual a la suma de los importes de los conceptos registrados."
  },
  "CFDI33107A": {
    "event": "CFDI33200",
    "message": u"El TipoDeComprobante es I,E o N, por lo que los atributos FormaPago y MetodoPago se vuelven requeridos."
  },
  "CFDI33107B": {
    "event": "CFDI33201",
    "message": u"El TipoDeComprobante es P o T por lo que los atributos FormaPago y MetodoPago no deben existir."
  },
  "CFDI33108": {
    "event": "CFDI33108",
    "message": u"El TipoDeComprobante es T o P y el importe no es igual a 0, o cero con decimales."
  },
  "CFDI33109": {
    "event": "CFDI33109",
    "message": u"El valor registrado en el campo Descuento no es menor o igual que el campo Subtotal."
  },
  "CFDI33110": {
    "event": "CFDI33110",
    "message": u"El TipoDeComprobante NO es I,E o N, y un concepto incluye el campo descuento. "
  },
  "CFDI33111": {
    "event": "CFDI33111",
    "message": u"El valor del campo Descuento excede la cantidad de decimales que soporta la moneda."
  },
  "CFDI33112": {
    "event": "CFDI33112",
    "message": u"El campo Moneda no contiene un valor del catálogo c_Moneda. "
  },
  "CFDI33113": {
    "event": "CFDI33113",
    "message": u"El campo TipoCambio no tiene el valor \"1\" y la moneda indicada es MXN."
  },
  "CFDI33114": {
    "event": "CFDI33114",
    "message": u"El campo TipoCambio se debe registrar cuando el campo Moneda tiene un valor distinto de MXN y XXX. "
  },
  "CFDI33115": {
    "event": "CFDI33115",
    "message": u"El campo TipoCambio no se debe registrar cuando el campo Moneda tiene el valor XXX."
  },
  "CFDI33116": {
    "event": "CFDI33116",
    "message": u"El campo TipoCambio no cumple con el patrón requerido."
  },
  "CFDI33117": {
    "event": "CFDI33117",
    "message": u"Cuando el valor del campo TipoCambio se encuentre fuera de los límites establecidos, debe existir el campo Confirmacion"
  },
  "CFDI33118": {
    "event": "CFDI33118",
    "message": u"El campo Total no corresponde con la suma del subtotal, menos los descuentos aplicables, más las contribuciones recibidas (impuestos trasladados - federales o locales, derechos, productos, aprovechamientos, aportaciones de seguridad social, contribuciones de mejoras) menos los impuestos retenidos."
  },
  "CFDI33119": {
    "event": "CFDI33119",
    "message": u"Cuando el valor del campo Total se encuentre fuera de los límites establecidos, debe existir el campo Confirmacion"
  },
  "CFDI33120": {
    "event": "CFDI33120",
    "message": u"El campo TipoDeComprobante, no contiene un valor del catálogo c_TipoDeComprobante."
  },
  "CFDI33121": {
    "event": "CFDI33121",
    "message": u"El campo MetodoPago, no contiene un valor del catálogo c_MetodoPago."
  },
  "CFDI33122": {
    "event": "CFDI33122",
    "message": u"Cuando se tiene el valor PIP en el campo MetodoPago y el valor en el campo TipoDeComprobante es I ó E, el CFDI debe contener un complemento de recibo de pago"
  },
  "CFDI33123": {
    "event": "CFDI33123",
    "message": u"Se debe omitir el campo MetodoPago cuando el TipoDeComprobante es T o P"
  },
  "CFDI33124": {
    "event": "CFDI33124",
    "message": u"Si existe el complemento para recepción de pagos en este CFDI este campo no debe existir."
  },
  "CFDI33125": {
    "event": "CFDI33125",
    "message": u"El campo LugarExpedicion, no contiene un valor del catálogo c_CodigoPostal."
  },
  "CFDI33126": {
    "event": "CFDI33126",
    "message": u"El campo Confirmacion no debe existir cuando los atributios TipoCambio y/o Total están dentro del rango permitido"
  },
  "CFDI33127": {
    "event": "CFDI33127",
    "message": u"Número de confirmación inválido"
  },
  "CFDI33128": {
    "event": "CFDI33128",
    "message": u"Número de confrirmación utilizado previamente"
  },
    "CFDI33128.1": {
    "event": "CFDI33128.1",
    "message": u"Número de confirmación ha caducado, fecha de solicitud mayor a 5 días"
  },
  "CFDI33129": {
    "event": "CFDI33129",
    "message": u"El campo TipoRelacion, no contiene un valor del catálogo c_TipoRelacion."
  },
  "CFDI33130": {
    "event": "CFDI33130",
    "message": u"El campo RegimenFiscal, no contiene un valor del catálogo c_RegimenFiscal."
  },
  "CFDI33131": {
    "event": "CFDI33131",
    "message": u"La clave del campo RegimenFiscal debe corresponder con el tipo de persona (fisica o moral) "
  },
  "CFDI33132": {
    "event": "CFDI33132",
    "message": u"Este RFC del receptor no existe en la lista de RFC inscritos no cancelados del SAT"
  },
  "CFDI33133": {
    "event": "CFDI33133",
    "message": u"El campo ResidenciaFiscal, no contiene un valor del catálogo c_Pais"
  },
  "CFDI33134": {
    "event": "CFDI33134",
    "message": u"El RFC del receptor es de un RFC registrado en el SAT o un RFC genérico nacional y EXISTE el campo ResidenciaFiscal."
  },
  "CFDI33135": {
    "event": "CFDI33135",
    "message": u"El valor del campo ResidenciaFiscal no puede ser MEX"
  },
  "CFDI33136": {
    "event": "CFDI33136",
    "message": u"Se debe registrar un valor de acuerdo al catálogo c_Pais en en el campo ResidenciaFiscal, cuando en el en el campo NumRegIdTrib se registre información."
  },
  "CFDI33137": {
    "event": "CFDI33137",
    "message": u"El valor del campo es un RFC inscrito no cancelado en el SAT o un RFC genérico nacional, y se registró el campo NumRegIdTrib."
  },
  "CFDI33138": {
    "event": "CFDI33138",
    "message": u"Para registrar el campo NumRegIdTrib, el CFDI debe contener el complemento de comercio exterior y el RFC del receptor debe ser un RFC genérico extranjero."
  },
  "CFDI33139": {
    "event": "CFDI33139",
    "message": u"El campo NumRegIdTrib no cumple con el patrón correspondiente. "
  },
  "CFDI33140": {
    "event": "CFDI33140",
    "message": u"El campo UsoCFDI, no contiene un valor del catálogo c_UsoCFDI."
  },
  "CFDI33141": {
    "event": "CFDI33141",
    "message": u"La clave del campo UsoCFDI debe corresponder con el tipo de persona (fisica o moral) "
  },
  "CFDI33142": {
    "event": "CFDI33142",
    "message": u"El campo ClaveProdServ, no contiene un valor del catálogo c_ClaveProdServ."
  },
  "CFDI33143": {
    "event": "CFDI33143",
    "message": u"No existe el complemento requerido para el valor de ClaveProdServ"
  },
  "CFDI33144": {
    "event": "CFDI33144",
    "message": u"No está declarado el impuesto relacionado con el valor de ClaveProdServ"
  },
  "CFDI33145": {
    "event": "CFDI33145",
    "message": u"El campo ClaveUnidad no contiene un valor del catálogo c_ClaveUnidad."
  },
  "CFDI33146": {
    "event": "CFDI33146",
    "message": u"El valor del campo ValorUnitario debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33147": {
    "event": "CFDI33147",
    "message": u"El valor del campo ValorUnitario debe ser mayor que cero (0) cuando el tipo de comprobante es Ingreso, Egreso o Nomina"
  },
  "CFDI33148": {
    "event": "CFDI33148",
    "message": u"El valor del campo Importe debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33149": {
    "event": "CFDI33149",
    "message": u"El valor del campo Importe no se encuentra entre el limite inferior y superior permitido"
  },
  "CFDI33150": {
    "event": "CFDI33150",
    "message": u"El valor del campo Descuento debe tener hasta la cantidad de decimales que tenga registrado el atributo importe del concepto."
  },
  "CFDI33151": {
    "event": "CFDI33151",
    "message": u"El valor del campo Descuento del nodo Concepto es mayor que el Importe."
  },
  "CFDI33152": {
    "event": "CFDI33152",
    "message": u"En caso de utilizar el nodo Impuestos en un concepto, se deben incluir impuestos  de traslado y/o retenciones"
  },
  "CFDI33153": {
    "event": "CFDI33153",
    "message": u"El valor del campo Base que corresponde a Traslado debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33154": {
    "event": "CFDI33154",
    "message": u"El valor del campo Base que corresponde a Traslado debe ser mayor que cero"
  },
  "CFDI33155": {
    "event": "CFDI33155",
    "message": u"El valor del campo Impuesto que corresponde a Traslado no contiene un valor del catálogo c_Impuesto."
  },
  "CFDI33156": {
    "event": "CFDI33156",
    "message": u"El valor del campo TipoFactor que corresponde a Traslado no contiene un valor del catálogo c_TipoFactor."
  },
  "CFDI33157": {
    "event": "CFDI33157",
    "message": u"Si el valor registrado en el campo TipoFactor que corresponde a Traslado es Exento no se deben registrar los campos TasaOCuota ni Importe."
  },
  "CFDI33158": {
    "event": "CFDI33158",
    "message": u"Si el valor registrado en el campo TipoFactor que corresponde a Traslado es Tasa o Cuota, se deben registrar los campos TasaOCuota e Importe."
  },
  "CFDI33159": {
    "event": "CFDI33159",
    "message": u"El valor del campo TasaOCuota que corresponde a Traslado no contiene un valor del catálogo c_TasaOCuota o se encuentra fuera de rango."
  },
  "CFDI33160": {
    "event": "CFDI33160",
    "message": u"El valor del campo Importe que corresponde a Traslado debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33161": {
    "event": "CFDI33161",
    "message": u"El valor del campo Importe o que corresponde a Traslado no se encuentra entre el limite inferior y superior permitido"
  },
  "CFDI33162": {
    "event": "CFDI33162",
    "message": u"El valor del campo Base que corresponde a Retención debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33163": {
    "event": "CFDI33163",
    "message": u"El valor del campo Base que corresponde a Retención debe ser mayor que cero."
  },
  "CFDI33164": {
    "event": "CFDI33164",
    "message": u"El valor del campo Impuesto que corresponde a Retención no contiene un valor del catálogo c_Impuesto."
  },
  "CFDI33165": {
    "event": "CFDI33165",
    "message": u"El valor del campo TipoFactor que corresponde a Retención no contiene un valor del catálogo c_TipoFactor."
  },
  "CFDI33166": {
    "event": "CFDI33166",
    "message": u"Si el valor registrado en el campo TipoFactor que corresponde a Retención debe ser distinto de Excento."
  },
  "CFDI33167": {
    "event": "CFDI33167",
    "message": u"El valor del campo TasaOCuota que corresponde a Retención no contiene un valor del catálogo c_TasaOcuota o se encuentra fuera de rango."
  },
  "CFDI33168": {
    "event": "CFDI33168",
    "message": u"El valor del campo Importe que corresponde a Retención debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33169": {
    "event": "CFDI33169",
    "message": u"El valor del campo Importe que corresponde a Retención no se encuentra entre el limite inferior y superior permitido."
  },
  "CFDI33170": {
    "event": "CFDI33170",
    "message": u"El número de pedimento es inválido"
  },
  "CFDI33171": {
    "event": "CFDI33171",
    "message": u"El NumeroPedimento no debe existir si se incluye el complemento de comercio exterior"
  },
  "CFDI33172": {
    "event": "CFDI33172",
    "message": u"El campo ClaveProdServ, no contiene un valor del catálogo c_ClaveProdServ."
  },
  "CFDI33173": {
    "event": "CFDI33173",
    "message": u"El valor del campo ValorUnitario debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33174": {
    "event": "CFDI33174",
    "message": u"El valor del campo ValorUnitario debe ser mayor que cero (0)"
  },
  "CFDI33175": {
    "event": "CFDI33175",
    "message": u"El valor del campo ValorUnitario debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33176": {
    "event": "CFDI33176",
    "message": u"El valor del campo Importe no se encuentra entre el limite inferior y superior permitido"
  },
  "CFDI33177": {
    "event": "CFDI33177",
    "message": u"El número de pedimento es inválido"
  },
  "CFDI33178": {
    "event": "CFDI33178",
    "message": u"El NumeroPedimento no debe existir si se incluye el complemento de comercio exterior"
  },
  "CFDI33179": {
    "event": "CFDI33179",
    "message": u"Cuando el TipoDeComprobante sea T o P, este elemento no debe existir."
  },
  "CFDI33180": {
    "event": "CFDI33180",
    "message": u"El valor del campo TotalImpuestosRetenidos debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33181": {
    "event": "CFDI33181",
    "message": u"El valor del campo TotalImpuestosRetenidos debe ser igual a la suma de los importes registrados en el elemento hijo Retencion."
  },
  "CFDI33182": {
    "event": "CFDI33182",
    "message": u"El valor del campo TotalImpuestosTrasladados debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33183": {
    "event": "CFDI33183",
    "message": u"El valor del campo TotalImpuestosTrasladados no es igual a la suma de los importes registrados en el elemento hijo Traslado"
  },
  "CFDI33184": {
    "event": "CFDI33184",
    "message": u"Debe existir el campo TotalImpuestosRetenidos"
  },
  "CFDI33185": {
    "event": "CFDI33185",
    "message": u"El campo Impuesto no contiene un valor del catálogo c_Impuesto."
  },
  "CFDI33186": {
    "event": "CFDI33186",
    "message": u"Debe haber sólo un registro por cada tipo de impuesto retenido."
  },
  "CFDI33187": {
    "event": "CFDI33187",
    "message": u"Debe existir el campo TotalImpuestosRetenidos"
  },
  "CFDI33188": {
    "event": "CFDI33188",
    "message": u"El valor del campo Importe correspondiente a Retención debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33189": {
    "event": "CFDI33189",
    "message": u"El campo Importe correspondiente a Retención no es igual a la suma de los importes de los impuestos retenidos registrados en los conceptos donde el impuesto sea igual al campo impuesto de este elemento."
  },
  "CFDI33190": {
    "event": "CFDI33190",
    "message": u"Debe existir el campo TotalImpuestosTrasladados"
  },
  "CFDI33191": {
    "event": "CFDI33191",
    "message": u"El campo Impuesto no contiene un valor del catálogo c_Impuesto."
  },
  "CFDI33192": {
    "event": "CFDI33192",
    "message": u"Debe haber sólo un registro con la misma combinación de impuesto, factor y tasa por cada traslado."
  },
  "CFDI33193": {
    "event": "CFDI33193",
    "message": u"El valor seleccionado debe corresponder a un valor del catalogo donde la columna impuesto corresponda con el campo impuesto y la columna factor corresponda con el campo TipoFactor"
  },
  "CFDI33194": {
    "event": "CFDI33194",
    "message": u"El valor del campo Importe correspondiente a Traslado debe tener hasta la cantidad de decimales que soporte la moneda."
  },
  "CFDI33195": {
    "event": "CFDI33195",
    "message": u"El campo Importe correspondiente a Traslado no es igual a la suma de los importes de los impuestos trasladados registrados en los conceptos donde el impuesto del concepto sea igual al campo impuesto de este elemento y la TasaOCuota del concepto sea igual al campo TasaOCuota de este elemento."
  },
  "CFDI33196": {
    "event": "CFDI33196",
    "message": u"El RFC no se encuentra registrado para aplicar el Estímulo Franja Fronteriza."
  },
  "CFDI33197": {
    "event": "CFDI33196",
    "message": u"No aplica Estímulo Franja Fronteriza para la clave de producto o servicio."
  },
  "CFDI33198": {
    "event": "CFDI33196",
    "message": u"El código postal no corresponde a Franja Fronteriza."
  },
  "CFDI33991": {
    "event": "CFDI33991",
    "message": u"Se debe omitir el atributo CondicionesDePago cuando el TipoDeComprobante es T, P o N."
  },
  "CFDI33992": {
    "event": "CFDI33992",
    "message": u"Se debe omitir el atributo Descuento de los conceptos cuando el TipoDeComprobante es T o P."
  },
  "CFDI33993": {
    "event": "CFDI33993",
    "message": u"Se debe omitir el elemento Impuestos cuando el TipoDeComprobante es T, P o N."
  },
  "CFDI33994": {
    "event": "CFDI33994",
    "message": u"El valor del atributo Traslado:Importe no debe contener valores negativos."
  },
  "CFDI33995": {
    "event": "CFDI33995",
    "message": u"El Rfc Emisor se encuentra en la lista del código 69b."
  },  
  "CFDI33996": {
    "event": "CFDI33996",
    "message": u"El Rfc Receptor se encuentra en la lista del código 69b."
  },  
  "CFDI33999": {
    "event": "CFDI33999",
    "message": u"Error No Clasificado."
  },


  # Reglas de Validacion para el complemento de Pagos10
  "CRP101": {
    "event": "CRP101",
    "message": u"El valor del campo TipoDeComprobante debe ser P"
  },
  "CRP102": {
    "event": "CRP102",
    "message": u"El valor del campo SubTotal debe ser cero 0."
  },
  "CRP103": {
    "event": "CRP103",
    "message": u"El valor del campo Moneda debe ser XXX."
  },
  "CRP104": {
    "event": "CRP104",
    "message": u"El campo FormaPago no se debe registrar en el CFDI."
  },
  "CRP105": {
    "event": "CRP105",
    "message": u"El campo MetodoPago no se debe registrar en el CFDI."
  },
  "CRP106": {
    "event": "CRP106",
    "message": u"El campo CondicionesDePago no se debe registrar en el CFDI."
  },
  "CRP107": {
    "event": "CRP107",
    "message": u"El campo Descuento no se debe registrar en el CFDI."
  },
  "CRP108": {
    "event": "CRP108",
    "message": u"El campo TipoCambio no se debe registrar en el CFDI."
  },
  "CRP109": {
    "event": "CRP109",
    "message": u"El valor del campo Total debe ser cero 0."
  },
  "CRP110": {
    "event": "CRP110",
    "message": u"El valor del campo UsoCFDI debe ser P01."
  },
  "CRP111": {
    "event": "CRP111",
    "message": u"Solo debe existir un Concepto en el CFDI. "
  },
  "CRP112": {
    "event": "CRP112",
    "message": u"No se deben registrar apartados dentro de Conceptos"
  },
  "CRP113": {
    "event": "CRP113",
    "message": u"El valor del campo ClaveProdServ debe ser 84111506."
  },
  "CRP114": {
    "event": "CRP114",
    "message": u"El campo NoIdentificacion no se debe registrar en el CFDI."
  },
  "CRP115": {
    "event": "CRP115",
    "message": u"El valor del campo Cantidad debe ser 1."
  },
  "CRP116": {
    "event": "CRP116",
    "message": u"El valor del campo ClaveUnidad debe ser ACT."
  },
  "CRP117": {
    "event": "CRP117",
    "message": u"El campo Unidad no se debe registrar en el CFDI."
  },
  "CRP118": {
    "event": "CRP118",
    "message": u"El valor del campo Descripcion debe ser Pago."
  },
  "CRP119": {
    "event": "CRP119",
    "message": u"El valor del campo ValorUnitario debe ser cero 0."
  },
  "CRP120": {
    "event": "CRP120",
    "message": u"El valor del campo Importe debe ser cero 0."
  },
  "CRP121": {
    "event": "CRP121",
    "message": u"El campo Descuento no se debe registrar en el CFDI."
  },
  "CRP122": {
    "event": "CRP122",
    "message": u"No se debe registrar el apartado de Impuestos en el CFDI."
  },
  "CRP201": {
    "event": "CRP201",
    "message": u"El valor del campo FormaDePagoP debe ser distinto de 99."
  },
  "CRP202": {
    "event": "CRP202",
    "message": u"El campo MonedaP debe ser distinto de XXX"
  },
  "CRP203": {
    "event": "CRP203",
    "message": u"El campo TipoCambioP se debe registrar."
  },
  "CRP204": {
    "event": "CRP204",
    "message": u"El campo TipoCambioP no se debe registrar."
  },
  "CRP205": {
    "event": "CRP205",
    "message": u"Cuando el valor del campo TipoCambioP se encuentre fuera de los límites establecidos, debe existir el campo Confirmacion"
  },
  "CRP206": {
    "event": "CRP206",
    "message": u"La suma de los valores registrados en el campo ImpPagado de los apartados DoctoRelacionado no es menor o igual que el valor del campo Monto."
  },
  "CRP207": {
    "event": "CRP207",
    "message": u"El valor del campo Monto no es mayor que cero 0."
  },
  "CRP208": {
    "event": "CRP208",
    "message": u"El valor del campo Monto debe tener hasta la cantidad de decimales que soporte la moneda registrada en el campo MonedaP."
  },
  "CRP209": {
    "event": "CRP209",
    "message": u"Cuando el valor del campo Monto se encuentre fuera de los límites establecidos, debe existir el campo Confirmacion"
  },
  "CRP210": {
    "event": "CRP210",
    "message": u"El RFC del campo RfcEmisorCtaOrd no se encuentra en la lista de RFC."
  },
  "CRP211": {
    "event": "CRP211",
    "message": u"El campo NomBancoOrdExt se debe registrar."
  },
  "CRP212": {
    "event": "CRP212",
    "message": u"El campo CtaOrdenante no se debe registrar."
  },
  "CRP213": {
    "event": "CRP213",
    "message": u"El campo CtaOrdenante no cumple con el patrón requerido."
  },
  "CRP214": {
    "event": "CRP214",
    "message": u"El campo RfcEmisorCtaBen no se debe registrar."
  },
  "CRP215": {
    "event": "CRP215",
    "message": u"El campo CtaBeneficiario no se debe registrar."
  },
  "CRP216": {
    "event": "CRP216",
    "message": u"El campo TipoCadPago no se debe registrar."
  },
  "CRP217": {
    "event": "CRP217",
    "message": u"El valor del campo MonedaDR debe ser distinto de XXX"
  },
  "CRP218": {
    "event": "CRP218",
    "message": u"El campo TipoCambioDR se debe registrar."
  },
  "CRP219": {
    "event": "CRP219",
    "message": u"El campo TipoCambioDR no se debe registrar."
  },
  "CRP220": {
    "event": "CRP220",
    "message": u"El campo TipoCambioDR debe ser 1."
  },
  "CRP221": {
    "event": "CRP221",
    "message": u"El campo ImpSaldoAnt debe mayor a cero."
  },
  "CRP222": {
    "event": "CRP222",
    "message": u"El valor del campo ImpSaldoAnt debe tener hasta la cantidad de decimales que soporte la moneda registrada en el campo MonedaDR."
  },
  "CRP223": {
    "event": "CRP223",
    "message": u"El campo ImpPagado debe mayor a cero."
  },
  "CRP224": {
    "event": "CRP224",
    "message": u"El valor del campo ImpPagado debe tener hasta la cantidad de decimales que soporte la moneda registrada en el campo MonedaDR."
  },
  "CRP225": {
    "event": "CRP225",
    "message": u"El valor del campo ImpSaldoInsoluto debe tener hasta la cantidad de decimales que soporte la moneda registrada en el campo MonedaDR."
  },
  "CRP226": {
    "event": "CRP226",
    "message": u"El campo ImpSaldoInsoluto debe ser mayor o igual a cero y calcularse con la suma de los campos ImSaldoAnt menos el ImpPagado o el Monto."
  },
  "CRP227": {
    "event": "CRP227",
    "message": u"El campo CertPago se debe registrar."
  },
  "CRP228": {
    "event": "CRP228",
    "message": u"El campo CertPago no se debe registrar."
  },
  "CRP229": {
    "event": "CRP229",
    "message": u"El campo CadPago se debe registrar."
  },
  "CRP230": {
    "event": "CRP230",
    "message": u"El campo CadPago no se debe registrar."
  },
  "CRP231": {
    "event": "CRP231",
    "message": u"El campo SelloPago se debe registrar."
  },
  "CRP232": {
    "event": "CRP232",
    "message": u"El campo SelloPago no se debe registrar."
  },
  "CRP233": {
    "event": "CRP233",
    "message": u"El campo NumParcialidad se debe registrar."
  },
  "CRP234": {
    "event": "CRP234",
    "message": u"El campo ImpSaldoAnt se debe registrar."
  },
  "CRP235": {
    "event": "CRP235",
    "message": u"El campo ImpPagado se debe registrar."
  },
  "CRP236": {
    "event": "CRP236",
    "message": u"El campo ImpSaldoInsoluto se debe registrar."
  },
  "CRP237": {
    "event": "CRP237",
    "message": u"No debe existir el apartado de Impuestos."
  },
  "CRP238": {
    "event": "CRP238",
    "message": u"El campo RfcEmisorCtaOrd no se debe registrar."
  },
  "CRP239": {
    "event": "CRP239",
    "message": u"El campo CtaBeneficiario no cumple con el patrón requerido."
  }, 
  "CRP996": {
    "event": "CRP996",
    "message": u'El elemento pago10:Pagos debe contener al menos un elemento hijo pago10:Pago.'
  },
  "CRP997": {
    "event": "CRP997",
    "message": u'El elemento pago10:Pagos.pago10:Pago debe contener al menos un elemento hijo pago10:DoctoRelacionado.'
  },
  "CRP998": {
    "event": "CRP998",
    "message": u"El campo NomBancoOrdExt no debe existir."
  },
  "CRP999": {
    "event": "CRP999",
    "message": u"Error no clasificado"
  },
  "CRP999.A": {
    "event": "CRP999.A",
    "message": u"El ImportePagado esta fuera del límite superior e inferior calculados."
  },
  ## ECC Complement
  '121': {
    'event': '121',
    'message': u"El valor del atributo '(ecc11:EstadoDeCuentaCombustible:SubTotal )' no coincide con la suma de los valores de los atributos [ConceptoEstadoDeCuentaCombustible]:[Importe]",
  },
  '122': {
    'event': '122',
    'message': "El valor del atributo '(ecc11:EstadoDeCuentaCombustible:Total)' debe ser igual a la suma del valor del atributo [SubTotal] y la suma de los valores de los atributos [ConceptoEstadoDeCuentaCombustible]:[Traslados]:[Traslado]:[Importe].",
  },
  '123': {
    'event': '123',
    'message': "El valor del atributo '(Conceptos:ConceptoEstadoDeCuentaCombustible:Rfc)' no existe en la Lista de Contribuyentes Obligados (LCO).",
  },
  '124':{
    'event': '124',
    'message': "El valor del atributo '([cfdi]:[TipoDeComprobante])'  debe ser {I}. ",
  },

  ## ECC 1.2 Complement
  'ECC121': {
    'event': 'ECC121',
    'message': u"El valor del atributo '(ecc11:EstadoDeCuentaCombustible:SubTotal )' no coincide con la suma de los valores de los atributos [ConceptoEstadoDeCuentaCombustible]:[Importe]",
  },
  'ECC122': {
    'event': 'ECC122',
    'message': "El valor del atributo '(ecc11:EstadoDeCuentaCombustible:Total)' no coincide con la suma del valor del atributo SubTotal y la suma de los valores de los atributos importe de los traslados.",
  },
  'ECC123': {
    'event': 'ECC123',
    'message': "El valor del atributo '(Conceptos:ConceptoEstadoDeCuentaCombustible:Rfc)' no existe en la Lista de Contribuyentes Obligados (LCO).",
  },
  'ECC124': {
    'event': 'ECC124',
    'message': "El atributo '([cfdi]:[TipoDeComprobante])'  no cumple con el valor permitido {I}. ",
  },
  'ECC125': {
    'event': 'ECC125',
    'message': "El atributo '([cfdi]:[Version])' debe tener el valor {3.3}.",
  },
  'ECC126': {
    'event': 'ECC126',
    'message': "El RFC enajenante del nodo Conceptos:ConceptoEstadoDeCuentaCombustible no puede hacer uso del impuesto IVA 0.080000",
  },
  'ECC127': {
    'event': 'ECC127',
    'message': "El valor del atributo TasaOCouta del nodo Traslados:Traslado debe contener el valor '0.080000' para el impuesto IVA",
  },
  'ECC128': {
    'event': 'ECC128',
    'message': "El RFC enajenante del nodo Conceptos:ConceptoEstadoDeCuentaCombustible no cuenta con las obligaciones necesarias para facturar.",
  },
  'ECC129': {
    'event': 'ECC129',
    'message': "El RFC enajenante del nodo Conceptos:ConceptoEstadoDeCuentaCombustible no puede hacer uso de los RFC XAXX010101000 o XEXX010101000.",
  },
  'ECC999': {
    'event': 'ECC999',
    'message': "Error no clasificado.",
  },
  ## IEEH 1.0
  'IEEH101': {
    'event': 'IEEH101',
    'message': u'El atributo Version no tiene un valor válido.'
  },
  'IEEH102': {
    'event': 'IEEH102',
    'message': 'El atributo TipoDeComprobante no cumple con el valor permitido.'
  },
  'IEEH103': {
    'event': 'IEEH103',
    'message': 'El valor del atributo Mes no corresponde al mes registrado en el atributo FechaFolioFiscalVinculado, o al de un mes anterior de calendario.'
  },
  'IEEH104': {
    'event': 'IEEH104',
    'message': 'El valor del atributo Porcentaje no es mayor a 0.'
  },
  'IEEH105': {
    'event': 'IEEH105',
    'message': 'El valor del atributo ContraprestacionPagadaOperador es diferente al valor registrado en el Total del comprobante.'
  },
  'IEEH999': {
    'event': 'IEEH999',
    'message': 'Error no clasificado'
  },
  ## GCEH 1.0 Complement
  'GCEH101': {
    'event': 'GCEH101',
    'message': u"El atributo Version no tiene un valor válido.",
  },
  'GCEH102': {
    'event': 'GCEH102',
    'message': u"El atributo TipoDeComprobante no cumple con el valor permitido.",
  },
  'GCEH103': {
    'event': 'GCEH103',
    'message': u"El atributo FolioFiscalVinculado no se debe registrar cuando el atributo OrigenErogacion es Extranjero.",
  },
  'GCEH104': {
    'event': 'GCEH104',
    'message': u"El atributo RFCProveedor no se debe registrar por que no existe el atributo FolioFiscalVinculado.",
  },
  'GCEH105': {
    'event': 'GCEH105',
    'message': u"El atributo RFCProveedor debe registrarse por que existe el atributo FolioFiscalVinculado.",
  },
  'GCEH106': {
    'event': 'GCEH106',
    'message': u"El atributo MontoTotalIVA no se debe registrar por que no existe el atributo FolioFiscalVinculado.",
  },
  'GCEH107': {
    'event': 'GCEH107',
    'message': u"El atributo MontoTotalIVA debe registrarse por que existe el atributo FolioFiscalVinculado.",
  },
  'GCEH108': {
    'event': 'GCEH108',
    'message': u"El atributo NumeroPedimentoVinculado no se debe registrar cuando el atributo OrigenErogacion es Nacional.",
  },
  'GCEH109': {
    'event': 'GCEH109',
    'message': u"El atributo ClavePedimentoVinculado no se debe registrar por que no existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH110': {
    'event': 'GCEH110',
    'message': u"El atributo ClavePedimentoVinculado debe registrarse por que existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH111': {
    'event': 'GCEH111',
    'message': u"El atributo ClavePagoPedimento no se debe registrar por que no existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH112': {
    'event': 'GCEH112',
    'message': u"El atributo ClavePagoPedimento debe registrarse por que existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH113': {
    'event': 'GCEH113',
    'message': u"El atributo MontoIVAPedimento no se debe registrar por que no existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH114': {
    'event': 'GCEH114',
    'message': u"El atributo MontoIVAPedimento debe registrarse por que existe el atributo NumeroPedimentoVinculado.",
  },
  'GCEH115': {
    'event': 'GCEH115',
    'message': u"El valor del atributo Mes no corresponde al mes registrado en el atributo FechaFolioFiscalVinculado, o al de un mes anterior de calendario respecto a dicho atributo.",
  },
  'GCEH116': {
    'event': 'GCEH116',
    'message': u"El valor del atributo Porcentaje no es mayor a 0.",
  },
  'GCEH117': {
    'event': 'GCEH117',
    'message': u"El atributo ActividadRelacionada no se debe registrar por que no existen los atributos SubActividadRelacionada y TareaRelacionada.",
  },
  'GCEH118': {
    'event': 'GCEH118',
    'message': u"El atributo ActividadRelacionada debe registrarse por que existen los atributos SubActividadRelacionada y TareaRelacionada.",
  },
  'GCEH119': {
    'event': 'GCEH119',
    'message': u"El atributo SubActividadRelacionada no se debe registrar por que no existen los atributos ActividadRelacionada y TareaRelacionada.",
  },
  'GCEH120': {
    'event': 'GCEH120',
    'message': u"El atributo SubActividadRelacionada debe registrarse por que existen los atributos  ActividadRelacionada y TareaRelacionada.",
  },
  'GCEH121': {
    'event': 'GCEH121',
    'message': u"El atributo TareaRelacionada no se debe registrar por que no existen los atributos ActividadRelacionada y SubActividadRelacionada.",
  },
  'GCEH122': {
    'event': 'GCEH122',
    'message': u"El atributo TareaRelacionada debe registrarse por que existen los atributos ActividadRelacionada y SubActividadRelacionada.",
  },
  'GCEH123': {
    'event': 'GCEH123',
    'message': u"El valor del atributo ActividadRelacionada no contiene una clave del catálogo catCEH:Actividad.",
  },
  'GCEH124': {
    'event': 'GCEH124',
    'message': u"El valor del atributo SubActividadRelacionada no contiene una clave del catálogo catCEH:SubActividad donde la columna c_Actividad sea igual a la clave registrada en el atributo ActividadRelacionada.",
  },
  'GCEH125': {
    'event': 'GCEH125',
    'message': u"El valor del atributo TareaRelacionada no contiene una clave del catálogo catCEH:Tarea donde la columna c_Subactividad sea igual a la clave registrada en el atributo SubActividadRelacionada y la columna c_Actividad sea igual a la clave registrada en el atributo ActividadRelacionada.",
  },
  'GCEH126': {
    'event': 'GCEH126',
    'message': u"El atributo Campo no se debe registrar por que no existen los atributos Yacimiento y Pozo.",
  },
  'GCEH127': {
    'event': 'GCEH127',
    'message': u"El atributo Campo debe registrarse por que existen los atributos  Yacimiento y Pozo.",
  },
  'GCEH128': {
    'event': 'GCEH128',
    'message': u"El atributo Yacimiento no se debe registrar por que no existen los atributos Campo y Pozo.",
  },
  'GCEH129': {
    'event': 'GCEH129',
    'message': u"El atributo Yacimiento debe registrarse por que existen los atributos  Campo y Pozo.",
  },
  'GCEH130': {
    'event': 'GCEH130',
    'message': u"El atributo Pozo no se debe registrar por que no existen los atributos Campo y Yacimiento.",
  },
  'GCEH131': {
    'event': 'GCEH131',
    'message': u"El atributo Pozo debe registrarse por que existen los atributos  Campo y Yacimiento.",
  },
  'GCEH132': {
    'event': 'GCEH132',
    'message': u"El atributo FechaFolioFiscalVinculado debe registrarse por que existe el atributo  FolioFiscalVinculado.",
  },
  'GCEH133': {
    'event': 'GCEH133',
    'message': u"El número de pedimento es inválido.",
  },
  'GCEH996': {
    'event': 'GCEH996',
    'message': u"Solo debe existir un elemento gceh:GastosHidrocarburos.",
  },
  'GCEH997': {
    'event': 'GCEH997',
    'message': u"El elemento gceh:GastosHidrocarburos debe ser un hijo de cfdi:Complemento.",
  },
  'GCEH998': {
    'event': 'GCEH998',
    'message': u"El valor del atributo Mes es inválido.",
  },
  'GCEH999': {
    'event': 'GCEH999',
    'message': u"Error no clasificado",
  },
  # Reglas de validacion para Retenciones Extra
  'RET101': {
    'event': 'RET101',
    'message': u'Existe un campo que contiene números negativos'
  },
  'RET999': {
    'event': 'RET999',
    'message': u'Error no clasificado '
  },
  # Reglas de Validacion para el complemento De Retenciones Planes De Retiro 1.1
  'PDR101': {
    'event': 'PDR101',
    'message': 'El atributo "MontTotExentRetiradoAnioInmAnt" debe de existir.'
  },
  'PDR102': {
    'event': 'PDR102',
    'message': 'El atributo "MontTotExedenteAnioInmAnt" debe de existir'
  },
  'PDR103': {
    'event': 'PDR103',
    'message': 'El valor de este campo debe ser igual a la suma de "MontTotExentRetiradoAnioInmAnt" mas "MontTotExedenteAnioInmAnt"'
  },
  'PDR104': {
    'event': 'PDR104',
    'message': 'El valor de cada uno de los campos "TipoAportacionODeposito" debe ser diferente entre si.'
  },
  'PDR999': {
    'event': 'PDR999',
    'message': 'Error no clasificado'
  },

  # Validación de Fechas
  'DTL101': {
    'event': 'DTL101',
    'message': u"Fecha Inválida.",
  },
  'DTL999': {
    'event': 'DTL999',
    'message': "Error no clasificado.",
  },
  # IRMGCT
  'IRMGCT101': {
    'event': 'IRMGCT101',
    'message': u'El atributo Version no tiene un valor válido.',
  },
  'IRMGCT102': {
    'event': 'IRMGCT102',
    'message': 'El atributo TipoDeComprobante no cumple con el valor permitido.',
  },
  'IRMGCT103': {
    'event': 'IRMGCT103',
    'message': u'El elemento "IdentificacionDelGasto" no se debe registrar.',
  },
  'IRMGCT104': {
    'event': 'IRMGCT104',
    'message': 'El elemento "DispersionDelRecurso" se debe registrar'
  },
  'IRMGCT105': {
    'event': 'IRMGCT105',
    'message': 'El elemento "IDispersionDelRecurso" no se debe registrar',
  },
  'IRMGCT106': {
    'event': 'IRMGCT106',
    'message': 'El elemento "IdentificacionDelGasto" se debe registrar',
  },
  'IRMGCT107': {
    'event': 'IRMGCT107',
    'message': 'El atributo "ReintegroRemanente" debe registrarse porque existe el atributo "Remanente".',
  },
  'IRMGCT108': {
    'event': 'IRMGCT108',
    'message': 'El atributo "ReintegroRemanFecha" debe registrarse porque existe el atributo "ReintegroRemanente".',
  },
  'IRMGCT109': {
    'event': 'IRMGCT109',
    'message': 'El atributo "FechaDeGasto" debe registrarse por que existe el atributo "NumFolioDoc".',
  },
  'IRMGCT110': {
    'event': 'IRMGCT110',
    'message': 'El atributo "ImporteGasto" debe registrarse por que existe el atributo "NumFolioDoc".',
  },
  'IRMGCT999': {
    'event': 'IRMGCT999',
    'message': 'Error no clasificado',
  },
  # Por cuenta de Terceros
  'PCT101': {
    'event': 'PCT101',
    'message': 'El rfc del nodo terceros:PorCuentadeTerceros no cuenta con las obligaciones necesarias para emitir el comprobante',
  },
  'PCT102': {
    'event': 'PCT102',
    'message': u'El codigoPostal del elemento "t_UbicacionFiscal" no se encuentra en el catálogo c_CodigoPostal o no tiene la marca de identificación fronteriza.',
  },
  'PCT103': {
    'event': 'PCT103',
    'message': u'(Complemento por cuenta de terceros) No aplica Estímulo Franja Fronteriza para la clave de producto o servicio.',
  },
  'PCT104': {
    'event': 'PCT104',
    'message': u'(Complemento por cuenta de terceros), El valor tasa del nodo terceros:Impuestos/terceros:Traslados/terceros:Traslado debe registrar el valor 8.000000.',
  },
  'PCT105': {
    'event': 'PCT105',
    'message': u'El valor TasaOCouta del nodo cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado debe registrar el valor 0.080000, para el Impuesto IVA.',
  },
  'PCT106': {
    'event': 'PCT106',
    'message': 'El rfc del nodo terceros:PorCuentadeTerceros no cuenta con las obligaciones necesarias para emitir el comprobante con estimulo fronterizo',
  },
  'PCT107': {
    'event': 'PCT107',
    'message': u'El rfc del nodo terceros:PorCuentadeTerceros no puede hacer uso de los RFC XAXX010101000 o XEXX010101000.',
  },
  'PCT999': {
    'event': 'PCT999',
    'message': u'Error no clasificado.',
  },
  #Servicios Plataformas Tecnologicas
  'SPT101': {
    'event':'SPT101',
    'message':u'El atributo Version tiene un valor inválido.',
  },
  'SPT102': {
    'event':'SPT102',
    'message':u'El atributo CveRetenc contiene una clave distinta a "26" (Servicios mediante Plataformas Tecnológicas)',
  },
  'SPT103': {
    'event':'SPT103',
    'message':u'Se registró el atributo DescRetenc.',
  },
  'SPT104': {
    'event':'SPT104',
    'message':u'El complemento “Servicios Plataformas Tecnológicas” no debe existir cuando el valor del atributo Nacionalidad es distinto de "Nacional".',
  },
  'SPT105': {
    'event':'SPT105',
    'message':u'El atributo RFCReceptor es inválido según la lista de RFC inscritos no cancelados en el SAT (l_RFC).',
  },
  'SPT106': {
    'event':'SPT106',
    'message':u'El valor del nodo MesFin es diferente al valor del atributo MesIni o mayor al mes en curso.',
  },
  'SPT107': {
    'event':'SPT107',
    'message':u'El valor del atributo Ejerc es menor a 2019 o mayor al valor del año en curso.',
  },
  'SPT108': {
    'event':'SPT108',
    'message':u'El valor del atributo montoTotOperacion es diferente al valor registrado en el atributo MonTotServSIVA.',
  },
  'SPT109': {
    'event':'SPT109',
    'message':u'El valor del atributo montoTotGrav es diferente al valor del atributo montoTotOperacion.',
  },
  'SPT110': {
    'event':'SPT110',
    'message':u'El valor del atributo montoTotExent es diferente de 0.00.',
  },
  'SPT111': {
    'event':'SPT111',
    'message':u'El valor del atributo montoTotRet es diferente de la suma de los atributos montoRet del nodo ImpRetenidos.',
  },
  'SPT112': {
    'event':'SPT112',
    'message':u'Existe más de 1 nodo de ImpRetenidos para cada tipo de impuesto ISR (01) o para IVA (02).',
  },
  'SPT113': {
    'event':'SPT113',
    'message':u'El valor del atributo BaseRet es diferente al valor del atributo montoTotOperacion o es diferente del valor contenido en uno de los rangos establecidos en los catálogos "c_RangoSemRet " o " c_RangoMenRet ".',
  },
  'SPT114': {
    'event':'SPT114',
    'message':u'El valor del atributo montoRet se encuentra fuera del rango establecido de acuerdo a la clave del atributo “Periodicidad”, registrada en el complemento o no corresponde con el factor aplicable del catálogo correspondiente.',
  },
  'SPT115': {
    'event':'SPT115',
    'message':u'El atributo Periodicidad tiene un valor no permitido.',
  },
  'SPT116': {
    'event':'SPT116',
    'message':u'El NumServ registrado es diferente de la suma de los elementos hijo del nodo “Servicios”.',
  },
  'SPT117': {
    'event':'SPT117',
    'message':u'El valor del atributo MonTotServSIVA es diferente de la suma de los atributos “PrecioServSinIVA” registrados en los nodos hijos “DetallesDelServicio”.',
  },
  'SPT118': {
    'event':'SPT118',
    'message':u'El valor del atributo TotalIVATrasladado es diferente de la suma de los atributos “Importe” del nodo “ImpuestosTrasladadosdelServicio”.',
  },
  'SPT119': {
    'event':'SPT119',
    'message':u'El valor del atributo TotalIVARetenido es diferente el producto obtenido al multiplicar el valor del atributo “MonTotServSIVA” por la tasa de retención de IVA del catálogo “c_RangoMenRet” o “c_RangoSemRet” según corresponda.',
  },
  'SPT120': {
    'event':'SPT120',
    'message':u'El valor del atributo TotalISRRetenido es diferente del producto obtenido al multiplicar el valor del atributo “MonTotServSIVA” por la tasa de retención de ISR del catálogo “c_RangoMenRet” o “c_RangoSemRet” según corresponda de acuerdo al rango en el que se encuentre el valor del atributo “MonTotServSIVA”.',
  },
  'SPT121': {
    'event':'SPT121',
    'message':u'El valor del atributo DifIVAEntregadoPrestServ es distinto del producto obtenido de la diferencia entre el valor del atributo “TotalIVATrasladado” y el valor de atributo “TotaldeIVARetenido”.',
  },
  'SPT122': {
    'event':'SPT122',
    'message':u'El valor del atributo MonTotalporUsoPlataforma es diferente la suma de los atributos “Importe” de los nodos “ComisiondelServicio”.',
  },
  'SPT123': {
    'event':'SPT123',
    'message':u'Se debe registrar el MonTotalContribucionGubernamental siempre que exista el nodo “ContribucionGubernamental” o su valor es diferente al resultado de la suma del atributo “ImpContrib” de los nodos hijos “ContribucionGubernamental” del nodo hijo “DetallesDelServicio”.',
  },
  'SPT124': {
    'event':'SPT124',
    'message':u'La clave registrada en el atributo FormaPagoServ es diferente a las contenidas en el catálogo c_FormaPagoServ.',
  },
  'SPT125': {
    'event':'SPT125',
    'message':u'El atributo TipoDeServ tiene una clave diferente a las establecidas en el catálogo c_TipoDeServ.',
  },
  'SPT126': {
    'event':'SPT126',
    'message':u'El valor del atributo SubTipServ es diferente a la relación del catálogo “c_SubTipoServ” con el tipo de servicio.',
  },
  'SPT127': {
    'event':'SPT127',
    'message':u'El valor capturado en el atributo RFCTerceroAutorizado es inválido según la lista de RFC inscritos no cancelados en el SAT (l_RFC).',
  },
  'SPT128': {
    'event':'SPT128',
    'message':u'El valor del atributo MesIni es diferente al valor registrado en el atributo FechaServ del CFDI de Retenciones o mayor al mes en curso.',
  },
  'SPT129': {
    'event':'SPT129',
    'message':u'El valor del atributo Base del nodo “ImpuestosTrasladadosdelServicio” es diferente al valor del atributo “PrecioServSinIVA”.',
  },
  'SPT130': {
    'event':'SPT130',
    'message':u'El valor del atributo Importe, del nodo “ImpuestosTrasladadosdelServicio es diferente del producto obtenido al multiplicar el valor del atributo “Base” por el valor del atributo “TasaCuota” del nodo hijo “ImpuestosTrasladadosdelServicio”.',
  },
  'SPT131': {
    'event':'SPT131',
    'message':u'El valor del atributo EntidadDondePagaLaContribucion es diferente de la clave del catálogo c_EntidadesFederativas.',
  },
  'SPT132': {
    'event':'SPT132',
    'message':u'El valor del atributo Importe del nodo “ComisiondelServicio” es igual a cero.',
  },
  'SPT999': {
    'event':'SPT999',
    'message':u'Error no clasificado.',
  },
  'CCO101': {
    'event': 'CCO101',
    'message': "El RFC enajenante de combustibles del nodo consumodecombustibles11:ConceptoConsumoDeCombustibles no puede hacer uso del impuesto IVA 0.080000",
  },
  'CCO102': {
    'event': 'CCO102',
    'message': "El valor del atributo TasaOCouta del nodo consumodecombustibles11:Determinado debe contener el valor '0.080000' para el impuesto IVA",
  },
  'CCO103': {
    'event': 'CCO103',
    'message': "El RFC enajenante de combustibles del nodo consumodecombustibles11:ConceptoConsumoDeCombustibles no cuenta con las obligaciones necesarias para facturar.",
  },
  'CCO999': {
    'event': 'CCO999',
    'message': "Error no clasificado.",
  },



  'DES101':{
    'event': 'DES101',
    'message': 'TipoSerie no contiene un valor del catálogo c_TipoSerie',
  },
  'DES999':{
    'event': 'DES999',
    'message': 'Error no clasificado',
  },


  'NOT101': {
    'event': 'NOT101',
    'message': "TipoInmueble no contiene un valor del catálogo c_TipoInmueble",
  },
  'NOT102': {
    'event': 'NOT102',
    'message': "NotariosPublicos:DescInmuebles:DesInmueble:Estado no contiene un valor del catálogo c_EntidadFederativa",
  },
  'NOT103': {
    'event': 'NOT103',
    'message': "NotariosPublicos:DescInmuebles:DesInmueble:Pais no contiene un valor del catálogo c_Pais",
  },
  'NOT104': {
    'event': 'NOT104',
    'message': "NotariosPublicos:DatosNotario:EntidadFederativa no contiene un valor del catálogo c_EntidadFederativa",
  },
  'NOT999': {
    'event': 'NOT999',
    'message': "Error no clasificado",
  },


  'OBR101': {
    'event': 'OBR101',
    'message': "TipoBien no contiene un valor del catálogo c_TipoBien",
  },
  'OBR102': {
    'event': 'OBR102',
    'message': "TituloAdquirido no contiene un valor del catálogo c_TituloAdquirido",
  },
  'OBR103': {
    'event': 'OBR103',
    'message': "CaracteristicasDeObraoPieza no contiene un valor del catálogo c_CaracteristicasDeObraoPieza",
  },
  'OBR999': {
    'event': 'OBR999',
    'message': "Error no clasificado",
  },


  'REN101': {
    'event': 'REN101',
    'message': "TipoDeDecreto no contiene un valor del catálogo c_TipoDecreto",
  },
  'REN102': {
    'event': 'REN102',
    'message': "DecretoRenovVehicular:VehEnaj no contiene un valor del catálogo c_VehiculoEnajenado",
  },
  'REN103': {
    'event': 'REN103',
    'message': "DecretoSustitVehicular:VehEnaj no contiene un valor del catálogo c_VehiculoEnajenado",
  },
  'REN104': {
    'event': 'REN104',
    'message': "DecretoRenovVehicular:VehiculosUsadosEnajenadoPermAlFab:TipoVeh no contiene un valor del catálogo c_TipoVehiculoRenovacion",
  },
  'REN105': {
    'event': 'REN105',
    'message': "DecretoSustitVehicular:VehiculoUsadoEnajenadoPermAlFab:TipoVeh no contiene un valor del catálogo c_TipoVehiculoSustitucion",
  },
  'REN999': {
    'event': 'REN999',
    'message': "Error no clasificado",
  },




}