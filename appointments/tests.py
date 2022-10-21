from django.test import TestCase
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.test import APITestCase
from rest_framework import status
from .models import App


class CreateAppointmentTests(TestCase):
    def test_appointments_count(self, date='2022-04-13', time='13:00:00'):
        q = App.objects.filter(date=date, time=time)
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
    data = {'date': '2022-10-10', 'time': '1:00:00'}
    
    def test_the_create_appointment_400_response(self, url=url, data=data):
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_the_create_appointment_405_response(self, url=url, data=data):
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)