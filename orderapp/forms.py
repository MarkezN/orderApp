from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser



class RegisterForm(UserCreationForm):  


	class Meta:    
		model = NewUser    
		fields = ('email', 'user_name', 'ime', 'prezime', 'adresa', 'password1', 'password2' )

		

class LoginForm(UserCreationForm):  


	class Meta:    
		model = NewUser    
		fields = ('email', 'password1')

		

  
		# widgets = {
  #           'user_name' : forms.TextInput(attrs = {'placeholder': 'Username'}),
  #           'email'    : forms.TextInput(attrs = {'placeholder': 'Email'}),
  #           'ime' : forms.TextInput(attrs = {'placeholder': 'Ime'}),
  #           'prezime'    : forms.TextInput(attrs = {'placeholder': 'Prezime'}),
  #           'adresa' : forms.TextInput(attrs = {'placeholder': 'Adresa'}),

           

  #           'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
  #           'password2' : forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
  #       }
		



