from app.core.models import Branch
from app.providers.models import Invoice as PInvoice
from app.invoicing.models import Invoice
from lxml import etree
from django.core.exceptions import MultipleObjectsReturned


def update_invoice_branch(invoice_id, modelname='SInvoice'):

  if modelname == 'SInvoice':
    model = SInvoice
  if modelname == 'PayRoll':
    model = PayRoll
  if modelname == 'Invoice':
    model = Invoice
  if modelname == 'RInvoice':
    model = RInvoice

  try:
    invoice = model.objects.get(id=invoice_id)
    try:    
      xml_etree = etree.fromstring(invoice.xml)
      zipcode = xml_etree.get('LugarExpedicion')
      try:
        try:
          branch = Branch.objects.get(zipcode=zipcode)
        except Branch.DoesNotExist:
          branch = Branch(name='Inexistente %s'%zipcode, zipcode=zipcode)
          branch.save()
        except MultipleObjectsReturned:
          branch = Branch.objects.filter(zipcode=zipcode).order_by('?').first()
        invoice.branch = branch
        invoice.save()
      except Exception, e1:
        print "Exception update_sinvoice_branch => %s" % str(e1)
        print "zipcode => %s" % zipcode
        print "%s => %s" % (invoice_id, invoice.uuid)
    except Exception, e2:
      print "Exception update_sinvoice_branch etree => %s" % str(e2)
  except Exception, e3:
    print "Exception update_sinvoice_branch %s => %s" % (model, str(e3))
    print "invoice_id => %s" % invoice_id
 

print "Processing SInvoice"
invoices = SInvoice.objects.filter(branch__isnull=True)
for invoice in invoices:
  update_invoice_branch(invoice.id, 'SInvoice')
print "EndProcessing PayRoll"

print "Processing PayRoll"
payrolls = PayRoll.objects.filter(branch__isnull=True)
for payroll in payrolls:
  update_invoice_branch(payroll.id, 'PayRoll')
print "EndProcessing PayRoll"

#invoices = Invoice.objects.filter(branch__isnull=True)
#for invoice in invoices:
#  update_invoice_branch(invoice.id, 'Invoice')

#invoices = RInvoice.objects.filter(branch__isnull=True)
#for invoice in invoices:
#  update_invoice_branch(invoice.id, 'RInvoice')

