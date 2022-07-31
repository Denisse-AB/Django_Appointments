from django.test import TestCase
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import App

class PostModelTests(TestCase):
    def test_appointments_count(self, date='2021-04-13', time='13:00:00'):
        q = App.objects.filter(date=date, time=time)
        count = q.count()
        self.assertIs(count > 3, False)

class EmailTest(TestCase):
    def test_send_email(self):
        input_name = 'Maria'
        context = {
            'name': input_name,
        }
        subject = 'Tu Cita!'
        html_message = render_to_string('citas\email.html', context)
        from_email = 'from@yourdjangoapp.com'
        to = 'to@yourdjangouser.com'

        return send_mail(subject, html_message, from_email, [to], html_message=html_message)