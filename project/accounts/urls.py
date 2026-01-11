from django.urls import path
from django.contrib.auth import authenticate, login, logout

from .views import (
    user_login_view,
    user_logout_view,
    user_forgetpass_view,
    user_profile_view,
    user_register_view,
    user_update_profile_view,
)

app_name = 'accounts'

urlpatterns = [
    path('account/login/', user_login_view, name='login'),
    path('account/logout/', user_logout_view, name='logout'),
    path('account/profile/', user_profile_view, name='profile'),
    path('account/resetpassword/', user_forgetpass_view, name='forgetpass'),
    path('account/register/', user_register_view, name='register'),
    path('account/edit/', user_update_profile_view, name='update_profile'),
]