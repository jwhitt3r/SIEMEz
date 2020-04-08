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
 customerid = models.BigIntegerField(blank=True, null=True)
 receivedat = models.DateTimeField()
 devicereportedtime = models.DateTimeField()
 facility = models.IntegerField()
 priority = models.IntegerField()
 fromhost = models.CharField(max_length=60)
 message = models.TextField()
 ntseverity = models.IntegerField(blank=True, null=True)
 importance = models.IntegerField(blank=True, null=True)
 eventsource = models.CharField(max_length=60, blank=True, null=True)
 eventuser = models.CharField(max_length=60, blank=True, null=True)
 eventcategory = models.IntegerField(blank=True, null=True)
 eventid = models.IntegerField(blank=True, null=True)
 eventbinary = models.TextField(blank=True, null=True)
 maxavailable = models.IntegerField(blank=True, null=True)
 currusage = models.IntegerField(blank=True, null=True)
 minusage = models.IntegerField(blank=True, null=True)
 maxusage = models.IntegerField(blank=True, null=True)
 infounitid = models.IntegerField()
 syslogtag = models.CharField(max_length=60)
 eventlogtype = models.CharField(max_length=60, blank=True, null=True)
 genericfilename = models.CharField(max_length=60, blank=True, null=True)
 systemid = models.IntegerField(blank=True, null=True)