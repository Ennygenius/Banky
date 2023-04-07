from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=150)
    descrption = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media" , null=True, blank=True)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/" , null=True, blank=True)


class rActivities(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    date_created = models.DateField()
    image = models.ImageField(upload_to="image",null=True, blank=True)
    

    class Meta:
        verbose_name_plural = "rActivities"

    def __str__(self):
        return self.title