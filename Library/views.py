from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
import requests
from .forms import AddressBook
from .models import Address
from numpy import delete


# Create your views here.

def addata(request):
    if request.method == 'POST':
        fm1 = AddressBook(request.POST)
        if fm1.is_valid():
            nm = fm1.cleaned_data['name']
            ct = fm1.cleaned_data['city']
            st = fm1.cleaned_data['state']
            mb = fm1.cleaned_data['mbno']
            make = Address(name=nm, city=ct, state=st, mbno=mb)
            make.save()
            fm1 = AddressBook()
    else:
        fm1 = AddressBook()
    result = Address.objects.all()
    return render(request,'project/index.html',{'form':fm1, 'result':result})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Address.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home') 

def update_data(request, id):
    if request.method == 'POST':
        pi = Address.objects.get(pk=id)
        fm1 = AddressBook(request.POST, instance=pi)
        if fm1.is_valid():
            fm1.save()
    else:
        pi = Address.objects.get(pk=id)
        fm1 = AddressBook(instance=pi)
    return render(request,'project/update.html', {'form':fm1})