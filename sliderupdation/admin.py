from django.contrib import admin
from sliderupdation.models import SliderUpdation
# Register your models here.
class AdminSlider(admin.ModelAdmin):
    list_display=('slider_title','slider_img','slider_desc','slider_uploading')
admin.site.register(SliderUpdation,AdminSlider)    
