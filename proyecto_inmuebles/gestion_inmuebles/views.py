from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Inmueble


# Create your views here.
def index(request):

    return render(request, "index.html", {"arriendos": Inmueble.objects.all()})


def registro(request):
    if request.user.is_authenticated:
        return redirect("indice")

    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("indice")
    else:
        form = forms.CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html", {})


def actualizar_perfil(request):
    if request.method == "POST":
        form = forms.ActualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = forms.ActualizarUsuarioForm(instance=request.user)
    return render(request, "actualizar_perfil.html", {"form": form})


def agregar_inmueble(request):
    if request.method == "POST":
        form = forms.AgregarInmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.dueno = request.user
            inmueble.save()
            return redirect("dashboard")
    else:
        form = forms.AgregarInmuebleForm()
    return render(request, "agregar_inmueble.html", {"form": form})
