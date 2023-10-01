from django.shortcuts import render
from django.views import  generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import SignUpForm, EditProfileForm
from django.contrib.auth import views as auth_views

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")

class  UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy("home")

    def get_object(self):
        if self.request.user:
            return self.request.user
        else:
            return  None


def password_success(request):
    render(request,'registration/password_success.html',{})