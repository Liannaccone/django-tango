from django.urls import path
from appTwo import views

urlpatterns = [
    path('help', views.help, name='help'),
    path('user', views.user_listing, name='user')
]
