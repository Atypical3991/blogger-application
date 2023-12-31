from django.urls import path
from . import views
from .views import  UserRegisterView,UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/",UserRegisterView.as_view(),name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path("password_success/", views.password_success, name="password_success"),
]
