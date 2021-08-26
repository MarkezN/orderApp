from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser
from .models import Pdfs, Comment



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
		fields = ('title', 'autor', 'fajlovi', 'broj_stranica', 'cena_stranica')
		ordering = ['-date_posted']

		widgets = {

			'title' : forms.TextInput(attrs ={'class': 'form-control', 'placeholder': "Title"}),
			'autor' : forms.TextInput(attrs ={'class': 'form-control', 'placeholder': "Autor"}),
			'fajlovi': forms.FileInput(attrs ={'class': 'form-control', 'placeholder': "Browse..."}),
			'broj_stranica': forms.NumberInput(attrs ={'class': 'form-control', 'placeholder': "Unesi broj stranica..."}),
			'cena_stranica': forms.NumberInput(attrs ={'class': 'form-control', 'placeholder': "Unesi cenu..."}),

		}


class CommentForm(forms.ModelForm):   
	class Meta:  
		model = Comment

		fields = ('fajl', 'headline', 'tekst')
		ordering = ['-date_posted']

		widgets = {
			'fajl' : forms.Select(attrs ={'class': 'form-control', 'placeholder': "Fajl.."}),
			#'autor' : forms.Select(attrs ={'class': 'form-control', 'placeholder': "Autor"}),
			'headline' : forms.TextInput(attrs ={'class': 'form-control', 'placeholder': "Headline"}),
			'tekst': forms.Textarea(attrs ={'class': 'form-control', 'placeholder': "Unesi tekst..."}),
		}

  

