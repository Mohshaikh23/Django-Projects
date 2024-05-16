"""
URL configuration for dmm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from dmm import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('admin/', admin.site.urls, name="admin"),
    path('services/', views.services, name="services"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact/', views.contact, name="contact"),
    path('userform/', views.userform, name="userform"),
    path('thankyou/', views.thankyou, name ="thankyou"),
    path('calc/', views.calculator, name = "calc"),
    path('evenodd/', views.even_odd, name="evenodd"),
    path('marksheet/', views.marksheet, name="marksheet"),
    path('courses/', views.course),
    path('courses/<courseid>', views.coursedetails),
    path('blogsview/<slug>', views.blogview, name = "blogview"),
]
