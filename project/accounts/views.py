from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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