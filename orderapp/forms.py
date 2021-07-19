
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser


class RegisterForm(UserCreationForm):  

	class Meta:    
		model = NewUser    
		fields = ['email', 'user_name', 'ime', 'prezime', 'adresa']



