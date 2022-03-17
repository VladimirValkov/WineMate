from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return resolve_url('home')
