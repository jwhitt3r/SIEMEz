from rest_framework import serializers
from siem.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'receivedat', 'devicereportedtime', 'facility', 'priority',
                  'fromhost', 'fromhostip', 'message', 'infounitid', 'syslogtag',)
        model = Event
