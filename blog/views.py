from django.shortcuts import render
from .models import Category,BlogPost

# Create your views here.
# home page a j logic gula set korbo oi gular jonno function
def home(request):
    categories = Category.objects.all()
    blog_info = BlogPost.objects.all()
    features_post = BlogPost.objects.filter(is_feature = True).first()
    recent_posts = BlogPost.objects.all().order_by('-id')[:2]
    context = {
        'features_post':features_post,
        'blog_info':blog_info,
        'categories':categories,
        'recent_posts':recent_posts
    }
    return render( request,'home.html', {'post_context': context} ) 
    