from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField()

    def __str__(self):
        return str(self.last_name + ", " + self.first_name)
