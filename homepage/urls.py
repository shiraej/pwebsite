from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('password/', views.passwordpage, name = 'passwordpage'),
    path('tryagain/', views.tryagain, name = 'tryagain')
]