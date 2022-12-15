from django.db import models

# Create your models here.
class series(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    Language=models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')


    def __str__(self):
        return self.name



