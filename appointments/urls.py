from django.urls import path
from .views import CreateAppointment


urlpatterns = [
    path('post/', CreateAppointment.as_view(), name='create'),
]