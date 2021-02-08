from django.urls import path

from . import views

urlpatterns = [
    path('', views.adv_gallery, name='gallery'),
    #path('entry/', views.guestentry, name = 'guestbook_entry')
]