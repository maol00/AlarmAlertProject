#!/bin/python3
#  Notify alert to uaw database
# Author: Mats Olsson
# Version: 1.1
# Date: 2025-10-08

import os
# import syslog
import base64
import datetime
import alert_common as common
import alert_creator as creator

# Get current timestamp as string
def get_timestamp():
  now = datetime.datetime.now()
  timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
  return timestamp

# Create base64 encoded id
def create_id(hostname, service, timestamp):
  Id = hostname + service + timestamp
  message_bytes = Id.encode('utf8')
  base64_bytes = base64.b64encode(message_bytes)
  base64_id = base64_bytes.decode('ascii')
  return base64_id

# Get environment variables from Checkmk/Nagios
# TODO add more variables if needed
def get_env():
  temp = os.environ.get('NOTIFY_HOSTNAME')
  if temp is not None:
    common.NOTIFY_HOSTNAME = temp
  temp = os.environ.get('NOTIFY_LASTHOSTSTATE')
  if temp is not None:
    common.NOTIFY_LASTHOSTSTATE = temp
  temp = os.environ.get('NOTIFY_LASTSERVICESTATE')
  if temp is not None:
    common.NOTIFY_LASTSERVICESTATE = temp
  temp = os.environ.get('NOTIFY_WHAT')
  if temp is not None:
    common.NOTIFY_WHAT = temp
  common.NOTIFY_SERVICEOUTPUT = common.NOTIFY_HOSTNAME + ' ' + common.NOTIFY_LASTHOSTSTATE + ' ' + common.NOTIFY_LASTSERVICESTATE + ' ' + common.NOTIFY_WHAT
  common.NOTIFY_HOSTOUTPUT = common.NOTIFY_HOSTNAME + ' ' + common.NOTIFY_LASTHOSTSTATE + ' ' + common.NOTIFY_LASTSERVICESTATE + ' ' + common.NOTIFY_WHAT

# Notify alert to uaw database
def notify_alert():
  # Get environment var
  get_env()
  # Check that we have down state for Host
  # TODO call method to check condition for alert
  if common.NOTIFY_WHAT == 'HOST' and common.NOTIFY_LASTHOSTSTATE == 'UP':
    exit(0)
  if common.NOTIFY_WHAT == 'HOST':
    data = common.create_host_data()
    service = common.NOTIFY_HOSTNAME
    additionalInfo = common.NOTIFY_HOSTOUTPUT
  else:
    data = common.create_service_data()
    service = common.NOTIFY_SERVICE
    additionalInfo = common.NOTIFY_SERVICEOUTPUT

  hostname = common.NOTIFY_HOSTNAME
  url = common.create_url()
  timestamp = get_timestamp()
  id = create_id(hostname, service, timestamp)

  # Create message in first db
  if common.db_host or common.mock:
    # syslog.syslog("Save message in database ({})".format(common.db_host))
    cm = creator.MessageCreator(common.db_host)
    cm.create_message(common.NOTIFY_HOSTNAME, common.NOTIFY_SERVICEDESC, data, additionalInfo, url, timestamp, id)
    del cm
