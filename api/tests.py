from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from siem.models import Event
from api.serializers import EventSerializer
import datetime



class AccountTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123',
        ) 
        self.event = Event.objects.create(
        receivedat = datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M'),
        devicereportedtime = datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M'),
        facility = 1,
        priority = 1,
        fromhost = 'testmachine',
        fromhostip = '127.0.0.1',
        message = 'this is a test message',
        infounitid = 1,
        syslogtag = 'testtag',
        )
        
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.url = reverse('api')

    def test_get_collection(self):
        self.response = self.client.get(self.url)
        self.events = Event.objects.all()
        self.serializer = EventSerializer(self.events, many=True)
        self.assertEqual(self.response.data, self.serializer.data)
        self.assertEqual(self.response.status_code, 200)

