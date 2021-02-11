from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    course = models.CharField(max_length=50)
    college =models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField( max_length=254)
        

    def __str__(self):
        return self.name
