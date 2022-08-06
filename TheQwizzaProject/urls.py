"""TheQwizzaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Qwizza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('discussion/', views.discussion, name='Discussion'),
    path('signup/', views.signup, name='Signup'),
    path('10english/', views.sub_english, name='10th Class: English'),
    path('10math/', views.sub_math, name='10th Class: Math'),
    path('10physci/', views.sub_physci, name='10th Class: Physical Science'),
    path('10social/', views.sub_social, name='10th Class: Social'),
    path('fib/', views.temp_fib, name='Template: Fill in the Blanks'),
    path('tof/', views.temp_tof, name='Template: True or False'),
    path('mcq/', views.temp_mcq, name='Template: Multiple Choice Questions'),


]
