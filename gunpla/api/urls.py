from django.urls import path

from . import views

urlpatterns = [
    path('mechanic', views.mechanic, name='mechanic'),
    path('join', views.join, name='join'),
]
