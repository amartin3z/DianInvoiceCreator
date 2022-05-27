# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

INVOICE_STATUS = (
  ('E', 'Error'),
  ('U', 'Uploaded'),
  ('P', 'Processed'),
  ('S', 'Stamped'),
  ('F', 'Finished'),
  ('C', 'Cancelled'),
  ('O', 'Other'),
)

INVOICE_STATUS_SAT = (
  ('V', 'Valid'),
  ('C', 'Cancelled'),
)

INVOICE_TYPE = (
  ('I', 'Ingreso'),  
  ('E', 'Egreso'),
  #('33', 'Ingreso'),  
  #('61', 'Egreso'),
  ('T', 'Traslado'),
  ('N', u'Nómina'),
  ('P', 'Pago'),
)

PAYROLL_TYPE = (
  ('O', 'Ordinaria'),  
  ('E', 'ExtraOrdinaria'),
)

PAYMENT_WAY = (
  ('01', 'Efectivo'),
  ('02', 'Cheque nominativo'),
  ('03', 'Transferencia electrónica de fondos'),
  ('04', 'Tarjeta de crédito'),
  ('05', 'Monedero electrónico'),
  ('06', 'Dinero electrónico'),
  ('08', 'Vales de despensa'),
  ('12', 'Dación en pago'),
  ('13', 'Pago por subrogación'),
  ('14', 'Pago por consignación'),
  ('15', 'Condonación'),
  ('17', 'Compensación'),
  ('23', 'Novación'),
  ('24', 'Confusión'),
  ('25', 'Remisión de deuda'),
  ('26', 'Prescripción o caducidad'),
  ('27', 'A satisfacción del acreedor'),
  ('28', 'Tarjeta de débito'),
  ('29', 'Tarjeta de servicios'),
  ('30', 'Aplicación de anticipos'),
  ('31', 'Intermediario pagos'),
  ('99', 'Por definir'),
)

PAYMENT_METHOD = (
  ('PUE', 'Pago en una sola exhibición'),
  ('PPD', 'Pago en parcialidades o diferido'),
)

REGIMEN_TYPE = (  
  ('02', '02 - Sueldos'),
  ('03', '03 - Jubilados'),
  ('04', '04 - Pensionados'),
  ('05', '05 - Asimilados Miembros Sociedades Cooperativas Produccion'),
  ('06', '06 - Asimilados Integrantes Sociedades Asociaciones Civiles'),
  ('07', '07 - Asimilados Miembros consejos'),
  ('08', '08 - Asimilados comisionistas'),
  ('09', '09 - Asimilados Honorarios'),
  ('10', '10 - Asimilados acciones'),
  ('11', '11 - Asimilados otros'),
  ('12', '12 - Jubilados o Pensionados'),
  ('99', '99 - Otro Regimen'),
)

WORKING_TYPE = (
  ('01', '01 - Diurna'),
  ('02', '02 - Nocturna'),
  ('03', '03 - Mixta'),
  ('04', '04 - Por hora'),
  ('05', '05 - Reducida'),
  ('06', '06 - Continuada'),
  ('07', '07 - Partida'),
  ('08', '08 - Por turnos'),
  ('99', '99 - Otra Jornada'),
)

RISK_TYPE = (
  ('1', '1 Clase I'),
  ('2', '2 Clase II'),
  ('3', '3 Clase III'),
  ('4', '4 Clase IV'),
  ('5', '5 Clase V'),
  ('99', '99 No aplica'),
)

OTHERPAYMENT_TYPE = (  
  ('001', 'Reintegro de ISR pagado en exceso (siempre que no haya sido enterado al SAT).'),
  ('002', 'Subsidio para el empleo (efectivamente entregado al trabajador).'),
  ('003', 'Viáticos (entregados al trabajador).'),
  ('004', 'Aplicación de saldo a favor por compensación anual.'),
  ('005', 'Reintegro de ISR retenido en exceso de ejercicio anterior (siempre que no haya sido enterado al SAT).'),
  ('999', 'Pagos distintos a los listados y que no deben considerarse como ingreso por sueldos, salarios o ingresos asimilados.'),
)

INABILITY_TYPE = (
  ('01', '01 - Riesgo de trabajo.'),
  ('02', '02 - Enfermedad en general.'),
  ('03', '03 - Maternidad.'),
)

PERIODICITY_TYPE = (
  ('01', 'Diario'),
  ('02', 'Semanal'),
  ('03', 'Catorcenal'),
  ('04', 'Quincenal'),
  ('05', 'Mensual'),
  ('06', 'Bimestral'),
  ('07', 'Unidad obra'),
  ('08', 'Comisión'),
  ('09', 'Precio alzado'),
  ('10', 'Decenal'),
  ('99', 'Otra Periodicidad'),
)

CONTRACT_TYPE = (
  ('01', 'Contrato de trabajo por tiempo indeterminado'),
  ('02', 'Contrato de trabajo para obra determinada'),
  ('03', 'Contrato de trabajo por tiempo determinado'),
  ('04', 'Contrato de trabajo por temporada'),
  ('05', 'Contrato de trabajo sujeto a prueba'),
  ('06', 'Contrato de trabajo con capacitación inicial'),
  ('07', 'Modalidad de contratación por pago de hora laborada'),
  ('08', 'Modalidad de trabajo por comisión laboral'),
  ('09', 'Modalidades de contratación donde no existe relación de trabajo'),
  ('10', 'Jubilación, pensión, retiro.'),
  ('99', 'Otro contrato'),
)

STATES = (
  ('AGU', 'Aguascalientes'),
  ('BCN', 'Baja California'),
  ('BCS', 'Baja California Sur'),
  ('CAM', 'Campeche'),
  ('CHP', 'Chiapas'),
  ('CHH', 'Chihuahua'),
  ('COA', 'Coahuila'),
  ('COL', 'Colima'),
  ('DIF', 'Ciudad de México'),
  ('DUR', 'Durango'),
  ('GUA', 'Guanajuato'),
  ('GRO', 'Guerrero'),
  ('HID', 'Hidalgo'),
  ('JAL', 'Jalisco'),
  ('MEX', 'Estado de México'),
  ('MIC', 'Michoacán'),
  ('MOR', 'Morelos'),
  ('NAY', 'Nayarit'),
  ('NLE', 'Nuevo Leon'),
  ('OAX', 'Oaxaca'),
  ('PUE', 'Puebla'),
  ('QUE', 'Querétaro'),
  ('ROO', 'Quintana Roo'),
  ('SLP', 'San Luis Potosí'),
  ('SIN', 'Sinaloa'),
  ('SON', 'Sonora'),
  ('TAB', 'Tabasco'),
  ('TAM', 'Tamaulipas'),
  ('TLA', 'Tlaxcala'),
  ('VER', 'Veracruz'),
  ('YUC', 'Yucatán'),
  ('ZAC', 'Zacatecas'),
)

PERCEPTION_TYPE = (
  ('001', 'Sueldos, Salarios  Rayas y Jornales'),
  ('002', 'Gratificación Anual (Aguinaldo)'),
  ('003', 'Participación de los Trabajadores en las Utilidades PTU'),
  ('004', 'Reembolso de Gastos Médicos Dentales y Hospitalarios'),
  ('005', 'Fondo de Ahorro'),
  ('006', 'Caja de ahorro'),
  ('009', 'Contribuciones a Cargo del Trabajador Pagadas por el Patrón'),
  ('010', 'Premios por puntualidad'),
  ('011', 'Prima de Seguro de vida'),
  ('012', 'Seguro de Gastos Médicos Mayores'),
  ('013', 'Cuotas Sindicales Pagadas por el Patrón'),
  ('014', 'Subsidios por incapacidad'),
  ('015', 'Becas para trabajadores y/o hijos'),
  ('019', 'Horas extra'),
  ('020', 'Prima dominical'),
  ('021', 'Prima vacacional'),
  ('022', 'Prima por antigüedad'),
  ('023', 'Pagos por separación'),
  ('024', 'Seguro de retiro'),
  ('025', 'Indemnizaciones'),
  ('026', 'Reembolso por funeral'),
  ('027', 'Cuotas de seguridad social pagadas por el patrón'),
  ('028', 'Comisiones'),
  ('029', 'Vales de despensa'),
  ('030', 'Vales de restaurante'),
  ('031', 'Vales de gasolina'),
  ('032', 'Vales de ropa'),
  ('033', 'Ayuda para renta'),
  ('034', 'Ayuda para artículos escolares'),
  ('035', 'Ayuda para anteojos'),
  ('036', 'Ayuda para transporte'),
  ('037', 'Ayuda para gastos de funeral'),
  ('038', 'Otros ingresos por salarios'),
  ('039', 'Jubilaciones, pensiones o haberes de retiro'),
  ('044', 'Jubilaciones, pensiones o haberes de retiro en parcialidades'),
  ('045', 'Ingresos en acciones o títulos valor que representan bienes'),
  ('046', 'Ingresos asimilados a salarios'),
  ('047', 'Alimentación'),
  ('048', 'Habitación'),
  ('049', 'Premios por asistencia'),
  ('050', 'Viáticos'),
  ('051',	'Pagos por gratificaciones, primas, compensaciones, recompensas u otros a extrabajadores derivados de jubilación en parcialidades'),
  ('052',	'Pagos que se realicen a extrabajadores que obtengan una jubilación en parcialidades derivados de la ejecución de resoluciones judicial o de un laudo'),
  ('053',	'Pagos que se realicen a extrabajadores que obtengan una jubilación en una sola exhibición derivados de la ejecución de resoluciones judicial o de un laudo'),
)

DEDUCTION_TYPE = (
  ('001', 'Seguridad social'),
  ('002', 'ISR'),
  ('003', 'Aportaciones a retiro, cesantía en edad avanzada y vejez.'),
  ('004', 'Otros'),
  ('005', 'Aportaciones a Fondo de vivienda'),
  ('006', 'Descuento por incapacidad'),
  ('007', 'Pensión alimenticia'),
  ('008', 'Renta'),
  ('009', 'Préstamos provenientes del Fondo Nacional de la Vivienda para los Trabajadores'),
  ('010', 'Pago por crédito de vivienda'),
  ('011', 'Pago de abonos INFONACOT'),
  ('012', 'Anticipo de salarios'),
  ('013', 'Pagos hechos con exceso al trabajador'),
  ('014', 'Errores'),
  ('015', 'Pérdidas'),
  ('016', 'Averías'),
  ('017', 'Adquisición de artículos producidos por la empresa o establecimiento'),
  ('018', 'Cuotas para la constitución y fomento de sociedades cooperativas y de cajas de ahorro'),
  ('019', 'Cuotas sindicales'),
  ('020', 'Ausencia (Ausentismo)'),
  ('021', 'Cuotas obrero patronales'),
  ('022', 'Impuestos Locales'),
  ('023', 'Aportaciones voluntarias'),
  ('024', 'Ajuste en Gratificación Anual (Aguinaldo) Exento'),
  ('025', 'Ajuste en Gratificación Anual (Aguinaldo) Gravado'),
  ('026', 'Ajuste en Participación de los Trabajadores en las Utilidades PTU Exento'),
  ('027', 'Ajuste en Participación de los Trabajadores en las Utilidades PTU Gravado'),
  ('028', 'Ajuste en Reembolso de Gastos Médicos Dentales y Hospitalarios Exento'),
  ('029', 'Ajuste en Fondo de ahorro Exento'),
  ('030', 'Ajuste en Caja de ahorro Exento'),
  ('031', 'Ajuste en Contribuciones a Cargo del Trabajador Pagadas por el Patrón Exento'),
  ('032', 'Ajuste en Premios por puntualidad Gravado'),
  ('033', 'Ajuste en Prima de Seguro de vida Exento'),
  ('034', 'Ajuste en Seguro de Gastos Médicos Mayores Exento'),
  ('035', 'Ajuste en Cuotas Sindicales Pagadas por el Patrón Exento'),
  ('036', 'Ajuste en Subsidios por incapacidad Exento'),
  ('037', 'Ajuste en Becas para trabajadores y/o hijos Exento'),
  ('038', 'Ajuste en Horas extra Exento'),
  ('039', 'Ajuste en Horas extra Gravado'),
  ('040', 'Ajuste en Prima dominical Exento'),
  ('041', 'Ajuste en Prima dominical Gravado'),
  ('042', 'Ajuste en Prima vacacional Exento'),
  ('043', 'Ajuste en Prima vacacional Gravado'),
  ('044', 'Ajuste en Prima por antigüedad Exento'),
  ('045', 'Ajuste en Prima por antigüedad Gravado'),
  ('046', 'Ajuste en Pagos por separación Exento'),
  ('047', 'Ajuste en Pagos por separación Gravado'),
  ('048', 'Ajuste en Seguro de retiro Exento'),
  ('049', 'Ajuste en Indemnizaciones Exento'),
  ('050', 'Ajuste en Indemnizaciones Gravado'),
  ('051', 'Ajuste en Reembolso por funeral Exento'),
  ('052', 'Ajuste en Cuotas de seguridad social pagadas por el patrón Exento'),
  ('053', 'Ajuste en Comisiones Gravado'),
  ('054', 'Ajuste en Vales de despensa Exento'),
  ('055', 'Ajuste en Vales de restaurante Exento'),
  ('056', 'Ajuste en Vales de gasolina Exento'),
  ('057', 'Ajuste en Vales de ropa Exento'),
  ('058', 'Ajuste en Ayuda para renta Exento'),
  ('059', 'Ajuste en Ayuda para artículos escolares Exento'),
  ('060', 'Ajuste en Ayuda para anteojos Exento'),
  ('061', 'Ajuste en Ayuda para transporte Exento'),
  ('062', 'Ajuste en Ayuda para gastos de funeral Exento'),
  ('063', 'Ajuste en Otros ingresos por salarios Exento'),
  ('064', 'Ajuste en Otros ingresos por salarios Gravado'),
  ('065', 'Ajuste en Jubilaciones, pensiones o haberes de retiro Exento'),
  ('066', 'Ajuste en Jubilaciones, pensiones o haberes de retiro Gravado'),
  ('067', 'Ajuste en Pagos por separación Acumulable'),
  ('068', 'Ajuste en Pagos por separación No acumulable'),
  ('069', 'Ajuste en Jubilaciones, pensiones o haberes de retiro Acumulable'),
  ('070', 'Ajuste en Jubilaciones, pensiones o haberes de retiro No acumulable'),
  ('071', 'Ajuste en Subsidio para el empleo (efectivamente entregado al trabajador)'),
  ('072', 'Ajuste en Ingresos en acciones o títulos valor que representan bienes Exento'),
  ('073', 'Ajuste en Ingresos en acciones o títulos valor que representan bienes Gravado'),
  ('074', 'Ajuste en Alimentación Exento'),
  ('075', 'Ajuste en Alimentación Gravado'),
  ('076', 'Ajuste en Habitación Exento'),
  ('077', 'Ajuste en Habitación Gravado'),
  ('078', 'Ajuste en Premios por asistencia'),
  ('079', 'Ajuste en Pagos distintos a los listados y que no deben considerarse como ingreso por sueldos, salarios o ingresos asimilados.'),
  ('080', 'Ajuste en Viáticos gravados'),
  ('081', 'Ajuste en Viáticos (entregados al trabajador)'),
  ('082', 'Ajuste en Fondo de ahorro Gravado'),
  ('083', 'Ajuste en Caja de ahorro Gravado'),
  ('084', 'Ajuste en Prima de Seguro de vida Gravado'),
  ('085', 'Ajuste en Seguro de Gastos Médicos Mayores Gravado'),
  ('086', 'Ajuste en Subsidios por incapacidad Gravado'),
  ('087', 'Ajuste en Becas para trabajadores y/o hijos Gravado'),
  ('088', 'Ajuste en Seguro de retiro Gravado'),
  ('089', 'Ajuste en Vales de despensa Gravado'),
  ('090', 'Ajuste en Vales de restaurante Gravado'),
  ('091', 'Ajuste en Vales de gasolina Gravado'),
  ('092', 'Ajuste en Vales de ropa Gravado'),
  ('093', 'Ajuste en Ayuda para renta Gravado'),
  ('094', 'Ajuste en Ayuda para artículos escolares Gravado'),
  ('095', 'Ajuste en Ayuda para anteojos Gravado'),
  ('096', 'Ajuste en Ayuda para transporte Gravado'),
  ('097', 'Ajuste en Ayuda para gastos de funeral Gravado'),
  ('098', 'Ajuste a ingresos asimilados a salarios gravados'),
  ('099', 'Ajuste a ingresos por sueldos y salarios gravados'),
  ('100', 'Ajuste en Viáticos exentos'),
  ('101', 'ISR Retenido de ejercicio anterior'),
  ('102',	'Ajuste a pagos por gratificaciones, primas, compensaciones, recompensas u otros a extrabajadores derivados de jubilación en parcialidades, gravados'),
  ('103',	'Ajuste a pagos que se realicen a extrabajadores que obtengan una jubilación en parcialidades derivados de la ejecución de una resolución judicial o de un laudo gravados'),
  ('104',	'Ajuste a pagos que se realicen a extrabajadores que obtengan una jubilación en parcialidades derivados de la ejecución de una resolución judicial o de un laudo exentos'),
  ('105',	'Ajuste a pagos que se realicen a extrabajadores que obtengan una jubilación en una sola exhibición derivados de la ejecución de una resolución judicial o de un laudo gravados'),
  ('106',	'Ajuste a pagos que se realicen a extrabajadores que obtengan una jubilación en una sola exhibición derivados de la ejecución de una resolución judicial o de un laudo exentos')

)

CURRENCIES = (
  ('MXN', 'MXN'),
  ('USD', 'USD'),
)

USE_CFDI = (
  ('G01', u'Adquisición de mercancias'),
  ('G02', u'Devoluciones, descuentos o bonificaciones'),
  ('G03', u'Gastos en general'),
  ('I01', u'Construcciones'),
  ('I02', u'Mobilario y equipo de oficina por inversiones'),
  ('I03', u'Equipo de transporte'),
  ('I04', u'Equipo de computo y accesorios'),
  ('I05', u'Dados, troqueles, moldes, matrices y herramental'),
  ('I06', u'Comunicaciones telefónicas'),
  ('I07', u'Comunicaciones satelitales'),
  ('I08', u'Otra maquinaria y equipo'),
  ('D01', u'Honorarios médicos, dentales y gastos hospitalarios.'),
  ('D02', u'Gastos médicos por incapacidad o discapacidad'),
  ('D03', u'Gastos funerales.'),
  ('D04', u'Donativos.'),
  ('D05', u'Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación).'),
  ('D06', u'Aportaciones voluntarias al SAR.'),
  ('D07', u'Primas por seguros de gastos médicos.'),
  ('D08', u'Gastos de transportación escolar obligatoria.'),
  ('D09', u'Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.'),
  ('D10', u'Pagos por servicios educativos (colegiaturas)'),
  ('P01', u'Por definir'),
)

TAX_REGIME = (
 ('601', u'General de Ley Personas Morales'),
 ('603', u'Personas Morales con Fines no Lucrativos'),
 ('605', u'Sueldos y Salarios e Ingresos Asimilados a Salarios'),
 ('606', u'Arrendamiento'),
 ('608', u'Demás ingresos'),
 ('609', u'Consolidación'),
 ('610', u'Residentes en el Extranjero sin Establecimiento Permanente en México'),
 ('611', u'Ingresos por Dividendos (socios y accionistas)'),
 ('612', u'Personas Físicas con Actividades Empresariales y Profesionales'),
 ('614', u'Ingresos por intereses'),
 ('616', u'Sin obligaciones fiscales'),
 ('620', u'Sociedades Cooperativas de Producción que optan por diferir sus ingresos'),
 ('621', u'Incorporación Fiscal'),
 ('622', u'Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras'),
 ('623', u'Opcional para Grupos de Sociedades'),
 ('624', u'Coordinados'),
 ('628', u'Hidrocarburos'),
 ('607', u'Régimen de Enajenación o Adquisición de Bienes'),
 ('629', u'De los Regímenes Fiscales Preferentes y de las Empresas Multinacionales'),
 ('630', u'Enajenación de acciones en bolsa de valores'),
 ('615', u'Régimen de los ingresos por obtención de premios'), 
)

LOG_MODULES = {
  'S': _('Create invoice'),
  'I': _(u'Manual billing'),
  'D': _('Download files'),
  'P': 'Proveedores',
  'A': u'Cancelación',
  'U': _('Users'),
  'L': 'Logs',
  'C': _('Business'),
  'O': _('Other'),
}