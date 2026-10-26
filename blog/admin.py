from django.contrib import admin
from .models import Category,BlogPost

# Register your models here.
admin.site.register(Category)

# BlogPost models register for show in database
# ei class tar kaj ami database a blogpost er ki ki asole dekhte chai samne
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','status','is_feature')
    list_editable = ('is_feature',)

admin.site.register(BlogPost,BlogAdmin)

