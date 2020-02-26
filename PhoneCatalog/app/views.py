from django.http import HttpResponse
from django.shortcuts import render
from .models import phone_catalog


def showNumbers(request):
    query = phone_catalog.objects.all()
    context = {'context':query}
    return render(request,'index.html',context)