from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from main.forms import JobForm

from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView



def home(request):
	return render(request, 'home.html')

class AddjobView(FormView):
	form_class = JobForm
	success_url = "/"
	template_name = 'new.html'

	def form_valid(self, form):
		form.save(commit = True)
		return super(AddjobView, self).form_valid(form)


def add(request):
	return render(request, 'new.html')


def logout(request):
    auth_logout(request)
    return redirect('/')