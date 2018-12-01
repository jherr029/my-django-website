from django.urls import path

from . import views

app_name = 'lytics'
urlpatterns = [
    path('', views.index, name='index'),
    path('lytics/', views.lytics, name='lytics'),
    path('lytics/<str:name>/data/', views.channelData, name='data'),
    path('lytics/<str:name>/slugs/', views.channelSlugs, name='slugs'),
    path('lytics/all_channels/', views.channelData_overview, name='channels_overview'),
    path('lytics/all_clips/', views.channelSlugs_overview, name='clips_overview'),
]