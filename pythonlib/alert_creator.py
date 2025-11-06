#!/bin/python3
#  Class that create Alert Message
# Author: Mats Olsson
# Version: 1.1
# Date: 2025-10-08

from mongoengine import *
import alert_common as common
# import syslog
import alert_message as Message
from mongoengine.connection import disconnect


class MessageCreator:
  def __init__(self, dbhost):
    connect(db='AddSecure-Op5', host=dbhost, username=common.db_user, password=common.db_password, authentication_source='admin')
    #connect(db='AddSecure-Link', host=dbhost, username=common.db_user, password=common.db_password,
     #       authentication_source='admin')

  def create_message(self, hostname, service, data, additionalInfo, url, timestamp, Id):
    message = Message.Message(
      _id=Id,
      HostName=hostname,
      Service=service,
      Data=data,
      AdditionalInfo=additionalInfo,
      Url=url,
      TimeStamp=timestamp
    )
    if not common.mock:
      message.save()
    else:
      # syslog.syslog(message.to_json())
      print(message.to_json())

  def __del__(self):
    disconnect()
    Message._collection = None
