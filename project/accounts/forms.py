from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = str(self.cleaned_data['first_name'])
        user.last_name = str(self.cleaned_data['last_name'])
        user.email = self.cleaned_data['email']
        # when is commit True it save it in the database
        if commit:
            user.save()

        return user

# we update the form to display what we want
class UpdateProfileFrom(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        # exclude = ('password1', 'password2')