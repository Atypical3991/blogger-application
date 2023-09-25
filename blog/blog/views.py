from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm


class PasswordChangeView(auth_views.PasswordChangeView):
    formclass = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy("home")

    def get_object(self):
        return  self.request.user