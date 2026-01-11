from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from django.http import HttpResponseRedirect


from django.shortcuts import render, get_object_or_404, redirect

from .models import UserProfile
from .forms import RegistrationForm

# Create your views here.
def user_login_view(request):
    templates = 'login.html'
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm(request)
        context = {
            'form': form,
        }
        return render(request, templates, context)

def user_logout_view(request):
    templates = 'logout.html'
    context = {

    }
    return render(request, templates, context)

def user_profile_view(request):
    templates = 'user_profile.html'
    user_instance = get_object_or_404(UserProfile, user=request.user)
    context = {
        'username': user_instance.user,
        'profile': user_instance.description,
        'email': user_instance.email,
        'city': user_instance.city,
        'country': user_instance.country,
        'phone': user_instance.phone,
        'weblink': user_instance.weblink,
        'created_at': user_instance.created_at,
        'updated_at': user_instance.updated_at,
    }
    return render(request, templates, context)


def user_forgetpass_view(request):
    templates = 'forgetpass.html'

    context = {}
    return render(request, templates, context)

def user_register_view(request):
    templates = 'registration.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, templates, context)


def user_update_profile_view(request):
    templates = 'update_profile.html'
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/account/profile')
    else:
        form = UserChangeForm(request.POST, instance=request.user)
        context = {
            'form': form,
        }
        return render(request, templates, context)
