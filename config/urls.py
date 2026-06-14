"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Library_System.urls')),
    path('albums/', include('photo_album.urls')),

    path('accounts/', include('accounts.urls')),

    ## Login and Registration Friendly top level urls
    path('login/', accounts_views.login, name='login'),
    path('registration/', accounts_views.registration, name='registration'),
    
]

handler404 = 'Library_System.views.custom_404_view'
