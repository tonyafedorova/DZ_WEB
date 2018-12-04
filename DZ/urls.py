"""DZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from dzrip.views import first, pictures, forLab5, Profile, firstnotlog, login, picturenotlog, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', first),
    url(r'^pictures/', pictures),
    path('lab5/', forLab5.as_view()),
    path('profile/', Profile.as_view()),
    path('firstnotlog/', firstnotlog),
    path('login/', login),
    path('picnotlog/', picturenotlog),
    path('signup/', signup)
]
