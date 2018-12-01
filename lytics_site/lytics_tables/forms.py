from django import forms

class ChannelForm(forms.Form):
    the_channel = forms.CharField(label='channel', max_length=30)