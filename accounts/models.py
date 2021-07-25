from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomAccManager(BaseUserManager):

	def create_user(self, email, user_name, ime, password, **other_fields):  


		if not email:
			raise ValueError("You must have an email")
		email = self.normalize_email(email)
		user = self.model(email=email, user_name=user_name,ime = ime, **other_fields)
		user.set_password(password)
		user.save()
		return user






	def create_superuser(self, email, user_name, ime, password, **other_fields):   
			other_fields.setdefault('is_staff', True)
			other_fields.setdefault('is_superuser', True)
			other_fields.setdefault('is_active', True)

			if other_fields.get('is_staff') is not True:   
				raise ValueError('is_staff must be True with Superuser')
			if other_fields.get('is_staff') is not True:   
				raise ValueError('is_superuser must be True with Superuser')


			return self.create_user(email, user_name, ime, password, **other_fields)	



# Create your models here.
class NewUser(AbstractBaseUser, PermissionsMixin):   
	email = models.EmailField(_('email address'), unique=True,)
	user_name= models.CharField(max_length=100, unique=True)
	ime = models.CharField(max_length=150, blank=True)
	prezime = models.CharField(max_length=150)
	adresa = models.CharField(max_length=150)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	objects = CustomAccManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_name', 'ime']

	def __str__(self):   
		return self.user_name





