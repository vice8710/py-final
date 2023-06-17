from django.db import models

# Create your models here.
from django.db import models

class contact(models.Model):
    Name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField(max_length=200)


    def __str__(self):
        return self.Name