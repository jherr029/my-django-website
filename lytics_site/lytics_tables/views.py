from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Channels, ChannelData

# Create your views here.
def index(request):
    return render(request, 'lytics_tables/index.html',{})
    # return HttpResponse("Hello, this is the homepage")

def lytics(request):
    table = Channels.objects.all()
    context = {'table': table}
    return render(request, 'lytics_tables/lytics.html', context)

def channelData(request, name):
    data = ChannelData.objects.filter(name=name)
    context = {'data': data}
    return render(request, 'lytics_tables/data.html', context)
    # table = ChannelData.objects.all()
    # context = {'table': table}
    # return render(request, 'lytics_tables/lytics.html', context, context)