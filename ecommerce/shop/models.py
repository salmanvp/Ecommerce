from django.db import models

class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='shop/category',null=True,blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/category', null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

