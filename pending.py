#!/opt/.virtualenvs/soriana/bin/python
import glob
import threading
from datetime import datetime
import os
if 'DJANGO_SETTINGS_MODULE' not in os.environ:
  os.environ['DJANGO_SETTINGS_MODULE'] = 'ublinvoice.settings.demo'
import django
django.setup()


def get_now():
  "Get the current date and time as a string"
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def split_seq(seq, num_pieces):
  start = 0
  for i in xrange(num_pieces):
    stop = start + len(seq[i::num_pieces])
    yield seq[start:stop]
    start = stop


def process_pending(pending=[], thread_num=1):
  for xml in pending:
    print("{} Thread {}: Processing: {}".format(get_now(), thread_num, xml))
    #stamp_obj = STAMPFK(xml_path=xml)


# # Patch initialize async tasks
# print(add(4,5))
# print(add.delay(4,5))
# print(add.apply_async((4,5),))
# EndPatch


THREADS_NUM = 1
thread_lst = []

path = '/var/sftp/soriana/ENTRADA'
pending_xmls = glob.glob('{}/*.xml'.format(path))

print("Pending Files: {}".format(len(pending_xmls))

thread_count = 1
for pending in split_seq(pending_xmls, THREADS_NUM):
  print("================THREAD=================")
  th = threading.Thread(target=process_pending, args=(pending, thread_count))
  thread_lst.append(th)
  thread_count += 1

for thread  in thread_lst:
  thread.start()

for thread  in thread_lst:
  thread.join()
