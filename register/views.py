import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView, Record

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, './index.html', {
#        'hostname': hostname,
#        'database': database.info(),
#        'count': PageView.objects.count()
    })

def register(request):
    if request.POST['email'] == 'af8dc2fc-c7db-4295-9728-2a26673c8705':
        return render(request, './report.html', {'data':Record.objects.all()})

    else:
        Record.objects.create(ip=get_client_ip(request), email=request.POST['email'])

        return render(request, './done.html')


def health(request):
    return HttpResponse(PageView.objects.count())
