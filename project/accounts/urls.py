from django.urls import path
from django.contrib.auth import authenticate, login

from .views import (
    user_login_view,
    user_logout_view,
    user_forgetpass_view,
    user_profile_view,
    user_register_view,

)

app_name = 'accounts'

urlpatterns = [
    path('user/login/', user_login_view, name='login'),
    path('user/logout/', user_logout_view, name='logout'),
    path('user/profile/', user_profile_view, name='profile'),
    path('user/resetpassword/', user_forgetpass_view, name='forgetpass'),
    path('user/register/', user_register_view, name='register'),
]