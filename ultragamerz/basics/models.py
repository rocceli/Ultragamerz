from django.db import models
from django.utils import timezone


# Create your models here.

class message(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to="product")
    sales = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class order(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    county=models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    total=models.IntegerField()
    def __str__(self):
        return str(self.id)
