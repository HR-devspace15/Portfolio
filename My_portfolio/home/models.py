from django.db import models
# create your models here .

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    date = models.DateField()

    def __str__(self):
        return self.name
