from django.contrib import admin
from .models import Category,Product
# Register your models here.

class productadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = (
    'pk',
    'title',
    'price',
    'stock')
    list_filter = ('category',)
    list_editable = ('title','price','stock',)

class categoryadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = (
    'pk',
    'title',
    'slug',
    'status'
    )
    list_filter = ('title',)
    list_editable = ('title','slug','status',)



admin.site.register(Category,categoryadmin)
admin.site.register(Product,productadmin)
