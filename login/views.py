from django.shortcuts import render

def index(request):
	context_dict ={}
	return render(request,'login/login.html',context=context_dict)

def register(request):
	context_dict ={}
	return render(request,'login/register.html',context=context_dict)
