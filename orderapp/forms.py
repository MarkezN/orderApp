from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser
from .models import Pdfs



class RegisterForm(UserCreationForm):  


	class Meta:    
		model = NewUser    
		fields = ('email', 'user_name', 'ime', 'prezime', 'adresa', 'password1', 'password2' )

		

class LoginForm(UserCreationForm):  


	class Meta:    
		model = NewUser    
		fields = ('email', 'password1')

		


class PdfsForm(forms.ModelForm):  
		  
	class Meta:  
		model = Pdfs
		fields = ('__all__')

  
		# widgets = {
  #           'user_name' : forms.TextInput(attrs = {'placeholder': 'Username'}),
  #           'email'    : forms.TextInput(attrs = {'placeholder': 'Email'}),
  #           'ime' : forms.TextInput(attrs = {'placeholder': 'Ime'}),
  #           'prezime'    : forms.TextInput(attrs = {'placeholder': 'Prezime'}),
  #           'adresa' : forms.TextInput(attrs = {'placeholder': 'Adresa'}),

           

  #           'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
  #           'password2' : forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
  #       }
		



