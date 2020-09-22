from django.shortcuts import render
from .models import Carousel,Page
from .forms import CarouselModelForm
from django.contrib import messages
# Create your views here.
def index(request):
    form = CarouselModelForm()
    if request.method == "POST":
        form=CarouselModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Başarılı Bir Şekilde Eklendi.")
    context={"form":form}
    return render(request,'home/index.html',context)
