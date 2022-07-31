from .models import App
from rest_framework import serializers

class AppSerializers(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['email', 'name', 'tel', 'date', 'time']