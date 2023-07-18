from django.shortcuts import render
from django.contrib import messages
from core.forms import MyForm

def home(request):
    return render(request, "home.html", context={})

def contact(request):
    messages.warning(request, "Esto es un test")
    form = MyForm
    return render(request, "contact.html", context={'form':form})