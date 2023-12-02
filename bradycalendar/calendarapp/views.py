from django.shortcuts import render
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

from datetime import datetime
# Create your views here.


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        month = self.request.GET.get('month', '')
        return Event.objects.filter(month = month)
