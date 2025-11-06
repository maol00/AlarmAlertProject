#!/bin/python3
#  Class that handle MongoDB Message
# Author: Mats Olsson
# Version: 1.1
# Date: 2025-10-08

from mongoengine import *
import datetime
from datetime import timezone

class Message(Document):
  """Message model."""
  _id = StringField()
  HostName = StringField()
  Service = StringField()
  TimeStamp = DateTimeField(default=datetime.datetime.now(timezone.utc))
  Data = StringField()
  AdditionalInfo = StringField()
  Url = StringField()
  HandleDate = StringField(null=True)
  meta = {'collection': 'Message'}
