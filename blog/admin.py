from django.contrib import admin
from .models import Category,BlogPost

# Register your models here.
admin.site.register(Category)

# BlogPost models register for show in database
admin.site.register(BlogPost)