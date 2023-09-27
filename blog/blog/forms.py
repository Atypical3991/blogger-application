from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.contrib.auth.models import User



class PasswordUpdatingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('old_password1', 'new_password1', 'new_password2')
