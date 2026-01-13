from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm,
)

from django.core.mail import EmailMessage

from django.utils import timezone
from django.urls import reverse


from .forms import (
    RegistrationForm,
    UpdateProfileFrom,
)

# Create your views here.
def user_login_view(request):
    templates = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
        context = {
            'form': form,
        }
        return render(request, templates, context)

def user_logout_view(request):
    templates = 'logout.html'
    logout(request)
    context = {}
    return render(request, templates, context)


def user_register_view(request):
    templates = 'registration.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, templates, context)

@login_required
def user_profile_view(request):
    templates = 'user_profile.html'
    context = {
        'user': request.user,
    }
    return render(request, templates, context)

@login_required
def user_update_profile_view(request):
    templates = 'update_profile.html'
    if request.method == 'POST':
        form = UpdateProfileFrom(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/account/profile')
    else:
        form = UpdateProfileFrom(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, templates, context)

@login_required
def user_change_password_view(request):
    templates = 'change_password.html'
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/user/account/profile')
        else:
            return redirect('/user/account/change/password')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form,
        }
        return render(request, templates, context)

from django.contrib.auth.forms import PasswordResetForm

@login_required
def user_reset_pass_view(request):
    templates = 'reset_password.html'
    if request.method == 'POST':
        reset_pass_form = PasswordResetForm()
        if reset_pass_form.is_valid():
            email = reset_pass_form.cleaned_data['email']
            email_user = User.objects.get(email=email)
            return redirect('/user/account/reset_password/'+email_user.username)
    else:
        # return redirect('/user/account/reset_password/')
        reset_pass_form = PasswordResetForm()
        context = {
            'reset_pass_form': reset_pass_form,
        }
        return render(request, templates, context)

@login_required
def user_reset_password_done(request):
    templates = 'reset_password_done.html'