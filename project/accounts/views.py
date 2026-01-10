from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def user_login_view(request):
    templates = 'login.html'
    form = AuthenticationForm()
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
    context = {}
    return render(request, templates, context)


def user_forgetpass_view(request):
    templates = 'forgetpass.html'
    context = {}
    return render(request, templates, context)

def user_register_view(request):
    templates = 'rwgistrations.html'
    context = {}
    return render(request, templates, context)