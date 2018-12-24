from django.urls import path

from . import views

app_name = 'lytics'
urlpatterns = [
    path('', views.index, name='index'),
    path('lytics/', views.lytics, name='lytics'),
    path('lytics/streamer/<str:name>/', views.channelOverview, name='overview'),
    path('lytics/streamer/<str:name>/channel/', views.channelData, name='channel'),
    path('lytics/streamer/<str:name>/clips/', views.channelSlugs, name='clips'),
    path('lytics/custom_query/<str:source>/<str:query>/', views.customQuery, name='customQuery'),
    path('lytics/all_channels/', views.channelData_overview, name='channels_overview'),
    path('lytics/all_clips/', views.channelSlugs_overview, name='clips_overview'),
    path('shuttle/', views.shuttle, name='shuttle'),
    path('shuttle/demo/', views.shuttleDemoResults, name='shuttle_demo'),

]