"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from SampleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/',views.demo),
    path('p/',views.sample),
    path('w/<str:aq>/',views.hrf),
    path('g/<int:y>/<str:r>/<int:t>/',views.student),
    path('k/',views.wg),
    path('y/<str:qw>/',views.af),
    path('h/<str:nm>/',views.ae),
    path('nu/<str:k>/',views.cy),
    path('mk/',views.hk),
    path('gh/<str:qy>/',views.vy),
    path('rg/',views.std),
    path('rm/',views.me),
   

]