from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('', views.ProfilePage, name='ProfilePage'),
    path('get/', views.getUsers.as_view(), name='gg'),
]
