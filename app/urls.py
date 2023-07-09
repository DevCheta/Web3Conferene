from django.urls import path, include
from .views import ListCreateSponsor, ListCreateTicket, ListCreateSpeaker

urlpatterns = [
    path('ticket/', ListCreateTicket.as_view(), name='ListCreateTicket'),
    path('sponsor/', ListCreateSponsor.as_view(), name='ListCreateSponsor'),
    path('speaker/', ListCreateSpeaker.as_view(), name='ListCreateSpeaker'),
]