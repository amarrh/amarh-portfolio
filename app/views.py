from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import App

# Create your views here.

def index(request):
    apps = App.objects
    return render(request, 'apps/index.html',{'apps':apps})

def detail(request,app_id):
    app_detail = get_object_or_404(App, pk=app_id)
    return render(request, 'apps/detail.html', {'app':app_detail})