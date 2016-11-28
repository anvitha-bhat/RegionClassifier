from django.http import HttpResponse,Http404
from django.shortcuts import render
# Create your views here.

def home(request):
	context = {
	}
	return render(request, 'home.html', context)
