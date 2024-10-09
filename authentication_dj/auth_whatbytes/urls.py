from django.contrib import admin
from django.urls import path
from .views import register, index, CustomPasswordChangeView, profile
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('profile/', profile, name='profile'),
]