from datetime import datetime
from django.contrib import messages
from .models import Contact
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'index.html')       

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Your information has been submitted successfully!")
        print(name,email,password,desc)
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def questions(request):
    return render(request, 'questions.html')