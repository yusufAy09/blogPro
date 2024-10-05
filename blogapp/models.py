from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField()
    image=models.ImageField(upload_to='pics')