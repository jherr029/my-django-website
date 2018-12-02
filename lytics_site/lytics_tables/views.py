from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .models import Channels, ChannelData, SlugsData
from .forms import ChannelForm


# TODO: implement get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'lytics_tables/index.html',{})
    # return HttpResponse("Hello, this is the homepage")

def lytics(request):
    if request.method == 'GET':

        print('POST occured')
        form = ChannelForm(request.GET)

        if form.is_valid():
            print('valid form')
            chan = form.cleaned_data['the_channel']

            return HttpResponseRedirect(reverse('lytics:overview', args=(chan,)))

        else:
            print('invalid form')
        
    else:
        print('not POST')
        form = ChannelForm()

    table = Channels.objects.all()
    context = {'table': table,
        'form': form,
    }
    return render(request, 'lytics_tables/lytics.html', context)

def channelData(request, name):
    # data = ChannelData.objects.filter(name=name)
    print('The name is', name)
    data = ChannelData.objects.select_related('name').filter(name=name)
    context = {'channel': data}

    if not data:
        print('does not exist')
        context.update({'unfound_channel': name})
        # return Http404(name + ' is not within the database')

    # data = get_object_or_404(ChannelData, name=name)
    return render(request, 'lytics_tables/data.html', context)


def channelSlugs(request, name):
    data = SlugsData.objects.select_related('name').filter(name=name)
    context = {'channel': data}

    if not data:
        print('does not exist')
        context.update({'unfound_channel': name})

    return render(request, 'lytics_tables/slugs.html', context)

def channelOverview(request, name):
    generalData = ChannelData.objects.select_related('name').filter(name=name)
    clipData = SlugsData.objects.select_related('name').filter(name=name)

    context = {
        'general': generalData,
        'clips': clipData
    }

    if not generalData:
        print('does not exist')
        context.update({'unfound_channel': name})

    return render(request, 'lytics_tables/overview.html', context)

def channelData_overview(request):
    data = ChannelData.objects.select_related('name')
    context = {'channel': data}
    return render(request,'lytics_tables/data.html', context)

def channelSlugs_overview(request):
    data = SlugsData.objects.select_related('name')
    context = {'channel': data}
    return render(request,'lytics_tables/slugs.html', context)