from django.shortcuts import render
from .models import Category,BlogPost

# Create your views here.
# home page a j logic gula set korbo oi gular jonno function
def home(request):
    categories = Category.objects.all()
    return render( request,'home.html', {'categories': categories} )

def blog_details(request):
    blog_info = BlogPost.objects.all()
    return blog_info
