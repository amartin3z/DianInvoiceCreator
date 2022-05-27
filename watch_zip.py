import os
import sys
import time
import logging
import getopt
from datetime import datetime
from collections import deque
import hashlib
import pyinotify
from pyunpack import Archive
import shutil
import glob
import django
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE
import asyncore

watch_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(watch_path) 
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'liverpool.settings.local')
django.setup()

from django.conf import settings


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USER = 'devsfinkok@gmail.com'
EMAIL_PASS = 'f@INKo19de!VEl'
EMAIL_TO_LST = ('desarrollo@finkok.com', 'aherrejon@finkok.com', 'amartinez@finkok.com', 'jperez@finkok.com', 'achavez@finkok.com')
EMAIL_MSG_TO = COMMASPACE.join(EMAIL_TO_LST)


def get_now():
    "Get the current date and time as a string"
    return "[{}]".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def getext(filename):
    "Get the file extension."
    return os.path.splitext(filename)[-1][1:].strip().lower()

def tail(fn, n):
  with open(fn) as fin:
    return list(deque(fin, n))

def checksum_md5(lst):
  md5_obj = hashlib.md5()
  md5_obj.update("".join(lst))
  return md5_obj.hexdigest()

def send_email(subject, message):
  server = smtplib.SMTP("{}:{}".format(EMAIL_HOST, EMAIL_PORT))
  server.starttls()
  server.login(EMAIL_USER, EMAIL_PASS)
  msg = MIMEMultipart()
  msg.attach(MIMEText(message))
  msg['Subject'] = subject
  msg['To'] = EMAIL_MSG_TO
  server.sendmail(EMAIL_USER, EMAIL_TO_LST, msg.as_string())


class LIVERPOOLHandler(pyinotify.ProcessEvent):

  def my_init(self, output=None):
    self.output = output

  def process_IN_CREATE(self, event):
    #print "Creating:", event.pathname
    pass

  def process_IN_DELETE(self, event):
    #print "Removing:", event.pathname
    pass

  def process_IN_CLOSE_WRITE(self, event):

    print("\n{} Processing: {}".format(get_now(), event.pathname))

    dirname = os.path.dirname(event.pathname)
    filename = os.path.basename(event.pathname)
    filesize = os.path.getsize(event.pathname)
    fileext = getext(event.pathname)

    if fileext in  ('xml', 'zip'):
      if fileext == 'xml':    
        if filesize < 15728640: # 15Mb
          if filesize > 10485760: # 10Mb
            try:        
              subject = 'LIVERPOOL FIRST LIMIT EXCEEDED'
              message = 'Liverpool has exceeded the first limit: file {} -> {} bytes.'.format(filename, filesize)
              send_email(subject, message)
            except Exception, e:
              print 'EXCEPTION FIRST LIMIT => {}'.format(str(e))
          liverpool_obj = LIVERPOOL(xml_path=event.pathname, output=self.output)
        else:
          try:
            subject = 'LIVERPOOL SECOND LIMIT EXCEEDED'
            message = 'Liverpool has exceeded the second limit: file {} -> {} bytes, the file was moved to exceeded directory.'.format(filename, filesize)
            send_email(subject, message)
          except Exception, e:
            print 'EXCEPTION SECOND LIMIT => {}',format(str(e))
          destination_path = os.path.join(dirname, '..', 'exceeded', filename)      
          shutil.move(event.pathname, destination_path)
          print 'File {} exceed 15 MB, actual size {}'.format(event.pathname, filesize)
      elif fileext == 'zip':
        try:
          Archive(event.pathname).extractall(dirname, patool_path='/usr/bin/patool')
        except Exception, e:
          print 'EXCEPTION DECOMPRESS FILE {}'.format(event.pathname)
          time.sleep(2)
          try:
            Archive(event.pathname).extractall(dirname, patool_path='/usr/bin/patool')
          except Exception, e2:
            print "EXCEPTION2 DECOMPRESS FILE {}".format(str(e2))            
        destination_path = os.path.join(dirname, '..', 'unzipped', filename)
        shutil.move(event.pathname, destination_path)
        print('{} EXTRACT DONE => {}'.format((get_now(), filename)))
    else:
      print("{} NOT XML OR ZIP FILE: {}".format(get_now(), event.pathname))

    return    


if __name__ == "__main__":

  path = None
  output = None

  try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:o:",["help", "directory=", "output"])
  except getopt.GetoptError:
    print 'watch.py -d <directory> -o <output>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print 'watch.py -d <directory> -o <output>'
      sys.exit()
    elif opt in ("-d", "--directory"):
      path = arg
    elif opt in ("-o", "--output"):
      output = arg

  if not path or not output:
    print('watch.py -d <directory> -o <output>')
    sys.exit(2)

  if not os.path.exists(path):
    print( "Error. Directory {} does not exist.".format(path))
    sys.exit(2)

  if not os.path.exists(output):
    print("Error. Output directory {} does not exist.".format(output))
    sys.exit(2)

  print("================================ Started at: {} ================================".format(get_now()))
  print("Input: {}".format(path))
  print("Output: {}".format(output))

  # PROCESS PENDING FILES
  pending_zip = glob.glob('{}/*.zip'.format(path))
  for zip_file in pending_zip:
    dirname = os.path.dirname(zip_file)
    filename = os.path.basename(zip_file)
    Archive(zip_file).extractall(os.path.dirname(zip_file))
    destination_path = os.path.join(dirname, '..', 'unzipped', filename)
    shutil.move(zip_file, destination_path)
 
  pending_xmls = glob.glob('{}/*.xml'.format(path))
  for xml_path in pending_xmls:
    print("\n{} Processing: {}".format(get_now(), xml_path))
    liverpool_obj = LIVERPOOL(xml_path=xml_path)
  ## END PROCESS PENDING FILES

  wm = pyinotify.WatchManager()
  mask = pyinotify.IN_CLOSE_WRITE 
  handler = LIVERPOOLHandler(output=output)
  notifier = pyinotify.AsyncNotifier(wm, handler)
  wdd = wm.add_watch(path, mask, rec=False)
  asyncore.loop()
