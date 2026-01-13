# To make it easy to see layout created account for the user for login, logout, register, forget password
# create profile, update profile delete profile and delete the username.

# WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server 
# instead. For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/

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

# Create UpdateProfile from UserProfile, first import UserChangeForm in the forms from auth.forms in django while we 
# create UpdateProfileFrom and inherited from UserChangeForm thoes fields not want to display like password 
# we can use exclude('password') or using Class Meta: model = user display the fields = ('first_name', etc ..)

# We rest password without touching django admin or change the password.
# To create change password user must be logged in and link the change password top profile when user change the 
# password it has to be loggedin after change the password using update_session_auth_hash

# Reset password or forget password next:
# Info and explain this line
    path('', include('django.contrib.auth.urls', namespace='auth')),

# Reference : https://docs.djangoproject.com/en/5.0/topics/auth/default/
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]

We can add this line in main urls.py to reduce coding for every forms related to authentication process like
login, password_reset, registration, change_password, 
# Refernces to use for Password_reset:
    https://github.com/django/django/blob/main/django/contrib/auth/urls.py
    https://github.com/django/django/blob/main/django/contrib/auth/views.py
    https://github.com/django/django/blob/main/django/contrib/auth/forms.py

Working or rest_password but all built function for Password_reset, Password_reset_done, Password_reset_confirm,
Password_reset_confirm_done has been changed still redirected me to admin page need extra works.
# The New function are PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView  

# To send email:
Looks like you are trying to send a mail (send_mail()) and your mail settings in your settings.py are not correct.

You should check the docs for sending emails.
For debugging purposes you could setup a local smtpserver with this command:

python -m smtpd -n -c DebuggingServer localhost:1025

# and adjust your mail settings accordingly:

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
