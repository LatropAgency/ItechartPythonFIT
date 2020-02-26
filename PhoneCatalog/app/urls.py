from django.urls import path

from . import views

urlpatterns = [
    path('', views.showNumbers, name='show'),
]