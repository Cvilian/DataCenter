from django.shortcuts import render
from django.http import HttpResponse

from .forms import DataForm
from .models import Data

# Create your views here.

def dataList(request):
    dataset = Data.objects.all()
    return render(request, 'storage/list.html', { 'dataset' : dataset})

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'storage/index.html')

