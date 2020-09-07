from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')
    #return HttpResponse('This is home')

def contact(request):
    return render(request, 'home/contact.html')
    #return HttpResponse('This is contact')

def about(request):
    return render(request, 'home/about.html')
    #return HttpResponse('This is about')