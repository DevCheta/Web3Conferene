from django.shortcuts import render
from rest_framework import generics, status
from .utils import Util
from .models import Speaker, Ticket, Sponsor
from .serializer import SpeakerSerializer, TicketSerializer, SponsorSerializer
# Create your views here.

class ListCreateSpeaker(generics.ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        speakers = Speaker.objects.filter(email=email)
        
        
        if speakers.exists():
            user = speakers.first()  # Get the first speaker with the matching email
        else:
            # Handle the case when no speaker with the given email is found
            # You can raise an appropriate exception or return a response indicating the error
            return Response({"error": "Speaker not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Rest of the code for sending emails to the user and admin
        
        # Send email to the user
        email_body = "Dear {},\n\nThank you for registering to be a speaker at the Web3 Global Conference. Your registration has been received, and we appreciate your interest in our event.\n\nPlease be patient for further information and updates regarding your speaking session.\n\nIf you have any other inquiries, kindly contact us at info.web3globalconference@gmail.com.\n\nBest regards,\nW3GC".format(user.name)
        email_subject = "Your Registration Confirmation for Web3 Global Conference"

        data = {
            "email_body": email_body,
            "email_subject": email_subject,
            "to_email": user.email,
        }
        Util.send_email(data)
        
        # Send email to the admin
        admin_email_body = "A new speaker has registered:\n\nName: {}\nEmail: {}\nTopic: {}\nBio: {}".format(user.name, user.email, user.topic, user.bio)
        admin_email_subject = "New Speaker Registration"

        admin_data = {
            "email_body": admin_email_body,
            "email_subject": admin_email_subject,
            "to_email": "info.web3globalconference@gmail.com",  # Replace with admin's email address
        }
        Util.send_email(admin_data)

        
class ListCreateSponsor(generics.ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        sponsor = Sponsor.objects.filter(email=email)
        
        
        if sponsor.exists():
            user = sponsor.first()  # Get the first sponsor with the matching email
        else:
            # Handle the case when no sponsor with the given email is found
            # You can raise an appropriate exception or return a response indicating the error
            return Response({"error": "Sponsor not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Rest of the code for sending emails to the user and admin
        
        # Send email to the user
        email_body = "Dear {},\n\nThank you for registering to be a sponsor at the Web3 Global Conference. Your registration has been received, and we appreciate your support for our event.\n\nPlease be patient for further information and updates regarding your sponsorship details.\n\nIf you have any other inquiries, kindly contact us at info.web3globalconference@gmail.com.\n\nBest regards,\nW3GC".format(user.name)
        email_subject = "Your Registration Confirmation for Web3 Global Conference"

        data = {
            "email_body": email_body,
            "email_subject": email_subject,
            "to_email": user.email,
        }
        Util.send_email(data)
        
        # Send email to the admin
        admin_email_body = "A new sponsor has registered:\n\nName: {}\nEmail: {}\nOption: {}\nAbstract: {}\nAvailability: {}\nDate: {}".format(user.name, user.email, user.option, user.abstract, user.availability, user.date)
        admin_email_subject = "New Sponsor Registration"

        admin_data = {
            "email_body": admin_email_body,
            "email_subject": admin_email_subject,
            "to_email": "info.web3globalconference@gmail.com",  # Replace with admin's email address
        }
        Util.send_email(admin_data)

        
class ListCreateTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        email = instance.email
        ticket = Ticket.objects.filter(email=email)
        
        
        if ticket.exists():
            user = ticket.first()  # Get the first ticket with the matching email
        else:
            # Handle the case when no ticket with the given email is found
            # You can raise an appropriate exception or return a response indicating the error
            return Response({"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Rest of the code for sending emails to the user and admin
        # Send email to the user
        email_body = "Dear {},\n\nThank you for purchasing a ticket to the Web3 Global Conference. Your order has been received, and we appreciate your participation in our event.\n\nPlease find below the details of your ticket purchase:\n\nName: {}\nEmail: {}\nTicket: {}\nComments: {}\nDate: {}\n\nIf you have any other inquiries, kindly contact us at info.web3globalconference@gmail.com.\n\nBest regards,\nW3GC".format(user.name, user.name, user.email, user.ticket, user.comments, user.date)
        email_subject = "Your Ticket Purchase Confirmation for Web3 Global Conference"

        data = {
            "email_body": email_body,
            "email_subject": email_subject,
            "to_email": user.email,
        }
        Util.send_email(data)
        
        # Send email to the admin
        admin_email_body = "A new ticket buyer has registered:\n\nName: {}\nEmail: {}\nTicket: {}\nComments: {}\nDate: {}".format(user.name, user.email, user.ticket, user.comments, user.date)
        admin_email_subject = "New Ticket Purchase"

        admin_data = {
            "email_body": admin_email_body,
            "email_subject": admin_email_subject,
            "to_email": "info.web3globalconference@gmail.com",  # Replace with admin's email address
        }
        Util.send_email(admin_data)
