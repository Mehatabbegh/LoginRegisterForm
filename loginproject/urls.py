"""loginproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from loginapp import views as loginapp
from loginproject import views as mainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserRegisterActions/", loginapp.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", loginapp.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", loginapp.UserHome, name="UserHome"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)