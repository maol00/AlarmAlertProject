#!/bin/python
# Author: Andreas Lindh
# Version: 1.0
# Date: 2020-04-21


# Database connection settings
db_host = "85.117.170.46"
db_user = "op5-admin"
db_user="iot-dbadmin"
db_password = "qTLdgz8x6jNuFOSKH4JX"
db_password = "uRHqVhVmz6zGuHM7JSi9"

# Set mock to "" to write to db
mock = None

## NOTIFY Environment variables
# Common
CHECKMK_URL='https://tri2-web-checkmk.iot.addsecure.com/link_cmkweb'
NOTIFY_HOSTNAME ='tri-e2e-fin'
NOTIFY_HOSTADDRESS = '100.123.1.1'
NOTIFY_SHORTDATETIME ='2025-10-02 18:13:38'
NOTIFY_HOSTURL = '/check_mk/index.py?start_url=view.py?view_name%3Dhoststatus%26host%3Dtri-e2e-sthlm%26site%3Dlink_tripnet1'
NOTIFY_MONITORING_HOST = 'tri1-checkmk.iot.addsecure.com'
OMD_ROOT = '/omd/sites/link_tripnet1'
NOTIFY_WHAT = 'HOST' # SERVICE or HOST

# Host Down
NOTIFY_LASTHOSTSTATE = 'DOWN'
NOTIFY_HOSTOUTPUT = 'CRIT - No heartbeat since 2025-10-02 18:13:38 (check interval 1m)'

# Service Critical
NOTIFY_SERVICEURL = '/check_mk/index.py?start_url=view.py?view_name%3Dservice%26host%3Dtri-e2e-fin%26service%3DCheck_MK%26site%3Dlink_tripnet1'
NOTIFY_LASTSERVICESTATE = 'CRITICAL'
NOTIFY_SERVICEDESC = 'Telia e2e test'
NOTIFY_SERVICEOUTPUT = 'CRIT - No heartbeat since 2025-10-02 18:13:38 (check interval 1m)'


def create_host_data():
  data = "Host {} detected {}.\r\n'{}' ({}) is {}".format(NOTIFY_HOSTNAME, NOTIFY_LASTHOSTSTATE, NOTIFY_HOSTNAME, NOTIFY_HOSTADDRESS, NOTIFY_LASTHOSTSTATE)
  return data


def create_service_data():
  data = "Service {} detected {}\r\n.{} on {} has passed the threshold".format(NOTIFY_SERVICEDESC, NOTIFY_LASTSERVICESTATE, NOTIFY_SERVICEDESC, NOTIFY_HOSTNAME)
  return data


def create_url():
    if NOTIFY_WHAT == 'SERVICE':
        return CHECKMK_URL + ''+ NOTIFY_SERVICEURL
    else:
        return CHECKMK_URL+ NOTIFY_HOSTURL
