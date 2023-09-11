from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from homepage.models import UserDefinedList

#Skjema for å oppdatere profil
class ProfileForm(ModelForm):
    #bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = Profile
        fields = ['bio', 'tlf']

class MakeFavouritesListForm(ModelForm):
    class Meta:
        model = UserDefinedList
        fields = ['listName']