from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        contactQuery = request.POST['contactQuery']
        print(name, email, phone, contactQuery)
        contact = Contact(name=name, phone=phone, email=email,contactQuery=contactQuery)
        contact.save()
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')