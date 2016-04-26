from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html')


def spainguide(request):
    return render(request, 'spainguide.html')
