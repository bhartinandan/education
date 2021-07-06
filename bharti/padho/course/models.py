from django.db import models

# Create your models here.
class Destination(models.Model):

    caption = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pics")
    video = models.FileField(upload_to="video/%y")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.caption

