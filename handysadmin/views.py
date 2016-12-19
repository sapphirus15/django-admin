from django.shortcuts import render
from .models import *

def adminuser_list(request):
    return render(request, 'handysadmin/adminuser_list.html', {})

def index(request):
    return render(request, 'handysadmin/index.html', {})

def base(request):
    return render(request, 'handysadmin/base.html', {})

def dashboard(request):
    return render(request, 'handysadmin/dashboard.html', {})

def host_list(request):
    print "host_list"
    hostlist = User.objects.all()
    return render(request, 'handysadmin/host_list.html', { 'hostlist':hostlist })
