from django.urls import path
from django.contrib.auth.views import  (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
# from django.contrib.auth.views import  PasswordReset

from .views import (
    user_change_password_view,
    user_login_view,
    user_logout_view,
    user_profile_view,
    user_register_view,
    user_update_profile_view,
    # user_reset_pass_view,
    # user_reset_pass_done_view,
    # user_reset_pass_confirm_view,
)

app_name = 'accounts'

urlpatterns = [
    path('account/login/', user_login_view, name='login'),
    path('account/logout/', user_logout_view, name='logout'),
    path('account/profile/', user_profile_view, name='profile'),
    path('account/register/', user_register_view, name='register'),
    path('account/edit/', user_update_profile_view, name='update_profile'),
    path('account/change/password/', user_change_password_view, name='change_pass'),

    path('account/reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('account/reset-password/done/', PasswordResetDoneView.as_view(), name='reset_password_done'),
    path('account/reset-password/confirm/', PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('account/reset-password/complete/', PasswordResetCompleteView.as_view(), name='reset_password_complete'),

    # path('account/reset-password/', user_reset_pass_view, name='reset_password'),
    # path('account/reset-password/done/', user_reset_pass_done_view, name='reset_password_done'),
    # path('account/reset-password/confirm/<uidb64>/<token>', user_reset_pass_confirm_view, name='reset_password_confirm'),
    # path('account/reset/done/', PasswordResetComplete, name='password_reset_complete'),

]