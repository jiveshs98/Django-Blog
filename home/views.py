from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
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

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(contactQuery)<2:
            messages.error(request, "Please fill the form correctly")
        else:   
            contact = Contact(name=name, phone=phone, email=email,contactQuery=contactQuery)
            contact.save()
            messages.success(request, 'Your form has been submitted successfully!!')
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')