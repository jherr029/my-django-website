from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.db import connection
from collections import namedtuple

from .models import Channels, ChannelData, SlugsData
from .forms import ChannelForm, CustomQueryForm, AddressFormset
import subprocess


# TODO:j include ddt on docker image

# Create your views here.
def index(request):
    return render(request, 'lytics_tables/index.html',{})
    # return HttpResponse("Hello, this is the homepage")

def lytics(request):
    if request.method == 'GET':
        print('GET occured')

        if 'the_channel' in request.GET:
            print('the_channel')
            channelForm = ChannelForm(request.GET)
            if channelForm.is_valid():
                print('Form is valid')
                chan = channelForm.cleaned_data['the_channel']

                return HttpResponseRedirect(reverse('lytics:overview', args=(chan,)))
        
        # elif 'custom_query' in request.GET:
        #     print('custom_query')
        #     queryForm = CustomQueryForm(request.GET)

        #     if queryForm.is_valid():
        #         print('Form is valid')
        #         query = queryForm.cleaned_data['custom_query']

        #         return HttpResponseRedirect(reverse('lytics:customQuery', args=('customQueryGeneral', query)))

        else:
            print('Invalid form')
    

    channelForm = ChannelForm()
    # queryForm = CustomQueryForm()

    table = Channels.objects.all()
    context = {'table': table,
        'channelForm': channelForm,
        # 'queryForm': queryForm,
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
    print('channel overview')
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

def customQuery(request, query, source):
    print('Custom Query function is being used')

    # raw queries are not good enough. they are bound by primary keys
    with connection.cursor() as cursor:
        cursor.execute(query)
        queryResult = dictfetchall(cursor)

        # print(queryResult)
    # queryResult = Channels.objects.raw(query)
    # print(queryResult)
# 
    # print(queryResult[0][0])

    context = {
        source : queryResult,
        'userQuery': query,
    }

    return render(request, 'lytics_tables/customQuery.html', context)

    # can not use get_list_or_404 due to this being a raw query
    # try:
    #     queryResult = Channels.objects.raw(query)
    #     print(queryResult)

    #     context = {
    #         'customQuery': queryResult
    #     }

    #     return render(request, 'lytics_tables/customQuery.html', context)

    # except:
    #     raise Http404('Invalid query')
        # instead of raising this create a 404 page to be more descriptive

    # queryResult = get_list_or_404(queryResult)




def channelData_overview(request):
    # if request.method == 'GET':
    #     print('GET occured')

    #     if 'custom_query' in request.GET:
    #         print('custom_query')
    #         queryForm = CustomQueryForm(request.GET)

    #         if queryForm.is_valid():
    #             print('Form is valid')
    #             query = queryForm.cleaned_data['custom_query']

    #             return HttpResponseRedirect(reverse('lytics:customQuery', args=('customQueryData', query)))

    data = ChannelData.objects.select_related('name')
    context = {'channel': data}

    return render(request,'lytics_tables/data.html', context)

def channelSlugs_overview(request):
    # if request.method == 'GET':
    #     print('GET occured')

    #     if 'custom_query' in request.GET:
    #         print('custom_query')
    #         queryForm = CustomQueryForm(request.GET)

    #         if queryForm.is_valid():
    #             print('Form is valid')
    #             query = queryForm.cleaned_data['custom_query']

    #             return HttpResponseRedirect(reverse('lytics:customQuery', args=('customQueryClips', query)))

    data = SlugsData.objects.select_related('name')
    context = {'channel': data}

    return render(request,'lytics_tables/slugs.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def shuttle(request):
    addrList = []
    if request.method == 'GET':
        formset = AddressFormset(request.GET or None)
    elif request.method == 'POST':
        formset = AddressFormset(request.POST)

        if formset.is_valid():

            tempFile = open("testFile.txt", "w")
            print(len(formset))
            print('printting: ',formset[0].cleaned_data.get('name'))

            if len(formset) == 1 and formset[0].cleaned_data.get('name') is None:
                context = {
                    'emptyInput': True,
                }

                return render(request, 'lytics_tables/shuttleError.html', context)

            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # print(name)
                if name is not None:
                    tempFile.write(name + "\n")
                    addrList.append(name)
                    
            print(addrList)

            tempFile.close()
            subprocess.call(["../../Shuttle/bin/shuttle", "read" ,"&"])
            resultsFile = open("results.txt", "r")

            fileLines = resultsFile.readlines()
            pathHistory = []

            if fileLines[0] == 'error\n':
               errorAt = fileLines[1] 
               resultsFile.close()

               print(addrList[int(errorAt) - 1])

               context = {
                   'errorAt': addrList[int(errorAt) - 1],
               }

               return render(request, 'lytics_tables/shuttleError.html', context)

            else:
                maxAddresses = int(fileLines[0])

                for x in range(1, maxAddresses):
                    pathHistory.append(fileLines[x].replace("+", " "))

                duration = fileLines[maxAddresses + 1]
                miles = fileLines[maxAddresses + 2]

                print(pathHistory)
                print(duration)
                print(miles)

                resultsFile.close()

                context = {
                    'addresses': addrList,
                    'pathHistory': pathHistory,
                    'duration': duration,
                    'miles': miles,
                }

                return render(request, 'lytics_tables/shuttleResults.html', context)

    context = {
        'formset': formset,
    }

    # print(formset)

    return render(request, 'lytics_tables/shuttle.html', context)

def shuttleDemoResults(request, context):
    print('Hi')

    print(context['addresses'])


    return render(request, 'lytics_tables/shuttleResult.html', context)
