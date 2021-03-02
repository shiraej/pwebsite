from django.urls import path

from . import views

urlpatterns = [
    path('', views.adv_gallery, name='gallery'),
    path('<int:adventure_id>/', views.adv_details, name='details')
    #path('entry/', views.guestentry, name = 'guestbook_entry')
]