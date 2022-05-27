#!/bin/sh

LOG_PATH=/var/log/herbalife/cron/clean_sftp.log
echo -e "\nStarting at $(date)" >> $LOG_PATH

echo "Try to clean CFDI..." >> $LOG_PATH
find /var/sftp/herbalife/CFDI -type f -name '*.xml' -mtime +3 -exec rm {} \;

echo "Try to clean PROCESADOS..." >> $LOG_PATH
find /var/sftp/herbalife/PROCESADOS -type f -name '*.xml' -mtime +3 -exec rm {} \;

echo "Try to clean REPROCESADOS..." >> $LOG_PATH
find /var/sftp/herbalife/REPROCESADOS -type f -name '*.xml' -mtime +3 -exec rm {} \;

echo "Try to clean LOGS..." >> $LOG_PATH
find /var/sftp/herbalife/LOGS -type d -mtime +3 -exec rm -rf {} \;

echo "Try to clean ERRONEOS DIRS..." >> $LOG_PATH
find /var/sftp/herbalife/ERRONEOS -type d -mtime +3 -exec rm -rf {} \;

echo "Try to clean ERRONEOS FILES..." >> $LOG_PATH
find /var/sftp/herbalife/ERRONEOS -type f -name '*.xml' -mtime +3 -exec rm -rf {} \;

echo "Try to clean /tmp/herbalife/zip..." >> $LOG_PATH
find /tmp/herbalife/zip -type f -name '*.zip' -mtime +1 -exec rm {} \;

echo "Try to clean /tmp/herbalife/pdf..." >> $LOG_PATH
find /tmp/herbalife/pdf -type f -name '*.pdf' -mtime +1 -exec rm {} \;

echo "Try to clean /tmp/herbalife/png..." >> $LOG_PATH
find /tmp/herbalife/png -type f -name '*.png' -mtime +1 -exec rm {} \;

echo "Finished at $(date)" >> $LOG_PATH

