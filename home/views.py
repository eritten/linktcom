from django.shortcuts import render
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    return render(request, 'home.html')

@api_view("POST")
def contact(request):
    name = request.data.get('name')
    email = request.data.get('email')
    telephone_number = request.data.get('tel')
    content = request.data.get('msg')
    send_mail("Client contact", content, email, [], fail_silently=True)
    return Response({"status": "Sent"})

