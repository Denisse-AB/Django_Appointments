from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import App


class CreateAppointmentTests(TestCase):
    def test_appointments_count(self):
        q = App.objects.filter(date='2022-08-01', time='11:00:00')
        count = q.count()
        self.assertIs(count > 3, False)

class EmailTest(TestCase):
    def test_send_email(self):
        input_name = 'Maria'
        context = {
            'name': input_name,
        }
        subject = 'Your appointment!'
        html_message = render_to_string('email/email.html', context)
        from_email = 'from@yourdjangoapp.com'
        to = 'to@yourdjangouser.com'
        
        self.assertTrue(send_mail(subject, html_message, from_email, [to], html_message=html_message))

class ResponseTest(APITestCase):
    url = reverse('create')
    data = { "email": "jane@doe.com", "name": "jane doe", "tel": 7874092828, "date": "2022-10-10", "time": "1:00:00"}
    
    def test_the_create_appointment_201_response(self, url=url, data=data):
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_the_create_appointment_405_response(self, url=url):
        response = self.client.get(url, data={"name": "jane doe"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_the_create_appointment_400_response(self):
        client = APIClient()
        response = client.post('/post/', {'title': 'new idea'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)