"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from seminarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inscritos/', views.InscritosList.as_view()),
    path('inscritos/<int:id>', views.InscritosDetalle.as_view()),
    path('inscritosJson/', views.inscripcionDB),
    path('institucion/', views.institucion_list),
    path('institucion/<int:id>', views.institucion_detalle),
    path('institucionJson/', views.institucionDB),
    path('lista/', views.listadoInscritos),
    path('agregar/', views.agregarInscritos),
    path('actualizar/<int:id>', views.actualizarInscritos),
    path('eliminar/<int:id>', views.eliminarInscritos),
]
