"""kaft_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import index,carousel_list,carousel_update
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('carousel_list/',carousel_list,name="carousel_list"),
    path('carousel_update/<int:pk>/',carousel_update,name="carousel_update")

]
urlpatterns += static(
    settings.MEDIA_URL,document_root=settings.MEDIA_ROOT
    )
