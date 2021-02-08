from django.shortcuts import render, redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def passwordpage(request):
    if request.method == 'POST':
	    username = 'visitor'
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return HttpResponseRedirect(reverse('homepage'))
	        
	    else:
        	return HttpResponseRedirect(reverse('tryagain'))
    else:
    	return render(request, 'homepage/password.html') 

def tryagain(request):
    if request.method == 'POST':
	    username = 'visitor'
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return HttpResponseRedirect(reverse('homepage'))
	        
	    else:
        	return HttpResponseRedirect(reverse('tryagain'))
    else:
    	return render(request, 'homepage/wrongpassword.html') 

@login_required
def homepage(request):
	return(render(request, 'homepage/home.html'))
