from django.db import models

# Create your models here.
class aboutpage(models.Model):
    aboutpage_title=models.CharField(max_length=500)
    aboutpage_img=models.CharField(max_length=500)
    aboutpage_desc=models.TextField()
    aboutpage_uploading=models.FileField(upload_to="aboutpage",max_length=500,null=True,default=None)




from django.db import models

class PromptLog(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PromptLog {self.id}"
