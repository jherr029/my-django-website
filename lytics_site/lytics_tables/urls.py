from django.urls import path

from . import views

app_name = 'lytics'
urlpatterns = [
    path('', views.index, name='index'),
    path('lytics/', views.lytics, name='lytics'),
    path('lytics/<str:name>/data/', views.channelData, name='data'),
]