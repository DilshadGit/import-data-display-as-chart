# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from accounts.forms import (
	RegistrationForm, 
	EditMyUserForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
	UserChangeForm,
	PasswordChangeForm,
)

# use when you update the password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import MyUser



# # redirect the index page to login page
def login_redirect(request):
	return redirect('/account/login')

def register(request):
	if request.method == 'POST':
		register_form = RegistrationForm(request.POST )
		if register_form.is_valid():
			register_form.save()
			return redirect('/')
	else:
		register_form = RegistrationForm()
		context = {'register_form': register_form}
		return render(request, 'register_form.html', context)

@login_required
def profile(request):
	mydata = MyUser.objects.all()
	for x in mydata:
		print(x.area, ' all data')
		print(x.tarrif, ' Tarrif')
	context = {
		'user': request.user,
		'mydata': mydata,
	}
	return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		edit_form = EditMyUserForm(request.POST, instance=request.user)

		if edit_form.is_valid():
			edit_form.save()
			return redirect('/account/profile')
	else:
		edit_form = EditMyUserForm(instance=request.user)
		context = {'edit_form': edit_form}
		return render(request, 'edit_profile.html', context)

'''
 https://docs.djangoproject.com/en/1.11/topics/auth/default/#django.contrib.auth.forms.PasswordResetForm.send_email
'''
@login_required
def change_password(request):
	if request.method == 'POST':
		change_form = PasswordChangeForm(data=request.POST, user=request.user)

		if change_form.is_valid():
			change_form.save()
			# will keep the user logedin even when you change the password
			update_session_auth_hash(request, change_form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')
	# else is the get request 
	else:
		change_form = PasswordChangeForm(user=request.user)
		context = {'change_form':change_form}
		return render(request, 'change_password.html', context)