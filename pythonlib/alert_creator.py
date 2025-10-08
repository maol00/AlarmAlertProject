#!/bin/python
# Author: Andreas Lindh
# Version: 1.0
# Date: 2020-04-21
from mongoengine import *

import alert_common as common
# import syslog
import alert_message as Message

from mongoengine.connection import disconnect


class MessageCreator:
  def __init__(self, dbhost):
    #connect(db='AddSecure-Op5', host=dbhost, username=common.db_user, password=common.db_password, authentication_source='admin')
    connect(db='AddSecure-Link', host=dbhost, username=common.db_user, password=common.db_password,
            authentication_source='admin')


  def create_message(self, hostname, service,data,additionalInfo,url,timestamp,id):
    "Create post in Message collection"
    message = Message.Message(
      _id=id,
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
        #syslog.syslog(message.to_json())
        print(message.to_json())


  def __del__(self):
    "Destructor. Close connection to db and set collection to null"
    disconnect()
    Message._collection = None
