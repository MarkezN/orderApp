from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, PdfsForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pdfs, Comment
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail  
from django.conf import settings



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


@login_required(login_url="log_view")	
def pdfs_list(request):  
   	pdfs = Pdfs.objects.all() 
   	
   	return render(request, 'orderapp/pdfslist.html', {'pdfs': pdfs}) 

@login_required(login_url="log_view")
def upload_pdfs(request):
    if request.method == 'POST':
        form = PdfsForm(request.POST, request.FILES)
        if form.is_valid():   
            form.save()
            return redirect('list')
    else:    
        form = PdfsForm()        
    return render(request, 'orderapp/upload.html', {'form': form})     

def delete_file(request,pk):   
	if request.method == 'POST':  
		pdf = Pdfs.objects.get(pk=pk)
		pdf.delete()
	return redirect('list')	


def create_comment(request):   
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
        	comment = form.save(commit=False)
        	if request.user == comment.autor:
            		form.save()
            		return redirect('comment_list')
        	else:
        			return redirect('create_comment')   

    else:    
        form = CommentForm()
    return render(request, 'orderapp/create_comment.html', {'form': form})  
    


def list_comment(request):    
    comment = Comment.objects.all()
    return render(request, 'orderapp/comment_list.html', {'comment': comment}) 


def delete_comment(request, pk):   
	if request.method == 'POST':   
		comment = Comment.objects.get(pk=pk)
		comment.delete()
	return redirect('comment_list')	   


def order(request):   
	if request.method == 'POST':  
		current_email = request.user.email
		host_email = settings.EMAIL_HOST_USER
		send_mail(
			 'Obavestenje',
			 'Postovani,vasa narudzbina je uspesno izvrsena. Hvala na poverenju.',
			 '',   
			 [current_email, host_email],    
			 fail_silently=False,
			 )
	return render(request, 'orderapp/order.html')




                 



