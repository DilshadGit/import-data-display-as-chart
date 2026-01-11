# To make it easy to see layout created account for the user for login, logout, register, forget password
# create profile, update profile delete profile and delete the username.

# Accounts

# Login view https://docs.djangoproject.com/en/5.0/_modules/django/contrib/auth/views/

# Linked the UserProfile to createsuperuser as soon you create a new user automatically create user_profile instance
# for you in the admin page and you can add user details when you need but we created UserProfile class in the models
# from the User On models.OneToOneField(User, on_delete=models.CASCADE) each user can have one profile OneToOne
# and when the user account is deleted the profile has to be delete there we have to use on_delete=models.CASCADE

# we can import logout method from django.contrib.auth import authenticate, login, logout and create in the urls.py
# without create extra methods in the view. files

# we imported from from django.contrib.auth.forms import UserCreationForm to create RegistrationForm without create
# extra class in models for the user like UserProfile

# Error :
The view accounts.views.user_login_view didn't return an HttpResponse object. It returned None instead.
# We use default django form before userprofile and form using AuthenticationForm() for login.
 # The error above came from this code below:
def user_login_view(request):
    templates = 'login.html'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/account/profile')
        else:
            form = AuthenticationForm(request)
            context = {
                'form': form,
            }
            return render(request, templates, context)

# To resolve the error we have to change to the below: 
def user_login_view(request):
    templates = 'login.html'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/account/profile')
    else:
        form = AuthenticationForm(request)
        context = {
            'form': form,
        }
        return render(request, templates, context)

# In the user_register_view we have used UserCreationForm for beginning were user can use username and password1
# with password2 before we create registration form in forms.py.

# We update UserCreateForm and changed to create own RegistrationForm inherited  UserCreationForm adding email
# include first_name, last_name with username and two passwords ad default in django however we can changed if we want.

