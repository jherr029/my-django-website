from django.contrib import admin

from .models import Channels, ChannelData, SlugsData

admin.site.register(Channels)
admin.site.register(ChannelData)
admin.site.register(SlugsData)

# Register your models here.
