from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
import datetime
from .views import CaseListView, CaseDeleteView, CaseDetailView, CaseUpdateView, CaseCreateView
from .models import Case
from siem.models import Event

class CasepageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
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
        self.case = Case.objects.create(
            date_created = datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M'),
            author = self.user,
            case_notes = "test note",
            case_name = "test case",
        )
        self.client.login(email='reviewuser@email.com', password='testpass123')

    def test_case_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('case_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Incident Cases')
        self.assertTemplateUsed('cases/case_list.html')

    def test_case_detail_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')        
        self.response = self.client.get(reverse('case_detail', args=(self.case.pk,)))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Test Case')
        self.assertNotContains(self.response, 'This should not be on the search events page.')
        self.assertTemplateUsed('cases/case_detail.html')

    def test_case_edit_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.response = self.client.get(reverse('case_edit', args=(self.case.pk,)))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Edit Post')
        self.assertNotContains(self.response, 'This should not be on the search events page.')

    def test_case_delete_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        self.response = self.client.get(reverse('case_delete', args=(self.case.pk,)))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'Delete Case')
        self.assertNotContains(self.response, 'This should not be on the search events page.')

    def test_case_creation(self):
        self.assertEqual(f'{self.case.author}', 'reviewuser')
        self.assertEqual(f'{self.case.case_notes}',  'test note')
        self.assertEqual(f'{self.case.case_name}', 'test case')

    def test_event_url_resolves_event(self):
        view = resolve('/cases/')
        self.assertEqual(
            view.func.__name__,
            CaseListView.as_view().__name__
        )

