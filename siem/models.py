from django.db import models
# 23 Columns (MINUS the ID as the rsyslog event follows a standard PK) -> THIS IS FOR THE STANDARD TEMPLATE for RSYSLOG (https://www.rsyslog.com/doc/v8-stable/configuration/modules/ompgsql.html)
# id -> integer
# customerid -> bigint
# receivedat -> timestamp (no timezone)
# devicereportedtime -> timestamp (no timezone)
# facility -> smallint
# priority -> smallint
# fromhost -> character varying (60)
# message -> text
# ntseverity -> integer
# importance -> integer
# eventsource -> character varying (60)
# eventuser -> character varying (60)
# eventcategory -> integer
# eventid -> integer
# eventbinary -> text
# maxavailable -> integer
# currusage -> integer
# minusage -> integer
# maxusage -> integer
# infounitid -> integer
# syslogtag -> character varying (60)
# genericfilename -> character varying (60)
# systemid -> integer

class Event(models.Model):
 receivedat = models.DateTimeField()
 devicereportedtime = models.DateTimeField()
 facility = models.SmallIntegerField(default=0)
 priority = models.SmallIntegerField(default=0)
 fromhost = models.CharField(max_length=60)
 fromhostip = models.CharField(max_length=60)
 message = models.TextField()
 infounitid = models.PositiveIntegerField()
 syslogtag = models.CharField(max_length=60)

 def __str__(self):
     return self.fromhost


    