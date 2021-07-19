from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm


def home_view(request):
	return render(request, 'orderapp/home.html')


def log_view(request):    
	return render(request, 'orderapp/log.html')


def reg_view(request):  
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():  
			form.save()
			return redirect('home_view')	   

	else:   
		form = RegisterForm()

	return render(request, 'orderapp/reg.html', {'form': form})	