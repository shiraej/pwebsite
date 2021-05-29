from django.urls import path

from . import views

urlpatterns = [
    path('', views.guestbook, name='guestbook'),
    path('entry/', views.guestentry, name = 'guestbook_entry'),
    path('thankyou/', views.thankyou, name = 'thankyou'),
]