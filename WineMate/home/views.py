from django.shortcuts import render
from accounts.decorators import admin_required
from django.http import HttpResponse
# Create your views here.


@admin_required()
def home(request):
    return render(request, 'home/home.html')

