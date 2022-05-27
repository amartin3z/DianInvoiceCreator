import sys
import os
import time
import logging
import getopt
from datetime import datetime
from collections import deque
import hashlib
import pyinotify
import asyncore
import django

watch_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(watch_path) 
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ublinvoice.settings.local')
django.setup()

from django.conf import settings
import glob


def get_now():
    "Get the current date and time as a string"
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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


class FileHandler(pyinotify.ProcessEvent):

  def process_IN_CREATE(self, event):
    #print "Creating:", event.pathname
    pass

  def process_IN_DELETE(self, event):
    #print "Removing:", event.pathname
    pass

  def process_IN_CLOSE_WRITE(self, event):

    ext = getext(event.pathname)
    ext = ext.lower()
    if ext not in ['zip']:
      print("{} NOT A VALID EXTENSION FILE: {}".format(get_now(), event.pathname))
      return

    #import pdb;pdb.set_trace()
    print("{} Processing: {}".format(get_now(), event.pathname))
    if ext == 'xml':
      stamp_obj = STAMPFK(xml_path=event.pathname)
    #elif ext == 'nom':
    #  stamp_obj = STAMPFKNOM(xml_path=event.pathname)    
    #stamp.apply_async((event.pathname,))
    #stamp(event.pathname)


if __name__ == "__main__":

  path = None

  # Patch initialize async tasks
  add(4,5)
  #add.delay(4,5)
  #add.apply_async((4,5),)
  # EndPatch

  try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "directory"])
  except getopt.GetoptError:
    print 'watch.py1 -d <directory>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print 'watch.py2 -d <directory>'
      sys.exit()
    elif opt in ("-d", "--directory"):
      path = arg

  print path
  if not path:
    print 'watch.py3 -d <directory>'
    sys.exit(2)

  if not os.path.exists(path):
    print("Error. Directory {} does not exist.".format(path))
    sys.exit(2)

  print("================================ Started at: {} ================================".format(get_now()))
  print("Input: {}".format(path))

  wm = pyinotify.WatchManager()
  mask = pyinotify.IN_CLOSE_WRITE | pyinotify.IN_DELETE | pyinotify.IN_CREATE

  handler = FileHandler()
  #notifier = pyinotify.Notifier(wm, handler)
  notifier = pyinotify.AsyncNotifier(wm, handler)
  wdd = wm.add_watch(path, mask, rec=False)

  #Process pending files
  """
  pending_xmls = glob.glob('{}/*.xml'.format(path))
  for xml_path in pending_xmls:
    print("{} Processing: {}".format(get_now(), xml_path))
    stamp_obj = STAMPFK(xml_path=xml_path)

  pending_nom = glob.glob('{}/*.nom'.format(path))
  for nom_path in pending_nom:
    print("{} Processing Nom: {}".format(get_now(), nom_path))
    stamp_obj = STAMPFKNOM(xml_path=nom_path)
  """
  #notifier.loop()
  asyncore.loop()
