from django.shortcuts import render
from .models import Category

# Create your views here.

def home(request):
    categories = Category.objects.all()
    return render( request,'home.html', {'categories': categories} )