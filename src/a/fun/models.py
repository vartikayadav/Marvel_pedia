from django.db import models

# Create your models here.
class Characters(models.Model):
    name=models.CharField(max_length=256)
    starting_alhphabet=models.CharField(max_length=1)
    def __str__(self):
        return self.name
