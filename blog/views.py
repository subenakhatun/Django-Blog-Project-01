from django.shortcuts import render
from .models import Category

# Create your views here.
# home page a j logic gula set korbo oi gular jonno function
def home(request):
    categories = Category.objects.all()
    return render( request,'home.html', {'categories': categories} )

