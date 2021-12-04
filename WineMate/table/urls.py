from django.urls import path

from . import views

urlpatterns = [
    path('', views.TableListView, name='table'),
    path('addtotable', views.addtotable, name='addtotable'),
    path('cellar', views.CellarView, name='cellar'),
]