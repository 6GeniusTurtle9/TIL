from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping),
    path('pong/', views.pong),

    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]
