"""
URL configuration for core project.

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
from django.urls import path
from panel.views import panel
from panel.views import KillAll
from panel.views import gamemode
from panel.views import Restart
from panel.views import register
from panel.views import reg, login, addServer, addsrv, console


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', panel, name="main"),
    path ('killAll/', KillAll),
    path ('gamemode/', gamemode),
    path ('restart/', Restart),
    path ('register/', register),
    path ('reg/', reg),
    path ('log/', login),
    path ('console/', console),
    path ('addserver/', addServer),
    path ('addsrv/', addsrv, name="addserver")
]
