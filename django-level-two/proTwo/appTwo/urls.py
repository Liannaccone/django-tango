from django.urls import path
from appTwo import views

urlpatterns = [
    path('user', views.users, name='user')
]
