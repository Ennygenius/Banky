from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=150)
    descrption = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media" , null=True, blank=True)

    def __str__(self):
        return self.title