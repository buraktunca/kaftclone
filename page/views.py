from django.shortcuts import render,redirect
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
        else:
            message.error(request,"Kaydedilemedi!")
    context={"form":form}
    return render(request,'home/index.html',context)

def carousel_list(request):
    carousellist=Carousel.objects.all()
    context={"item":carousellist}
    return render(request,"manage/carousel_list.html",context)

def carousel_update(request,pk):
    item=Carousel.objects.get(pk=pk)
    form=CarouselModelForm(instance=item)
    if request.method =="POST":
        form=CarouselModelForm(request.POST,request.FILES,instance=item)
        form.save()
        return redirect('carousel_list')
        
    content={"item":item,"form":form}
    return render(request,"manage/carousel_update.html",content)
