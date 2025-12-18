from django.db import models

# Create your models here. 
class SliderUpdation(models.Model):
    slider_title=models.CharField(max_length=500)
    slider_img=models.CharField(max_length=500)
    slider_desc=models.TextField()
    slider_uploading=models.FileField(upload_to="media",null=True,default=None)

