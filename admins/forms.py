from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm, UserCreationForm

# extend original model
class UCFWithEmail(UserCreationForm):
    # username = email
    username = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]