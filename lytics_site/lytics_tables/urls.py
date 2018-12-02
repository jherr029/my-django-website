from django.urls import path

from . import views

app_name = 'lytics'
urlpatterns = [
    path('', views.index, name='index'),
    path('lytics/', views.lytics, name='lytics'),
    path('lytics/<str:name>/', views.channelOverview, name='overview'),
    path('lytics/<str:name>/channel/', views.channelData, name='channel'),
    path('lytics/<str:name>/clips/', views.channelSlugs, name='clips'),
    path('lytics/all_channels/', views.channelData_overview, name='channels_overview'),
    path('lytics/all_clips/', views.channelSlugs_overview, name='clips_overview'),
]