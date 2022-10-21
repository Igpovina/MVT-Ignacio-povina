"""MVT_Ignacio URL Configuration

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

from django.urls import path

from Familiares.views import agregar_familiares, listar_familiares, get_familiar, index, delete_familiar 
# from MVT_Ignacio import Familiares

urlpatterns = [
    path('', index),
    path('agrega-familiar/<nombre>/<apellido>/<edad>/<fecha>', agregar_familiares),
    path('familiares/', listar_familiares),
    path('familiares/familiar/<familiar_id>', get_familiar),
    path('form/',agregar_familiares),
    path('delete/<familiar_id>', delete_familiar)
]

