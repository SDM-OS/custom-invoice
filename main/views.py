from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from main.forms import JobForm

from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView



def home(request):
	return render(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')