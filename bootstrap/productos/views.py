from django.shortcuts import render
from .forms import ProductForm, AddressForm

# Create your views here.
def new(request):
    form = ProductForm()
    return render(request, "productos/new.html", context={'form':form})

def new_address(request):
    form = AddressForm()
    return render(request, "productos/new_address.html", context={'form':form})