from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
# Create your views here.

def meet(request):
    return render(request, 'meet.html')