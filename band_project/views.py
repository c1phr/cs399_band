from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from band_project.models import Tour_Dates


def home(request):
    return render(request, 'index.html', {'tour_dates': Tour_Dates.objects.all()})
# Create your views here.

def meet(request):
    return render(request, 'meet.html')

def tour(request):
    return render(request, 'tour.html', {'tour_dates': Tour_Dates.objects.all()})

def get_tour_dates(request):
    toRet = serializers.serialize('json', Tour_Dates.objects.all(), fields=('coords_x', 'coords_y'))
    return HttpResponse(toRet, content_type='application/json')

def news(request):
    return render(request, 'news.html')
def music(request):
    return render(request, 'music.html')
def contact(request):
    return render(request, 'contact.html')