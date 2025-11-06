#!/bin/python
# Author: Mats
# Version: 1.1
# Date: 2025-10-21

from datetime import datetime, timezone

# Database connection settings
db_host = "85.117.160.5"
#db_host = "85.117.170.46"
db_user = "op5-admin"
#db_user = "iot-dbadmin"
db_password = "qTLdgz8x6jNuFOSKH4JX"
#db_password = "uRHqVhVmz6zGuHM7JSi9"

# Set mock to "" to write to db
mock = None
now = datetime.now()

# NOTIFY Environment variables
# Common
CHECKMK_URL = 'https://tri2-web-checkmk.iot.addsecure.com/link_cmkweb'
NOTIFY_HOSTNAME = 'tri1-checkmk-test'
NOTIFY_HOSTADDRESS = '85.117.171.70'
NOTIFY_SHORTDATETIME = now.strftime('%Y-%m-%d %H:%M:%S')
NOTIFY_HOSTURL = '/check_mk/index.py?start_url=%2Flink_cmkweb%2Fcheck_mk%2Fview.py%3Fhost%3Dtri1-checkmk-test%26site%3Dlink_tripnet1%26view_name%3Dhost'
NOTIFY_MONITORING_HOST = 'tri1-checkmk.iot.addsecure.com'
OMD_ROOT = '/omd/sites/link_tripnet1'
NOTIFY_WHAT = 'SERVICE'  # SERVICE or HOST

# Host Down
NOTIFY_HOSTSTATE = 'DOWN'
NOTIFY_HOSTOUTPUT = 'CRIT - No heartbeat since 2025-10-02 18:13:38 (check interval 1m)'

# Service Critical
NOTIFY_SERVICEURL = '/check_mk/index.py?start_url=%2Flink_cmkweb%2Fcheck_mk%2Fview.py%3Fhost%3Dtri1-checkmk-test%26service%3DFilesystem%2B%252F%26site%3Dlink_tripnet1%26view_name%3Dservice'
NOTIFY_SERVICESTATE = 'CRITICAL'
NOTIFY_SERVICEDESC = 'Filesystem'
NOTIFY_SERVICEOUTPUT = 'CRIT - No heartbeat since 2025-10-02 18:13:38 (check interval 1m)'
ADD_INFO = ''


def create_host_data():
  data = "Host {} detected {}.\r\n'{}' ({}) is {}".format(NOTIFY_HOSTNAME, NOTIFY_HOSTSTATE, NOTIFY_HOSTNAME,
                                                          NOTIFY_HOSTADDRESS, NOTIFY_HOSTSTATE)
  return data


def create_service_data():
  data = "Service {} detected {}\r\n.{} on {} has passed the threshold".format(NOTIFY_SERVICEDESC, NOTIFY_SERVICESTATE,
                                                                               NOTIFY_SERVICEDESC, NOTIFY_HOSTNAME)
  return data


def create_url():
  if NOTIFY_WHAT == 'SERVICE':
    return CHECKMK_URL + '' + NOTIFY_SERVICEURL
  else:
    return CHECKMK_URL + NOTIFY_HOSTURL


def get_env():
  import os
  # Common Env. Var.
  temp = os.environ.get('NOTIFY_MONITORING_HOST')
  if temp is not None:
    global NOTIFY_MONITORING_HOST
    NOTIFY_MONITORING_HOST = temp
  temp = os.environ.get('OMD_ROOT')
  if temp is not None:
    global OMD_ROOT
    OMD_ROOT = temp
  temp = os.environ.get('NOTIFY_WHAT')
  if temp is not None:
    global NOTIFY_WHAT
    NOTIFY_WHAT = temp
  temp = os.environ.get('NOTIFY_SHORTDATETIME')
  if temp is not None:
    global NOTIFY_SHORTDATETIME
    NOTIFY_SHORTDATETIME = temp

  # Host Env. Var.
  temp = os.environ.get('NOTIFY_HOSTNAME')
  if temp is not None:
    global NOTIFY_HOSTNAME
    NOTIFY_HOSTNAME = temp
  temp = os.environ.get('NOTIFY_HOSTADDRESS')
  if temp is not None:
    global NOTIFY_HOSTADDRESS
    NOTIFY_HOSTADDRESS = temp
  temp = os.environ.get('NOTIFY_HOSTSTATE')
  if temp is not None:
    global NOTIFY_HOSTSTATE
    NOTIFY_HOSTSTATE = temp
  temp = os.environ.get('NOTIFY_HOSTURL')
  if temp is not None:
    global NOTIFY_HOSTURL
    NOTIFY_HOSTURL = temp
  temp = os.environ.get('NOTIFY_HOSTOUTPUT')
  if temp is not None:
    global NOTIFY_HOSTOUTPUT
    NOTIFY_HOSTOUTPUT = temp

  # Service Env. Var.
  temp = os.environ.get('NOTIFY_SERVICEDESC')
  if temp is not None:
    global NOTIFY_SERVICEDESC
    NOTIFY_SERVICEDESC = temp
  temp = os.environ.get('NOTIFY_SERVICESTATE')
  if temp is not None:
    global NOTIFY_SERVICESTATE
    NOTIFY_SERVICESTATE = temp
  temp = os.environ.get('NOTIFY_SERVICEURL')
  if temp is not None:
    global NOTIFY_SERVICEURL
    NOTIFY_SERVICEURL = temp
  temp = os.environ.get('NOTIFY_SERVICEOUTPUT')
  if temp is not None:
    global NOTIFY_SERVICEOUTPUT
    NOTIFY_SERVICEOUTPUT = temp

  global ADD_INFO
  ADD_INFO = ('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}'.format(NOTIFY_MONITORING_HOST, OMD_ROOT,
                                                                              NOTIFY_SHORTDATETIME, NOTIFY_WHAT,
                                                                              NOTIFY_HOSTNAME, NOTIFY_HOSTADDRESS,
                                                                              NOTIFY_HOSTSTATE, NOTIFY_HOSTURL,
                                                                              NOTIFY_HOSTOUTPUT, NOTIFY_SERVICEDESC,
                                                                              NOTIFY_SERVICESTATE,
                                                                              NOTIFY_SERVICEURL, NOTIFY_SERVICEOUTPUT))
  ADD_INFO = ('{0} ({1}). Monitoring source: {2} '.format(NOTIFY_HOSTNAME, NOTIFY_HOSTADDRESS, NOTIFY_MONITORING_HOST))
