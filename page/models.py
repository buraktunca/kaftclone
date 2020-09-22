from django.db import models

# Create your models here.
STATUS =[
    ('1','Taslak'),
    ('2','Yayınlandı'),
    ('3','Silindi'),
]
class Page(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="")
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page',null=True,blank=True)
    status = models.CharField(default='1',choices=STATUS,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Carousel(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    cover_image = models.ImageField(upload_to='carousel',null=True,blank=True)
    status = status = models.CharField(default='1',choices=STATUS,max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
