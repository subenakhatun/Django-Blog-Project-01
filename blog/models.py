from django.db import models

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

'''
Category tho korlam. akon eita html page a kivabe add korbo manue te:
1. views.py 
    from .models import Category
2. function create korte hobe category objects er value gular jonno
    def home(request):
        categories = Category.objects.all()
        return render(request,'home.html',{'categories'}:categories)

Category.objects.all() → Database থেকে সব Category নিয়ে আসবে।
categories → পাওয়া Category-গুলো সংরক্ষণ করবে।
render() → Data-সহ HTML Template দেখাবে।
{'categories': categories} → Template-এ categories নামে Data পাঠাবে।
'''