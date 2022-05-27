from django.conf import settings
from django.conf import settings as dj_settings
from django.contrib.auth.models import User
from app.core.models import Business
from datetime import datetime, timedelta
import json
from lxml import etree
import re
import os
import qrcode
import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, SimpleDocTemplate, Frame, Paragraph, Image, Spacer, Table, TableStyle)
from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import inch, mm, cm
import sys
import traceback
from decimal import Decimal
from .moneda import numero_a_letras
from reportlab.lib.utils import ImageReader
from pdb import set_trace

from app.sat.models import Moneda, FormaPago, MetodoPago, UsoCFDI, RegimenFiscal, TipoDeComprobante

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
  reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR))
  #~ STANDARD
  FONT_NAME = 'Lato-Light'
  FONT_FILENAME = 'Lato-Light.ttf'
  
  #~ BOLD
  FONT_NAME_BOLD = 'Lato-Bold'
  FONT_FILENAME_BOLD = 'Lato-Bold.ttf'
  
  #~ Register font from ".ttf" file.
  pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_FILENAME))
  pdfmetrics.registerFont(TTFont(FONT_NAME_BOLD, FONT_FILENAME_BOLD))
except Exception as e:
  print("Error configurando el tipo de fuente | {}".format(str(e)))

HEADERS = ParagraphStyle('HEADERS', fontName=FONT_NAME_BOLD, fontSize=8, leading=10, alignment=TA_CENTER, spaceAfter=0, spaceBefore=0, textColor='white')
HEADER_LEFT = ParagraphStyle('HEADER_LEFT', fontName=FONT_NAME_BOLD, fontSize=8, leading=10, alignment=TA_LEFT, spaceAfter=0, spaceBefore=0, textColor='white')
FOLIO_STYLE = ParagraphStyle('FOLIO_STYLE', fontName=FONT_NAME, fontSize=8, leading=9, alignment=TA_RIGHT, spaceAfter=0, spaceBefore=0, textColor='red')
CONTENT_CENTER = ParagraphStyle('CONTENT_CENTER', fontName=FONT_NAME, fontSize=7, leading=8, alignment=TA_CENTER, spaceAfter=0, spaceBefore=0)
CONTENT_RIGHT = ParagraphStyle('CONTENT_RIGHT', fontName=FONT_NAME, fontSize=7, leading=8, alignment=TA_RIGHT, spaceAfter=0, spaceBefore=0)
CONTENT_LEFT = ParagraphStyle('CONTENT_LEFT', fontName=FONT_NAME, fontSize=7, leading=8, alignment=TA_LEFT, spaceAfter=0, spaceBefore=0)
SUBHEADER_CENTER = ParagraphStyle('SUBHEADER_CENTER', fontName=FONT_NAME_BOLD, fontSize=7, leading=8,  alignment=TA_CENTER, spaceAfter=0, spaceBefore=0)
SUBHEADER_LEFT = ParagraphStyle('SUBHEADER_LEFT', fontName=FONT_NAME_BOLD, fontSize=7, leading=8, alignment=TA_LEFT, spaceAfter=0, spaceBefore=0)
SUBHEADER_RIGHT = ParagraphStyle('SUBHEADER_RIGHT', fontName=FONT_NAME_BOLD, fontSize=7, leading=8, alignment=TA_RIGHT, spaceAfter=0, spaceBefore=0)
TYPE_PDF = ParagraphStyle('TYPE_PDF', fontName=FONT_NAME, fontSize=10, leading=10,  alignment=TA_CENTER, spaceAfter=0, spaceBefore=0, textColor='white')
TOTAL_STYLE = ParagraphStyle('TOTAL_STYLE', fontName=FONT_NAME_BOLD, fontSize=8, leading=8.5, alignment=TA_RIGHT, spaceAfter=0, spaceBefore=0)
HEAD_TDF = ParagraphStyle('HEAD_TDF', fontName=FONT_NAME_BOLD, fontSize=9, leading=9, alignment=TA_LEFT, spaceAfter=0, spaceBefore=0,)
NULL = Paragraph('', CONTENT_CENTER)

class CreatePDF(object):

  def __init__(self, xml_string, filename, status, notes='', subtotal_precalculated=0.00, iva_pdf=0.00):
    #xml_file = open(xml_path, 'r')
    #xml_string = xml_file.read()
    #xml_file.close()
    self.success = False
    self.filename = filename
    self.status = status
    self.subtotal_precalculated = subtotal_precalculated
    self.iva_pdf = iva_pdf
    self.notes = notes
    self.cfdi_type_legend = u'Factura Electrónica'
    
    #set_trace()
    try:
      #xml_parser = etree.XMLParser(remove_blank_text=True)
      xml_parser = etree.XMLParser(remove_blank_text=True, recover=True) #~ Fix error "Not found URI"
      try:
        try:
          xml_encoded = xml_string.encode('utf-8')
        except:
          xml_encoded = xml_string.decode('utf-8')
        xml_etree = etree.XML(xml_encoded.encode('utf-8'), parser=xml_parser)
      except:
        xml_etree = etree.XML(xml_string, parser=xml_parser)
      
      try: 
        n_comp = xml_etree.xpath('//cfdi:Comprobante', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
        self.version = n_comp.get('Version')
        self.date = n_comp.get('Fecha')
        self.cfdi_type = n_comp.get('TipoDeComprobante')
        self.folio = n_comp.get('Folio', '')
        self.serial = n_comp.get('Serie', '')
        self.moneda = Moneda.objects.get(clave=n_comp.get('Moneda', '')).descripcion if n_comp.get('Moneda', '') else None
        self.certificate_serial = n_comp.get('NoCertificado')
        self.expedition_place = n_comp.get('LugarExpedicion') 
        self.pay_method = MetodoPago.objects.get(clave=n_comp.get('MetodoPago')).descripcion if n_comp.get('MetodoPago') else ''
        self.way_payment = FormaPago.objects.get(clave=n_comp.get('FormaPago')).descripcion if n_comp.get('FormaPago') else ''
        self.discount = n_comp.get('Descuento', 0.00)
        self.total = n_comp.get('Total')
        self.total_con_letra = ''
        try:
          self.total_con_letra = numero_a_letras(float(self.total))
        except:
          pass
        self.sub_total = n_comp.get('SubTotal')
        self.payment_terms = n_comp.get('CondicionesDePago', '')
      except Exception as e:
        raise Exception("Exception get node Comprobante => %s" % str(e))
      
      # Emisor
      try:
        n_emisor = xml_etree.find('cfdi:Emisor', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})   
        self.name = n_emisor.get('Nombre')
        self.taxpayer_id = n_emisor.get('Rfc')
        self.regimen = RegimenFiscal.objects.get(clave=n_emisor.get('RegimenFiscal')).descripcion
      except Exception as e:
        raise Exception("Exception get node Emisor => %s" % str(e))

      # Receptor
      try: 
        n_receptor = xml_etree.find('cfdi:Receptor', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})
        self.rtaxpayer_id =  n_receptor.get('Rfc')
        self.rname = n_receptor.get('Nombre')
        self.uso_cfdi = UsoCFDI.objects.get(clave=n_receptor.get('UsoCFDI')).descripcion
      except Exception as e:
        raise Exception("Exception get node Receptor => %s" % str(e))
      
      # Conceptos
      try:
        self.conceptos = xml_etree.xpath('cfdi:Conceptos/cfdi:Concepto', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})
      except:
        self.conceptos = None
        raise Exception("Exception get node Conceptos => %s" % str(e))

      # total impuestos trasladados
      try:
        self.total_tra = 0.00
        self.total_tra = xml_etree.xpath('//cfdi:Comprobante/cfdi:Impuestos/@TotalImpuestosTrasladados', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
      except:
        pass
      
      # total impuestos retenidos
      try:
        self.total_ret = 0.00
        self.total_ret = xml_etree.xpath('//cfdi:Comprobante/cfdi:Impuestos/@TotalImpuestosRetenidos', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
      except:
        pass

      # Complementos
      if self.cfdi_type == 'N':
        self.cfdi_type_legend = u'Recibo de Nómina'
        self.signature_legend = u"Se puso a mi disposición el archivo XML correspondiente y recibí de la empresa arriba mencionada la cantidad neta que este documento se refiere estando conforme con las percepciones y deducciones que en él aparecen especificados."

        try:
          n_nomina = xml_etree.xpath('//tmp:Nomina', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]
          self.tot_ded = n_nomina.get('TotalDeducciones')
          self.tot_per = n_nomina.get('TotalPercepciones')
          self.tot_otpa = n_nomina.get('TotalOtrosPagos')
          self.fe_exped = n_nomina.get('FechaFinalPago')
          self.paid_days = n_nomina.get('NumDiasPagados')
          paid_from = n_nomina.get('FechaInicialPago')
          paid_to = n_nomina.get('FechaFinalPago')
          #paid_from_2 = datetime.strptime(paid_from, '%Y-%m-%d').strftime('%d/%b/%Y').upper()
          #paid_to_2 = datetime.strptime(paid_to, '%Y-%m-%d').strftime('%d/%b/%Y').upper()
          #self.period = "%s al %s" % (paid_from_2, paid_to_2)
          self.period = "%s al %s" % (paid_from, paid_to)

          # Emisor Nomina
          #self.employer_regist = xml_etree.xpath('//tmp:Emisor/@RegistroPatronal', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]

          # Receptor Nomina
          n_receptor = xml_etree.xpath('//tmp:Receptor', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]
          self.emp_num = n_receptor.get('NumEmpleado')
          self.curp = n_receptor.get('Curp')
          self.imss = n_receptor.get('NumSeguridadSocial')
          self.depart = n_receptor.get('Departamento')
          self.posit = n_receptor.get('Puesto')
          self.s_diario = n_receptor.get('SalarioDiarioIntegrado')
          self.ss_no = n_receptor.get('NumSeguridadSocial')
          self.emp_regimen = REG_EMP[n_receptor.get('TipoRegimen')]

          # Deducciones
          if len(xml_etree.xpath('//tmp:Deducciones', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})) > 0:
            self.deducciones = xml_etree.xpath('//tmp:Deducciones', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]
            self.tot_isr = self.deducciones.get('TotalImpuestosRetenidos') if self.deducciones.get('TotalImpuestosRetenidos') else '0.00'
            self.tot_ded = self.deducciones.get('TotalOtrasDeducciones') if self.deducciones.get('TotalOtrasDeducciones') else '0.00'
          else:
            self.deducciones = []
            self.tot_isr = '0.00'
            self.tot_ded = '0.00'
        
          # Percepciones
          if len(xml_etree.xpath('//tmp:Percepciones', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})) > 0:
            self.percepciones = xml_etree.xpath('//tmp:Percepciones', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]
          else:
            self.percepciones = []
        
          # OtrosPagos
          if len(xml_etree.xpath('//tmp:OtrosPagos', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})) > 0:
            try:
              self.n_otros_pagos = xml_etree.xpath('//tmp:OtrosPagos', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})[0]
              self.otros_p = True
            except:
              self.otros_p = False
              pass
          else:
            pass
        
          # Incapacidades
          if len(xml_etree.xpath('//tmp:Incapacidades', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})) > 0:
            #set_trace()
            self.n_incapacidades = []
            self.nodos_incapacidades = xml_etree.xpath('//tmp:Incapacidades', namespaces={'tmp':'http://www.sat.gob.mx/nomina12'})
          
            for nodo_inc in self.nodos_incapacidades:
              for inc in nodo_inc:
                self.n_incapacidades.append(inc)
            self.incapacidades = True
          else:
            self.incapacidades = False
            pass
        except Exception as e:
          #self.errors.append('Error obteniendo datos del nodo Nómina | {}'.format(str(e)))
          raise Exception('Error obteniendo datos del nodo Nómina | {}'.format(str(e)))

      if self.cfdi_type == 'P':
        self.cfdi_type_legend = u'Recibo Electrónico de Pagos'
        try:
          self.n_pagos = xml_etree.xpath('//pago10:Pagos', namespaces={'pago10':'http://www.sat.gob.mx/Pagos'})[0]
        except Exception as e:
          #self.errors.append('Error obteniendo datos del nodo Pagos | {}'.format(str(e)))
          raise Exception('Error obteniendo datos del nodo Pagos | {}'.format(str(e)))
      
      # TFD
      try: 
        n_tfd = xml_etree.xpath('//cfdi:TimbreFiscalDigital', namespaces={'cfdi':'http://www.sat.gob.mx/TimbreFiscalDigital'})[0]
        self.uuid = n_tfd.get('UUID')
        self.seal_cfd = n_tfd.get('SelloCFD')
        self.seal_sat = n_tfd.get('SelloSAT')
        self.serial_sat = n_tfd.get('NoCertificadoSAT')
        self.date_cert = n_tfd.get('FechaTimbrado')
        self.original_string_tfd = '||1.1|%s|%s|%s|%s||' % (self.uuid, self.date_cert, self.seal_cfd, self.serial_sat)
      except Exception as e:
        raise Exception("Exception get node TFD => %s" % str(e))

      self.issuing_address = u"Camino al ITESO, 8900 Int 1-A Parque Jalisco<br/>Col. El Mante, Tlaquepaque, Jalisco<br/>C.P. 45609, México. Tel (01 33) 3770-5400<br/><br/>RFC: {}<br/>Régimen Fiscal: {}".format(self.taxpayer_id, self.regimen)

      self.lightgrey = colors.lightgrey
      self.bg_color = colors.Color(red=(0.486), green=(0.756), blue=(0.266))  # HERBALIFE
      if self.taxpayer_id not in settings.TAXPAYER_ID_LIST:
        self.bg_color = colors.Color(red=(0.188), green=(0.486), blue=(0.509)) # PROVIDERS

      self.success = self.tables_builder()
    except Exception as e:
      print('-'*60)
      print(f"Exeption Constructor => {e}")
      traceback.print_exc(file=sys.stdout)
      print('-'*60)
      
  def settings(self, canvas, doc):
    try: 
      canvas.saveState()

      canvas.setFont(FONT_NAME_BOLD, 9)
      canvas.setFillColor(HexColor('#000000'))
      canvas.drawRightString(6*inch, 0.4*inch, 'Este documento es una representación impresa de un CFDI')
      
      canvas.setFont(FONT_NAME, 8)
      canvas.setFillColor(HexColor('#555759'))
      canvas.drawString(0.4*inch, 0.2*inch, 'Powered by')
      coords = (0.3*inch, 0.4*inch, 1.5*inch, 0.1*inch)
      canvas.linkURL('https://www.google.com', coords, thickness=0)
      canvas.drawString(1*inch, 0.2*inch, 'UNNAMED')
      
      canvas.setTitle('Factura Electrónica')
      canvas.setSubject('Factura Electrónica')
      canvas.setAuthor('-')
      canvas.setKeywords(['PAC', 'CFDI', 'TIMBRADO', 'SAT'])
      canvas.setCreator('-')
      
      if self.status == 'C':
        cancelled_logo = ImageReader('./static/img/logos/cancelado.png')
        canvas.drawImage(cancelled_logo, 60, 450, width=500, height=200, mask='auto')

      self.header(canvas)
      canvas.restoreState()
    except Exception as e:
      print("Exception header() =>  %s" % str(e))
      self.message = "Exception header() =>  %s" % str(e)

  def header(self, canvas):
    try:
      # Emisor
      if self.taxpayer_id in settings.TAXPAYER_ID_LIST:
        logo = Image('{}/img/pdf/herbalife.png'.format(dj_settings.STATIC_DIR), width=8*cm, height=1.2*cm)

        issuing_data = [
          [logo, Paragraph("%s" % self.cfdi_type_legend, TYPE_PDF), NULL],
          [NULL, Paragraph('Tipo de CFDI: %s' % (TIPO_COMPROBANTE[self.cfdi_type]), CONTENT_LEFT), Paragraph('Versión del CFDI: %s' % self.version, CONTENT_RIGHT)],
          [Paragraph(self.name, HEAD_TDF), Paragraph('%s %s' % (self.serial, self.folio), FOLIO_STYLE), NULL],
          [Paragraph(self.issuing_address, CONTENT_LEFT), NULL, NULL],
        ]

        table_issuing = Table(issuing_data, colWidths=[14*cm, 3*cm, 3*cm], style=[
          #('GRID', (0,0), (-1,-1), 1, colors.gray),
          ('BACKGROUND', (1,0), (1,0), self.bg_color),
          ('VALIGN', (0,0), (-1,1), 'MIDDLE'),
          ('SPAN', (0,0),(0,1)),
          ('SPAN', (1,0),(-1,0)),
          ('SPAN', (1,2),(-1,-1)),
          ('VALIGN', (0,2), (-1,2), 'TOP'),
          ('TOPPADDING', (0,0), (-1,-1), 0),
          ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
          ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
          ('LEFTPADDING', (0,0), (-1,-1), 0),
          ('RIGHTPADDING', (0,0), (-1,-1), 0),
          ('LEFTPADDING', (0,0), (0,1), 0),
        ])

        table_issuing.wrapOn(canvas, 0.82*cm, 23.5*cm)
        table_issuing.drawOn(canvas, 0.82*cm, 23.5*cm)
      else:
        issuing_data = [
          [Paragraph("%s" % self.name, HEAD_TDF), Paragraph("%s" % self.cfdi_type_legend, TYPE_PDF), NULL],
          [Paragraph("RFC: %s" % self.taxpayer_id, CONTENT_LEFT), Paragraph('Tipo de CFDI: %s' % (TipoDeComprobante.objects.get(clave=self.cfdi_type).descripcion), CONTENT_LEFT), Paragraph('Versión del CFDI: %s' % (self.version), CONTENT_RIGHT)],
          [Paragraph(u"Régimen Fiscal: %s" % self.regimen, CONTENT_LEFT), Paragraph('%s %s' % (self.serial, self.folio), FOLIO_STYLE), NULL],
        ]
        table_issuing = Table(issuing_data, colWidths=[14*cm, 3*cm, 3*cm], style=[
          #('GRID', (0,0), (-1,-1), 1, colors.gray),
          ('BACKGROUND', (1,0), (-1,0), self.bg_color),
          ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
          ('SPAN', (1,0),(-1,0)),
          ('SPAN', (1,-1),(-1,-1)),
          ('VALIGN', (-1,1), (-1,2), 'TOP'),
          ('TOPPADDING', (0,0), (-1,-1), 0),
          ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
          ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
          ('LEFTPADDING', (0,0), (-1,-1), 0),
          ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ])

        table_issuing.wrapOn(canvas, 0.8*cm, 25.8*cm)
        table_issuing.drawOn(canvas, 0.8*cm, 25.8*cm)

      # Receptor
      if self.cfdi_type == 'N':
        receiver_data = [
          [Paragraph('RECEPTOR', HEADERS), NULL],
          [Paragraph('ID: %s' % self.emp_num, CONTENT_LEFT), Paragraph('Régimen del trabajador: %s' % self.emp_regimen, CONTENT_LEFT)],
          [Paragraph('Nombre: %s' % self.rname, CONTENT_LEFT), Paragraph('Periodo del: %s' % self.period, CONTENT_LEFT)],
          [Paragraph('CURP: %s' % self.curp, CONTENT_LEFT), Paragraph('Días pagados: %s' % self.paid_days, CONTENT_LEFT)],
          [Paragraph('RFC: %s' % self.rtaxpayer_id, CONTENT_LEFT), NULL],
        ]
  
        table_receiver = Table(receiver_data, colWidths=[10*cm, 10*cm], style=[
          #('GRID', (0,0),(-1,-1), 1, colors.gray),
          ('BACKGROUND', (0,0),(-1,0), self.bg_color),
          ('TOPPADDING', (0,0),(-1,-1), 0.5),
          ('BOTTOMPADDING', (0,0),(-1,-1), 0.5),
          ('SPAN', (0,0),(-1,0)),
          ('VALIGN', (0,1),(-1,-1), 'TOP'),
          ('LEFTPADDING', (0,0), (-1,-1), 0),
          ('RIGHTPADDING', (0,0), (-1,-1), 0),
          ('LINEBELOW', (0,-1), (-1,-1), 1, self.bg_color),
        ])
        table_receiver.wrapOn(canvas, 0.82*cm, 21.7*cm)
        table_receiver.drawOn(canvas, 0.82*cm, 21.7*cm)
      else:
        receiver_data = [
          [Paragraph('RECEPTOR', HEADERS)],
          [Paragraph('Nombre: %s' % self.rname, CONTENT_LEFT)],
          [Paragraph('RFC: %s' % self.rtaxpayer_id, CONTENT_LEFT)],
          [Paragraph('Uso del CFDI: %s' % self.uso_cfdi, CONTENT_LEFT)],
        ]
 
        table_receiver = Table(receiver_data, colWidths=[20*cm], style=[
          #('GRID', (0,0),(-1,-1), 1, colors.gray),
          ('BOX', (0,0), (-1,0), 1, self.bg_color),
          ('BACKGROUND', (0,0),(-1,0), self.bg_color),
          ('TOPPADDING', (0,0),(-1,-1), 0.5),
          ('BOTTOMPADDING', (0,0),(-1,-1), 0.5),
          ('VALIGN', (0,1),(-1,-1), 'TOP'),
          ('LINEBELOW', (0,-1), (-1,-1), 1, self.bg_color),
          ('LEFTPADDING', (0,0), (-1,-1), 0),
          ('RIGHTPADDING', (0,0), (-1,-1), 0),
          ('BOTTOMPADDING', (0,-1),(-1,-1), 2),
        ])

        #if self.subtotal_precalculated:
        if self.taxpayer_id in settings.TAXPAYER_ID_LIST:
          table_receiver.wrapOn(canvas, 0.82*cm, 22*cm)
          table_receiver.drawOn(canvas, 0.82*cm, 22*cm)
        else:
          table_receiver.wrapOn(canvas, 0.8*cm, 24.1*cm)
          table_receiver.drawOn(canvas, 0.8*cm, 24.1*cm)
    except Exception as e:
      print('-'*60)
      print("Error al generar la tabla emisor/receptor => %s" % str(e))
      traceback.print_exc(file=sys.stdout)
      print('-'*60)

  def tables_builder(self):
    try:
      success = False
      story=[]
      if self.subtotal_precalculated:
        table_concepts_c = self.concepts_customized()
        story.append(table_concepts_c)
      else:
        table_concepts = self.concepts()
        story.append(table_concepts)
        story.append(Spacer(0,11))
      
      #set_trace()
      if self.cfdi_type == 'N':
        table_nomina = self.nomina()
        story.append(table_nomina)
        story.append(Spacer(0,9))
        table_totales_nomina = self.totales_nomina()
        story.append(table_totales_nomina)
        story.append(Spacer(0,5))
        table_signature = self.employe_signature()
        story.append(table_signature)

      elif self.cfdi_type == 'P':
        #table_concepts_pagos = self.concepts_pagos()
        #story.append(table_concepts_pagos)
        table_pagos, table_doctos = self.pagos()
        story.append(table_pagos)
        story.append(Spacer(0,13))
        story.append(table_doctos)
        story.append(Spacer(0,13))

      if not self.cfdi_type == 'N':
        story.append(Spacer(0,9))
        table_totales = self.totales()
        #story.append(table_totales)
        story.append(KeepTogether(table_totales))
      
      story.append(Spacer(0,9))
      table_tfd = self.tfd()
      story.append(table_tfd)
      
      story.append(Spacer(0,9))
      table_tfd_seals = self.tfd_seals()
      story.append(table_tfd_seals)
      
      if self.taxpayer_id in settings.TAXPAYER_ID_LIST:
        frame = Frame(74, 45, 465, 565)
      else:
        frame = Frame(74, 45, 465, 630)
        #frame = Frame(74, 45, 465, 570) #~ Use this frame when you includes the issuing address
      
      header = PageTemplate(id='header', frames=frame, onPage=self.settings)

      self.pdf_path = '{}/{}'.format(settings.PDF_PATH, self.filename)
      self.doc = BaseDocTemplate(self.pdf_path, pageTemplates=[header], pagesize=letter)
      self.doc.build(story, canvasmaker=NumberedCanvas)
      success = True
    except Exception as e:
      print("Exception tables_builder() => %s" % str(e))
    return success

  def nomina(self):
    try:
      per_ded_data = [
        [Paragraph('PERCEPCIONES', HEADERS), NULL, NULL, NULL, Paragraph('DEDUCCIONES', HEADERS), NULL, NULL],
        [Paragraph('Clave', SUBHEADER_CENTER), Paragraph('Descripción', SUBHEADER_LEFT), Paragraph('Importe', SUBHEADER_RIGHT), NULL, Paragraph('Clave', SUBHEADER_CENTER), Paragraph('Descripción', SUBHEADER_LEFT), Paragraph('Importe', SUBHEADER_RIGHT)],
      ]
      
      #set_trace()
      if len(self.percepciones) >= len(self.deducciones):
        pos = 0
        for percepcion in self.percepciones:
          clave_ded = ''
          concepto_ded = ''
          importe_ded = ''

          try:
            clave_ded = self.deducciones[pos].get('Clave')
          except:
            pass
          
          try:
            concepto_ded = self.deducciones[pos].get('Concepto')
          except:
            pass
          
          try:
            importe_ded = self.deducciones[pos].get('Importe')
            importe_ded = self.truncate(Decimal(importe_ded), 2)
          except:
            pass

          per_ded_data.append([Paragraph(percepcion.get('Clave'), CONTENT_CENTER), Paragraph(percepcion.get('Concepto'), CONTENT_LEFT), Paragraph(self.truncate(Decimal('%.2f' % (float(percepcion.get('ImporteExento')) + float(percepcion.get('ImporteGravado')))), 2), CONTENT_RIGHT), NULL, Paragraph(clave_ded, CONTENT_CENTER), Paragraph(concepto_ded, CONTENT_LEFT), Paragraph(importe_ded, CONTENT_RIGHT)]),
          pos += 1
      elif  len(self.percepciones) < len(self.deducciones):
        pos = 0
        for deduccion in self.deducciones:
          clave_per = ''
          concepto_per = ''
          importe_per = ''

          try:
            clave_per = self.percepciones[pos].get('Clave')
          except:
            pass
          
          try:
            concepto_per = self.percepciones[pos].get('Concepto')
          except:
            pass
          
          try:
            importe_per = '%.2f' % (float(self.percepciones[pos].get('ImporteGravado')) + float(self.percepciones[pos].get('ImporteExento')))
            importe_per = self.truncate(Decimal(importe_per), 2)
          except:
            pass

          per_ded_data.append([Paragraph(clave_per, CONTENT_CENTER), Paragraph(concepto_per, CONTENT_LEFT), Paragraph(importe_per, CONTENT_RIGHT), NULL, Paragraph(deduccion.get('Clave'), CONTENT_CENTER), Paragraph(deduccion.get('Concepto'), CONTENT_LEFT), Paragraph(self.truncate(Decimal('%.2f' % float(deduccion.get('Importe'))), 2), CONTENT_RIGHT)]),
          pos += 1
      
      table_per_ded=Table(per_ded_data, colWidths=[1.2*cm, 6.6*cm, 2*cm, 0.4*cm, 1.2*cm, 6.6*cm, 2*cm], repeatRows=2, style=[
        #('GRID', (0,0),(-1,-1), 1, colors.black),
        #('BOX', (0,0),(-1,-1), 1, self.bg_color),
        ('BACKGROUND', (0,0),(2,0), self.bg_color),
        ('BACKGROUND', (4,0),(-1,0), self.bg_color),
        ('SPAN', (0,0),(2,0)), # PERCEPCIONES
        ('SPAN', (4,0),(-1,0)), # DEDUCCIONES
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('VALIGN', (0,2),(-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0),(-1,-1), 2.5),
        ('LEFTPADDING', (0,0),(-1,-1), 2.5),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 0.5),
        ('BOTTOMPADDING', (0,1),(-1,1), 2),
        ('LINEBELOW',(0,1),(2,1), 1, self.bg_color), # Draw a line below headers PERCEPCIONES
        ('LINEBELOW',(4,1),(-1,1), 1, self.bg_color), # Draw a line below headers DEDUCCIONES
        ('LINEBELOW',(0,-1),(2,-1), 1, self.bg_color), # Draw a line after last row PERCEPCIONES
        ('LINEBELOW',(4,-1),(-1,-1), 1, self.bg_color), # Draw a line after last row DEDUCCIONES
        ('LINEBELOW',(0,"splitlast"),(2,"splitlast"), 1, self.bg_color),
        ('LINEBELOW',(4,"splitlast"),(-1,"splitlast"), 1, self.bg_color),
        ('BOTTOMPADDING',(0,-1),(-1,-1), 2),
        #('LINEBELOW',(0,"splitlast"),(-1,"splitlast"), 1, colors.gray),
      ])

    except Exception as e:
      #self.errors.append("Exception nomina() | %s" % str(e))
      print('Exception nomina() | %s' % str(e))
    return table_per_ded

  def concepts(self):
    try:
      concepts_data = [
        [Paragraph('CONCEPTOS', HEADERS), NULL, NULL, NULL, NULL, NULL],
        [Paragraph('Cantidad', SUBHEADER_CENTER), Paragraph('Clave Unidad', SUBHEADER_CENTER), Paragraph('ClaveProdServ', SUBHEADER_CENTER), Paragraph('Descripción', SUBHEADER_LEFT), Paragraph('P. Unitario', SUBHEADER_CENTER), Paragraph('Importe', SUBHEADER_RIGHT)],
      ]

      for concept in self.conceptos:
        cantidad = self.truncate(Decimal(concept.get('Cantidad')), 2)
        p_unitario = self.truncate(Decimal(concept.get('ValorUnitario')), 2)
        importe = self.truncate(Decimal(concept.get('Importe')), 2)
        concepts_data.append([Paragraph(cantidad, CONTENT_CENTER), Paragraph(concept.get('ClaveUnidad') if concept.get('ClaveUnidad') else '', CONTENT_CENTER), Paragraph(concept.get('ClaveProdServ'), CONTENT_CENTER), Paragraph(concept.get('Descripcion'), CONTENT_LEFT), Paragraph(p_unitario, CONTENT_CENTER), Paragraph(importe, CONTENT_RIGHT)]),
      
      table_concepts=Table(concepts_data, colWidths=[2*cm, 2*cm, 2*cm, 10*cm, 2*cm, 2*cm], repeatRows=2, style=[
        #('GRID', (0,0), (-1,-1),1, colors.gray),
        ('SPAN', (0,0), (-1,0)),
        ('VALIGN', (0,1), (-1,0), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,0), self.bg_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.1),
        ('TOPPADDING', (0,0), (-1,-1), 0.5),
        ('LINEBELOW', (0,1), (-1,1), 1, self.bg_color),
        ('VALIGN', (0,1), (-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 2.5),
        ('LINEBELOW', (0,-1), (-1,-1), 1, self.bg_color),
        ('LINEBELOW',(0,"splitlast"),(-1,"splitlast"), 1, self.bg_color),
      ])

    except Exception as e:
      print("Exception concepts() => %s" % str(e))
    return table_concepts

  def concepts_customized(self):
    try:
      concepts_data = [
        [Paragraph('CONCEPTOS', HEADERS), NULL, NULL, NULL, NULL],
        [Paragraph('ClaveProd<br/>Serv', SUBHEADER_CENTER),
          Paragraph('Cantidad', SUBHEADER_RIGHT),
          Paragraph('Clave<br/>Unidad', SUBHEADER_CENTER),
          Paragraph('SKU', SUBHEADER_CENTER),
          Paragraph('Descripción', SUBHEADER_LEFT),
          Paragraph('Valor<br/>Unitario', SUBHEADER_RIGHT),
          Paragraph('Importe', SUBHEADER_RIGHT),
          Paragraph('Descuento', SUBHEADER_RIGHT),
          Paragraph('Base', SUBHEADER_RIGHT),
          Paragraph('Tasa IVA', SUBHEADER_RIGHT),
          Paragraph('IVA', SUBHEADER_RIGHT)
        ],
      ]

      sum_valor_unit = 0.00
      sum_importe = 0.00
      sum_descuento = 0.00
      sum_base = 0.00
      empaque = False
      valor_unit_yyyy = 0.00
      iva_002_yyyy = '0.00'
      importe_yyyy = 0.00
      base_yyyy = 0.00
      
      for concepto in self.conceptos:
        base = '0.00'
        tasaCuota = '-'
        impuesto = ''
        tipoFactor = ''
        iva_002 = '-'
        importe_ieps = 0.00
        descripcion = ''
        descuento = 0.00
        valor_unitario_ieps = 0.00
        importe_con_ieps = 0.00
        num_pedimento = ''

        try:
          descuento = concepto.get('Descuento', 0.00)
        except:
          pass
        try:
          base = concepto.xpath('cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="002"]/@Base', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
        except:
          pass
        try:
          tasaCuota = concepto.xpath('cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="002"]/@TasaOCuota', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
          tasaCuota = '%.0f%%' % (float(tasaCuota) * 100)
        except:
          pass
        try:
          iva_002 = concepto.xpath('cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="002"]/@Importe', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
          iva_002 = self.truncate(Decimal(iva_002), 2)
        except:
          pass
        try:
          importe_ieps = concepto.xpath('cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado[@Impuesto="003"]/@Importe', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
        except:
          pass
        try:
          num_pedimento = concepto.xpath('cfdi:InformacionAduanera/@NumeroPedimento', namespaces={'cfdi':'http://www.sat.gob.mx/cfd/3'})[0]
        except:
          pass

        valor_unitario_ieps = float(concepto.get('ValorUnitario')) + float(importe_ieps)
        importe_con_ieps = float(concepto.get('Importe')) + float(importe_ieps)
        descripcion = concepto.get('Descripcion')
        noIdent = concepto.get('NoIdentificacion')
        if noIdent == 'XXXX':
          descripcion = 'Cargos logísticos'
        elif noIdent == 'YYYY':
          empaque = True
          valor_unit_yyyy += (valor_unitario_ieps + valor_unit_yyyy)
          importe_yyyy += (importe_con_ieps + importe_yyyy)
          iva_002_yyyy += str(float(iva_002) + iva_002_yyyy)
          descripcion = 'Otros cargos'
          
          if not isinstance(base, str):
            base_yyyy += float(base)  
          else:
            base_yyyy = '-'
        elif noIdent == 'ZZZZ' and empaque:
          del concepts_data[-2] # Remove YYYY
          valor_unitario_ieps = (valor_unitario_ieps + valor_unit_yyyy)
          importe_con_ieps = (importe_con_ieps + importe_yyyy)
          iva_002 = str((float(iva_002) + iva_002_yyyy))
          
          if not isinstance(base, str):
            base = str(base_yyyy + float(base))
          else:
            base = '-'
          descripcion = 'Otros cargos'
          noIdent = 'YYYY'

        sum_valor_unit += valor_unitario_ieps
        sum_importe += importe_con_ieps
        sum_base = '-'
        if not isinstance(base, str):
          sum_base += float(base)
        sum_descuento += float(descuento)

        if concepto.get('NoIdentificacion') == 'ZZZZ':
          sum_valor_unit -= valor_unit_yyyy 
          sum_importe -= importe_yyyy
          sum_base = '-'
          if not isinstance(base_yyyy, str):
            sum_base -= base_yyyy
        sum_descuento += float(descuento)

        concepts_data.append([
          Paragraph(concepto.get('ClaveProdServ'), CONTENT_RIGHT),
          Paragraph(self.truncate(Decimal(concepto.get('Cantidad')), 2), CONTENT_RIGHT),
          Paragraph(concepto.get('ClaveUnidad'), CONTENT_CENTER),
          Paragraph(noIdent, CONTENT_CENTER),
          Paragraph('%s%s' % (descripcion, '<br/>%s' % num_pedimento if num_pedimento else ''), CONTENT_LEFT),
          Paragraph(self.truncate(Decimal(str(valor_unitario_ieps)), 2), CONTENT_RIGHT),
          Paragraph(self.truncate(Decimal(str(importe_con_ieps)), 2), CONTENT_RIGHT),
          Paragraph(self.truncate(Decimal(descuento), 2), CONTENT_RIGHT),
          Paragraph(self.truncate(Decimal(base), 2), CONTENT_RIGHT),
          Paragraph(tasaCuota, CONTENT_RIGHT),
          Paragraph(iva_002, CONTENT_RIGHT)
        ])
      
      concepts_data.append([
        Paragraph('', CONTENT_RIGHT),
        Paragraph('', CONTENT_RIGHT),
        Paragraph('', CONTENT_RIGHT),
        Paragraph('', CONTENT_RIGHT),
        Paragraph('Total:', CONTENT_RIGHT),
        Paragraph('%.2f' % float(sum_valor_unit), CONTENT_RIGHT),
        Paragraph('%.2f' % float(sum_importe), CONTENT_RIGHT),
        Paragraph('%.2f' % float(sum_descuento), CONTENT_RIGHT),
        Paragraph(sum_base, CONTENT_RIGHT),
        Paragraph('', CONTENT_RIGHT),
        Paragraph(str(self.iva_pdf), CONTENT_RIGHT)
      ])

      table_concepts=Table(concepts_data, colWidths=[1.5*cm, 1.3*cm, 1.2*cm, 1.3*cm, 6*cm, 1.5*cm, 1.6*cm, 1.5*cm, 1.6*cm, 1*cm, 1.5*cm], repeatRows=2, style=[
        ('SPAN', (0,0), (-1,0)),
        ('BACKGROUND', (0,0), (-1,0), self.bg_color),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1.1),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        #('BOTTOMPADDING', (0,1),(-1,-1), 1),
        ('VALIGN', (0,0), (-1,1), 'MIDDLE'), # Encabezados
        ('VALIGN', (0,2), (-1,-1), 'TOP'), # Todo el resto
        ('RIGHTPADDING', (0,0), (-1,-1), 2.5), # Todo
        ('LEFTPADDING', (0,0), (-1,-1), 2.5), # Todo
        ('LINEABOVE',(0,-1),(-1,-1), 1, self.bg_color),
        ('LINEBELOW',(0,-1),(-1,-1), 1, self.bg_color),
        ('LINEBELOW',(0,1),(-1,1), 1, self.bg_color),
        ('LINEBELOW',(0,"splitlast"),(-1,"splitlast"), 1, self.bg_color),
      ])
    except Exception as e:
      print("Exception concepts_customized() => %s" % str(e))
      print('-'*60)
      traceback.print_exc(file=sys.stdout)
      print('-'*60)
    return table_concepts

  def pagos(self):
    try:
      pagos = [
        [Paragraph('PAGOS', HEADERS), NULL, NULL, NULL, NULL, NULL, NULL],
        [Paragraph('Pago', SUBHEADER_CENTER), Paragraph('Fecha Pago', SUBHEADER_CENTER), Paragraph('Forma Pago', SUBHEADER_CENTER), Paragraph('Moneda Pago', SUBHEADER_CENTER), Paragraph('Tipo Cambio', SUBHEADER_CENTER),  Paragraph('No. Operación', SUBHEADER_CENTER), Paragraph('Monto Pagado', SUBHEADER_RIGHT)],
      ]

      doctos_rel = [
        [Paragraph('DOCUMENTOS RELACIONADOS', HEADERS), NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
        [Paragraph('Pago', SUBHEADER_CENTER), Paragraph('UUID', SUBHEADER_CENTER), Paragraph('Serie Folio', SUBHEADER_CENTER), Paragraph('Moneda', SUBHEADER_CENTER), Paragraph('TipoCambio', SUBHEADER_CENTER), Paragraph('Método Pago', SUBHEADER_CENTER),  Paragraph('Parcialidad', SUBHEADER_CENTER), Paragraph('Saldo Anterior', SUBHEADER_RIGHT), Paragraph('Importe Pago', SUBHEADER_RIGHT), Paragraph('Saldo Pendiente', SUBHEADER_RIGHT)],
      ]
      
      item = 1
      
      for pago in self.n_pagos:
        try:
          FechaPago = pago.get('FechaPago', '')
        except:
          pass

        try:
          FormaPago = pago.get('FormaDePagoP', '')
        except:
          pass

        try:
          MonedaPago = pago.get('MonedaP', '')
        except:
          pass

        try:
          TipoCambio = pago.get('TipoCambioP', '')
        except:
          pass

        try:
          NumOperacion = pago.get('NumOperacion', '')
        except:
          pass

        try:
          MontoPagado = pago.get('Monto', '')
        except:
          pass

        #set_trace()
        for docto in pago:
          try:
            idDoc = docto.get('IdDocumento', '')
          except:
            pass
          
          try:
            serie = docto.get('Serie', '-')
          except:
            pass

          try:
            folio = docto.get('Folio', '-')
          except:
            pass

          try:
            monedaDR = docto.get('MonedaDR', '')
          except:
            pass

          try:
            tipoCambioDR = docto.get('TipoCambioDR', '')
          except:
            pass

          try:
            metodoDePagoDR = docto.get('MetodoDePagoDR', '')
          except:
            pass
          
          try:
            numParcialidad = docto.get('NumParcialidad', '')
          except:
            pass
          
          try:
            impSaldoAnt = docto.get('ImpSaldoAnt', '')
          except:
            pass

          try:
            impPago = docto.get('ImpPagado', '')
          except:
            pass

          try:
            impSaldoIns = docto.get('ImpSaldoInsoluto', '')
          except:
            pass

          doctos_rel.append([Paragraph(str(item), CONTENT_CENTER), Paragraph(idDoc, CONTENT_CENTER), Paragraph('{} {}'.format(serie, folio), CONTENT_CENTER), Paragraph(monedaDR, CONTENT_CENTER), Paragraph(tipoCambioDR, CONTENT_CENTER), Paragraph(metodoDePagoDR, CONTENT_CENTER),  Paragraph(numParcialidad, CONTENT_CENTER), Paragraph(impSaldoAnt, CONTENT_RIGHT), Paragraph(impPago, CONTENT_RIGHT), Paragraph(impSaldoIns, CONTENT_RIGHT)])
        pagos.append([Paragraph(str(item), CONTENT_CENTER), Paragraph(FechaPago, CONTENT_CENTER), Paragraph(FormaPago, CONTENT_CENTER), Paragraph(MonedaPago, CONTENT_CENTER), Paragraph(TipoCambio, CONTENT_CENTER),  Paragraph(NumOperacion, CONTENT_CENTER), Paragraph(MontoPagado, CONTENT_RIGHT)])
        item += 1
      
      table_pagos=Table(pagos, colWidths=[1.2*cm, 3*cm, 3.2*cm, 3.2*cm, 3.2*cm, 3.2*cm, 3*cm], repeatRows=2, style=[
        #('GRID', (0,0),(-1,-1), 1, colors.gray),
        ('SPAN', (0,0),(-1,0)), # HEADER
        ('BACKGROUND', (0,0),(-1,0), self.bg_color), # HEADER
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('VALIGN', (0,2),(-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0),(-1,-1), 2.5),
        ('LEFTPADDING', (0,0),(-1,-1), 2.5),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0),(-1,0), 0.5),
        ('BOTTOMPADDING', (0,1),(-1,-1), 2),
        ('LINEBELOW',(0,1),(-1,1), 1, self.bg_color),
        ('LINEBELOW',(0,2),(-1,-1), 0.5, self.bg_color),
      ])

      table_doctos=Table(doctos_rel, colWidths=[1*cm, 5.6*cm, 1.8*cm, 1.0*cm, 1.5*cm, 1.5*cm, 1.4*cm, 2*cm, 2*cm, 2.2*cm], repeatRows=2, style=[
        #('GRID', (0,0),(-1,-1), 1, colors.gray),
        ('SPAN', (0,0),(-1,0)), # HEADER
        ('BACKGROUND', (0,0),(-1,0), self.bg_color), # HEADER
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('VALIGN', (0,2),(-1,-1), 'TOP'),
        ('RIGHTPADDING', (0,0),(-1,-1), 1),
        ('LEFTPADDING', (0,0),(-1,-1), 1),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        ('BOTTOMPADDING', (0,0),(-1,0), 0.5),
        ('BOTTOMPADDING', (0,1),(-1,-1), 2),
        ('LINEBELOW',(0,1),(-1,1), 1, self.bg_color),
        ('LINEBELOW',(0,2),(-1,-1), 0.5, self.bg_color),
      ])

    except Exception as e:
      print("Exception pagos() | %s" % str(e))
    return table_pagos, table_doctos

  def totales(self):
    #import pdb; pdb.set_trace()
    try:
      subtotal = self.sub_total if not self.subtotal_precalculated else self.subtotal_precalculated
      total_tra = self.total_tra if not self.iva_pdf else self.iva_pdf

      total_data =[
        [Paragraph('Condiciones de pago: %s' % self.payment_terms, CONTENT_LEFT), Paragraph('Subtotal:', CONTENT_RIGHT), Paragraph('%s' % self.truncate(Decimal(subtotal), 2), CONTENT_RIGHT)],
        [Paragraph('Moneda: %s' % self.moneda, CONTENT_LEFT), Paragraph('Descuento:', CONTENT_RIGHT), Paragraph('- %s' % self.truncate(Decimal(self.discount), 2), CONTENT_RIGHT)],
        [Paragraph('Importe con letra:', SUBHEADER_LEFT), Paragraph('Total IVA:', CONTENT_RIGHT), Paragraph('+ %s' % self.truncate(Decimal(total_tra), 2), CONTENT_RIGHT)],
        [Paragraph(self.total_con_letra, CONTENT_LEFT), Paragraph('Total a pagar:', TOTAL_STYLE), Paragraph('$ %s' % self.truncate(Decimal(self.total), 2), TOTAL_STYLE)],
        [Paragraph('Observaciones: %s' % self.notes, CONTENT_LEFT), NULL, NULL],
      ]

      table_totales = Table(total_data, colWidths=[14*cm, 2.5*cm, 3.5*cm ], style=[
        #('GRID', (0,0), (-1, -1), 1, colors.gray),
        ('BACKGROUND', (1,-2), (-1,-2), self.lightgrey),
        ('LINEABOVE', (1,-2),(-1,-2), 1, self.bg_color),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('VALIGN', (1,2),(-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1.1),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        ('LEFTPADDING', (0,0),(0,-1), 0),
        ('RIGHTPADDING', (-2,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,2),(-1,-1), 2.5),
      ])
    except Exception as e:
      print("Exception totales() => %s" % str(e))
    return table_totales
  
  def totales_nomina(self):
    try:
      total_data =[
        [NULL, Paragraph('Percepciones', CONTENT_RIGHT), Paragraph('%s' % self.truncate(Decimal(self.sub_total), 2), CONTENT_RIGHT)],
        [NULL, Paragraph('Deducciones sin ISR', CONTENT_RIGHT), Paragraph('- %s' % self.truncate(Decimal(self.tot_ded), 2), CONTENT_RIGHT)],
        [Paragraph('Importe con letra:', SUBHEADER_LEFT), Paragraph('ISR Retenido', CONTENT_RIGHT), Paragraph('- %s' % self.truncate(Decimal(self.tot_isr), 2), CONTENT_RIGHT)],
        [Paragraph(self.total_con_letra, CONTENT_LEFT), Paragraph('Total', TOTAL_STYLE), Paragraph('$ %s' % self.truncate(Decimal(self.total), 2), TOTAL_STYLE)],
      ]

      table_totales = Table(total_data, colWidths=[13*cm, 4*cm, 3*cm ], style=[
        #('GRID', (0,0), (-1, -1), 1, colors.gray),
        ('LINEBELOW', (1,2),(-1,2), 1, self.bg_color),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('VALIGN', (1,2),(-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1.1),
        ('TOPPADDING', (0,0),(-1,-1), 0.5),
        ('LEFTPADDING', (0,0),(0,-1), 0),
        ('RIGHTPADDING', (-2,0),(-1,-1), 3),
        ('BOTTOMPADDING', (0,2),(-1,-1), 2.5),
      ])
    
    except Exception as e:
      #self.errors.append("Exception totales_nomina() | %s" % str(e))
      print('Exception totales_nomina() | %s' % str(e))
    return table_totales

  def employe_signature(self):
    try:
      signature_data = [
        [Paragraph(self.signature_legend, CONTENT_LEFT), Paragraph('FIRMA:', CONTENT_RIGHT), NULL],
      ]

      table_signature = Table(signature_data, colWidths=[12*cm, 1*cm, 7*cm], style=[
        #('GRID', (0,0),(-1,-1), 1, colors.gray),
        ('LINEBELOW', (-1,0),(-1,0), 1, self.bg_color),
        ('RIGHTPADDING', (0,0),(-1,-1), 0.3),
        ('LEFTPADDING', (0,0),(-1,-1), 0.3),
        ('BOTTOMPADDING', (0,0),(-1,-1), 0),
        ('VALIGN', (0,0),(-1,-1), 'BOTTOM'),
      ])
    except Exception as e:
      print("Exception employe_signature() => %s" % str(e))
    return table_signature

  def tfd(self):
    try:
      data_tfd = [
        [Paragraph('COMPROBANTE FISCAL DIGITAL POR INTERNET', HEADERS), NULL],
        [Paragraph('Folio fiscal: %s' % self.uuid, CONTENT_LEFT), Paragraph('Lugar de emisión: %s' % self.expedition_place, CONTENT_LEFT)],
        [Paragraph(u'Fecha y hora de certificación: %s' % self.date_cert, CONTENT_LEFT), Paragraph(u'Fecha y hora de emisión: %s' % self.date, CONTENT_LEFT)],
        [Paragraph('No. de serie del CSD del SAT: %s' % self.serial_sat, CONTENT_LEFT), Paragraph(u'No. de serie del CSD del emisor: %s' % self.certificate_serial, CONTENT_LEFT)],
        [Paragraph(u'Forma de pago: %s' % self.way_payment, CONTENT_LEFT), Paragraph(u'Método de pago: %s' % self.pay_method, CONTENT_LEFT)],
      ]

      table_tfd = Table(data_tfd, colWidths=[10*cm, 10*cm], style=[
        #('GRID', (0,0),(-1,-1), 1, colors.gray),
        ('SPAN', (0,0),(-1,0)),
        ('BACKGROUND', (0,0),(-1,0), self.bg_color),
        ('TOPPADDING', (0,0),(-1,-1), 1),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
      ])
      
    except Exception as e:
      print("Exception tfd() => %s" % str(e))
    return table_tfd

  def tfd_seals(self):
    try:
      self.createqr()
      QR = Image('{}/{}.png'.format(settings.QR_PATH, self.uuid), 1.3*inch, 1.3*inch)
      
      data_tfd = [
        [QR, Paragraph('Cadena Original del Complemento de Certificación Digital del SAT', HEAD_TDF)],
        [NULL, Paragraph(self.original_string_tfd, CONTENT_LEFT)],
        [NULL, Paragraph('Sello Digital del Contribuyente Emisor', HEAD_TDF)],
        [NULL, Paragraph(self.seal_cfd, CONTENT_LEFT)],
        [NULL, Paragraph('Sello Digital del SAT', HEAD_TDF)],
        [NULL, Paragraph(self.seal_sat , CONTENT_LEFT)],
      ]

      table_tfd =Table(data_tfd, colWidths=[4*cm, 16*cm], style=[
        #('GRID',(0,0),(-1,-1), 1, color.gray),
        ('LINEAFTER',(0,0),(0,-1), 1.5, self.bg_color),
        ('SPAN',(0,0),(0,-1)), # QR CODE
        ('VALIGN',(0,0),(-1,-1), 'MIDDLE'),
        ('ALIGN',(0,0),(-1,-1), 'LEFT'),
        ('TOPPADDING', (1,0),(-1,0), 2.5),
        ('BOTTOMPADDING', (1,-1),(-1,-1), 2.5),
        ('TOPPADDING', (1,1),(1,1), 0),
        ('BOTTOMPADDING', (1,1),(1,1), 3),
        ('TOPPADDING', (1,3),(1,3), 0),
        ('BOTTOMPADDING', (1,3),(1,3), 3),
        ('TOPPADDING', (1,5),(1,5), 0),
        ('BOTTOMPADDING', (1,5),(1,5), 3),
        ('LEFTPADDING', (0,0), (0,-1), 0),
        ('RIGHTPADDING', (1,0), (-1,-1), 0),
      ])

    except Exception as e:
      print("Exception tfd_seals() | %s" % str(e))
    return table_tfd

  def createqr(self):
    try:
      qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=0,
      )
      total = self.total.rstrip('+-0').lstrip('+-0')
      total = total.rstrip('.')
      seal = self.seal_cfd[-8:]
      qr.add_data("https://verificacfdi.facturaelectronica.sat.gob.mx/default.aspx?id=%s&re=%s&rr=%s&tt=%s&fe=%s" % (self.uuid, self.taxpayer_id, self.rtaxpayer_id, total, seal))

      qr.make(fit=True)
      img = qr.make_image()
      f = open('{}/{}.png'.format(settings.QR_PATH, self.uuid), "wb")
      img.save(f)
      img.close()
      f.close()
    except Exception as e:
      print("Error al crear el CodigoQR => %s" % str(e))
      #self.message = "Error al crear el CodigoQR => %s" % str(e)

  def truncate(self, f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{:,}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


class NumberedCanvas(canvas.Canvas):
  def __init__(self, *args, **kwargs):
    canvas.Canvas.__init__(self, *args, **kwargs)
    self._saved_page_states = []

  def showPage(self):
    self._saved_page_states.append(dict(self.__dict__))
    self._startPage()

  def save(self):
    """add page info to each page (page x of y)"""
    num_pages = len(self._saved_page_states)
    for state in self._saved_page_states:
      self.__dict__.update(state)
      self.draw_page_number(num_pages)
      canvas.Canvas.showPage(self)
    canvas.Canvas.save(self)

  def draw_page_number(self, page_count):
    # Change the position of this to wherever you want the page number to be
    #self.setFont('Helvetica-Bold', 8)
    self.setFont(FONT_NAME, 8)
    self.setFillColor(HexColor('#555759'))
    self.drawRightString(8.1*inch, 0.2*inch, "Página %d de %d" % (self._pageNumber, page_count))
