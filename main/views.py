from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'index.html')


def logout(request):
    auth_logout(request)
    return redirect('/')