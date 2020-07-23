from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from .views import *

urlpatterns = [
    path('registration', CreateUserView.as_view(), name='registration'),
    path('login', obtain_auth_token, name='login'),
    path('get-list', get_list, name='get_list'),
    path('edit-list', edit_list, name='edit-list')
]
