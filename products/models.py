from django.db import models

# Create your models here.
<<<<<<< HEAD
# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    brand=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
    cost=models.FloatField()
    release_date=models.DateField()
    description=models.TextField(max_length=5000)
    averagerating=models.FloatField(default=0)
    # photo = models.URLField(default=None, null=True)
    photo = models.ImageField(default = 'default.jpg', upload_to = 'product_pics')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
=======
>>>>>>> 91026d0 (Homepage linked with base.html)
