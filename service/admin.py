from django.contrib import admin
from service.models import Service
# Register your models here.
class AdminSlider(admin.ModelAdmin):
    list_display=('slider_title','slider_img','slider_desc','slider_uploading')
admin.site.register(Service,AdminSlider)    


# Register your models here.
