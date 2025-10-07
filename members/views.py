from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ContactMe
from .forms import ContactForm

def member_list(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message.")
    form = ContactForm()
    return render(request, 'members/index.html',{'form':form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message.")
    form = ContactForm()
    return render(request, "members/contact.html", {'form':form})



