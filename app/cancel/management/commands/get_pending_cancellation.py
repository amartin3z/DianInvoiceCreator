from django.core.management.base import BaseCommand, CommandError
from app.cancel.tasks import consult_pending_cancellation
from pdb import set_trace
from django.conf import settings

import fnmatch
class Command(BaseCommand):
  help = 'Closes the specified poll for voting'

  #def add_arguments(self, parser):
  #    parser.add_argument('poll_id', nargs='+', type=int)

  def handle(self, *args, **options):
    consult_pending_cancellation()
