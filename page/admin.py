from django.contrib import admin
from .models import Page,Carousel
# Register your models here.


class pageadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = (
    'pk',
    'title',
    'status',
    'updated_at')
    list_filter = ('status',)
    list_editable = ('title','status',)

class carouseladmin(admin.ModelAdmin):

    list_display = (
    'pk',
    'title',
    'status',
    'updated_at')

admin.site.register(Page,pageadmin)
admin.site.register(Carousel,carouseladmin)
