from django.db import models

# Create your models here.
class Category(models.Model):
    catname=models.CharField(max_length=250)   
    def __str__(self):
        return self.catname

class Blog(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    datetime_post=models.DateTimeField(default=None)
    category_name=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title