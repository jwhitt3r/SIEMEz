from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
import datetime
from .views import HomePageView, SearchEventResultsListView, EventListView
from .models import Event

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the Home Page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class EventpageTests(TestCase):
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


    def test_event_creation(self):
        self.assertEqual(f'{self.event.receivedat}', datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M'))
        self.assertEqual(f'{self.event.devicereportedtime}', datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M'))
        self.assertEqual(f'{self.event.facility}', '1')
        self.assertEqual(f'{self.event.priority}', '1')
        self.assertEqual(f'{self.event.fromhost}',  'testmachine')
        self.assertEqual(f'{self.event.message}', 'this is a test message')
        self.assertEqual(f'{self.event.infounitid}', '1')
        self.assertEqual(f'{self.event.syslogtag}', 'testtag')

    def test_event_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='testpass123')
        response = self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testmachine')
        self.assertTemplateUsed('siem/event.html')


    def test_event_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/event/' % (reverse('account_login')))
        response = self.client.get('%s?next=/event/' % (reverse("account_login")))
        self.assertContains(response, 'Log In')

    def test_searchevent_url_resolves_searchevent(self):
        view = resolve('/event/')
        self.assertEqual(
            view.func.__name__,
            EventListView.as_view().__name__
        )

class TestSearchView(TestCase):
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
            priority = 3,
            fromhost = 'testmachine',
            fromhostip = '127.0.0.1',
            message = 'this is a test message',
            infounitid = 1,
            syslogtag = 'testtag',
        )
        self.client.login(email='reviewuser@email.com', password='testpass123')

    def test_search_view_template(self):
        self.response = self.client.get(reverse('search_event'))
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'siem/search_event.html')
        self.assertContains(self.response, 'Return to Events')
        self.assertNotContains(self.response, 'This should not be on the search events page.')

    def test_event_list_view_for_logged_in_user(self):
        self.response = self.client.get(reverse('search_event'), data={'hostname': self.event.fromhost, 'start': self.event.receivedat, 'end': self.event.receivedat, 'facility': self.event.facility, 'priority':self.event.priority, 'fromhostip': self.event.fromhostip, 'message': self.event.message, 'infounitid': self.event.infounitid, 'syslogtag': self.event.syslogtag})
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'testmachine')
        self.assertContains(self.response, '1')
        self.assertContains(self.response, '3')
        self.assertContains(self.response, 'this is a test message')
        self.assertContains(self.response, 'testtag')

    def test_searchevent_url_resolves_searchevent(self):
        view = resolve('/search_event/')
        self.assertEqual(
            view.func.__name__,
            SearchEventResultsListView.as_view().__name__
        )

