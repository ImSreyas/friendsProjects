from django.db import models

# Create your models here.
class review(models.Model):
    title=models.TextField()
    feedback=models.TextField()
    feeddate=models.DateField(auto_now_add=True)
    username=models.TextField()


    
    