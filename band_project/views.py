from django.shortcuts import render
from band_project.models import Tour_Dates


def home(request):
    return render(request, 'index.html', {'tour_dates': Tour_Dates.objects.all()})
# Create your views here.

def meet(request):
    return render(request, 'meet.html')

def tour(request):
    return render(request, 'tour.html', {'tour_dates': Tour_Dates.objects.all()})
def news(request):
    return render(request, 'news.html')
def music(request):
    return render(request, 'music.html')
def contact(request):
    return render(request, 'contact.html')