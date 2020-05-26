from django.contrib.auth.forms import (UserCreationForm)
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import Profile


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'First Name'}))

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Last Name'}))

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder ': 'Password'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]


# Profile + Country + Edit
class CountryEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country']
        widgets = {'country': CountrySelectWidget(
            attrs={'class': 'form-control'},
            layout='{widget}<img class="country-select-flag" id="{flag_id}" style="margin: 6px 4px 0; display:none;" src="{country.flag}">',
        )}
        exclude = ('user',)


# Profile + City + Edit
class CityEditForm(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'City'}))

    class Meta:
        model = Profile
        fields = ['city']
        exclude = ('user',)


# Profile + PhoneNumber + Edit
class PhoneNumberForm(forms.ModelForm):
    # phone = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Phone Number'}))
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'City'}))

    class Meta:
        model = Profile
        fields = ['city']
        exclude = ('user',)
