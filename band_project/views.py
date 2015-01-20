from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
# Create your views here.

def meet(request):
    return render(request, 'meet.html')

def tour(request):
    return render(request, 'tour.html')
def news(request):
    return render(request, 'news.html')
def music(request):
    return render(request, 'music.html')
def contact(request):
    return render(request, 'contact.html')