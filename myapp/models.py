from django.db import models

class Patient(models.Model):
  name = models.CharField(max_length=200)
  mobile = models.CharField(max_length=10)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=200)
  age = models.IntegerField()
  address = models.CharField(max_length=500)

  def __str__(self):
    return self.name
