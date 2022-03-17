from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url


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

class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return resolve_url('home')
