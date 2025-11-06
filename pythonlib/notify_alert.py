#!/bin/python3
#  Notify alert to UAW database
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


# Notify alert to uaw database
def notify_alert():
  # Get environment var
  common.get_env()
  # Check that we have down state for Host or Critical for Service
  if common.NOTIFY_WHAT == 'HOST' and common.NOTIFY_HOSTSTATE == 'UP':
    exit(0)
  if common.NOTIFY_WHAT == 'SERVICE' and common.NOTIFY_SERVICESTATE != 'CRITICAL':
    exit(0)
  if common.NOTIFY_WHAT == 'HOST':
    data = common.create_host_data()
    service = common.NOTIFY_HOSTNAME
  else:
    data = common.create_service_data()
    service = common.NOTIFY_SERVICEDESC

  additionalInfo = common.ADD_INFO
  hostname = common.NOTIFY_HOSTNAME
  url = common.create_url()
  timestamp = get_timestamp()
  Id = create_id(hostname, service, timestamp)

  # Create message in first db
  if common.db_host or common.mock:
    # syslog.syslog("Save message in database ({})".format(common.db_host))
    cm = creator.MessageCreator(common.db_host)
    cm.create_message(common.NOTIFY_HOSTNAME, service, data, additionalInfo, url, timestamp, Id)
    del cm
