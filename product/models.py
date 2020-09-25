from django.db import models

# Create your models here.
STATUS =[
    ('1','Aktif'),
    ('2','Pasif'),
    ('3','Taslak'),
    ]

class Category(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="")
    status = models.CharField(default='1',choices=STATUS,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="")
    stock = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(default='1',choices=STATUS,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='product',null=True,blank=True)
    content=models.TextField()
    category=models.ForeignKey("Category",on_delete=models.CASCADE )
    price=models.FloatField()
