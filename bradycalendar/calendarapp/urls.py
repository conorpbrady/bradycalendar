from django.urls import path
from calendarapp import views

urlpatterns = [
        path('api/events', views.EventList.as_view()),
        ]
