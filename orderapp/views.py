from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required




@login_required(login_url="log_view")
def home_view(request):
	return render(request, 'orderapp/home.html')


def log_view(request):  

	if request.method == 'POST':


	
		email = request.POST.get('email')
		password = request.POST.get('password1')

		user = authenticate(request, email=email, password=password)
		if user != None:
			
			login(request, user)
			is_active = True
		
			return redirect('home_view')

		else:   
			messages.info(request, "Username or password incorrect")	

	form = LoginForm()
	return render(request, 'orderapp/log.html', {'form': form})

def logout_view(request):   
	logout(request)
	return redirect("log_view")

def reg_view(request):  
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():  
			form.save()
			return redirect('log_view')	   

	else:   
		form = RegisterForm()

	return render(request, 'orderapp/reg.html', {'form': form})	