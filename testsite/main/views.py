from django.shortcuts import render
from django.views import generic

# Create your views here.
def mainView(request):
    return render(request, 'main/index.html')