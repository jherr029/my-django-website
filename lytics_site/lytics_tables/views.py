from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Channels, ChannelData, SlugsData
from .forms import ChannelForm

# Create your views here.
def index(request):
    return render(request, 'lytics_tables/index.html',{})
    # return HttpResponse("Hello, this is the homepage")

def lytics(request):
    # if request.method == 'POST':

    #     form = ChannelForm(request.POST)

    #     if form.is_valid():
    #         context = {'data': form.cleaned_data['the_channel']}

    #         return render(request, 'lytics_tables/data.hmtl', context)
        
    # else:
    #     form = ChannelForm()

    table = Channels.objects.all()
    context = {'table': table}
    return render(request, 'lytics_tables/lytics.html', context)

def channelData(request, name):
    # data = ChannelData.objects.filter(name=name)
    data = ChannelData.objects.select_related('name').filter(name=name)
    # data = get_object_or_404(ChannelData, name=name)
    context = {'data': data}
    return render(request, 'lytics_tables/data.html', context)


def channelSlugs(request, name):
    data = SlugsData.objects.select_related('name').filter(name=name)
    context = {'data': data}
    return render(request, 'lytics_tables/slugs.html', context)

def channelData_overview(request):
    data = ChannelData.objects.select_related('name')
    context = {'data': data}
    return render(request,'lytics_tables/data.html', context)

def channelSlugs_overview(request):
    data = SlugsData.objects.select_related('name')
    context = {'data': data}
    return render(request,'lytics_tables/slugs.html', context)