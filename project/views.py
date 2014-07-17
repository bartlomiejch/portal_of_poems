from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)
	
def auth_views(request):
	nzw = request.POST.get('username','')
	haslo = request.POST.get('password','')	
	user = auth.authenticate(username=nzw, password=haslo)
    
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

	
def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})	
	
def invalid_login(request):
	return render_to_response('invalid_login.html')	
	
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')		

def register_user(request):
	if request.method == 'POST':
		a = request.POST.get("login")
		b = request.POST.get("password")
		c = request.POST.get("confirmed_password")
		if b==c:
			args = {}
			args.update(csrf(request))
			user = User.objects.create_user(username = a, password = b)
			user.save()
			return HttpResponseRedirect('/accounts/register_success/', args)
		else:
			return HttpResponseRedirect('/accounts/invalid/')
	else:
		args = {}
		args.update(csrf(request))
		return render_to_response('register.html', args)


def register_success(request):
	return render_to_response('register_success.html')
