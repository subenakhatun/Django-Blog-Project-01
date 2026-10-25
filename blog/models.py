from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
Model create korte hobe->migrate korte hobe->admin a jeye class register korte hobe
'''

# Model create korar por terminal er makemigrations kore migrate korte hobe
# admin.py a jeye admin.site.register(Category) korte hobee
class Category(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # name onujai show korbe database a catagory, na hole object_1 ei vabe show korto
    def __str__(self):
        return self.name


# BlogPost class create
STATUS_MODE = (
    (0, 'Draft'),
    (1, 'Published'),
)
class BlogPost(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.CharField(max_length = 200,unique=True,blank =True)
    # category delete hole auto delete
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    # user delete hole post delete hoye jabe
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    short_description = models.CharField(max_length = 400)
    blog_body = models.CharField(max_length = 2000)
    status = models.IntegerField(choices = STATUS_MODE)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

# makemigrations ->migrate