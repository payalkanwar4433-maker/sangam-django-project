from django.contrib import admin

# Register your models here.

from blogpanel.models import Category,Blog

class AdminCategory(admin.ModelAdmin):
    list_diplay=('id','catname')
class AdminPost(admin.ModelAdmin):
    list_diplay=('id','title','content','datetime_post','category_name')

admin.site.register(Category,AdminCategory)
admin.site.register(Blog,AdminPost)

