from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="indice"),
    path("cuenta/", include("django.contrib.auth.urls")),
    path("cuenta/registro/", views.registro, name="registro"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("actualizar_perfil/", views.actualizar_perfil, name="actualizar_perfil"),
    path("agregar_inmueble/", views.agregar_inmueble, name="agregar_inmueble"),
]
