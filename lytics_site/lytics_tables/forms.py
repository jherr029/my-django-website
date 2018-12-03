from django import forms

class ChannelForm(forms.Form):
    the_channel = forms.CharField(label='channel', max_length=30)

class CustomQueryForm(forms.Form):
    custom_query = forms.CharField(label='sql', max_length=200)