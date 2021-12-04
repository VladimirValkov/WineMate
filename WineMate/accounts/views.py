from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class Register(View):
    def get(self, request):
        register_form = UserCreationForm()
        context = {'form': register_form}
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()

        context = {'form': register_form}
        return render(request, 'accounts/register.html', context)


class Login(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
