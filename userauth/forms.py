from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email'}))
                   
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter a password'}))
            
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm your password'}))

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2']

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Choose a username'}),
                   
                    
                  }
