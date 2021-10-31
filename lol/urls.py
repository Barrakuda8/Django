"""lol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mainapp import views as mainapp
from authapp import views as authapp
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('', authapp.index, name='index'),
    path('home/', mainapp.index, name="home"),
    path('collection/', include('mainapp.urls', namespace='collection')),
    path('loot/', mainapp.loot, name="loot"),
    path('store/', mainapp.store, name="store"),
    path('auth/', include('authapp.urls', namespace='auth')),


    path('loot/chests/', mainapp.loot, name="loot_chests"),
    path('loot/champs/', mainapp.loot, name="loot_champs"),
    path('loot/skins/', mainapp.loot, name="loot_skins"),
    path('loot/emotes/', mainapp.loot, name="loot_emotes"),
    path('loot/wards/', mainapp.loot, name="loot_wards"),
    path('loot/icons/', mainapp.loot, name="loot_icons"),

    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
