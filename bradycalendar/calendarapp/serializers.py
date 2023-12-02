from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('month', 'event_date', 'death_date', 'is_anniversary', 'name', 'second_name')
