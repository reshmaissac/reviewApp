from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=300) 
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    brand=models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost=models.FloatField()
    release_date=models.DateField()
    description=models.TextField(max_length=5000)
    averagerating=models.FloatField(default=0)
    # photo = models.URLField(default=None, null=True)
    photo = models.ImageField(default = 'default_prod.jpg', upload_to = 'product_pics')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Review(models.Model):
    product=models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, default=1)
    rating=models.IntegerField(default=0)
    comment=models.TextField()
    date_time=models.DateField()