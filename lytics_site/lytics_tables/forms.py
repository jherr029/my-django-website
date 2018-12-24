from django import forms
from django.forms import formset_factory

class ChannelForm(forms.Form):
    the_channel = forms.CharField(label='channel', max_length=30)

class CustomQueryForm(forms.Form):
    custom_query = forms.CharField(label='sql', max_length=200)

class AddressForm(forms.Form):
    name = forms.CharField(
        label='Address Please',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Address address here please'
        })
    )

AddressFormset = formset_factory(AddressForm, extra=1)