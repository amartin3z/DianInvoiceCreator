#!/usr/bin/sh
MONITORING_PATH='/var/sftp/herbalife/ENTRADA'
MAX_INVOICES=3000
count_xml=$(find "$MONITORING_PATH" -iname '*.xml' | wc -l)
if [ $count_xml -gt $MAX_INVOICES ] ; then
  pending_is_running=$(supervisorctl status herbalife-pending | awk '{ print $2}')
  if [ ! $pending_is_running = 'RUNNING' ]; then
    supervisorctl stop herbalife-sftpwatch
    supervisorctl start herbalife-pending
    supervisorctl start herbalife-sftpwatch
    watch_is_running=$(supervisorctl status herbalife-sftpwatch | awk '{ print $2}')
    #if [ ! $watch_is_running = 'RUNNING' ]; then
    #fi
  fi
fi
