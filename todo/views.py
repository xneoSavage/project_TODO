from django.shortcuts import render, redirect
from django.http import request, response


# Create your views here.
def index(request):
	return render(request, 'index.html')