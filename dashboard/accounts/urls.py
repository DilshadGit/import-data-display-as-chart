from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import (
	login, 
	logout,
)


urlpatterns = [
	url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', login, {'template_name': 'logout.html'}, name='logout'),
	url(r'^register/$', views.register, name='register_form'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^change-password/$', views.change_password, name='change_password'),

	# redirect the user to login when you type 127.0.0.1:8000/account
	url(r'^$', views.login_redirect, name='login_redirect'),
]