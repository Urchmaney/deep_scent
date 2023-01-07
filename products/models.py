from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length = 100)
  size_in_liter = models.PositiveIntegerField(default=0)
  price = models.PositiveIntegerField()
  image_url = models.CharField(max_length = 400)

  def __str__(self):
    return self.name