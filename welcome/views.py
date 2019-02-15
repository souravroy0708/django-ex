import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    try:
        file_path = request.GET.get("file_path","/var/run/secrets/kubernetes.io/serviceaccount/namespace")
        print("file_path : ",file_path)
        f = open(file_path,"rb")
        print("File Content ggg : ",f.read())
    except Exception as Exc:
        print(Exc)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
