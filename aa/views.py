from django.shortcuts import render
from datetime import date, datetime
from aa.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'Home.html')
def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save() 
        messages.success(request, 'Message has been Sent !')
        return render(request,'Home.html')
def contribute(request):
    return render(request,'contribute.html')