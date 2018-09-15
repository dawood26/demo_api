from django.db import models
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
