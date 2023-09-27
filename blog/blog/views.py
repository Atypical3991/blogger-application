from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm

from .forms import PasswordUpdatingForm


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordUpdatingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy("password_success")

    def get_object(self):
        return  self.request.user