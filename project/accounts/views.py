from django.shortcuts import render

# Create your views here.
def user_login_view(request):
    templates = 'login.html'
    context = {}
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